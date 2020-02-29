import cv2
from matplotlib import pyplot as plt
import numpy as np
img=cv2.imread("./Assignment 3/d.jpg",0)

#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow(img)
#cv2.waitkey(0)
#plt.show()
#print(img)
#print(img.size)
print(img.shape)
total=img.size
print (total)
#matrix to list
list1=[]
for row in img:
    for item in row:
        list1.append(item)
list3=list1
list1=sorted(list1)
#print (list1)
print (len(list1))

#
r=[]
p=[]
for i in range(256):
    r.append(i)
    p.append(0)
#print(r)
#print(p)

#for probabolity distribution


for item in r:
    for i in list1:
        if item==i:
            p[item]=p[item]+1
pr=[]
for item in p:
    pr.append(float(item/total))
#print (pr)
#print (p[73])

#for summation pf pr

cum_pr=[]

# for i in range(256):
#     cum_pr.append(0)

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
print (s)

#for r to s maping
list2=[]
for item in list3:
    for i in range (256):
        if item==r[i]:
            list2.append(s[i])
print (list2)
print (len(list2))
matrix=img*0
l=0
for i in range(258):
    for j in range(221):
        matrix[i][j]=list2[l]
        l=l+1
'''
cv2.imshow('Dark_image',img)
cv2.waitKey(100)
cv2.imshow('bright_image',matrix)
cv2.waitKey(0)
'''
print(matrix)
print(matrix.shape)
print(matrix.size)
plt.subplot(221)
b=plt.imshow(img,cmap='gray')
plt.subplot(222)
plt.hist(matrix.ravel(),256,[0,256])
plt.subplot(223)
plt.hist(img.ravel(),256,[0,256])
plt.subplot(224)
a=plt.imshow(matrix,cmap='gray')
plt.show()
