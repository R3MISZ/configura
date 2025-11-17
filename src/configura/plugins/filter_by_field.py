from typing import Any
from configura.constants import TYPE_DATA

class FilterByField:
    def __init__(
            self,
            key_name: str,
            operator: str,
            value: Any,
            fail_on_type_error: bool = False
    ) -> None:
        self.key_name = key_name
        self.operator = operator
        self.value = value
        self.fail_on_type_error = fail_on_type_error
        
    @staticmethod
    def _get_by_path(obj: dict[str, Any], path: list[str]) -> Any:
        """
        Example:
        - obj = {"payload": {"temp_c": 18.7}}
        - path = ["payload", "temp_c"]
        - RETURN -> value of "temp_c" -> 18.7
        """
        curr = obj
        for key in path:
            if not isinstance(curr, dict) or key not in curr:
                return None
            curr = curr[key]
        return curr

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

        predicate = op_mapping.get(self.operator)
        if predicate is None:
            raise ValueError(f"Unsupported operator: {self.operator}")

        result: TYPE_DATA = []
        key_path = self.key_name.split(".")

        for item in data:
            field_value = self._get_by_path(item, key_path)

            # Pfad existiert nicht → skip
            if field_value is None:
                continue

            # Apply the operator
            try:
                if predicate(field_value, self.value):
                    result.append(item)
            except TypeError:
                if self.fail_on_type_error:
                    # explode hard to see the error
                    raise
                # Otherwise: just skip this row
                continue
        return result
