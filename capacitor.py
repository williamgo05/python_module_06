from ex3 import TransformCreatureFactory
from ex3.creature import Shiftling, Morphagon


def main() -> None:
    factory = TransformCreatureFactory()

    creatures: list[Shiftling | Morphagon] = [
        factory.create_base(), factory.create_evolved()
        ]

    for creature in creatures:
        print(creature.describe())
        print(creature.attack())
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


if __name__ == "__main__":
    main()
