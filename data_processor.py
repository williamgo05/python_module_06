from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.data: list[str] = []
        self.ranks: list[int] = []
        self.data_processed = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise ValueError("No data to output")
        data = self.data.pop(0)
        rank = self.ranks.pop(0)
        return (rank, data)


class NumericProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError("Invalid numeric data!")

        if not isinstance(data, list):
            data = [data]

        for item in data:
            self.data.append(str(item))
            self.ranks.append(self.data_processed)
            self.data_processed += 1


class TextProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError("Invalid text data!")

        if not isinstance(data, list):
            data = [data]

        for item in data:
            self.data.append(item)
            self.ranks.append(self.data_processed)
            self.data_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
                )

        if isinstance(data, list):
            return all(
                isinstance(item, dict) and all(
                    isinstance(key, str) and isinstance(value, str)
                    for key, value in item.items()
                )
                for item in data
            )

        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError("Invalid log data")

        if not isinstance(data, list):
            data = [data]

        for item in data:
            self.data.append(str(item))
            self.ranks.append(self.data_processed)
            self.data_processed += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    numeric = NumericProcessor()
    print("Data '42' = ", numeric.validate(42))
    print("Data 'invalid' = ", numeric.validate("invalid"))

    print("\nTesting Text Processor...")
    text = TextProcessor()
    print("Data 'Hello' = ", text.validate("Hello"))
    print("Data '42' = ", text.validate(42))

    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(
        "Valid log =", log.validate({"level": "INFO", "message": "Started"})
    )
    print("Invalid log =", log.validate("invalid"))

    print("\nTesting invalid ingestion...")
    try:
        numeric.ingest("invalid")
    except ValueError as error:
        print(f"Exception caught: {error}")

    numeric.ingest([10, 20, 30])
    text.ingest(["Hello", "World"])
    log.ingest([
        {"level": "INFO", "message": "Started"},
        {"level": "ERROR", "message": "Failed"}
    ])

    print("\nTesting output()...")
    for processor in (numeric, text, log):
        print(f"\n{processor.__class__.__name__}:")

        while processor.data:
            rank, data = processor.output()
            print(f"Rank: {rank}, Data: {data}")

    print("\nTesting output() with empty processor...")
    try:
        numeric.output()
    except ValueError as error:
        print(f"Exception caught: {error}")


if __name__ == "__main__":
    main()
