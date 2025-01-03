class flashCards :
    def __init__(self,word,meaning):
        self.word = word 
        self.meaning = meaning

    def __str__(self):
        return self.word + "(" + self.meaning + ")"
    
flash = []
print("Welcome to flash cards loop .")

while (True) :
    word = input("Enter the word : ")
    meaning = input ("Enter the meaning : ")

    flash.append(flashCards(word,meaning))
    option = input ("Do you want to add more wore words ? (y/n  :  )")

    if option == 'n' :
       break


print("\n your Flash cards are ready !!! \n")
for i in flash :
    print(i)
        