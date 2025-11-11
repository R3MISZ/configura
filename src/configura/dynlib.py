import importlib
import inspect

class DynamicLib:
    @staticmethod
    def load_lib(string: str):
        if not string:
            raise ValueError("Kein Typ-String angegeben.")
        
        module_path, _class = string.split(":")
        module = importlib.import_module(module_path)
        return getattr(module, _class)
    
    @staticmethod
    def run_lib(step : dict, data):
        _module = DynamicLib.load_lib(step.get("type", ""))
        params = step.get("params", {}) or {}

        # Can be method or class
        obj = _module(**params)

        # If class has attr process
        if inspect.isclass(_module):
            if hasattr(_module, "process"):
                return obj.process(data)
            else:
                raise AttributeError(f"{step.get("type")} has no process()-method.")
        # Function    
        else:
            # obj is result of method
            return obj

    @staticmethod
    def run_step(item, data):
        # steps --> list[dict] or dict
        if isinstance(item, dict):
            return DynamicLib.run_lib(item, data)
        elif isinstance(item, list):
            for _step in item:
                data = DynamicLib.run_lib(_step, data)
            return data
        else:
            raise ValueError(f"{item} is invaild type")