import csv
import math

sepal_length = []  # ~ N(5.84, 0.69)
sepal_width = []  # ~ Uniform(2.0, 4.4)
petal_width = []  # ~ Exp(1.19)

with open("iris.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar="|")
    next(reader, None)
    for row in reader:
        sepal_length.append(float(row[3]))
        sepal_width.append(float(row[4]))
        petal_width.append(float(row[6]))

sampleMean_sepal_length = sum(sepal_length) / len(sepal_length)
sampleMean_sepal_width = sum(sepal_width) / len(sepal_width)
sampleMean_petal_width = sum(petal_width) / len(petal_width)

# sepal_length
mean_sepal_length_MLE = sampleMean_sepal_length
variance_sepal_length_MLE = sum(
    [(x - mean_sepal_length_MLE) ** 2 for x in sepal_length]
) / len(sepal_length)

mean_sepal_length_MME = sampleMean_sepal_length
variance_sepal_length_MME = (
    sum([x**2 for x in sepal_length]) / (len(sepal_length))
    - mean_sepal_length_MME**2
)

# sepal_width
a_sepal_width_MLE = min(sepal_width)
b_sepal_width_MLE = max(sepal_width)

a_sepal_width_MME = sampleMean_sepal_width - math.sqrt(3) * math.sqrt(
    sum([(x - sampleMean_sepal_width) ** 2 for x in sepal_width]) / len(sepal_width)
)
b_sepal_width_MME = sampleMean_sepal_width + math.sqrt(3) * math.sqrt(
    sum([(x - sampleMean_sepal_width) ** 2 for x in sepal_width]) / len(sepal_width)
)

# petal_width
lambda_petal_width_MLE = 1 / sampleMean_petal_width
lambda_petal_width_MME = 1 / sampleMean_petal_width


print("mean_sepal_length_MLE = %.5f" % mean_sepal_length_MLE)
print("variance_sepal_length_MLE = %.5f" % variance_sepal_length_MLE)
print("mean_sepal_length_MME = %.5f" % mean_sepal_length_MME)
print("variance_sepal_length_MME = %.5f" % variance_sepal_length_MME)

print("a_sepal_width_MLE = %.5f" % a_sepal_width_MLE)
print("b_sepal_width_MLE = %.5f" % b_sepal_width_MLE)
print("a_sepal_width_MME = %.5f" % a_sepal_width_MME)
print("b_sepal_width_MME = %.5f" % b_sepal_width_MME)

print("lambda_petal_width_MLE = %.5f" % lambda_petal_width_MLE)
print("lambda_petal_width_MME = %.5f" % lambda_petal_width_MME)
