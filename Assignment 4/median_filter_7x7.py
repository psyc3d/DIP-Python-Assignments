import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.util import random_noise as rn

#-------------------------x----------------------------x-----------------------------x-----------------------x--------------------x---------
#Creating Salt & paper noise image


def outimg():
    img = cv2.imread("./lena.png", 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img , cv2.COLOR_RGB2GRAY)
    image = 0*img

    for i in range(10):
        noise_img = rn(img, mode='s&p',amount =0.01*(i+1))
        image=image+noise_img

    out1 = np.array(255 * image, dtype='uint8')

    out = np.divide(image, 10)
    plt.subplot(2, 1, 1)
    plt.imshow(out1)
    plt.subplot(2, 1, 2)
    plt.imshow(out)
    plt.show()
    return  out

gray = outimg()


#----------------------x--------------------x---------------------x--------------------x-----------------x--------------------x-------------
#Filter
median_filter = []
row = 7
column = 7

for r in range(row):
    r=[]
    for col in range(column):
        r.append(1.0)
    median_filter.append(r)


#-----------------------x-----------------------x--------------------x----------------------x------------------------x------------------x---------
#corelation

l=len(gray) + 2*row
m=len(gray) + 2*column
Matrix = []
g=[]


Matrix = np.zeros((m,l))
g = np.zeros((m-row-1, l-column-1))


for i in range(len(gray)):
    for j in range(len(gray)):
       Matrix[i+row][j+column] = Matrix[i+row][j+column] + gray[i][j]


#---------------------------------------x--------------------------x-----------------------------x----------------------------x--------------------
for x in range(len(gray)+row-1):
    for y in range(len(gray)+column-1):
        sum = 0
        for i in range(-1,1):
            for j in range(-1,1):
                sum = sum + Matrix[x+i][y+j]*median_filter[i+1][j+1]
        g[x][y] = sum

#---------------------------x----------------------------------x---------------------------------x--------------------------x-----------------------

plt.subplot(2, 1, 1)
plt.imshow(gray ,cmap='gray')
plt.subplot(2, 1, 2)
plt.imshow(g,cmap='gray')
plt.show()
