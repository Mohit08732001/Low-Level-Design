"""
SOLID Principles
"""

# S -> Single Responsibility Principle (SRP)
# It means a class should only have one reason to change, it basically should handle only one task

class FileManager:
    def read(self, file_name):
        # This function reads the file
        pass

    def write(self, file_name):
        # This function writes in the file
        pass

    def compress(self, file_name):
        # This function compresses the file
        pass

    def decompress(self, file_name):
        # This function decompresses the file
        pass

# Above class is violating SRP, because it is handling two different tasks i.e. read/write and compress/decompres
# Let's appply SRP to it

class FileManager:
    def read(self, file_name):
        # This function reads the file
        pass

    def write(self, file_name):
        # This function writes in the file
        pass

class ZipFileManager:
    def compress(self, file_name):
        # This function compresses the file
        pass

    def decompress(self, file_name):
        # This function decompresses the file
        pass

# Here we solved the problem by dividing the class, into two classes which both have only one reason to change now


# O -> Open Closed Principle
# This principle states that a class should be open for extension but closed for modification

from math import pi
from typing import Any
class Shape:
    def __init__(self, shape_type, **kwargs) -> None:
        self.shape_type = shape_type
        if shape_type == 'circle':
            self.radius = kwargs.get('radius')
        elif shape_type == 'rectangle':
            self.height = kwargs.get('height')
            self.width = kwargs.get('width')
    
    def calculate_area(self):
        if self.shape_type == 'circle':
            return pi*self.radius*self.radius
        elif self.shape_type == 'rectangle':
            return self.height*self.width

# This class is violating OCP, because say in future we have a new shape_type, then we need to change all methods in the class

from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, shape_type) -> None:
        self.shape_type = shape_type
    
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, height, width) -> None:
        super().__init__('rectangle')
        self.height = height
        self.width = width
    
    def calculate_area(self):
        return self.height * self.width

class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__('circle')
        self.radius = radius
    
    def calculate_area(self):
        return pi * self.radius * self.radius

# Here we solved the issue of OCP, by creating an abstract class shape, which will never be modified, now if new shape comes we can create a new
# class for that shape-type which will implement Shape abstarct class


# L -> Liskov Substition Principle
# It states that subtypes must be substitutable with their base types
# This principle is about making your subclasses behave like their base classes
# without breaking anyone’s expectations when they call the same methods

class Rectangle:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
    
    def calculate_area(self):
        return self.height * self.width

class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(side, side)
    
    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)
        if name in ["width", "height"]:
            self.__dict__["height"] = value
            self.__dict__["width"] = value

# Here we are violating LSP, because for square shape it works fine, but now if we were to replace rectangle with sqaure it will not work as
# we are setting height and width value same

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
    
    def calculate_area(self):
        return self.height * self.width

class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2

def get_total_sum_of_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)

# Here we solve the problem of LSP, by making sibling relation instead of parent child relation, and only common function is calculate_area between them
# which can be used irrespective of shape


# I -> Interface Segregation Principle(ISP)
# Clients should not be forced to depend on those methods which they don't want to use. Interfaces belongs to clients, not hierarchies

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f'Prints {document} in black and white')
    
    def fax(self, document):
        raise NotImplementedError()
    
    def scan(self, document):
        raise NotImplementedError()

class ModernPrinter(Printer):
    def print(self, document):
        print(f'Prints {document} in color')
    
    def fax(self, document):
        print(f'Faxing {document}')
    
    def scan(self, document):
        print(f'Scanning {document}')
    
# Here, we are violating ISP, by making OldPrinter to implement fax and scan methods, even if does not support those

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scan(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f'Prints {document} in black and white')

class ModernPrinter(Printer, Fax, Scan):
    def print(self, document):
        print(f'Prints {document} in color')
    
    def fax(self, document):
        print(f'Faxing {document}')
    
    def scan(self, document):
        print(f'Scanning {document}')

# Here we have fixed the issue by segrating the single interface into three interfaces with different responsibilities. OldPrinter now only
# implement Printer interface and does not have unused methods
