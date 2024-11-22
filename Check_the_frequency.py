test = {'sara':'science','Mahtab':'Arts','Zara':'commerce','Taha':'science'}

print("The original dict:",test)
    

subject = input("Enter the subject : ")

result = 0

for key in test :
    if test[key] == subject :
        result = result+1

print( f"Students studying the subject {subject} : ",result)