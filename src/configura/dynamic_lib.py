import importlib
import inspect

from typing import Any
from configura.constants import *

def load_class(type_string: str) -> type:
    """
    Load a class based on a type_string

    Example type_string: 'configura.plugins.builtin.transform_upper:TransformUpper'
    
    - module_path: 'configura.plugins.builtin.transform_upper'
    - attr: 'TransformUpper'
    """
    if not type_string:
        raise ValueError("No type string provided (step['type'] is empty)")

    # Split once to avoid unpack errors when ':' appears more than once
    try:
        module_path, attr = (part.strip() for part in type_string.split(":", 1))
    except ValueError as exc:
        raise ValueError(f"Invalid type string '{type_string}'. Expected '<module>:<ClassName>'") from exc

    if not module_path or not attr:
        raise ValueError(f"Invalid type string '{type_string}'. Expected '<module>:<ClassName>'")

    module = importlib.import_module(module_path)

    try:
        dynamic_class = getattr(module, attr)
    except AttributeError as exc:
        raise AttributeError(f"Module '{module_path}' does not define '{attr}'") from exc

    if not inspect.isclass(dynamic_class):
        raise TypeError(f"'{type_string}' does not refer to a class")

    return dynamic_class

def process_class(step: dict[str, Any], data: TYPE_DATA) -> TYPE_DATA:
    """
    Execute a single pipeline step

    If the type refers to a class:
        instance = Class(**params)
        return instance.process(data)
    """
    dynamic_class = load_class(step.get("type", ""))
    params = step.get("params") or {}

    if not isinstance(params, dict):
        raise TypeError("step['params'] must be a mapping (dict)")

    instance = dynamic_class(**params)

    if not hasattr(instance, "process"):
        raise AttributeError(f"{step.get('type', '<unknown>')} does not define a process(data) method")

    result = instance.process(data)
    return result
    # return cast(TYPE_DATA, result)