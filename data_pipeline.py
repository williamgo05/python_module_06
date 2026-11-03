from typing import Protocol, Any
from data_processor import (
                    DataProcessor,
                    NumericProcessor,
                    TextProcessor,
                    LogProcessor,
                )


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExporter:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [text for _, text in data]
        csv_data = ",".join(values)
        print(csv_data)


class JSONExporter:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = []

        for index, text in data:
            item = f'{{"id": {index}, "value": "{text}"}}'
            items.append(item)

        json_data = "[\n " + ",\n ".join(items) + "\n]"
        print(json_data)


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:

        for processor in self.processors:
            data: list[tuple[int, str]] = []
            for _ in range(nb):
                if processor.data:
                    data.append(processor.output())
                else:
                    break

            plugin.process_output(data)

    def process_stream(self, stream: list[Any]) -> None:
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


def main():
    stream = DataStream()
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

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

    print("Processing data stream...")
    stream.process_stream(data)

    print("\nExporting to CSV...")
    stream.output_pipeline(3, CSVExporter())


if __name__ == "__main__":
    main()
