import math
import matplotlib.pyplot as plt
import numpy as np

data_path="/home/mete/"
train_data=np.loadtxt(data_path+"mnist_train.csv",delimiter=",")
test_data=np.loadtxt(data_path+"mnist_test.csv",delimiter=",")

print(test_data[:10])
