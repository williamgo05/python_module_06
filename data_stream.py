import typing
from data_processor import (
                    DataProcessor,
                    NumericProcessor,
                    TextProcessor,
                    LogProcessor,
                )


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for data in stream:
            processed = False

            for processor in self.processors:
                if processor.validate(data):
                    processor.ingest(data)
                    processed = True

            if not processed:
                print(f"DataStream error - Can't "
                      f"process element in stream: {data}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return

        for processor in self.processors:
            total = processor.data_processed
            remaining = len(processor.data)

            print(
                f"{type(processor).__name__}: "
                f"total {total} items processed, "
                f"remaining {remaining} on processor"
            )


def main() -> None:
    stream = DataStream()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Initialize Data Stream...")
    stream.print_processors_stats()

    print("\nRegistering processors...")
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    data = [
        42,
        "Hello",
        {"log_level": "INFO", "log_message": "Started"},
        [10, 20, 30],
        "World",
    ]

    print("\nProcessing data stream...")
    stream.process_stream(data)

    stream.print_processors_stats()

    print("\nConsuming elements...")
    for processor in stream.processors:
        if processor.data:
            processor.output()

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
