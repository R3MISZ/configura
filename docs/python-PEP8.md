### Python - PEP8

Example file demonstrating many PEP 8 rules:
- Imports, constants, classes, functions
- Type hints
- Line breaks for long signatures / calls
- Spacing, naming, docstrings

```python
from __future__ import annotations

import logging
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable, Iterator, Optional

# Standard logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)

LOGGER = logging.getLogger(__name__)

# Constants in ALL_CAPS
DEFAULT_ENCODING = "utf-8"
MAX_ITEMS = 100
PI_HALF = math.pi / 2


def read_text_file(path: Path, encoding: str = DEFAULT_ENCODING) -> str:
    """
    Reads a text file and returns its content as a string.

    Args:
        path: File path.
        encoding: Text encoding, default is utf-8.

    Returns:
        Content of the file as string.

    Raises:
        FileNotFoundError: If the file does not exist.
        UnicodeDecodeError: If the file cannot be decoded with the given encoding.
    """
    if not path.is_file():
        msg = f"File does not exist: {path}"
        raise FileNotFoundError(msg)

    LOGGER.debug("Reading file %s with encoding %s", path, encoding)

    with path.open("r", encoding=encoding) as file:
        return file.read()


def chunk_items(
    items: Iterable[Any],
    chunk_size: int,
) -> Iterator[list[Any]]:
    """
    Splits an iterable into fixed-size chunks.

    Args:
        items: Any iterable.
        chunk_size: Size of each chunk. Must be > 0.

    Yields:
        Lists containing up to `chunk_size` items.
    """
    if chunk_size <= 0:
        msg = "chunk_size must be greater than zero"
        raise ValueError(msg)

    current_chunk: list[Any] = []

    for item in items:
        current_chunk.append(item)
        if len(current_chunk) >= chunk_size:
            # Yield chunk and reset list
            yield current_chunk
            current_chunk = []

    if current_chunk:
        yield current_chunk


@dataclass(slots=True)
class Record:
    """
    Example data class.

    PEP 8:
    - Class names use CapWords.
    - Attributes use lower_case_with_underscores.
    """

    id: int
    name: str
    value: float
    active: bool = True

    def is_large(self, threshold: float = 0.0) -> bool:
        """
        Checks whether the value is larger than a threshold.
        """
        return self.value > threshold

    def as_dict(self) -> dict[str, Any]:
        """
        Returns the object as a dictionary (useful for logging or JSON).
        """
        return {
            "id": self.id,
            "name": self.name,
            "value": self.value,
            "active": self.active,
        }


class RecordProcessor:
    """
    Processes a list of `Record` objects.

    PEP 8:
    - Methods start with `self`.
    - One blank line between class methods.
    """

    def __init__(
        self,
        records: list[Record],
        transform: Optional[Callable[[Record], Record]] = None,
    ) -> None:
        self.records = records
        self.transform = transform

    def filter_active(self) -> list[Record]:
        """
        Returns only active records.
        """
        return [record for record in self.records if record.active]

    def apply_transform(self) -> None:
        """
        Applies a transform function to all records, if provided.
        """
        if self.transform is None:
            return

        transformed: list[Record] = []
        for record in self.records:
            try:
                new_record = self.transform(record)
            except Exception as exc:
                # Broad except is allowed when logged properly
                LOGGER.error("Transform failed for %s: %s", record, exc)
            else:
                transformed.append(new_record)

        self.records = transformed

    def summarize(self) -> dict[str, float]:
        """
        Returns basic statistics for the `value` field.
        """
        if not self.records:
            return {"count": 0, "min": 0.0, "max": 0.0, "avg": 0.0}

        values = [record.value for record in self.records]
        return {
            "count": float(len(values)),
            "min": min(values),
            "max": max(values),
            "avg": sum(values) / len(values),
        }


def format_summary(summary: dict[str, float]) -> str:
    """
    Formats the summary dictionary into a string.

    Demonstrates multi-line f-strings using parentheses, not backslashes.
    """
    return (
        f"Count: {summary['count']:.0f}, "
        f"Min: {summary['min']:.2f}, "
        f"Max: {summary['max']:.2f}, "
        f"Avg: {summary['avg']:.2f}"
    )


def example_long_function_signature(
    first_param: int,
    second_param: float,
    third_param: str,
    very_long_optional_parameter: Optional[list[int]] = None,
    *,
    keyword_only_flag: bool = False,
) -> dict[str, Any]:
    """
    Example of a long function signature formatted according to PEP 8.

    PEP 8:
    - Opening parenthesis on its own line, parameters indented.
    - Trailing commas allowed.
    """
    LOGGER.info("Running example_long_function_signature")
    return {
        "first": first_param,
        "second": second_param,
        "third": third_param,
        "optional": very_long_optional_parameter or [],
        "flag": keyword_only_flag,
    }


def _internal_helper(value: float) -> float:
    """
    Private helper function (leading underscore).
    """
    normalized = value / PI_HALF  # One space around binary operators
    return normalized * normalized


def main() -> None:
    """
    Application entry point.

    PEP 8:
    - Define `main` and call it in `if __name__ == "__main__"`.
    """
    records = [
        Record(id=1, name="Alpha", value=_internal_helper(1.0)),
        Record(id=2, name="Beta", value=_internal_helper(2.0)),
        Record(id=3, name="Gamma", value=_internal_helper(3.0), active=False),
    ]

    processor = RecordProcessor(records=records)
    active_records = processor.filter_active()
    LOGGER.info("Active records: %s", [r.as_dict() for r in active_records])

    processor.apply_transform()
    summary = processor.summarize()
    LOGGER.info("Summary: %s", format_summary(summary))

    for chunk in chunk_items(range(10), chunk_size=3):
        LOGGER.debug("Chunk: %s", chunk)


if __name__ == "__main__":
    main()
```