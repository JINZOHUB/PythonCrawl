#Section 02-3
#파이썬 크롤링 기초
# lxml 함수 기초 사용법
#pip install lxml, requests, cssselect

import requests
import lxml.html

def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인함수
    """

    response = requests.get("https://www.naver.com")

    urls = scrape_news_list_page(response)

    for url in urls:
        print(url)

def scrape_news_list_page(response):
    urls=[]

    root = lxml.html.fromstring(response.content)


    for a in root.cssselect('.thumb_area .thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid .popup_wrap a.btn_popup'):
        url = a.get('href')
        urls.append(url)

    return urls



if __name__ == "__main__":
    main()

