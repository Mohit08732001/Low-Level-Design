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