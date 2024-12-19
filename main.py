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

# some_animal = Dog()
#
# test = some_animal.Move()
# print(test)
# some_animal.Speak()


# Задание 2

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Speak(self):
        print(f"My name is {self.name}.")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def Study(self, thing):
        print(f"I have grade {self.grade} and I study {thing}")


# Bob = Student("Bob", 23, 4)
#
# Bob.Speak()
# Bob.Study("math")


# Задание 3

