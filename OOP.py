class Animal:
    def Speak(self):
        return "Sound_Animal"

    def Move(self):
        return "type_of_move"

class Dog(Animal):
    def Speak(self):
        return "Wow"

class Bird(Animal):
    def Move(self):
        return "I can fly"

baffy = Bird()

print(baffy.Move())