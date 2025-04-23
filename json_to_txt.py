import json
import sys

def json_to_txt(json_file):
    with open(json_file) as f:
        data = json.load(f)
        for segment in data['segments']:
            print(f"{segment['start']} - {segment['end']}: {segment['text']}")

if __name__ == "__main__":
    json_to_txt(sys.argv[1])
