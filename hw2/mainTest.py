import numpy as np
from scipy import optimize
import math

def circleFitByDss(data):
	Mx = np.mean(data[0])
	My = np.mean(data[1])
	Mp = np.array([Mx, My])
	global Data
	Data = np.array(data).T
	alld = np.sqrt(np.sum(np.asarray(Mp - Data)**2, axis=1))
	r = sum(alld)/len(data[0])
	theta0 = [Mx, My, r]

	def f(theta):
		a, b, r = theta
		p = [a,b]
		d = np.sqrt(np.sum(np.asarray(p - Data)**2, axis=1))	
		return sum(abs(np.array(d) - r))

	ans = optimize.minimize(f, theta0)
	return (ans.x)

def CircleFitting():
	def Load_Coordinates():
		data = [[float(val) for val in input().split()] for i in range(2)]
		return data

	for _ in range(5):
		data = Load_Coordinates()
		a, b, r = circleFitByDss(data)
		print('{} {} {}'.format(a, b, r))

if __name__ == '__main__':
	CircleFitting()