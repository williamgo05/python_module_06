from ex3 import FlameFactory, TransformCreatureFactory
from ex3.creature_factory import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())


def fight(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print(f"{creature1.creature_name} vs. "
          f"{creature2.creature_name} fight!")

    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    test_factory(flame_factory)
    test_factory(transform_factory)

    fight(flame_factory, transform_factory)


if __name__ == "__main__":
    main()
