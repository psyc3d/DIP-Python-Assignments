
rows, cols = (5,5)
arr = [[0 for i in range(cols)] for j in range(rows)]

for i in range(cols):
    for j in range(rows):
        arr[i][j] = float(input(f"Please enter the number for column {i} and row {j}: ") or 0)
       
for i in range(cols):
    print(arr[i])

#SUM of all intergers in the matrix
s = 0
for i in range(cols):
    for j in range(rows):
        s = s + arr[i][j]

print("The sum of all elements is :",s)

#Maximum of the matrix
s = arr[0][0]
for i in range(cols):
    for j in range(rows):
        if s <= arr[i][j]:
            s = arr[i][j]

print("The max of all elements is :",s)

#Mean of the matrix
s = 0

for i in range(cols):
    for j in range(rows):
        s = s + arr[i][j]
mn = s/25
print("The mean of all elements is :",mn)

#Median

k = 0 
sub = [0]*25
for i in range(cols):
    for j in range(rows):
        sub[k] = arr[i][j]
        k=k+1

sub.sort()
print("The median is :",sub[13])

#mode
mod = [0]*25
count = 1
for i in range(24):
    if sub[i] == sub[i+1]:
        count = count+1
    if sub[i] != sub[i+1]:
        mod[i] = count
        count = 1
mod[24] = count
#print(mod)
print("The mode is :",sub[mod.index(max(mod))])


#Standard Deviation

std = 0
for i in range(25):
    std = std + (sub[i]-mn)*(sub[i]-mn)

std = std/24
std = pow(std,0.5)

print("The standard deviation is :",std)
    
#Frequency deviation
freq = [0]*25
count = 1
for i in range(24):
    if sub[i] == sub[i+1]:
        count = count+1
    if sub[i] != sub[i+1]:
        freq[i] = count
        print(f"The frequency distribution of {sub[i]} is",count)
        count = 1