import numpy as np
from .dictionary import NOUNS, VERBS, SINES, JITTERS

def generate_sentence(start_noun, end_noun, verb_name, t_array):
    """
    Generate a life signal from start -> end noun via verb
    t_array: np.linspace(0,1,num_points)
    """
    start = NOUNS[start_noun]
    end = NOUNS[end_noun]
    delta_theta = (end["theta"] - start["theta"] + 180) % 360 - 180
    verb_func = VERBS[verb_name]

    signals = []
    for t in t_array:
        u = verb_func(t)
        theta_t = start["theta"] + delta_theta * u
        x_t = np.cos(np.deg2rad(theta_t))
        y_t = np.sin(np.deg2rad(theta_t))
        # Choose pulse or jitter
        signal_fn = SINES[start["signal"]] if x_t > 0 else JITTERS[start["signal"]]
        signal_value = signal_fn() * y_t if callable(signal_fn) else signal_fn
        signals.append(signal_value)
    return np.array(signals)
