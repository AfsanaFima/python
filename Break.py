word = input("Enter a word : ")
k_word = input("Enter the key : ")

for i in word :
    if (i == k_word):
        print("{} is found ".format(k_word))
        break
    else:
        print("{} is not found ".format(k_word))