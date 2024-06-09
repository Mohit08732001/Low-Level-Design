class MyClass:
    def method(self):
        print("Regular method called", self)
    
    @classmethod
    def classmethod(cls):
        print("Class method called", cls)
    
    @staticmethod
    def staticmethod():
        print("Static method called")

c = MyClass()
c.method()
c.classmethod()
c.staticmethod()

# MyClass.method()   Error is thrown here
MyClass.staticmethod()
MyClass.classmethod()


# Interface in Python
from abc import ABC, abstractmethod
class MyInterface(ABC):
    @abstractmethod
    def my_method(self):
        pass

class MyClass(MyInterface):
    def my_method(self):
        print("Hi, Hello")

my_class = MyClass()
my_class.my_method()