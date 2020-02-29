import cv2
import numpy as np
from matplotlib import pyplot as plt
import math as mt

img_lena = cv2.imread('./Assignment 5/lena.png' , 0)
img_lena = cv2.cvtColor(img_lena ,cv2.COLOR_BGR2RGB)
gray_lena = cv2.cvtColor(img_lena ,cv2.COLOR_RGB2GRAY)

dim = (256,256)

lena_r = cv2.resize(gray_lena,dim,interpolation = cv2.INTER_AREA)

plt.imshow(lena_r, cmap= 'gray')
plt.show()

img_dog = cv2.imread('./Assignment 5/dog.tif' , 0)
img_dog = cv2.cvtColor(img_dog ,cv2.COLOR_BGR2RGB)
gray_dog = cv2.cvtColor(img_dog ,cv2.COLOR_RGB2GRAY)

dog_r = cv2.resize(gray_dog,dim,interpolation = cv2.INTER_AREA)

plt.imshow(dog_r, cmap= 'gray')
plt.show()

#-----------------------x---------------------------x-----------------------------------x---------------------x--------------------------x----------
#DFT ALGORITHM

a=[]
def DFT(X):
    a = [0]*len(X)
    z = -1j * 2 * (np.pi)
    z = z / len(X)
    z = np.exp(z)
    for i in range(len(X)):
        s=0
        y = z ** i
        for k in range(len(X)):
        #s =s + (x[i]*((np.exp(-1j*2*(np.pi)*i*k))/len(x)))
        #a.append(s)
            s = s + X[k]*(y ** k)
        a[i] = s
    return a


#---------------------------------x--------------------------------x-----------------------x-------------------------------x-----------------x--------
#FFT ALGORITHM

g=[]
h=[]

def FFT(x):
    FL = []
    FR = []

    if (len(x) == 2):
        return DFT(x)
    else:
        g = FFT([x[i] for i in range(0,len(x),2)])
        h = FFT([x[i] for i in range(1 ,len(x) ,2) ])

        for i in range(len(g)):
            L = g[i] + h[i] * np.exp(-1j * 2 * np.pi * i/(2*len(g)))
            FL.append(L)
            R = g[i] - h[i] * np.exp(-1j * 2 * np.pi * i/(2*len(g)))
            FR.append(R)
        # print len(FL+FR)

        return FL + FR



#-----------------------------x------------------------------------x------------------------------x-----------------------x------------------x--------

def extract(i):
    X = i
    X = np.array(X)
    x=[]
    rows ,cols = X.shape

    end = []
    final = []
    final_mag = []
    final_ang = []

    for i in range(rows):
        x = X[i ,:]
        I = mt.log(len(x),2)
        r = FFT(x)
        end.append(r)

    # print len(end)
    # print end
    end = np.array(end)


    for i in range(cols):
        x = end[:, i]
        # print x
        I = mt.log(len(x),2)
        r = FFT(x)
        final.append(r)
        final_mag.append(20*np.log(np.abs(r)))
        final_ang.append(np.angle(r,deg = True))

    final = np.array(final)
    final_mag = np.array(final_mag)
    final_ang = np.array(final_ang)

    return final_mag,final_ang



lena_mag = []
lena_ang = []
lena_mag,lena_ang = extract(lena_r)

plt.imshow(lena_mag, cmap= 'gray')
plt.show()
plt.imshow(lena_ang, cmap= 'gray')
plt.show()


dog_mag = []
dog_ang = []

dog_mag,dog_ang = extract(dog_r)
plt.imshow(dog_mag, cmap= 'gray')
plt.show()
plt.imshow(dog_ang, cmap= 'gray')
plt.show()

#-------------------x--------------------------------------x--------------------------------------x------------------------------------x----------

