# take the lena image and add s&p noise to it
import cv2
import numpy as np
from matplotlib import pyplot as plt 
from skimage.util import random_noise as rn  


# Generating set
img1 = cv2.imread("./Assignment 4/2a_resized.png",0)
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img1 = cv2.cvtColor(img1,cv2.COLOR_RGB2GRAY)

img2 = cv2.imread("./Assignment 4/2a_crop.png",0)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)

print(img1.shape)
print(img2.shape)
# plt.subplot(2,1,1)
# plt.imshow(img1)
# plt.subplot(2,1,2)
# plt.imshow(img2)
# plt.show()

r1,c1 = img1.shape
r2,c2 = img2.shape

print(r1,c1)
print(r2,c2)
s = np.zeros((r1+2*r2-1,c1+2*c2-1))
for i in range(r1):
    for j in range(c1):
        s[i+r2][j+c2] = img1[i][j]
li = np.zeros((r1+r2-1,c1+c2-1))

for i in range(0,r1+r2-1):
    for j in range(0,c1+c2-1):
        sum = 0
        for k in range(0,r2):
            for m in range(0,c2):
                sum = sum + img2[k][m]*s[i][j]        
        li[i][j] = sum
        print(li[i][j])


plt.imshow(li,cmap='gray')
plt.show()
jh = np.amax(li)

n = np.zeros((r2,c2))

r3,c3 = li.shape
for x in range(r3):
    for y in range(c3):
        if jh == li[x][y]:
            pr = x
            pk = y

for i in range(pr,pr+r2):
    for j in range(pk,pk+c2):
        n[i-pr][j-pk] = img1[i][j]

plt.imshow(n,cmap='gray')

plt.show()








# Creating the filter

# ni = rn(img,mode = 's&p')
# ni = np.array(255*ni, dtype = 'uint8')
# print("Please give the filter size")
# a = int(input())
# ip = np.zeros((512+2*a-2,512+2*a-2))
# outimg = np.zeros((512+2*a-2,512+2*a-2))

# for i in range(0,512):
#     for j in range(0,512):
#         ip[i+a-1][j+a-1]=ni[i][j]

# for i in range(a-1,512+2*a-2):
#     for j in range(a-1,512+2*a-2):
#         for k in range(i-a-1,i):
#             for m in range(j-a-1,j):
#                 outimg[i][j] = outimg[i][j] + ip[k][m]
        
# out2 = outimg/9

# plt.imshow(out2,cmap='gray')
# plt.show()











# noise_img = []
# k = 0
# for i in range(10): 
#     k = float(k+0.1)
#     noise_img.append(rn(img,mode = 's&p',amount = k))
#     noise_img[i] = np.array(255*noise_img[i], dtype = 'uint8')


# for i in range(1,11):
#     plt.subplot(2,5,i)
#     plt.imshow(noise_img[i-1])
#     plt.title(f"s&p level {float(i/10)}")
    
# plt.show()