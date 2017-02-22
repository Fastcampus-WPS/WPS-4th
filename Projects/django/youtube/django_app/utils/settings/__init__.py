import json
import os


def get_setting():
    path_utils = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path_root = os.path.dirname(os.path.dirname(path_utils))
    path_conf = os.path.join(path_root, '.conf')
    path_file_settings_local = os.path.join(path_conf, 'settings_local.json')
    with open(path_file_settings_local, 'r') as f:
        config_str = f.read()
    config = json.loads(config_str)
    return config
