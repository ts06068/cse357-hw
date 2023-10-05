import matplotlib.pyplot as plt
import random


dictfreq = dict()
dictcum = dict()

dictfreqList = [dict(), dict(), dict()]  # 10, 100, 1000
dictcumList = [dict(), dict(), dict()]  # 10, 100, 1000
numsamples = [0, 0, 0]
result = [[], [], []]

samplesize = [10, 100, 1000]

# for each sample size,
for n in range(len(samplesize)):
    # make a frequency list
    for i in range(samplesize[n]):
        num = random.randint(1, 99)
        try:
            dictfreqList[n][num] += 1
        except KeyError:
            dictfreqList[n][num] = 1
        numsamples[n] += 1

    freqlist = sorted(dictfreqList[n].items(), key=lambda x: x[0])
    keys = sorted(dictfreqList[n].keys())

    print(freqlist)

    # make a cumulative frequency list
    for i in range(len(keys)):
        try:
            dictcumList[n][keys[i]] = (
                dictcumList[n][keys[i - 1]] + dictfreqList[n][keys[i]]
            )
        except KeyError:
            dictcumList[n][keys[i]] = dictfreqList[n][keys[i]]

    result[n] = sorted(dictcumList[n].items(), key=lambda x: x[0])

    print("numsamples = %d" % numsamples[n])
    print("cumlist = %s" % result[n])

# create a x and y list for each sample size for plotting
X = [[], [], []]
Y = [[], [], []]

for i in range(len(result)):
    X[i] = [0, 0]
    Y[i] = [0, 0]
    for j in range(len(result[i])):
        X[i] = X[i] + [result[i][j][0], result[i][j][0]]
        Y[i] = Y[i] + [result[i][j][1] / samplesize[i], result[i][j][1] / samplesize[i]]
    X[i] = X[i] + [100, 100]
    Y[i] = Y[i] + [1, 1]

plt.figure("eCDF")

for i in range(len(numsamples)):
    plt.plot(X[i], Y[i], label="eCDF %d" % numsamples[i] + " samples")
    plt.scatter(
        X[i],
        [0] * len(X[i]),
        color=["red", "green", "purple"][i % 3],
        marker="x",
        s=[100, 50, 10][i % 3],
        label="samples",
    )
plt.xlabel("x")
plt.ylabel("Pr[X<=x]")
plt.legend(loc="upper left")
plt.grid()
plt.show()
