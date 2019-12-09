import numpy as np
import matplotlib.pyplot as plt

im_1=plt.imread("test.jpg")
m,n,p=im_1.shape
im_3=np.zeros((m,n),dtype=np.uint8)
im_3=im_1[:,:,0]

im_4=np.zeros((m,n),dtype=np.uint8)

for i in range(1,m-1):
    for j in range(1,n-1):
        s=(im_3[i+1,j]/9+im_3[i+1,j-1]/9+im_3[i+1,j+1]/9+
        im_3[i,j]/9+im_3[i,j-1]/9+im_3[i,j+1]/9+
        im_3[i-1,j]/9+im_3[i-1,j-1]/9+im_3[i-1,j+1]/9)
        im_4[i,j]=int(s)

plt.subplot(1,2,1)
plt.imshow(im_4,cmap='gray')
plt.show()
