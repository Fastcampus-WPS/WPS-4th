"""
1. .conf폴더의 settings_local.json파일 내용을 불러와
    json.loads()하여 config변수에 할당
"""
import json
import os

CUR_PATH = os.path.abspath(__file__)
SMS_TEST_PATH = os.path.dirname(CUR_PATH)
ROOT_PATH = os.path.dirname(SMS_TEST_PATH)
CONF_PATH = os.path.join(ROOT_PATH, '.conf')

config = json.loads(open(os.path.join(CONF_PATH, 'settings_local.json')).read())
