#swipe the value in the list
n=int(input("Enter the number"))
matrix=[]
for i in range(n):
    matrix.append([int(ele) for ele in input().split()])
for i in range(n):
    for j in range(n):
        if j > i:
            temp=matrix[j][i]
            matrix[j][i]=matrix[i][j]
            matrix[i][j]=temp
for i in range(n):
    print(matrix[i])
