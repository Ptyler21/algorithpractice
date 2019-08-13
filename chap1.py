"""
This is mean to be a LIFO stack
"""

class BagStats:
    #the function needs to take an array of numbers
    def __init__(self, arrayOfInput):
        self.arrayOfInput = arrayOfInput
        self.numbers = arrayOfInput.split()


    @classmethod
    def fromInput(cls):
        return cls(input("give me a number: "))

    def userme(self):
        #self.numbers.append(self.arrayOfInput)
        self.arrayOfInput = self.arrayOfInput.strip().split()
        


classvar = BagStats.fromInput()
classvar.userme()

