import numpy as np

def normalize_angle(theta):
    return (theta + np.pi) % (2*np.pi) - np.pi
