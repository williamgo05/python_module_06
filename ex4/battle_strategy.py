from abc import ABC, abstractmethod
from ex3.creature import Creature, TransformCapability
from typing import Protocol, cast


class TransformableCreature(Protocol):

    def attack(self) -> str:
        pass

    def transform(self) -> str:
        pass

    def revert(self) -> str:
        pass


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.creature_name}' "
                "for this aggressive strategy"
            )

        target = cast(TransformableCreature, creature)
        print(target.transform())
        print(target.attack())
        print(target.revert())
