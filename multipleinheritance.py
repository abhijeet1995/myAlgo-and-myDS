class Name:
    def hey(self):
        print("hey! I'm Name class")

class Game:
    def hey(self):
        print("hey! this is Game class")

class Same(Game, Name):
    pass

Same().hey()
