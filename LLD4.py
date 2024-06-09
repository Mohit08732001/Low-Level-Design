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