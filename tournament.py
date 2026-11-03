from ex3 import FlameFactory, TransformCreatureFactory
from ex3.creature_factory import CreatureFactory
from ex3.creature import Creature
from ex4 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    InvalidStrategyError,
)


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:

    entities: list[tuple[Creature, BattleStrategy]] = [
        (factory.create_base(), strategy)
        for factory, strategy in opponents
    ]

    print("*** Tournament ***")
    print(f"{len(entities)} opponents involved")

    for i in range(len(entities)):
        for j in range(i + 1, len(entities)):
            creature_a, strategy_a = entities[i]
            creature_b, strategy_b = entities[j]
            print("\n=== Battle ===")
            print(creature_a.describe())
            print("     vs.")
            print(creature_b.describe())

            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


print("Tournament 0 (basic)")
print(" [ (Flameling+Normal), (Shiftling+Aggressive) ]")

battle([
    (FlameFactory(), NormalStrategy()),
    (TransformCreatureFactory(), AggressiveStrategy()),
])

print("\nTournament 1 (error)")
battle([
    (TransformCreatureFactory(), AggressiveStrategy()),
    (FlameFactory(), AggressiveStrategy()),
])
