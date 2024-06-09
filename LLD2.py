# Inheritance in Python
# When one class inherits another class

class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"
    
    def speaks(self):
        return f"{self.name} says woof woof"

class GermanShephard(Dog):
    def speaks(self):
        return f"{self.name} barks and growls"

d1 = Dog("Tom", 2)
d2 = GermanShephard("Bruce", 4)

print(d1.speaks(), d2.speaks())
print(isinstance(d1, GermanShephard))

# Copy Constrcutor in Pyton, Python has copy module which can help us with this, but we can also use copy constructor
class MyClass:
   def __init__(self, value):
       self.value = value

   # Copy constructor
   def __init__(self, other):
       self.value = other.value

# Polymorhism in python can be achieved by method overloading and method overriding
# Method overriding can be achieved by inheritance, but for method overloading in python we use dispath decorator
from multipledispatch import dispatch

class Cat:
    @dispatch()
    def speak(self):
        print("Meow")

    @dispatch(str)
    def speak(self, sound):
        print(sound)

c = Cat()
c.speak()