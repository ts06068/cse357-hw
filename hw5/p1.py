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


data = [1.33, 3.11, 1.99, 1.61, 2.31, 3.6, 2.25, 3.4, 2.71, 2.56]
data = sorted(data)

print("data: ", data)
