from copy import deepcopy

class Prototype:
    def clone(self):
        return deepcopy(self)

class ConcretePrototyeA(Prototype):
    def __init__(self, data) -> None:
        self.data = data

class ConcretePrototyeB(Prototype):
    def __init__(self, data) -> None:
        self.data = data

class PrototypeRegistry:
    def __init__(self) -> None:
        self.prototypes = {}

    def set_prototype(self, name, prototype):
        self.prototypes[name] = prototype
    
    def get_prototype(self, name):
        if name in self.prototypes:
            return self.prototypes[name].clone()
        else:
            raise Exception(f"Prototype {name} not found")

prototype_a = ConcretePrototyeA("Prototype A data")
prototype_b = ConcretePrototyeB("Prototype B data")

registry = PrototypeRegistry()
registry.set_prototype("Prototype A", prototype_a)
registry.set_prototype("Prototype B", prototype_b)

clonned_prototype_a = registry.get_prototype("Prototype A")
clonned_prototype_b = registry.get_prototype("Prototype B")

print(clonned_prototype_a.data)
print(clonned_prototype_b.data)

