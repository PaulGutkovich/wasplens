import numpy as np
import math
import pyransac3d as pyrsc

def find_centroid(points):
    A = 2*(points[0,:] - points[1:, :])
    C = np.linalg.norm(points, axis=1)**2
    B = C[0] - C[1:]

    centroid = np.matmul(np.linalg.inv(A), B) 
    
    return centroid

def find_sphere_centroids(points):
    N = 100000
    centroids = np.zeros((N, 3))
    n = 0
    while n < N:
        np.random.shuffle(points)
        for idx in range(points.shape[0]-4):
            centroid = find_centroid(points[idx:idx+4, :])
            centroids[n, :] = centroid
            n += 1
            if n == N:
                break

    centroids


    center = np.median(centroids, axis=0)

    radius = np.mean(np.linalg.norm(center - points, axis=1))

    return center, radius

def fit_sphere_ransac(points):
	sph = pyrsc.Sphere()
	center, radius, inliers = sph.fit(points, thresh=0.4)

	return center, radius

def sphereFit(points):
    #   Assemble the A matrix
    spX = points[:, 0]
    spY = points[:, 1]
    spZ = points[:, 2]
    A = np.zeros((len(spX),4))
    A[:,0] = spX*2
    A[:,1] = spY*2
    A[:,2] = spZ*2
    A[:,3] = 1

    #   Assemble the f matrix
    f = np.zeros((len(spX),1))
    f[:,0] = (spX*spX) + (spY*spY) + (spZ*spZ)
    C, residules, rank, singval = np.linalg.lstsq(A,f)

    #   solve for the radius
    t = (C[0]*C[0])+(C[1]*C[1])+(C[2]*C[2])+C[3]
    radius = math.sqrt(t)

    #print("lstsq", C[:3])
    return C[:3], radius