from scipy.stats import poisson
from scipy.stats import binom
from scipy.stats import norm
import numpy as np
import math
import matplotlib.pyplot as plt

n = 7072
p = 0.45
x = np.arange(0, n, 1)

plt.plot(x, poisson.pmf(x, mu = n * p, loc = 0))
plt.plot(x, binom.pmf(x, n, p))
plt.plot(x, norm.pdf(x, n * p, n * p * (1 - p)))

plt.show()