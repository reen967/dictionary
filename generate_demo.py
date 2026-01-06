import numpy as np
import json
from sentence_engine import generate_sentence  # your MVP engine

t = np.linspace(0, 1, 100)
signal = generate_sentence("Sleepy", "Alarmed", "Snap", t)

json_data = {"t": t.tolist(), "signal": signal.tolist()}
with open("data/demo_signals.json", "w") as f:
    json.dump(json_data, f)

print("demo_signals.json generated!")
