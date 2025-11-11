# Files
import sys
import os

# Command help
import argparse

# JSON Schema generation
import json
from genson import SchemaBuilder

def load_json_or_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
            # .jsonl - JSON Lines File
        if path.endswith(".jsonl"):
            return [json.loads(line) for line in f if line.strip()]
        else:
            # .json - JSON File
            return json.load(f)
    
def generate_schema(data):
    builder = SchemaBuilder()
    builder.add_schema({"$schema": "http://json-schema.org/draft-07/schema#"})
    if isinstance(data, list):
        for item in data:
            builder.add_object(item)
    else:
        builder.add_object(data)
    return builder.to_schema()

def coppy_input_name(input_path: str) -> str:
    # input_path: /path/to/events.jsonl
    file_name = os.path.basename(input_path)         
    name, file_type = os.path.splitext(file_name)            
    return f"{name}_schema.json"

def main():
    parser = argparse.ArgumentParser(
        prog="schema_generator.py",
        description="Generate JSON Schema from JSON or JSONL using Genson.",
    )
    parser.add_argument(
        "input",
        help="Input file path (.json or .jsonl)"
    )
    parser.add_argument(
        "-o",
        "--output",
        help=("Output path. Can be a filename, a directory, or a full path. If omitted, the output is created automatically in the current directory.")
    )

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"File not found: {args.input}")
        sys.exit(1)

    # If no output specified run method
    output_path = args.output or coppy_input_name(args.input)

    data = load_json_or_jsonl(args.input)
    schema = generate_schema(data)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(schema, f, indent=4, ensure_ascii=False)

    print(f"Schema generated: {output_path}")


if __name__ == "__main__":
    main()