"""
sms에 view를 생성 (index)
수신자번호, 메시지를 입력받을수 있는 Form클래스 구현
해당 Form에서 데이터를 받아 문자를 전송하도록 함
끝
"""
import json
import os

CUR_PATH = os.path.abspath(__file__)
SMS_TEST_PATH = os.path.dirname(CUR_PATH)
ROOT_PATH = os.path.dirname(SMS_TEST_PATH)
CONF_PATH = os.path.join(ROOT_PATH, '.conf')

config = json.loads(open(os.path.join(CONF_PATH, 'settings_local.json')).read())
