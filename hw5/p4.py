import csv
import itertools
import random


def ecdf(data):
    dictfreq = dict()
    dictcum = dict()

    # make a frequency list
    for i in range(len(data)):
        try:
            dictfreq[data[i]] += 1
        except KeyError:
            dictfreq[data[i]] = 1

    numsamples = len(data)

    freqlist = sorted(dictfreq.items(), key=lambda x: x[0])
    keys = sorted(dictfreq.keys())

    # make a cumulative frequency list
    for i in range(len(keys)):
        try:
            dictcum[keys[i]] = dictcum[keys[i - 1]] + dictfreq[keys[i]]
        except KeyError:
            dictcum[keys[i]] = dictfreq[keys[i]]

    cumlist = sorted(dictcum.items(), key=lambda x: x[0])

    for i in range(len(cumlist)):
        cumlist[i] = (
            cumlist[i][0],
            cumlist[i][1] / numsamples,
        )

    return cumlist


def closestPointLeft(data, x):
    for i in range(len(data)):
        if data[i][0] > x:
            return i - 1
    return len(data) - 1


def closestPointRight(data, x):
    for i in range(len(data)):
        if data[i][0] >= x:
            return i
    return len(data) - 1


def KSTest(data1, data2):
    d_max = 0

    print("----------------------------------")
    for i in range(1, len(data1)):
        fx_minus = data1[i - 1][1]
        fx_plus = data1[i][1]
        fy_minus = data2[closestPointLeft(data1, data1[i][0])][1]
        fy_plus = data2[closestPointRight(data1, data1[i][0])][1]
        d_minus = abs(fx_minus - fy_minus)
        d_plus = abs(fx_plus - fy_plus)

        print("", i)
        print("\tfx-, fx+: \t", fx_minus, fx_plus)
        print("\tfy-, fy+: \t", fy_minus, fy_plus)
        print("\td-, d+: \t", d_minus, d_plus)
        d_max = max(d_max, d_minus, d_plus)
    print("----------------------------------")

    return d_max


confirmed = []
temperature = []
humidity = []

confirmed_cold = []
confirmed_warm = []

confirmed_humid = []
confirmed_dry = []

with open("a5_q4.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader, None)
    for row in reader:
        confirmed.append(int(row[-7]))
        temperature.append(float(row[-2]))
        humidity.append(float(row[-1]))

for i in range(len(confirmed)):
    if temperature[i] < 12:
        confirmed_cold.append(confirmed[i])
    else:
        confirmed_warm.append(confirmed[i])
    if humidity[i] < 65:
        confirmed_dry.append(confirmed[i])
    else:
        confirmed_humid.append(confirmed[i])

# print("Confirmed cases: ", confirmed)
# print("Temperature: ", temperature)
# print("Humidity: ", humidity)

# eCDF for confirmed cases
ecdf_confirmed_cold = ecdf(confirmed_cold)
ecdf_confirmed_warm = ecdf(confirmed_warm)
ecdf_confirmed_dry = ecdf(confirmed_dry)
ecdf_confirmed_humid = ecdf(confirmed_humid)

ecdf_confirmed_cold = [(-1, 0)] + ecdf_confirmed_cold
ecdf_confirmed_warm = [(-1, 0)] + ecdf_confirmed_warm

# print("eCDF for confirmed cases")
# print("Cold: ", ecdf_confirmed_cold)
# print("Warm: ", ecdf_confirmed_warm)

# Perform KS test for ecdf_confirmed_cold and ecdf_confirmed_warm


print(
    "KS test for ecdf_confirmed_cold and ecdf_confirmed_warm: ",
    KSTest(ecdf_confirmed_cold, ecdf_confirmed_warm),
)

print(
    "KS test for ecdf_confirmed_dry and ecdf_confirmed_humid: ",
    KSTest(ecdf_confirmed_dry, ecdf_confirmed_humid),
)

m = len(confirmed_cold)
n = len(confirmed_warm)

Tobs = abs(
    sum(confirmed_cold) / len(confirmed_cold)
    - sum(confirmed_warm) / len(confirmed_warm)
)


for i in [500, 1000]:
    acc = 0
    new_confirmed_cold_warm = confirmed_cold + confirmed_warm
    for j in range(i):
        random.shuffle(new_confirmed_cold_warm)

        new_confirmed_cold = new_confirmed_cold_warm[:m]
        new_confirmed_warm = new_confirmed_cold_warm[m:]

        Ti = abs(
            sum(new_confirmed_cold) / len(new_confirmed_cold)
            - sum(new_confirmed_warm) / len(new_confirmed_warm)
        )

        if Ti > Tobs:
            acc += 1

    print("p-value for", i, "permutations for confirmed_cold_warm: ", acc / i)

for i in [500, 1000]:
    acc = 0
    new_confirmed_dry_humid = confirmed_dry + confirmed_humid
    for j in range(i):
        random.shuffle(new_confirmed_dry_humid)

        new_confirmed_dry = new_confirmed_dry_humid[:m]
        new_confirmed_humid = new_confirmed_dry_humid[m:]

        Ti = abs(
            sum(new_confirmed_dry) / len(new_confirmed_dry)
            - sum(new_confirmed_humid) / len(new_confirmed_humid)
        )

        if Ti > Tobs:
            acc += 1
    print("p-value for", i, "permutations for confirmed_dry_humid: ", acc / i)
