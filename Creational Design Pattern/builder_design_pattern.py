from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Any

@dataclass
class Pizza:
    name: str
    type: str
    price: int

class BaseBuilder(ABC):
    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def set_type(self, type):
        pass

    @abstractmethod
    def set_price(self, price):
        pass

class PizzaBaseBuilder(BaseBuilder):
    def set_name(self, name):
        self._name = name
        return self
    
    def set_type(self, type):
        self._type = type
        return self
    
    def set_price(self, price):
        self._price = price
        return self
    
    def build(self):
        return Pizza(name=self._name, price=self._price, type=self._type)

pizza = PizzaBaseBuilder().set_name("Margherita").set_type("Veg").set_price(500).build()
print(pizza)