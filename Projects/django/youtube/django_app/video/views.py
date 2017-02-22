"""
1. .conf폴더의 settings_local.json을 읽어온다
2. 해당 내용을 json.loads()를 이용해 str -> dict형태로 변환
3. requests 라이브러리를 이용(pip install requests), GET요청으로 데이터를 받아온 후
4. 해당 내용을 다시 json.loads()를 이용해 파이썬 객체로 변환
5. 이후 내부에 있는 검색결과를 적절히 루프하며 print해주기
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
        'maxResults': 30,
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
    if request.method == 'POST':
        keyword = request.POST['keyword']
        items = get_search_list_from_youtube(keyword)
        for item in items:
            youtube_id = item['id']['videoId']
            title = item['snippet']['title']
            description = item['snippet']['description']
            published_date_str = item['snippet']['publishedAt']
            published_date = parse(published_date_str)
            defaults = {
                'title': title,
                'description': description,
                'published_date': published_date
            }
            Video.objects.get_or_create(
                youtube_id=youtube_id,
                defaults=defaults
            )

    videos = Video.objects.all()
    context = {
        'videos': videos,
    }
    return render(request, 'video/search.html', context)
