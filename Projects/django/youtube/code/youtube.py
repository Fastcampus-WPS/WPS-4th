"""
1. .conf폴더의 settings_local.json을 읽어온다
2. 해당 내용을 json.loads()를 이용해 str -> dict형태로 변환
3. requests 라이브러리를 이용(pip install requests), GET요청으로 데이터를 받아온 후
4. 해당 내용을 다시 json.loads()를 이용해 파이썬 객체로 변환
5. 이후 내부에 있는 검색결과를 적절히 루프하며 print해주기
"""
import json
import os
from datetime import datetime

from dateutil.parser import *
import requests

# 1. .conf폴더의 settings_local.json을 읽어온다
# .conf폴더까지의 PATH를 특정화해서 변수에 할당
# -> print(특정화한 PATH변수) 를 하면
#       .....(경로)/.conf/settings_local.json
#            이 출력되어야 함
# 파이썬에서 파일 읽는 내장함수를 사용해서 결과를 다시 변수에 할당
# 현재 파일 (youtube/code/youtube.py)
current_file_path = os.path.abspath(__file__)
print('current_file_path : \n%s' % current_file_path)

# 현재 파일에서 한 단계 부모 디렉토리 (youtube/code)
path_dir_code = os.path.dirname(current_file_path)
print('path_dir_code : \n%s' % path_dir_code)

# code디렉토리 보다 한 단계 위, 즉 현재 파이참 프로젝트 루트 폴더 (youtube)
path_dir_youtube = os.path.dirname(path_dir_code)
print('path_dir_youtube : \n%s' % path_dir_youtube)

# 루트 폴더의 바로 아래 .conf폴더 (youtube/.conf)
path_dir_conf = os.path.join(path_dir_youtube, '.conf')
print('path_dir_conf : \n%s' % path_dir_conf)

# .conf폴더 내부의 settings_local.json파일
path_file_settings_local = os.path.join(path_dir_conf, 'settings_local.json')
print('path_file_settings_local : \n%s' % path_file_settings_local)

# 파일을 열고 읽고 닫아준다
# f = open(path_file_settings_local, 'r')
# config_str = f.read()
# f.close()
with open(path_file_settings_local, 'r') as f:
    config_str = f.read()
print(config_str)
print('type(config_str) : %s' % type(config_str))

# 2. 해당 내용을 json.loads()를 이용해 str -> dict형태로 변환
# 해당내용 -> 1번에서 최종 결과
config = json.loads(config_str)
print('type(config) : %s' % type(config))
print('config : %s' % config)
youtube_api_key = config['youtube']['API_KEY']
print('youtube_api_key : %s' % youtube_api_key)

# 3. requests 라이브러리를 이용(pip install requests), GET요청으로 데이터를 받아온 후
# 이렇게 Parameter와 URL을 분리합니다
params = {
    'part': 'snippet',
    'q': '걸스데이 민아 직캠',
    'maxResults': 30,
    'key': youtube_api_key,
}
r = requests.get('https://www.googleapis.com/youtube/v3/search', params=params)
result = r.text

# 4. 해당 내용을 다시 json.loads()를 이용해 파이썬 객체로 변환
result_dict = json.loads(result)

# 5. 이후 내부에 있는 검색결과를 적절히 루프하며 print해주기
# pprint(result_dict)
kind = result_dict['kind']
etag = result_dict['etag']
next_page_token = result_dict['nextPageToken']
region_code = result_dict['regionCode']
page_info = result_dict['pageInfo']
page_info_total_results = page_info['totalResults']
page_info_results_per_page = page_info['resultsPerPage']

print('kind : %s' % kind)
print('etag : %s' % etag)
print('next_page_token : %s' % next_page_token)
print('region_code : %s' % region_code)
print('page_info_total_results : %s' % page_info_total_results)
print('page_info_results_per_page : %s' % page_info_results_per_page)

items = result_dict['items']
for index, item in enumerate(items):
    title = item['snippet']['title']
    published_date = item['snippet']['publishedAt']