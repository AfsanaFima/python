import array as arr

array1 = arr.array('b',[18,33,13,25,15,])
print(array1[1])

array1.reverse()
print(array1)

array1.append(77)
print(array1)


array1.insert(4,88)
print(array1)

array1.remove(88)
print(array1)

array1.pop(2)
print(array1)


#set intersection

setx = {'pink','Lavender'}
sety = {'Lavender','blue','black'}

setz = setx.intersection(sety)
print(setz)

setz = setx.union(sety)
print(setz)


