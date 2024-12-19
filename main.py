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

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return math.pi * self.radius * 2


# rectangle = Rectangle(4, 5)
# print("Площадь:", rectangle.area())
# print("Периметр:", rectangle.perimeter())
#
# rectangle2 = Rectangle(7, 6)
# print("Площадь:", rectangle2.area())
#
# circle = Circle(3)
# print("Площадь:", circle.area())
# print("Периметр:", circle.perimeter())


# Задание 4

from typing import Union

# Вариант 1
def calculate_area(arg1: Shape, *args: Shape):
    Sum_area = arg1.area()
    for arg in args:
        Sum_area = Sum_area + arg.area()
    return Sum_area


# Вериант 2
def calculate_area_2(list_shapes: Union[Rectangle, Circle]):
    Sum_area = 0
    for shape in list_shapes:
        Sum_area = Sum_area + shape.area()
    return Sum_area

# print(calculate_area(rectangle, circle, rectangle2))
# list_shapes = (rectangle, circle, rectangle2)
# print(calculate_area_2(list_shapes))
#
# Задание 5


class BankAccount:
    def __init__(self):
        pass

    def