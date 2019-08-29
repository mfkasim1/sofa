import numpy as np
import shapely.geometry as spg
import shapely.affinity as spa

def fwd(ys, angles):
    """
    Calculate the area of the sofa when the trajectory is given by `ys` and
    `angles`. It starts from coordinate (-sqrt(2),0) with angle 45 and should
    finish at coordinate (sqrt(2),0) with angle -45.

    For every element in `ys` and `angles`, it get the polygon difference
    with the walls until it finishes.
    The area of the last polygon will be returned.
    The initial sofa is 1 unit vertically and 3 units horizontally.
    """
    if len(ys) != len(angles):
        raise RuntimeError("The input arguments in sofa's fwd must be the "
                           "same length")
    # construct the sofa
    x0 = np.sqrt(2)
    w0 = 3.0
    h0 = 1.0
    sof = spg.box([-x0-w0*.5, -h0*.5, -x0+w0*.5, h0*.5])
    centre = np.array([-x0, 0.0])
    sof = spa.rotate(sof, 45)

    # construct the wall

    # move the sofa!
    n = len(ys)
    xs = np.linspace(-x0, x0, n)
    for i in range(n):
        x = xs[i]
        y = ys[i]
        angle = angles[i]
