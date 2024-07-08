from abc import ABC, abstractmethod

class Flyweight(ABC):
    @abstractmethod
    def operation(self, extrinsic_state):
        pass


class ConcreteFlyweight(Flyweight):
    def __init__(self, intrinsic_state) -> None:
        self._intrinsic_state = intrinsic_state
    
    def operation(self, extrinsic_state):
        return f"Concrete Flyweight Intrinsic State: {self._intrinsic_state} and Extrinsic State: {extrinsic_state}"


class FlyweightFactory:
    _cache = {}
    @staticmethod
    def get_flyweight(key):
        if key not in FlyweightFactory._cache:
            FlyweightFactory._cache[key] = ConcreteFlyweight(key)
        return FlyweightFactory._cache[key]


class Client:
    def __init__(self, key) -> None:
        self.flyweight = FlyweightFactory.get_flyweight(key)
    
    def operation(self, extrinsic_state):
        return self.flyweight.operation(extrinsic_state)

c1 = Client("shared")
c2 = Client("shared")
c3 = Client("unique")

print(c1.operation("State1"))
print(c2.operation("State2"))
print(c3.operation("State3"))