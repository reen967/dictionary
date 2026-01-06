import numpy as np
from dictionary import nouns, verbs, sines, jitters

def generate_sentence(start_noun, end_noun, verb_name, t_array):
    start = nouns[start_noun]
    end = nouns[end_noun]
    verb = verbs[verb_name]

    u = verb(t_array)
    theta = np.arctan2(end["y"], end["x"]) - np.arctan2(start["y"], start["x"])
    theta_t = np.arctan2(start["y"], start["x"]) + u * theta

    # Mix signals
    x_t = np.cos(theta_t)
    y_t = np.sin(theta_t)
    signal = np.zeros_like(t_array)

    for i in range(len(t_array)):
        if x_t[i] > 0:
            signal[i] = y_t[i] + sines[start["signal"]](t_array[i])
        else:
            signal[i] = y_t[i] + jitters[start["signal"]](t_array[i])

    return signal
