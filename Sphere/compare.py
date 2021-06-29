from methods import *
from test import *
import matplotlib.pyplot as plt
from time import time as t

n=500

ransac_errors = []
centroid_errors = []
lstsq_errors = []
errors = [0.01, 0.025, 0.05, 0.1, 0.25]

for error in errors:
	ransac_errors.append(calc_error(n, error, fit_sphere_ransac))
	centroid_errors.append(calc_error(n, error, find_sphere_centroids))
	lstsq_errors.append(calc_error(n, error, sphereFit))

#print(ransac_errors, centroid_errors, lstsq_errors)
ransac_errors = np.array(ransac_errors)
centroid_errors = np.array(centroid_errors)
lstsq_errors = np.array(lstsq_errors)

fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(ransac_errors[:,0], 'g-')
ax1.plot(centroid_errors[:,0], 'r-')
ax1.plot(lstsq_errors[:,0], 'b-')
ax1.set_xticklabels(["0", "0.01", "", "0.025", "", "0.05", "", "0.1", "", "0.25"])

ax2.plot(ransac_errors[:,1], 'g-')
ax2.plot(centroid_errors[:,1], 'r-')
ax2.plot(lstsq_errors[:,1], 'b-')
ax2.set_xticklabels(["0", "0.01", "", "0.025", "", "0.05", "", "0.1", "", "0.25"])

plt.show()

plt.savefig("img_"+str(t())+".jpg")