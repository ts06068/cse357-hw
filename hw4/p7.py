import csv
import math

Dx = []
Dy = []

with open("q7_b_X.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    next(reader, None)
    for row in reader:
        num = row[0].split(",")[-1]
        Dx.append(float(num))

with open("q7_b_Y.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    next(reader, None)
    for row in reader:
        num = row[0].split(",")[-1]
        Dy.append(float(num))

# print("Dx = %s" % Dx)
# print("Dy = %s" % Dy)

sampleMeanX = sum(Dx) / len(Dx)
sampleMeanY = sum(Dy) / len(Dy)

mean_X_MLE = sampleMeanX
mean_Y_MLE = sampleMeanY

delta_MLE = mean_X_MLE - mean_Y_MLE

variance_X_MLE = sum([(x - mean_X_MLE) ** 2 for x in Dx]) / len(Dx)
variance_Y_MLE = sum([(y - mean_Y_MLE) ** 2 for y in Dy]) / len(Dy)

se_delta_MLE = (variance_X_MLE / len(Dx) + variance_Y_MLE / len(Dy)) ** 0.5

# perform Wald's test

W = math.fabs(delta_MLE / se_delta_MLE)

alpha = 0.05
z_alpha = 1.96

print("mean_X_MLE = %.5f" % mean_X_MLE)
print("mean_Y_MLE = %.5f" % mean_Y_MLE)
print("variance_X_MLE = %.5f" % variance_X_MLE)
print("variance_Y_MLE = %.5f" % variance_Y_MLE)


print("delta_MLE = %.5f" % delta_MLE)
print("se_delta_MLE = %.5f" % se_delta_MLE)
print("W = %.5f" % W)
print("z_alpha = %.5f" % z_alpha)

if W > z_alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")
