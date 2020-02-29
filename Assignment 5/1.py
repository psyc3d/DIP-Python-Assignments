import cv2
import numpy as np
from matplotlib import pyplot as plt
import math as mt

#-----------------------x---------------------------x-----------------------------------x---------------------x--------------------------x----------
#DFT ALGORITHM

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
        print ("g is",g)
        h = FFT([x[i] for i in range(1 ,len(x) ,2) ])
        print ("h is",h)

        for i in range(len(g)):
            print(len(g))
            print(len(h))
            L = g[i] + h[i] * np.exp(-1j * 2 * np.pi * i/(2*len(g)))
            FL.append(L)
            R = g[i] - h[i] * np.exp(-1j * 2 * np.pi * i/(2*len(g)))
            FR.append(R)
        return FL + FR

#-----------------------------x------------------------------------x------------------------------x-----------------------x------------------x--------

x = [1,2,3,4]
I = mt.log(len(x),2)

if len(x) == (2 ** int(I)):
    x=x
elif len(x) == (2 ** (int(I)+1)) and len(x) != (2 ** int(I)):
    x=x
else:
    for i in range(len(x),(2 ** (int(I)+1))):
        x.append(0)


r = FFT(x)
print (r)
