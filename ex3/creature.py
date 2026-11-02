import abc


class Creature(abc.ABC):
    def __init__(self, name: str, type: str):
        self.creature_name = name
        self.creature_type = type

    @abc.abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (f"{self.creature_name} is a "
                f"{self.creature_type} type Creature")


class Flameling(Creature):

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class TransformCapability(abc.ABC):
    def __init__(self):
        self.is_transformed = False

    @abc.abstractmethod
    def transform(self) -> str:
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, type: str):
        Creature.__init__(self, name, type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return "Shiftling performs a boosted strike!"
        else:
            return "Shiftling attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, type: str):
        Creature.__init__(self, name, type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return "Morphagon unleashes a devastating morph strike!"
        else:
            return "Morphagon attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "Morphagon stabilizes its form."
