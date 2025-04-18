#how to take input in 2D List
n=int(input("Enter the number"))
m=int(input("Enter the number"))
grid=[]
for i in range(n):
    tempList=[int(item) for item in input().split()]
    grid.append(tempList)
print(grid)
