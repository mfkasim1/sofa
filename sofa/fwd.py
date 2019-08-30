import numpy as np
import shapely.geometry as spg
import shapely.affinity as spa

def fwd(ys, angles, animation=False):
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

    if animation:
        import matplotlib.pyplot as plt
        plt.ion()

    # construct the sofa
    w0 = 3.0
    h0 = 1.0
    x0 = (w0*0.5 + h0*0.5) / np.sqrt(2)
    sof = spg.box(-x0-w0*.5, -h0*.5, -x0+w0*.5, h0*.5)
    centre = np.array([-x0, 0.0])
    sof = spa.rotate(sof, 45)

    # construct the walls
    # wall_sub needs to be subtracted
    corner0 = (0,np.sqrt((w0*0.5)**2+(h0*0.5)**2-x0**2))
    wall_sub = spg.box(corner0[0]-5, corner0[1]-5, corner0[0], corner0[1])
    wall_sub = spa.rotate(wall_sub, 45, origin=corner0)

    # wall_int needs to be intersected
    corner1 = (0,corner0[1] + np.sqrt(2))
    wall_int = spg.box(corner1[0]-7, corner1[1]-7, corner1[0], corner1[1])
    wall_int = spa.rotate(wall_int, 45, origin=corner1)

    # move the sofa!
    n = len(ys)
    xs = np.linspace(-x0, x0, n)
    curr_x, curr_y = centre
    curr_angle = 45
    dt = 1. / n
    for i in range(n):
        x = xs[i]
        y = ys[i]
        angle = angles[i]

        # move the sofa
        dx = x - curr_x
        dy = y - curr_y
        dangle = angle - curr_angle
        sof = spa.translate(sof, dx, dy)
        sof = spa.rotate(sof, dangle, origin=(x, y))

        # subtract the sofa with the walls
        sof = sof.difference(wall_sub)
        sof = sof.intersection(wall_int)

        if animation:
            plt.clf()
            plt.plot(*sof.exterior.xy)
            plt.plot(*wall_sub.exterior.xy)
            plt.plot(*wall_int.exterior.xy)
            plt.draw()
            plt.pause(dt)

        # update the current positions
        curr_x = x
        curr_y = y
        curr_angle = angle
    return sof

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    x0 = np.sqrt(2)
    n = 100
    x = np.linspace(-x0, x0, n)
    ys = -x**2 + np.sqrt((1.5)**2+(0.5)**2-2) + np.sqrt(2)*.5
    angles = np.linspace(45, -45, n)
    sof = fwd(ys, angles, True)
    print(sof.area)
