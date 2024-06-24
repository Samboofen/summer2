class StringManipulator:
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input()

    def printString(self):
        print(self.str.upper())
if __name__ == "__main__":
    str = StringManipulator()
    str.getString()
    str.printString()