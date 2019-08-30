import maleo
import numpy as np
from sofa.fwd import fwd
from functools import reduce

def cost(y_func, angle_func):
    n = 100
    xs = np.linspace(0, 1, n)
    ys = [y_func(x) for x in xs]
    angles = [angle_func(x) for x in xs]
    sof = fwd(ys, angles)
    return -sof.area

def main():
    # Set the name of the process. If the process is failed, then it can be
    # resumed if the name remains the same.
    is_functional = True
    interp = "linear"
    name = "sofa-functional-%s"%interp
    op = maleo.Solver(name)
    op.set_algorithm(maleo.alg.FunctionalCMAInterp(
        max_fevals=10000,
        populations=16))
    op.add_resource(maleo.LocalResource(
        max_jobs=8,
        scheduler="taskset"))
    op.set_function(cost)

    # set variables
    op.add_variable(maleo.Interp1DFcn('y_func', xrange=(0,1), yrange=(0,1.5),
        interp=interp, fixed_pts=[(0.0, 0.0), (1.0, 0.0)]))
    op.add_variable(maleo.Interp1DFcn('angle_func', xrange=(0,1), yrange=(-50.0,50.0),
        interp=interp, fixed_pts=[(0.0, 45.0), (1.0, -45.0)]))

    res = op.run()

    # print the output
    op.print_result("%s.results.txt"%name)
    op.print_history("%s.history.txt"%name)

if __name__ == "__main__":
    main()
