from configura.constants import TYPE_DATA


class RenameFields:
    """
    Renames multiple fields in each record based on a mapping.

    Example mapping:
        {"firstName": "first_name", "lastName": "last_name"}

    YAML:
    ```yaml
        - type: "configura.plugins.rename_fields:RenameFields"
          params:
            mapping:
              firstName: first_name
              lastName: last_name
    ```
    """

    def __init__(self, mapping: dict[str, str]) -> None:
        self.mapping = mapping

    def process(self, data: TYPE_DATA) -> TYPE_DATA:
        if data is None:
            return []

        result: TYPE_DATA = []

        for row in data:
            # shallow copy
            new_row = dict(row)  

            for old_key, new_key in self.mapping.items():
                if old_key in new_row:
                    value = new_row.pop(old_key)
                    new_row[new_key] = value

            result.append(new_row)

        return result
