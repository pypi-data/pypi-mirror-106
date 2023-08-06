from collections import OrderedDict
import math
import itertools

class Parameter:
    def __init__(self, name, initial_value=None, min=None, max=None, grid=None, integral=False, dx=None):
        self.name = name
        if grid is not None:
            if min is None or max is None:
                raise ValueError("using the grid option requires min and max values to be set")
            if min >= max:
                raise ValueError("inconsistent min and max values")
        if initial_value is None and grid is None:
            raise ValueError("either initial_value or grid settings must be specified")
        if initial_value is not None and grid is not None:
            raise ValueError("initial_value and grid settings can't be specified both")
        self.initial_value = initial_value
        self.min = min
        self.max = max
        self.grid = grid
        self.integral = integral
        if dx is None:
            if integral:
                dx = 1
            elif initial_value is not None:
                if initial_value == 0:
                    raise ValueError("if initial_value is 0, a dx value must be specified")
                dx = initial_value / 1000
            else:
                dx = (max - min) / 1000
        self.dx = dx

    def limit (self, x0, xdiff):
        if self.integral:
            if xdiff > 0:
                xdiff = math.ceil(xdiff)
            elif xdiff < 0:
                xdiff = math.floor(xdiff)
        x = x0 + xdiff
        if self.min is not None and x < self.min:
            x = self.min
        if self.max is not None and x > self.max:
            x = self.max
        return x

    def grid_points(self):
        if not self.grid:
            return [self.initial_value]
        points = []
        interval = (self.max - self.min) / self.grid
        x0 = self.min
        for _ in range(self.grid):
            point = x0 + interval/2
            if self.integral:
                point = round(point)
            points.append(point)
            x0 += interval
        return points

class Optimizer:
    def __init__(self, function, args='enum', zoom_limit=1e6, cfactor=0.5, momentum=0, iterations=100, min_improvement=0, trace=False, debug=False):
        self.function = function
        self.args = args
        self.parmap = {}
        self.parameters = []
        self.zoom_limit = zoom_limit
        self.cfactor = cfactor
        self.momentum = momentum
        self.iterations = iterations
        self.min_improvement = min_improvement
        self.trace = trace
        self.debug = debug

    def add_par(self, par:Parameter):
        self.parameters.append(par)
        self.parmap[par.name] = par

    def add_parameter(self, name, initial_value=None, min=None, max=None, grid=None, integral=False, dx=None):
        self.add_par (Parameter(name, initial_value, min, max, grid, integral, dx))

    def optimize (self):
        self.npars = len(self.parameters)
        if self.has_grid():
            return self.optimize_grid()
        x0 = [p.initial_value for p in self.parameters]
        return self.optimize_point(x0)

    def invoke(self, x):
        if self.args == 'list':
            return self.function(x)
        if self.args == 'enum':
            return self.function(*x)
        argmap = {p.name: xi for (p, xi) in zip(self.parameters, x)}
        if self.args == 'dict':
            return self.function(argmap)
        if self.args == 'kwargs':
            return self.function(**argmap)
        raise ValueError("unknown args value: " + self.args)

    def optimize_point(self, x0):
        self.zoomin = 1
        self.last_change = None
        y0 = self.invoke(x0)
        dx = [p.dx for p in self.parameters]
        if self.debug:
            print ("x0", x0, ":", y0)
        for iter in range(self.iterations):
            dy = self.build_gradient (x0, y0, dx)
            if self.debug:
                print("dx " + str(dx))
                print("dy " + str(dy))
            x1, y1, alpha = self.apply_gradient (x0, y0, dx, dy)
            if self.debug or self.trace:
                print("iteration", iter, "zoom", self.zoomin, "at", x1, ":", y1)
            if y1 >= y0:
                if self.zoomin < self.zoom_limit:
                    self.zoomin *= 2
                    continue
                return self.as_dict(x0), y0
            if y0 - y1 <= self.min_improvement:
                break
            x0 = x1
            y0 = y1
        return self.as_dict(x1), y1

    def as_dict(self, x):
        return {par.name: xi for par, xi in zip(self.parameters, x)}

    def has_grid(self):
        for par in self.parameters:
            if par.grid is not None:
                return True
        return False

    def optimize_grid(self):
        gridlist = [par.grid_points() for par in self.parameters]
        startpoints = list(itertools.product(*gridlist))
        results = [self.optimize_point(list(x)) for x in startpoints]
        best = min(results, key=lambda r: r[1])
        return best

    def build_gradient (self, x0, y0, dx):
        dy = []
        for i, x0i, dxi, par in zip(range(self.npars), x0, dx, self.parameters):
            x = x0.copy()
            zoom = 1 if par.integral else self.zoomin
            x[i] = x0i + dxi / zoom
            dyi = self.invoke(x) - y0
            if par.integral and dyi > 0 and dxi == 1:
                x[i] = x0i - dxi
                otherway = self.invoke(x) - y0
                if otherway > 0:
                    #both directions +/- 1 are worse
                    dyi = 0
            elif dyi == 0 and zoom == 1:
                for _ in range(8):
                    dxi = 2 * dxi
                    x[i] = x0i + dxi
                    dyi = self.invoke(x) - y0
                    if dyi != 0:
                        dx[i] = dxi
                        break;
            dy.append(dyi)
        return dy


    def apply_gradient(self, x0, y0, dx, dy):
        s2 = sum((dyi/dxi)**2 for dxi, dyi in zip(dx, dy))
        alpha = 0.5 * y0 / s2
        for _ in range(20):
            x1 = []
            for i, par, x0i, dxi, dyi in zip(range(self.npars), self.parameters, x0, dx, dy):
                s = dyi/dxi
                delta = - s * alpha
                if self.momentum != 0 and self.zoomin == 1 and self.last_change is not None:
                    delta += self.momentum * self.last_change[i]
                x = par.limit(x0i, delta)
                x1.append (x)
            try:
                y1 = self.invoke(x1)
                if self.debug:
                    print("with alpha = " + str(alpha) + ", x " + str(x1) + ", y1 is " + str(y1))
                if y0 - y1 >= alpha * self.cfactor * s2:
                    if self.momentum != 0:
                        self.last_change = [x1i - x0i for x1i, x0i in zip(x1, x0)]
                    return x1, y1, alpha
            except Exception:
                pass
            alpha = alpha / 2
        return x0, y0, 0




