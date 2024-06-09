from typing import Any

class SingletonMetaClass(type):
    _instances = {}
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMetaClass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMetaClass):
    def __init__(self, data=None) -> None:
        self.data = data

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)