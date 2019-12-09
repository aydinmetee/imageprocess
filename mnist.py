import math
import numpy as np
import matplotlib.pyplot as plt

data_path="/home/mete/"
train_data=np.loadtxt(data_path +"mnist_train.csv",delimiter=",")
train_test=np.loadtxt(data_path +"mnist_test.csv",delimiter=",")

def ortalama_varyans(k=0,l=0,m=10000):
    s=0;
    t=0;
    for i in range(m):
        if(train_data[i,0]==k):
            s=s+1
            t=t+train_data[i,l+1]
    ortalama=t/s
    t=0
    s=0
    for i in range(m):
        if(train_data[i,0]==k):
            s=s+1
            diff_1=train_data[i,l+1]-ortalama
            t=t+diff_1*diff_1
    varyans=t/(s-1)

    return ortalama,varyans

def my_pdf_1(x,mu=0.0,sigma=0.0):
    eps=np.finfo(float).eps
    x=float(x-mu)/(sigma+eps)
    return math.exp(-x*x/2.0)/math.sqrt(2.0*math.pi)/(sigma+eps)

im_1=plt.imread("index.png")
plt.imshow(im_1,cmap='gray')
plt.show()

