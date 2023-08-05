from pathlib import Path
import os
import json
from faraday_agent_parameters_types.data_types import DATA_TYPE

DATA_FOLDER = Path(__file__).parent.parent / "data"


def indentify(obj):
    return type(DATA_TYPE[obj["type"]])


def generate_manifests():
    return [
        {
            "id_str": "old_manifest",
            "dir": DATA_FOLDER / "old_tool_manifest.json",
            "data": ["www.google.com", "80"],
        },
        {
            "id_str": "manifest",
            "dir": DATA_FOLDER / "tool_manifest.json",
            "data": ["www.ole.com", "80"],
        },
    ]


def generate_env(manifest):
    arguments_keys = []
    position = 0
    with open(manifest["dir"], "r") as f:
        data = json.load(f)

    for key, value in data["arguments"].items():
        key = f"EXECUTOR_CONFIG_{key}"
        os.environ[key] = manifest["data"][position]
        data_type = {
            "name": key,
        }
        value_type = get_type(value)
        if value_type is not None:
            data_type["type"] = value_type
        arguments_keys.append(data_type)
        position += 1
    return arguments_keys


def get_type(value):
    if isinstance(value, dict):
        return value["type"]
    else:
        return None
