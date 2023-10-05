import csv
import matplotlib.pyplot as plt
import numpy as np


dictfreq = dict()
dictcum = dict()

with open("pokemon.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    next(reader, None)
    numsamples = 0
    for row in reader:
        num = int(", ".join(row))
        try:
            dictfreq[num] += 1
        except KeyError:
            dictfreq[num] = 1
        numsamples += 1

freqlist = sorted(dictfreq.items(), key=lambda x: x[0])
keys = sorted(dictfreq.keys())

for i in range(len(keys)):
    try:
        dictcum[keys[i]] = dictcum[keys[i - 1]] + dictfreq[keys[i]]
    except KeyError:
        dictcum[keys[i]] = dictfreq[keys[i]]

cumlist = sorted(dictcum.items(), key=lambda x: x[0])

# construct a 95% confidence interval for ecdf
upper = []
lower = []

for i in range(len(cumlist)):
    upper.append(
        cumlist[i][1] / numsamples
        + (
            np.sqrt(
                (cumlist[i][1] / numsamples)
                * (1 - (cumlist[i][1] / numsamples))
                / numsamples
            )
        )
        * 1.96
    )
    lower.append(
        cumlist[i][1] / numsamples
        - (
            np.sqrt(
                (cumlist[i][1] / numsamples)
                * (1 - (cumlist[i][1] / numsamples))
                / numsamples
            )
        )
        * 1.96
    )

print("numsamples = %d" % numsamples)
print("cumlist = %s" % cumlist)

X = []
Y = []

for i in range(len(cumlist)):
    X = X + [cumlist[i][0]]
    Y = Y + [cumlist[i][1] / numsamples]

plt.figure("eCDF")
plt.plot(X, Y, label="eCDF")
plt.plot(X, upper, label="upper bound")
plt.plot(X, lower, label="lower bound")
plt.scatter(X, [0] * len(X), color="purple", marker="x", s=50, label="samples")
plt.xlabel("x")
plt.ylabel("Pr[X<=x]")
plt.legend(loc="upper left")
plt.grid()
plt.show()
