import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread("./Assignment 3/lena.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# img = cv2.resize(img,None,fx = 0.5,fy = 0.5 ,interpolation=cv2.INTER_LINEAR)
# scaling to 0.5 by taking 4 pixels as 1

out1 = np.ones(shape=(512,256))
out2 = np.ones(shape=(256,256))

for i in range(0,511,1):
    for j in range(0,510,2):
        out1[i][int(j/2)] = img[i][j]/2+img[i][j+1]/2
for j in range(0,256,1):
    for i in range(0,510,2):
        out2[int(i/2)][j] = out1[i][j]+out1[i+1][j]/2 


img = cv2.resize(img,None,fx = 0.5,fy = 0.5 ,interpolation=cv2.INTER_AREA)
plt.subplot(2,1,1)
plt.imshow(img,cmap='gray')
plt.subplot(2,1,2)
plt.imshow(out2,cmap='gray')
plt.show()