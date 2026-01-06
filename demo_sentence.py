import numpy as np
from url.sentence_engine import generate_sentence

t = np.linspace(0,1,100)
signal = generate_sentence("Sleepy","Alarmed","Snap", t)
print(signal)
