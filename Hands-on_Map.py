#Addition using map and lamda 
num1 = [1,4,5,3]
num2 = [7,8,2,6]

results = map(lambda x,y: x+y, num1,num2)
print(list(results))

#square

num3 = [1,3,5,4,6]
def square (x):
    return x*x
square = map(square,num3)
print(list(square))