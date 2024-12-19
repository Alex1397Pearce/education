# 1. ** Создание базового класса: **
# - Реализуйте базовый класс `Animal` с методами `speak()` и `move()`.
# - Создайте подклассы `Dog` и `Bird`, переопределяющие эти методы.
# 2. ** Наследование: **
# - Реализуйте класс `Person` с атрибутами `name` и `age`.
# - Создайте класс `Student`, наследующий от `Person`, добавьте атрибут `grade` и метод `study()`.
# 3. ** Абстрактные классы: **
# - Создайте абстрактный класс `Shape` с методом `area()`.
# - Реализуйте два подкласса `Circle` и `Rectangle`, которые вычисляют площадь.
# 4. ** Полиморфизм: **
# - Реализуйте функцию `calculate_area(shapes)` для вычисления общей площади объектов `Shape`.
# - Передайте список объектов `Circle` и `Rectangle`.
# 5. ** Инкапсуляция: **
# - Создайте класс `BankAccount` с приватным атрибутом `_balance`.
# - Реализуйте методы `deposit()` и `withdraw()` для управления балансом.
# 6. ** Декоратор: **
# - Напишите класс `Logger`, который декорирует методы других классов и записывает их вызовы в лог.
# 7. ** Singleton: **
# - Реализуйте класс `Config` с использованием паттерна Singleton.Пусть он хранит настройки приложения.
# 8. ** Фабрика: **
# - Напишите класс `CarFactory`, который создает объекты азных классов: `Sedan`, `SUV` и `Truck`, в зависимости от  типамашины.
# 9. ** Observer: **
# - Реализуйте систему уведомлений  для класса Stock`, где наблюдатели будут получать уведомление при изменении цены.
# 10. ** Асинхронное программирование: **
# - Напишите асинхронный класс `TaskRunner`, который выполняет  задачи вслучайном порядке с спользованием asyncio.


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
        print("I believe I can flyyy")

some_animal = Dog()

test = some_animal.Move()
print(test)
some_animal.Speak()


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
        self.__balance = 0

    def get_Balance(self):
        print(self.__balance)

    def deposit(self, money):
        self.__balance = self.__balance + money

    def withdraw(self, money):
        if self.__balance > money:
            self.__balance = self.__balance - money
        else:
            print("недостаточно средств")

acc00551166 = BankAccount()
# acc00551166.get_Balance()
acc00551166.deposit(1000)
# acc00551166.get_Balance()
# acc00551166.withdraw(1500)
# acc00551166.get_Balance()
# acc00551166.withdraw(500)
# acc00551166.get_Balance()

# Задание 6

class Logger:
    @staticmethod
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            print(f"Произведено выполнение функции {func}")
            return result
        return wrapper

logger = Logger()


class MicroFinance(BankAccount):
    def __init__(self, name):
        super().__init__()
        self.name = name

    @logger.decorator
    def show_name(self, mess):
        return f"||{mess}||-||{self.name}||"

# microkred = MicroFinance("Имя_Персонажа")
#
# print(microkred.show_name("test"))

# Задание 7


class Config:

    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__()
        return cls._instance

    __path_to_db = r"\\server\folder\database"

conf = Config()
configuration = Config()

if conf is configuration:
    print("yes")
