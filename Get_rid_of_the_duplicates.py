student_data = {
    'id1':
    {
        'name':['sara'],
        'class':['nine'],
        'subject':['Science']
    },
    'id2':
    {
        'name':['Zara'],
        'class':['Ten'],
        'subject':['Bgs']
    },
    'id3':
    {
        'name':['sara'],
        'class':['nine'],
        'subject':['Science']
    },
}

result = {}
for key,value in student_data.items() :
    if value not in result.values():
        result[key] = value
print(result)