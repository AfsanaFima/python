class Pair_Elements():
    def sum(self,num,target):
        store = {}

        for i, num in enumerate(num):
            if target - num in store:
                return(target - num,num)
            store[num] = i

num = (10,20,30,40,50,60,70,80,90,100)
target = int(input("Enter the element : "))
print(Pair_Elements().sum(num,target))
