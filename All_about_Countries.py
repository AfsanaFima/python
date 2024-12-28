class Bangladesh():
    def capital(self):
        print("Dhaka is the capital of bangladesh")

    def Language(self):
        print("Bangla is the the mother tongue of bangladesh")

    def type(self):
        print("Bangladesh is a developing country")


class USA():
    def capital(self):
        print("Washinton D.C is the capital of bangladesh")

    def Language(self):
        print("English is the the mother tongue of bangladesh")

    def type(self):
        print("USA is a developed country")

bng = Bangladesh()
usa =USA()

for country in(bng,usa):
    country.capital()
    country.Language()
    country.type()
    

    print("")