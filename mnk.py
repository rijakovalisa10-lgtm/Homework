import numpy as np


def mnk_coefficients(x, y):
	x = np.asarray(x)
	y = np.asarray(y)
	
	if x.shape[0] != y.shape[0] or len(x) == 0 or len(y) == 0:
		raise ValueError()
	
	A = np.vstack([x, np.ones(x.shape[0])]).T
	
	a, b = np.linalg.lstsq(A, y, rcond=None)[0]
	
	return a, b
