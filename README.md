<p align="center"><img src="docs/assets/configura_logo.png" alt="Configura Logo" width="400"/></p>
<p align="center"><b>A lightweight, config-driven pipeline engine for structured data processing.</b></p>

---
### Why Configura

* Configura removes boilerplate and keeps data pipelines clean
* Instead of scattering I/O code, transformations, and logic across multiple scripts, everything is split into **small, reusable components**.
* **Adapters** handle I/O, **plugins** handle logic, and the **pipeline** defines all steps in **YAML/JSON**.
* This makes your flows easier to understand, extend, and maintain -- without **changing existing code** or adding complexity.

---
## Quickstart

### 1. Installation
```bash
git clone https://github.com/R3MISZ/configura
cd configura
pip install -e .
```

### 2. Input data `data/input/records.jsonl`

```json
{"id": 1, "value": 10}
{"id": 2, "value": 20}
{"id": 3, "value": 25}
{"id": 4, "value": 5}
```

### 3. Pipeline `data/configs/pipeline.yaml`

```yaml
pipeline:
  - type: "configura.adapters.jsonl_adapter:ReadJsonl"
    params: { path: "data/input/records.jsonl" }

  - type: "configura.plugins.filter_by_field:FilterByField"
    params: { key_name: "value", operator: ">=", value: 20 }

  - type: "configura.adapters.jsonl_adapter:WriteJsonl"
    params: { path: "data/output/records_output.jsonl" }
```

### 4. Run

```bash
# Default
configura --config data/configs/pipeline.yaml

# Default + debug output
configura --config data/configs/pipeline.yaml --verbose
```

or

```python
# configura/my_module.py
from configura.engine import run_pipeline_from_config

run_pipeline_from_config("data/configs/pipeline.yaml")
```

### 5. Result `data/output/records_output.jsonl`
```json
{"id": 2, "value": 20}
{"id": 3, "value": 25}
```

---
## How it Works

Every pipeline step is a Python `Class` which executes `process(data)`:

```python
def process(self, data):
    # code ...
    return data
```

Design principles:

* `adapters/` load or write data, define I/O boundaries
* `plugins/` modify or filter data, encapsulate transformation logic
* `engine.py` chains steps, handles ordering, passes outputs as inputs
* `loader.py` resolves class paths dynamically, enabling config-driven behavior

---
### Pipeline flow

Every step consumes data, transforms it, and outputs the result to the next step.
This allows new adapters or plugins to be added without modifying the engine.

<img src="docs/assets/flow.png" alt="Pipeline flow" width="500"/>

---

## Writing Your Own Plugin

### 1. Code

```python
# configura/plugins/normalize.py
class Normalize:
    def __init__(self, field: str):
        self.field = field

    def process(self, data: list[dict]):
        for row in data:
            value = row.get(self.field)
            if isinstance(value, str):
                row[self.field] = value.strip().lower()
        return data
```

### 2. Config

```yaml
# data/configs/my_config.yaml
- type: configura.plugins.normalize:Normalize
  params:
    field: "name"
```

**That’s it** -- the engine loads the class, injects parameters, and calls `process()`.

---

## Project Structure

```bash
src/
  configura/
    cli.py                # CLI entrypoint
    engine.py             # Pipeline executor
    loader.py             # Dynamic class loader (adapters, plugins, ...)
    io.py                 # Input/output utilities

    adapters/             # Input/output components
      base_adapter.py
      json_adapter.py
      ...

    plugins/              # Data transformations
      filter_by_field.py
      ...
data/
  configs/                # Pipeline definitions
  input/                  # Raw data
  dlq/                    # Failed/invalid data
  output/                 # Processed data
```

---

## Testing

Test adapters/plugins directly:

```python
from configura.plugins.filter_by_field import FilterByField

def test_filter_by_field():
    plugin = FilterByField(key_name="value", operator=">=", value=20)
    data = [
        {"id": 1, "value": 10},
        {"id": 2, "value": 20},
    ]

    result = plugin.process(data)

    assert result == [{"id": 2, "value": 20}]
```

Tests run without CLI dependency and can be applied directly to adapters/plugins

---
## Roadmap

- Improved error reporting
- Plugin discovery
- Graph visualization
- Parallel execution
- Stronger type validation


---
## License

MIT
