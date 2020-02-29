import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.util import random_noise as rn

#-------------------------x----------------------------x-----------------------------x-----------------------x--------------------x---------
#Creating Salt & paper noise image


def outimg():
    img = cv2.imread("./Assignment 4/lena_resized.png", 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img , cv2.COLOR_RGB2GRAY)
    image = 0*img


    # for i in range(10):
    #     noise_img = rn(img, mode='s&p',amount =0.01*(i+1))
    #     image=image+noise_img

    # out1 = np.array(255 * image, dtype='uint8')

    # out = np.divide(image, 10)
    # plt.subplot(2, 1, 1)
    # plt.imshow(out1)
    # plt.subplot(2, 1, 2)
    # plt.imshow(out)
    # plt.show()
    return  img

gray = outimg()



#----------------------x--------------------x---------------------x--------------------x-----------------x--------------------x-------------
#Filter/pic


img1 = cv2.imread("./Assignment 4/lena_crop.png", 0)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img1 = cv2.cvtColor(img1 , cv2.COLOR_RGB2GRAY)




# plt.imshow(avg_filter,cmap='gray')
# plt.show()
# rows , columns = avg_filter.shape

rows , columns = img1.shape

pic = np.zeros((min(rows , columns),min(rows , columns)))
print (pic)

x=min(rows,columns)
for i in range(x):
    for j in range(x):
        pic[i][j] =pic[i][j]+ img1[i][j]


rows , columns = pic.shape
row = rows
column = columns
plt.imshow(pic,cmap='gray')
plt.show()

sk1 = 0
for i in range(rows):
    for j in range(columns):
        sk1 = sk1 + pic[i][j]
sk1 = float(sk1/(rows*columns))
print(sk1)

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
       Matrix[i+row][j+column] = Matrix[i+row][j+column] +  gray[i][j]
plt.imshow(Matrix,cmap='gray')
plt.show()

r1, c1 = Matrix.shape
print(r1,c1)
sk = 0
for i in range(r1):
    for j in range(c1):
        sk = sk + Matrix[i][j]
sk = float(sk/(r1*c1))
print(sk)

k=int((rows-1)/2)
for x in range(len(gray)+row-1):
    for y in range(len(gray)+column-1):
        sum = 0
        sum1 = 0
        sum2 = 0
        for i in range(-k,k):
            for j in range(-k,k):
                sum = sum + Matrix[x+i+k][y+j+k]*pic[i+k][j+k]
        g[x][y] = round(sum/(2*rows))
                # sum = sum + (Matrix[x+i+k][y+j+k]-sk)*(pic[i+k][j+k]-sk1)
                # sum1 = sum1 + (Matrix[x+i+k][y+j+k]-sk)**2
                # sum2 = sum2 + (pic[i+k][j+k]-sk1)**2

        # g[x][y] = float(sum/((sum1**1/2)*(sum2**1/2)))
        print (g[x][y])
jh = np.amax(g)


plt.subplot(2, 1, 1)
plt.imshow(gray ,cmap='gray')
plt.subplot(2, 1, 2)
plt.imshow(g,cmap='gray')
plt.show()


for x in range(len(gray)+row-1):
    for y in range(len(gray)+column-1):
        if jh == (g[x][y]):
            pr = x
            pk = y

n = np.zeros((row,column))

for i in range(pr,pr+row):
    for j in range(pk,pk+column):
        n[i-pr][j-pk] = Matrix[i][j]


plt.imshow(n,cmap='gray')

plt.show()

