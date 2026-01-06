# dictionary.py
nouns = {
    "Sleepy": {"x": 0.03, "y": -1.0, "signal": "S1"},
    "Calm": {"x": 0.41, "y": -0.91, "signal": "S1"},
    "Alarmed": {"x": -0.11, "y": 0.99, "signal": "J4"}
}

verbs = {
    "Snap": lambda t: 1 - (1 - t)**4,
    "Glide": lambda t: 3*t**2 - 2*t**3
}

sines = {
    "S1": lambda t: 0.02 * np.sin(5*t),
    "S2": lambda t: 0.05 * np.sin(10*t)
}

jitters = {
    "J1": lambda t: 0,
    "J4": lambda t: 0.15 * np.random.uniform(-1,1,len(t))
}
