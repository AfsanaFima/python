n1 = {1,2,3,4,5,}
n2 = {"Afia","aria","abony","Afrida","Afnan"}
n3 = list(zip(n1,n2))
print(n3)
#zip two lists
b = [2,4,6,8,3,]
b2 = [200,400,500,567,897]
b1 = list(zip(b,b2[::-1]))

for x,y in b1:
    print(x,y)

#zip two dictionaries

sto = ['reliance','infy','tcs']
pri = [2000,60000,50000]
zipDic = zip(sto,pri)

nDic = {sto:pri for sto,pri in zipDic}
print(nDic)