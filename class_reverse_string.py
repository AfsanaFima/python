class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        return ' '.join(reversed(words))


sentence = "Hello World Python"
reverser = StringReverser(sentence)
print(reverser.reverse_words())  
