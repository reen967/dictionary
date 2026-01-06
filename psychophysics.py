# psychophysics.py
def stevens_law(signal, exponent):
    return np.sign(signal) * (np.abs(signal) ** exponent)
