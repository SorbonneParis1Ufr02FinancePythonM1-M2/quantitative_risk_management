import json
import os

import tomli
import yaml


def get_serialized_data(full_path: str) -> dict:
    """
    return serialized information as dictionary from a yaml, json, or toml file
    :param full_path: source file full path
    :return: information as dict
    """
    _, file_extension = os.path.splitext(full_path)
    with open(full_path, mode='rb') as f:
        if file_extension == '.yaml':
            return yaml.load(f, Loader=yaml.FullLoader)
        elif file_extension == '.json':
            return json.load(f)
        elif file_extension == '.toml':
            return tomli.load(f)
        else:
            raise ValueError(f'Unsupported file format {file_extension}')
