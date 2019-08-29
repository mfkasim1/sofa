import time
import numpy as np
import matplotlib.pyplot as plt
import shapely.geometry as spg
import shapely.affinity as spa

poly1 = spg.Polygon([(0,0), (2,0), (2,1), (0,1)])

t0 = time.time()
poly2 = spa.translate(spa.rotate(poly1, 30), 1.5)
poly3 = poly1.difference(poly2)
print(time.time() - t0)
plt.plot(*poly1.exterior.xy)
plt.plot(*poly2.exterior.xy)
plt.plot(*poly3.exterior.xy)
plt.show()
