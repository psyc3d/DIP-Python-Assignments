import cv2
import numpy as np
from matplotlib import pyplot as plt 
from skimage.util import random_noise as rn    

def outimg(num1,num2,num):    
    img = cv2.imread("./Assignment 2/lena.png",0)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    image = []

    for i in range(num):
        noise_img = rn(img,mode = 'gaussian',mean = 0, var = 0.01)
        image.append(noise_img)

    out = image[0]
    for i in range(num-1):
        out = out+image[i+1]

    out1=out
    out1 = np.array(255*out1, dtype = 'uint8')


    out = np.divide(out,num)

    """for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(image[i])"""

    plt.subplot(2,6,num1)
    plt.imshow(out1)
    plt.subplot(2,6,num2)
    plt.imshow(out)
    
j = 1

for i in range(6):
    outimg(j,j+1,5*(i+1))
    plt.title(f"Gaussian Noise {5*(i+1)}")
    j = j+2
plt.show()
    
