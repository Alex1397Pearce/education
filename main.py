# Задание 1
class Animal():
    def Speak(self):
        return "I can't speak"

    def Move(self):
        return "I can't move"

class Dog(Animal):
    def Speak(self):
        print("Wow")

    def Move(self):
        print("Тыгдык-тыгдык")

class Bird(Animal):
    def Speak(self):
        print("Чик-чирик")

    def Move(self):
        print("I belive I can flyyy")

some_animal = Dog()

some_animal.Move()
some_animal.Speak()


# Задание 2

