import cv2
from matplotlib import pyplot as plt
import numpy as np
img1=cv2.imread("./Assignment 3/d.jpg",0)
img2=cv2.imread("./Assignment 3/b.jpg",0)

def histoeq(img):
    total=img.size
    list1=[]
    for row in img:
        for item in row:
            list1.append(item)
    list3=list1
    list1.sort

    r=[]
    p=[]
    
    for i in range(256):
        r.append(i)
        p.append(0)
    
    #for probability distribution


    for item in r:
        for i in list1:
            if item==i:
                p[item]=p[item]+1
    pr=[]

    for item in p:
        pr.append(float(item/total))

    #for summation pf pr

    cum_pr=[]

    for i in range(256):
        cum_pr.append(0)

    for i in range(256):
        if i==1:
            cum_pr[i] =pr[i]
        else:
            cum_pr[i]=cum_pr[i-1]+pr[i]
    #print (cum_pr)

    #for s
    s=[]
    for item in cum_pr:
        s.append(round(item*255))
    #print (s)

    return r, s,list3


r1,s1,list1=histoeq(img1)
r2,s2,list2=histoeq(img2)
#print (r1)
#print (s1)
#print (r2)
#print (s2)

u=[]
count = 0
for item in r1:
    o = 0
    while o!=1:
        for i in range(256):
            if s1[item]== s2[i]:
                u.append(r2[i])
                o=o+1
                break
        s1[item]=s1[item]+1
        count += 1
        if s1[item] >= 256:
            break


print (u)

list10=[]
for item in list1:
    for i in range (256):
        if item==r1[i]:

            list10.append(u[i])
img3 = img1 * 0
l = 0
for i in range(258):
    for j in range(221):
        img3[i][j] = list10[l]
        l = l + 1

print(img3)
print(img3.shape)
print(img3.size)
plt.subplot(221)
b=plt.imshow(img1,cmap='gray')
plt.subplot(222)
plt.hist(img3.ravel(),256,[0,256])
plt.subplot(223)
plt.hist(img1.ravel(),256,[0,256])
plt.subplot(224)
a=plt.imshow(img3,cmap='gray')
plt.show()