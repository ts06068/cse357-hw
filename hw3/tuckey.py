import numpy as np


def tuckey(nums, alpha):
    q3 = np.percentile(nums, 75, axis=0)
    q1 = np.percentile(nums, 25)
    iqr = q3 - q1
    lower = q1 - alpha * iqr
    upper = q3 + alpha * iqr
    print("q1 = %f, q3 = %f, iqr = %f" % (q1, q3, iqr))
    print("lower = %f, upper = %f" % (lower, upper))
    return lower, upper


tuckey([14, 300, 13, 11, 67, 10, 12, 45, 2, 7, 68, 77, 50], 1.5)
