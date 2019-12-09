import numpy as np
import matplotlib.pyplot as plt

def red_deger(im_3,s):
    im_1=im_3
    m,n,p=im_1.shape
    im_2=np.zeros((m,n,3),dtype=int)
    im_2=im_2.astype(np.uint8)
    for m in range(im_1.shape[0]):
        for n in range(im_1.shape[1]):
            if(im_1[m,n,0]<204):
                im_2[m,n,0]=im_1[m,n,0]+s
            
            im_2[m,n,1]=im_1[m,n,1]
            im_2[m,n,2]=im_1[m,n,2]
    return im_2

def boyutlandir(im_3):
    im_1=im_3
    m,n,p=im_1.shape
    new_m=int(m/2)
    new_n=int(n/2)
    im_2=np.zeros((new_m,new_n),dtype=int)
    for m in range(im_2.shape[0]):
        for n in range(im_2.shape[1]):
            s=(im_1[m*2,n*2,0]+im_1[m*2,n*2,1]+im_1[m*2,n*2,2])/3
            im_2[m,n]=int(s)

    return im_2

def bozulmadan_boyutlandir(im_3):
    im_1=im_3
    m,n,p=im_1.shape
    new_m=int(m/2)
    new_n=int(n/2)
    im_2=np.zeros((new_m,new_n,3),dtype=int)
    im_2=im_2.astype(np.uint8)
    for m in range(im_2.shape[0]):
        for n in range(im_2.shape[1]):
            im_2[m,n,0]=int(im_1[m*2,n*2,0])
            im_2[m,n,1]=int(im_1[m*2,n*2,1])
            im_2[m,n,2]=int(im_1[m*2,n*2,2])
    return im_2

def siyah_beyaz(im_3):
    im_1=im_3
    m,n,p=im_1.shape
    im_2=np.zeros((m,n),dtype=float)
    im_1=im_1.astype(np.float32)

    for m in range(im_1.shape[0]):
        for n in range(im_1.shape[1]):
            s=(im_1[m,n,0]+im_1[m,n,1]+im_1[m,n,2])/3
            im_2[m,n]=s
    return im_2;

def doksan_cevir(im_3):
    im_1=im_3
    m,n,p=im_1.shape
    im_2=np.zeros((n,m,3),dtype=int)
    im_2=im_2.astype(np.uint8)
    for m in range(im_1.shape[0]):
        for n in range(im_1.shape[1]):
            im_2[n,m,0]=im_1[m,n,0]
            im_2[n,m,1]=im_1[m,n,1]
            im_2[n,m,2]=im_1[m,n,2]
    return im_2

def ters_cevir(im_3):
    im_1=im_3
    m,n,p=im_1.shape
    s=im_1.shape[0]-1
    p=im_1.shape[1]-1
    im_2=np.zeros((m,n,3),dtype=int)
    im_2=im_2.astype(np.uint8)
    for m in range(im_1.shape[0]):
        for n in range(im_1.shape[1]):
            im_2[s-m,p-n,0]=im_1[m,n,0]
            im_2[s-m,p-n,1]=im_1[m,n,1]
            im_2[s-m,p-n,2]=im_1[m,n,2]
    return im_2

def kac_var_red(im_3=plt.imread('test.jpg')):
    my_histogram={}
    m,n,p=im_3.shape
    for i in range(m):
        for j in range(n):
            if im_3[i,j,0] in my_histogram.keys():
                my_histogram[im_3[i,j,0]]=my_histogram[im_3[i,j,0]]+1
            else:
                my_histogram[im_3[i,j,0]]=1
    return my_histogram

def kac_var_tablo(my_histogram=kac_var_red()):
    x=[]
    y=[]
    for key in my_histogram.keys():
        x.append(key)
        y.append(my_histogram[key])
    return x,y

im_test=plt.imread('test.jpg')
#print(type(im_test[100,100,1]))
#plt.imshow(im_test)
#plt.show()
x,y=kac_var_tablo()
plt.bar(x,y)
plt.show()

#plt.imshow(im_new,cmap='gray')
#plt.show()

