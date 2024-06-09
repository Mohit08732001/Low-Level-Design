"""
Programming Paradigms In Language
Procedural, Object Oriented, Functional

Since we are focusing on Python, Python uses OOP

OOP is basically real world entites called as classes and instance of those created are called as objects.
OOP is based on abstraction
Pillars of OOP: Encapsulation, Polymorphism, Inheritance
"""

# Created a class called as House
class House:
    def __init__(self) -> None:
        print('Constructor of house is called')

# Created a instance of class which is called object
h = House()

# Lets take another example of Dog class
class Dog:
    species = "German Shephard" # This is a class attribute
    def __init__(self, name, age) -> None:
        self.name = name        # This is an instance attribute
        self.age = age
    
    def description(self):      # This is an instance method
        return f"{self.name} is {self.age} years old"
    
    def __str__(self) -> str:   # This is a special method/ dunder methods
        return self.description()

d1 = Dog("Tom", 2)
d2 = Dog("Bruce", 4)

# But description doesn't seem like a pythonic way, say if we use print statement, we get address of the object can we instead return description from there
print(d1)
