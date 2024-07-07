from abc import ABC, abstractmethod

class Localizer(ABC):
    @abstractmethod
    def localize(self, msg):
        pass


class FrenchLocalizer(Localizer):
    def __init__(self) -> None:
        self.message = {
            "car": "voiture",
            "bike": "vélo",
            "cycle": "faire du vélo"
        }

    def localize(self, msg):
        return self.message.get(msg, msg)


class EnglishLocalizer(Localizer):
    def localize(self, msg):
        return msg


class GermanLocalizer(Localizer):
    def __init__(self) -> None:
        self.message = {
            "car": "Auto",
            "bike": "Fahrrad",
            "cycle": "Zyklus"
        }

    def localize(self, msg):
        return self.message.get(msg, msg)


class LocalizerFactory(ABC):
    @abstractmethod
    def create_localizer(self):
        pass


class FrenchLocalizerFactory(LocalizerFactory):
    def create_localizer(self):
        return FrenchLocalizer()


class EnglishLocalizerFactory(LocalizerFactory):
    def create_localizer(self):
        return EnglishLocalizer()


class GermanLocalizerFactory(LocalizerFactory):
    def create_localizer(self):
        return GermanLocalizer()


if __name__ == "__main__":
    # Create Factory instances for different languages
    f = FrenchLocalizerFactory()
    e = EnglishLocalizerFactory()
    s = GermanLocalizerFactory()

    message = ["car", "bike", "cycle"]

    for msg in message:
        # Create and use localizers without knowing the concrete classes
        print(f.create_localizer().localize(msg), end = "|")
        print(e.create_localizer().localize(msg), end = "|")
        print(s.create_localizer().localize(msg))