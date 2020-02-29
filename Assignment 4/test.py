# take the lena image and add s&p noise to it

import cv2
import numpy as np
from matplotlib import pyplot as plt 
from skimage.util import random_noise as rn  


# Generating set
img = cv2.imread("./Assignment 4/lena.png",0)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

ni = rn(img,mode = 's&p')
ni = np.array(255*ni, dtype = 'uint8')


print(ni[10][10])