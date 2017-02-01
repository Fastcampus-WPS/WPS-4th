import requests
from bs4 import BeautifulSoup


def get_soup_from_url(url, params=None):
    '''
    url과 parameter를 사용해서 해당 URL에 GET요청을 보낸 결과(HTML text)로
    BeautifulSoup객체를 생성해 반환
    :param url: GET요청을 보낼 URL string
    :param params: GET요청 매개변수 dict
    :return: BeautifulSoup object
    '''
    # requests.get요청을 보낸 결과값(response객체)을 r변수에 할당
    r = requests.get(url, params=params)
    # response객체에서 text메서드를 사용해 내용을 html_doc변수에 할당
    html_doc = r.text

    # BeautifulSoup객체를 생성, 인자는 html text
    soup = BeautifulSoup(html_doc, 'lxml')
    return soup


