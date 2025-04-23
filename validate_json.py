import json
import sys
from jsonschema import validate, ValidationError

def main(json_file, schema_file):
    with open(json_file) as jf, open(schema_file) as sf:
        data = json.load(jf)
        schema = json.load(sf)
        try:
            validate(instance=data, schema=schema)
            print("Validation successful.")
        except ValidationError as e:
            print("Validation error:", e)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
