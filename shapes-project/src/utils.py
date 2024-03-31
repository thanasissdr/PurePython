import json


def load_json(filepath: str):
    with open(filepath, "r") as f:
        data = json.load(f)
    return data
