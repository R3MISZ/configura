from typing import Optional
from configura.constants import TYPE_DATA

class Limit:
    """
    Limits the data by:
        - count: first N records
        - start + end: slice by index range [start:end]

    Rules:
        - If start or end is provided → use range slicing
        - Else if count is provided → take first count
        - Else → error
    """

    def __init__(
        self,
        count: Optional[int] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
    ) -> None:
        self.count = count
        self.start = start
        self.end = end

        if self.start is not None or self.end is not None:
            # Valid range mode
            if self.start is None or self.end is None:
                raise ValueError("Both 'start' and 'end' must be provided for range mode.")
        else:
            # No range mode → fall back to count
            if self.count is None:
                raise ValueError("Either 'count' or ('start' and 'end') must be provided.")

    def process(self, data: TYPE_DATA) -> TYPE_DATA:
        if data is None:
            return []

        # Range mode
        if self.start is not None and self.end is not None:
            return data[self.start : self.end]

        # Count mode
        return data[: self.count]
