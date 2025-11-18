import json
import random
from datetime import datetime, timedelta
from pathlib import Path

TYPES = ["sensor_reading", "telemetry"]
STATUSES = ["ok", "warning"]

def generate_record(record_id: int, base_time: datetime) -> dict:
    ts = base_time.isoformat() + "Z"

    return {
        "id": record_id,
        "ts": ts,
        "type": random.choice(TYPES),
        "password": f"secret{record_id}",
        "debug": random.choice([True, False]),
        "internal_id": f"A-{record_id:03d}",
        "temp_flag": random.choice([True, False]),
        "payload": {
            "temp_c": round(random.uniform(18.0, 23.0), 1),
            "status": random.choice(STATUSES),
        },
    }

def generate_jsonl(filename: str = "generated_records.jsonl", count: int = 100) -> None:
    script_dir = Path(__file__).parent
    output_path = script_dir / filename
    base_time = datetime(2025, 11, 1, 12, 0, 0)

    with output_path.open("w", encoding="utf-8") as f:
        for i in range(1, count + 1):
            record_time = base_time + timedelta(seconds=i * random.randint(10, 90))
            record = generate_record(i, record_time)
            f.write(json.dumps(record) + "\n")

    print(f"Generated: {output_path}")


if __name__ == "__main__":
    generate_jsonl("records.jsonl", count=20)
