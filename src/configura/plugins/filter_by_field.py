from typing import Any
from configura.constants import TYPE_DATA

class FilterByField:
    def __init__(self, key_name: str, operator: str, value: Any) -> None:
        self.key_name = key_name
        self.operator = operator
        self.value = value

    def process(self, data: TYPE_DATA) -> TYPE_DATA:
        if data is None:
            return []

        op_mapping = {
            "==": lambda a, b: a == b,
            "!=": lambda a, b: a != b,
            ">":  lambda a, b: a > b,
            "<":  lambda a, b: a < b,
            ">=": lambda a, b: a >= b,
            "<=": lambda a, b: a <= b,
        }

        if self.operator not in op_mapping:
            raise ValueError(f"Unsupported operator: {self.operator}")

        found_op = op_mapping[self.operator]

        result: TYPE_DATA = []
        for item in data:
            value = item.get(self.key_name)
            if found_op(value, self.value):
                result.append(item)

        return result
