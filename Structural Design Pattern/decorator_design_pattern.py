from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def get_damage(self):
        pass


class BasicCharacter(Character):
    def description(self):
        return "Basic character "
    
    def get_damage(self):
        return 10


class CharacterDecorator(Character):
    def __init__(self, character) -> None:
        self._character = character
    
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def get_damage(self):
        pass


class DoubleDamageDecorator(CharacterDecorator):
    def description(self):
        return self._character.description() + "with double damage "
    
    def get_damage(self):
        return self._character.get_damage() * 2


class FireBallDecorator(CharacterDecorator):
    def description(self):
        return self._character.description() + "with fire ball "
    
    def get_damage(self):
        return self._character.get_damage() + 20


class InvisibilityDecorator(CharacterDecorator):
    def description(self):
        return self._character.description() + "with invisibility "
    
    def get_damage(self):
        return self._character.get_damage()


if __name__ == '__main__':
    base_character = BasicCharacter()
    print(base_character.description())
    print(base_character.get_damage())

    base_character_with_double_damage = DoubleDamageDecorator(base_character)
    base_character_with_fireball = FireBallDecorator(base_character)
    base_character_with_invisibilty = InvisibilityDecorator(base_character)

    print(base_character_with_double_damage.description())
    print(base_character_with_double_damage.get_damage())

    print(base_character_with_fireball.description())
    print(base_character_with_fireball.get_damage())

    print(base_character_with_invisibilty.description())
    print(base_character_with_invisibilty.get_damage())

    base_character_with_double_damage_and_fireball = DoubleDamageDecorator(FireBallDecorator(base_character))
    print(base_character_with_double_damage_and_fireball.description())
    print(base_character_with_double_damage_and_fireball.get_damage())