import numpy as np
import matplotlib.pyplot as plt
from scipy import special

mu = 0  # mean
sigma = 1  # standard deviation
sample = 1000  # sample times

S = np.random.normal(mu, sigma, sample)
n = len(S)
Srt = sorted(S)
delta = 0.1
X = [min(Srt) - delta]
Y = [0]
for i in range(0, n):
    X = X + [Srt[i], Srt[i]]
    Y = Y + [Y[len(Y) - 1], Y[len(Y) - 1] + (1 / n)]
X = X + [max(Srt) + delta]
Y = Y + [1]

Y2 = []
X2 = np.arange(min(Srt) - 10 * delta, max(Srt) + 10 * delta, 0.1)
for i in X2:
    Y2.append((1 + special.erf((i - mu) / (np.sqrt(2 * (sigma**2))))) / 2)

plt.figure("eCDF")
plt.plot(X, Y, label="eCDF")
plt.scatter(Srt, [0] * n, color="red", marker="x", s=100, label="samples")
if 1:
    plt.plot(X2, Y2, label="true CDF")
plt.xlabel("x")
plt.ylabel("Pr[X<=x]")
plt.title("eCDF with %d samples. Sample mean = %.2f." % (n, np.mean(S)))
plt.legend(loc="upper left")
plt.grid()
plt.show()
