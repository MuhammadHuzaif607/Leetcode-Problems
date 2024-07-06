import math
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
lst = []

for i in range(len(matrix[0])):
    lst.append(matrix[0][i])

print(lst)

for j in range(1,len(matrix)):
    lst.append(matrix[j][-1])

print(lst)

if len(matrix) > 1:
    for k in range(len(matrix[0])-2,-1,-1):
        lst.append(matrix[-1][k])

print(lst)

st = int(math.ceil(len(matrix))/2)

if len(matrix) > 2 :
    for l in range(0,len(matrix[0])-1):
        lst.append(matrix[st][l])

print(lst)


