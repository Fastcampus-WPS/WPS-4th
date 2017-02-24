import json
import os


def get_config():
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    return json.loads(open(os.path.join(os.path.join(root_path, '.conf'), 'settings_local.json')).read())
