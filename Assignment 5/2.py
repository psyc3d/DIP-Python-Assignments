import cv2
import numpy as np
from matplotlib import pyplot as plt
import math as mt

img = cv2.imread('./Assignment 5/Lena.png' , 0)
img = cv2.cvtColor(img ,cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img ,cv2.COLOR_RGB2GRAY)
dim = (256,256)

img = cv2.resize(gray,dim,interpolation=cv2.INTER_AREA)

plt.imshow(img , cmap= 'gray')
plt.show()


#-----------------------x---------------------------x-----------------------------------x---------------------x--------------------------x----------
#DFT ALGORITHM

a=[]
def DFT(X):
    a = [0, 0]
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
    rows,cols = X.shape

    end = []
    final = []

    for i in range(rows):
        x = X[i ,:]
        r = FFT(x)
        end.append(r)

    # print len(end)
    # print end
    end = np.array(end)


    for i in range(cols):
        x = end[:, i]
        r = FFT(x)
        final.append(r)
    final = np.array(final)

    return final

lena_final = extract(img)
print( lena_final)



