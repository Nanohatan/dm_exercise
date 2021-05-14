"""
>>> true_function(0)
0.0
"""
import numpy as np
import matplotlib.pyplot as plt

def true_function(x):
    y = np.sin(np.pi * x * 0.8) * 10
    return y

freqs = np.arange(-1.0, 1.0, 0.1)
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
t = np.arange(-1.0, 1.0, 0.1)
s = np.sin(np.pi * t * 0.8)*10
l, = plt.plot(t, s, lw=2)
plt.show()

if __name__ == "__main__":
    import doctest
    doctest.testmod()