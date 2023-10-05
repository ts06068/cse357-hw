import matplotlib.pyplot as plt
import random


dictfreq = dict()
dictcum = dict()

eCDFs = []  # 10, 100, 1000
numsamples = [0, 0, 0]

num_students = [10, 100, 1000]

# for each list of samples (10, 100, 1000 students in each list, and each student has 10 samples),
for n in range(len(num_students)):
    result = []
    avg_result = []

    for j in range(num_students[n]):
        dictfreq = dict()

        # make a frequency list for each student in the list
        for i in range(10):
            num = random.randint(1, 99)
            try:
                dictfreq[num] += 1
            except KeyError:
                dictfreq[num] = 1
            numsamples[n] += 1

        # So, in result, in each row a student gets 10 sample data.
        # result[i][j] means i-th student's freqency of j-th sample data.
        result.append(dictfreq)

    # print("result = %s" % result)

    sum_result = dict()

    # sum up all the frequency of each sample data
    for i in range(len(result)):
        for k in result[i].keys():
            try:
                sum_result[k] += result[i][k]
            except KeyError:
                sum_result[k] = result[i][k]

    # print("sum_result = %s" % sum_result)

    keys = sorted(sum_result.keys())
    sum_ecdf = dict()

    # make a cumulative frequency list
    for i in range(0, len(keys)):
        try:
            sum_ecdf[keys[i]] = sum_ecdf[keys[i - 1]] + sum_result[keys[i]]
        except:
            sum_ecdf[keys[i]] = sum_result[keys[i]]

    print("sum_ecdf = %s" % sum_ecdf)
    eCDFs.append(sorted(sum_ecdf.items(), key=lambda x: x[0]))


# create a x and y plot list for each student size. For Y, divide by the total number of samples (# of samples for each student * # of students)
X = [[], [], []]
Y = [[], [], []]

for i in range(len(eCDFs)):
    X[i] = [0, 0]
    Y[i] = [0, 0]
    for j in range(len(eCDFs[i])):
        X[i] = X[i] + [eCDFs[i][j][0], eCDFs[i][j][0]]
        Y[i] = Y[i] + [eCDFs[i][j][1] / numsamples[i], eCDFs[i][j][1] / numsamples[i]]
    X[i] = X[i] + [100, 100]
    Y[i] = Y[i] + [1, 1]

plt.figure("eCDF")

for i in range(len(numsamples)):
    plt.plot(
        X[i],
        Y[i],
        label="eCDF %d" % num_students[i] + " students, each has %d samples" % 10,
    )
plt.xlabel("x")
plt.ylabel("Pr[X<=x]")
plt.legend(loc="upper left")
plt.grid()
plt.show()
