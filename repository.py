import os
from constants import CONFIG_FILE
from helpers.helpers_serialize import get_serialized_data


class Repository:
    def __init__(self):
        print("Initializing repository")
        self._repository_full_path = os.path.dirname(__file__)
        config_full_path = os.path.join(os.path.dirname(__file__), CONFIG_FILE)
        print(f"config_full_path={config_full_path}")
        config = get_serialized_data(config_full_path)
