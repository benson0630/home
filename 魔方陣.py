import numpy as np

a = int(input("輸入奇數"))
center = a//2

array = np.zeros((a,a) , dtype=int)
row = 0
col = center
array[row,col] = 1


for i in range(2,(a*a)+1):
    row -= 1
    col -= 1
    if row < 0 and col < 0:
        row += 2
        col += 1
    elif row < 0:
        row = a-1
    elif col < 0:
        col = a-1
    if array[row,col] != 0:
        row += 2
        col += 1
    array[row,col] =i
    # print("["+str(row)+","+str(col)+"]"+"="+str(i)) 
print(array)
