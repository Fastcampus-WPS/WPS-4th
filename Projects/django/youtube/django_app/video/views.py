"""
search view의 동작 변경
1. keyword로 전달받은 검색어를 이용한 결과를 데이터베이스에 저장하는 부분 삭제
2. 결과를 적절히 가공하거나 그대로 템플릿으로 전달
3. 템플릿에서는 해당 결과를 데이터베이스를 거치지 않고 바로 출력

Next, Prev버튼 추가
1. Youtube Search API에 요청을 보낸 후, 결과에
    1-2. nextPageToken만 올 경우에는 첫 번째 페이지
    1-3. 둘다 올 경우에는 중간 어딘가
    1-4. prevPageToken만 올 경우에는 마지막 페이지 임을 알 수 있음
2. 템플릿에 nextPageToken, prevPageToken을 전달해서
    해당 token(next또는 prev)값이 있을 경우에 따라
    각각 '다음' 또는 '이전' 버튼을 만들어 줌
"""
import json

import requests
from dateutil.parser import parse
from django.shortcuts import render

from utils.settings import get_setting
from video.models import Video


def get_search_list_from_youtube(keyword):
    youtube_api_key = get_setting()['youtube']['API_KEY']
    # 3. requests 라이브러리를 이용(pip install requests), GET요청으로 데이터를 받아온 후
    # 이렇게 Parameter와 URL을 분리합니다
    params = {
        'part': 'snippet',
        'q': keyword,
        'maxResults': 5,
        'type': 'video',
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
    return items


def search(request):
    # 검색결과를 담을 리스트
    videos = []
    keyword = request.GET.get('keyword', '').strip()
    if keyword != '':
        items = get_search_list_from_youtube(keyword)

        for item in items:
            published_date_str = item['snippet']['publishedAt']

            # 실제로 사용할 데이터
            youtube_id = item['id']['videoId']
            title = item['snippet']['title']
            description = item['snippet']['description']
            published_date = parse(published_date_str)
            url_thumbnail = item['snippet']['thumbnails']['high']['url']

            # 현재 item을 dict로 정리
            cur_item_dict = {
                'title': title,
                'description': description,
                'published_date': published_date,
                'youtube_id': youtube_id,
                'url_thumbnail': url_thumbnail,
            }
            videos.append(cur_item_dict)
    # POST, GET요청 모두 results키에 값을 전달하지만, GET의 경우에는 해당내용이 비어있음
    context = {
        'videos': videos,
    }
    return render(request, 'video/search.html', context)
