# Nouns
NOUNS = {
    "Sleepy":  {"theta": 271.9, "x": 0.03, "y": -1.0, "signal": "S1"},
    "Calm":    {"theta": 294.1, "x": 0.41, "y": -0.91, "signal": "S1"},
    "Relaxed": {"theta": 310.2, "x": 0.65, "y": -0.76, "signal": "S2"},
    "Alarmed": {"theta": 96.5,  "x": -0.11, "y": 0.99, "signal": "J4"},
    "Angry":   {"theta": 119.5, "x": -0.49, "y": 0.87, "signal": "J5"}
}

# Verbs
VERBS = {
    "Snap":  lambda t: 1-(1-t)**4,  # Logarithmic rise
    "Glide": lambda t: 3*t**2-2*t**3,  # Sigmoid
    "Surge": lambda t: t**4,  # Exponential
    "Fade":  lambda t: 1-(1-t)**2,
    "Yield": lambda t: t**0.5
}

# Sine/Jitter signals
SINES = {
    "S1": lambda t: 0.02 * np.sin(5*t),
    "S2": lambda t: 0.05 * np.sin(10*t),
    "S3": lambda t: 0.10 * np.sin(15*t),
    "S4": lambda t: 0.20 * np.sin(25*t),
    "S5": lambda t: 0.25 * np.sin(35*t)
}

JITTERS = {
    "J1": lambda: 0.0,
    "J2": lambda: 0.05*np.random.uniform(-1,1),
    "J3": lambda: 0.10*np.random.uniform(-1,1),
    "J4": lambda: 0.15*np.random.uniform(-1,1),
    "J5": lambda: 0.20*np.random.uniform(-1,1)
}
