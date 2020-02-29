import random
from random import randint as ri
import cv2 as cv
print(cv._version_)
r = 0
c = 0

print("Please enter the rows:")
r = int(input())
print("Please enter the columns:")
c = int(input())

tot = r*c

rows, cols = (r,c)
arr = [[0 for i in range(cols)] for j in range(rows)]

for i in range(cols):
    for j in range(rows):
        #arr[i][j] = int(input(f"Please enter the number for column {i} and row {j}: "))
        arr[j][i] = ri(0,9)
print(arr)
#SUM of all intergers in the matrix
s = 0
for i in range(cols):
    for j in range(rows):
        s = s + arr[j][i]

print("The sum of all elements is :",s)

#Maximum of the matrix
s = arr[0][0]
for i in range(cols):
    for j in range(rows):
        if s <= arr[j][i]:
            s = arr[j][i]

print("The max of all elements is :",s)

#Mean of the matrix
s = 0

for i in range(cols):
    for j in range(rows):
        s = s + arr[j][i]
mn = s/tot
print("The mean of all elements is :",mn)

#Median

k = 0 
sub = [0]*tot
for i in range(cols):
    for j in range(rows):
        sub[k] = arr[j][i]
        k=k+1

sub.sort()
if tot%2 == 0:
    o = int(tot/2)
    med = (sub[o]+sub[1+o])/2
if tot%2 != 0:
    med = sub[(tot+1)/2]

print("The median of the matrix is:",med)

#mode
mod = [0]*tot
count = 1
for i in range(tot-1):
    if sub[i] == sub[i+1]:
        count = count+1
    if sub[i] != sub[i+1]:
        mod[i] = count
        count = 1
mod[tot-1] = count
#print(mod)
print("The mode is :",sub[mod.index(max(mod))])


#Standard Deviation

std = 0
for i in range(tot):
    std = std + (sub[i]-mn)*(sub[i]-mn)

std = std/(tot-1)
std = pow(std,0.5)

print("The standard deviation is :",std)
    
#Frequency deviation
freq = [0]*tot
count = 1
for i in range(tot-1):
    if sub[i] == sub[i+1]:
        count = count+1
    if sub[i] != sub[i+1]:
        freq[i] = count
        print(f"The frequency distribution of {sub[i]} is",count)
        count = 1