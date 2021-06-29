import numpy as np
from random import random as r
from math import pi, sin, cos

def theta():
	return 0.5*pi*r()

def point(c, r):
	alpha = theta()
	beta = theta()
	return [c[0]+r*cos(alpha)*cos(beta), c[1]+r*sin(alpha)*cos(beta), c[2]+r*sin(beta)]

def epsilon(sigma, n):
	mu = np.array([0,0,0])
	cov = np.array([
		[sigma**2, 0, 0],
		[0, sigma**2, 0],
		[0, 0, sigma**2]
		])

	return np.random.multivariate_normal(mu, cov, size=n)


def sample(n, c, r, sigma):
	epsilons = epsilon(sigma, n)

	points = np.array([
		point(c, r)+epsilons[i] for i in range(n)
		])

	return points

def point_error(points, c, r):
	ds = np.linalg.norm(points-c, axis=1)
	r_dev = np.linalg.norm(ds-r)**2

	return r_dev.mean()

def center_error(c, c_bar):
	return np.linalg.norm(c-c_bar)

def calc_error(n, sigma, f):
	c = np.array([1,1,1])
	r = 1
	points = sample(n, c, r, sigma)
	center, radius = f(points)

	return [center_error(c, center), radius]

