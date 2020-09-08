import json


def read_json_file(filename: str) -> dict:
    with open(filename, "r") as f:
        data: dict = json.load(f)
    return data
