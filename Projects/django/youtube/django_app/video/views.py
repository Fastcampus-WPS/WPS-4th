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


def search_from_youtube(keyword, page_token=None):
    youtube_api_key = get_setting()['youtube']['API_KEY']
    # 3. requests 라이브러리를 이용(pip install requests), GET요청으로 데이터를 받아온 후
    # 이렇게 Parameter와 URL을 분리합니다
    params = {
        'part': 'snippet',
        'q': keyword,
        'maxResults': 15,
        'type': 'video',
        'key': youtube_api_key,
    }
    # 페이지 토큰값이 전달되었을 때만 params에 해당 내용을 추가해서 요청
    if page_token:
        params['pageToken'] = page_token

    r = requests.get('https://www.googleapis.com/youtube/v3/search', params=params)
    result = r.text

    # 4. 해당 내용을 다시 json.loads()를 이용해 파이썬 객체로 변환
    result_dict = json.loads(result)
    return result_dict


def search(request):
    videos = []
    context = {
        'videos': videos,
    }

    keyword = request.GET.get('keyword', '').strip()
    page_token = request.GET.get('page_token')

    if keyword != '':
        # 검색 결과를 받아옴
        search_result = search_from_youtube(keyword, page_token)

        # 검색결과에서 이전/다음 토큰, 전체 결과 개수를 가져와
        # 템플릿에 전달할 context객체에 할당
        next_page_token = search_result.get('nextPageToken')
        prev_page_token = search_result.get('prevPageToken')
        total_results = search_result['pageInfo'].get('totalResults')
        context['next_page_token'] = next_page_token
        context['prev_page_token'] = prev_page_token
        context['total_results'] = total_results
        context['keyword'] = keyword

        # 검색결과에서 'items'키를 갖는 list를 items변수에 할당 후 loop
        items = search_result['items']
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

    return render(request, 'video/search.html', context)
