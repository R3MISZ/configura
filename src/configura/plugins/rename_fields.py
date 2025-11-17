from configura.constants import TYPE_DATA
from typing import Any

class RenameFields:
    def __init__(self, mapping: dict[str, str]) -> None:
        self.mapping = mapping

    @staticmethod
    def _get_by_path(obj: dict[str, Any], path: list[str]) -> Any:
        """
        Example:
        - obj = {"payload": {"temp_c": 18.7}}
        - path = ["payload", "temp_c"]
        - RETURN -> value of "temp_c" -> 18.7
        """
        curr: Any = obj
        for key in path:
            if not isinstance(curr, dict):
                return None
            if key not in curr:
                return None
            curr = curr[key]
        return curr

    @staticmethod
    def _delete_by_path(obj: dict[str, Any], path: list[str]) -> None:
        """
        Example:
        - obj = {"payload": {"temp_c": 18.7}}
        - path = ["payload", "temp_c"]
        - DELETE -> "temp_c" in "payload
        """
        if not path:
            return

        curr: Any = obj
        for key in path[:-1]:
            if not isinstance(curr, dict):
                return
            if key not in curr:
                return
            curr = curr[key]

        if isinstance(curr, dict):
            curr.pop(path[-1], None)

    @staticmethod
    def _set_by_path(obj: dict[str, Any], path: list[str], value: Any) -> None:
        """
        Example:
        - obj = {"payload": {"status": "ok"}}
        - path = ["payload", "temp_celsius"]
        - value = 18.7
        - SET -> obj["payload"]["temp_celsius"] = value (18.7)
        - RESULT -> {"payload": {"status": "ok", "temp_celsius": 18.7}}
        """
        if not path:
            return

        curr: Any = obj
        for key in path[:-1]:
            if not isinstance(curr.get(key), dict):
                return  # key does not exist -> no change
            curr = curr[key]

        if isinstance(curr, dict):
            curr[path[-1]] = value

    def process(self, data: TYPE_DATA) -> TYPE_DATA:
        if data is None:
            return []

        result: TYPE_DATA = []

        for item in data:
            copied_item: dict[str, Any] = dict(item) # Shallow Copy

            # str1, str2 in dict[str1, str2]
            for old_key, new_key in self.mapping.items():

                #key -> payload.temp_C
                old_path: list[str] = old_key.split(".")
                new_path: list[str] = new_key.split(".")

                # 1. Wert über Pfad suchen
                value = self._get_by_path(copied_item, old_path)
                if value is None:
                    continue # does not exist -> skip

                # 2. Delete old key
                self._delete_by_path(copied_item, old_path)

                # 3. Set new key
                self._set_by_path(copied_item, new_path, value)

            result.append(copied_item)

        return result
