import csv
import math
from random import sample

from numpy import mat

height_female_a = []
height_female_b = []

# Settlement A
with open("height_female.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader, None)
    for row in reader:
        height_female_a.append(float(row[0]))

# Settlement B
with open("height_female_200.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader, None)
    for row in reader:
        height_female_b.append(float(row[0]))

# Perform Z test for single population
sampleMeanHeightFemaleA = sum(height_female_a) / len(height_female_a)
sampleMeanHeightFemaleB = sum(height_female_b) / len(height_female_b)

print("sampleMeanHeightFemaleA: ", sampleMeanHeightFemaleA)  # u0
print("sampleMeanHeightFemaleB: ", sampleMeanHeightFemaleB)

# H0: sampleMeanHeightFemaleB = sampleMeanHeightFemaleA (X_bar = u0)
# H1: sampleMeanHeightFemaleB != sampleMeanHeightFemaleA (X_bar != u0)
# Z test is possible because n > 30

n = 200
v = 121

alpha = 0.05

Z = abs((sampleMeanHeightFemaleB - sampleMeanHeightFemaleA) / (math.sqrt(v / n)))

print("Z: ", Z)  # > 1.96, reject H0
print("Z > 1.96, reject H0")


# Perform Z test for two independent population, this time male and female in settlement A

height_female_a_first50 = height_female_a[:50]
height_male_a = []
height_male_a_first50 = []

with open("height_male.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader, None)
    for row in reader:
        height_male_a.append(float(row[0]))

height_male_a_first50 = height_male_a[:50]

print(len(height_female_a_first50))
print(len(height_male_a_first50))

sampleMeanHeightFemaleAFirst50 = sum(height_female_a_first50) / 50
sampleMeanHeightMaleAFirst50 = sum(height_male_a_first50) / 50

print("sampleMeanHeightFemaleAFirst50: ", sampleMeanHeightFemaleAFirst50)
print("sampleMeanHeightMaleAFirst50: ", sampleMeanHeightMaleAFirst50)


# H0: d = 0
# H1: d != 0
# d = sampleMeanHeightFemaleA - sampleMeanHeightMaleA
# Assumption: X and Y are iid sample from normal distribution
# Z test is possible because n > 30

v_male_a = 110
v_female_a = 121

Z2 = abs(
    (sampleMeanHeightMaleAFirst50 - sampleMeanHeightFemaleAFirst50)
    / math.sqrt(v_male_a / 50 + v_female_a / 50)
)

print("Z: ", Z2)  # > 1.96, reject H0
print("Z > 1.96, reject H0")


# Perform T test for single population in settlement B male
# H0 = u = u0
# H1 = u != u0
# Assumption: X is iid sample from normal distribution

sampleMaleHeightB = [
    157.74,
    155.98,
    186.2,
    171.63,
    169.11,
    168.71,
    179.55,
    174.7,
    183.09,
    152.33,
]

meanHeightMaleA = sum(height_male_a) / len(height_male_a)
sampleMeanHeightMaleB = sum(sampleMaleHeightB) / len(sampleMaleHeightB)
correctedSampleVarianceHeightMaleB = 0

for i in range(len(sampleMaleHeightB)):
    correctedSampleVarianceHeightMaleB += (
        sampleMaleHeightB[i] - sampleMeanHeightMaleB
    ) ** 2

correctedSampleVarianceHeightMaleB /= len(sampleMaleHeightB) - 1

print("meanHeightMaleA: ", meanHeightMaleA)
print("sampleMeanHeightMaleB: ", sampleMeanHeightMaleB)

T = abs(
    (sampleMeanHeightMaleB - meanHeightMaleA)
    / (math.sqrt(correctedSampleVarianceHeightMaleB / len(sampleMaleHeightB)))
)

print("T: ", T)  # > t 0.05, 9 = 2.262, reject H0
print("T < 2.262, accept H0")


# Conduct paired T test
# H0: d = 0
# H1: d != 0
# Assumption: d is iid sample from normal distribution

sampleMaleHeightANow = [
    158.2,
    160.5,
    174.1,
    162.36,
    162.84,
    172.70,
    186.92,
    183.01,
    167.22,
    159.19,
]
sampleMaleHeightALater = [
    167.04,
    161.54,
    174.31,
    162.56,
    163.84,
    172.73,
    188.62,
    184.62,
    168.43,
    171.19,
]

d = []

for i in range(len(sampleMaleHeightANow)):
    d.append(sampleMaleHeightANow[i] - sampleMaleHeightALater[i])

sampleMeanD = sum(d) / len(d)
correctedVarianceD = 0

for i in range(len(d)):
    correctedVarianceD += (d[i] - sampleMeanD) ** 2

correctedVarianceD /= len(d) - 1

T2 = abs(sampleMeanD / (math.sqrt(correctedVarianceD / len(d))))

print("T2: ", T2)  # > t 0.05, 9 = 2.262, reject H0
print("T2 < 2.262, accept H0")


# Conduct unpaired T test for 2 independent population
# Assumption: each X and Y are iid sample from normal distribution

sampleMaleHeightAIndependent1 = [
    158.17,
    175.87,
    147.86,
    138.77,
    165.57,
    166.56,
    180.09,
    175.14,
    171.21,
    179.0,
]
sampleMaleHeightAIndependent2 = [
    145.74,
    174.73,
    154.43,
    142.25,
    142.74,
    160.88,
    160.82,
    170.01,
    165.45,
    170.04,
]

sampleMeanHeightMaleIndependent1 = sum(sampleMaleHeightAIndependent1) / len(
    sampleMaleHeightAIndependent1
)
sampleMeanHeightMaleIndependent2 = sum(sampleMaleHeightAIndependent2) / len(
    sampleMaleHeightAIndependent2
)

correctedVaricneHeightMaleIndependent1 = 0
correctedVarianceHeightMaleIndependent2 = 0

for i in range(len(sampleMaleHeightAIndependent1)):
    correctedVaricneHeightMaleIndependent1 += (
        sampleMaleHeightAIndependent1[i] - sampleMeanHeightMaleIndependent1
    ) ** 2
    correctedVarianceHeightMaleIndependent2 += (
        sampleMaleHeightAIndependent2[i] - sampleMeanHeightMaleIndependent2
    ) ** 2

correctedVaricneHeightMaleIndependent1 /= len(sampleMaleHeightAIndependent1) - 1
correctedVarianceHeightMaleIndependent2 /= len(sampleMaleHeightAIndependent2) - 1

print("sampleMeanHeightMaleIndependent1: ", sampleMeanHeightMaleIndependent1)
print("sampleMeanHeightMaleIndependent2: ", sampleMeanHeightMaleIndependent2)

T3 = abs(
    (sampleMeanHeightMaleIndependent1 - sampleMeanHeightMaleIndependent2)
    / math.sqrt(
        correctedVaricneHeightMaleIndependent1 / len(sampleMaleHeightAIndependent1)
        + correctedVarianceHeightMaleIndependent2 / len(sampleMaleHeightAIndependent2)
    )
)

print("T3: ", T3)  # > t 0.05, 18 = 2.101, reject H0
print("T3 < 2.101, accept H0")
