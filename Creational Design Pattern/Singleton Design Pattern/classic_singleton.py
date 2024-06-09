# Singleton Design Pattern
# It focuses on saying that a class has only one instance and providing a global point of access to that instance.

class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)