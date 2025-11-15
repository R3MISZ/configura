from configura.constants import TYPE_DATA

class DropFields:
    """
    Removes the specified fields from every record.
    """

    def __init__(self, fields: list[str]) -> None:
        self.fields = fields

    def process(self, data: TYPE_DATA) -> TYPE_DATA:
        if data is None:
            return []

        result: TYPE_DATA = []

        for row in data:
            new_row = {}

            # Copy all keys except the ones we want to drop
            for key, value in row.items():
                if key not in self.fields:
                    new_row[key] = value

            result.append(new_row)

        return result
