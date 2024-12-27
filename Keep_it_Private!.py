class myClass:
    __myVariable = 10

    def __priMethod(self):
        print("This is a private method.")

    def pubMethode(self):
        print("This is a public method.")
        self.__priMethod()
        print(self.__myVariable + 10.88)


v1 = myClass()
v1.pubMethode()
