from scipy import optimize
import numpy as np
import math

def f(theta):
	a, b, r = theta
	p = [a,b]
	d = np.sqrt(np.sum(np.asarray(p - Data)**2, axis=1))	
	return sum(abs(np.array(d) - r))

def circleFitByDss(data):
    Mx = np.mean(data[0])
    My = np.mean(data[1])
    Mp = np.array([Mx, My])
    n = len(data[0])
    global Data
	Data = np.array(data).T
	alld = np.sqrt(np.sum(np.asarray(Mp - Data)**2, axis=1))
	r = sum(alld)/n

	theta0 = [Mx, My, r]
	ans = optimize.minimize(f, theta0)
	return (ans.x)

'''
scipy.optimize
https://www.mathworks.com/help/matlab/ref/fminsearch.html#bvadxhn-8
https://stackoverflow.com/questions/13670333/multiple-variables-in-scipys-optimize-minimize

1 point to all point distance
https://blog.csdn.net/Tan_HandSome/article/details/79753504


'''