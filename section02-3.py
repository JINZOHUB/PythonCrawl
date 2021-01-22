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
   # 되게 코드를 수정한 것들
   #  // *[ @ id = "NM_NEWSSTAND_DEFAULT_THUMB"] / div[1] / div[1] / div / div[2] / div[1] / div / a[3]
   #  # NM_NEWSSTAND_DEFAULT_THUMB > div._NM_UI_PAGE_CONTAINER > div:nth-child(1) > div > div.thumb_area > div:nth-child(1) > div > a:nth-child(3)
   #
   # ".thumb_area .thumb_box._NM_NEWSSTAND_THUMB._NM_NEWSSTAND_THUMB_press_valid .popup_wrap a.btn_popup:last-child"
   #  a[data-clk="logo"]
   #  '.thumb_area .thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid .popup_wrap a.btn_popup' 안되는 내가 짠 코드
    for a in root.cssselect('a[data-clk="logo"] '):
        url = a.get('href')
        urls.append(url)

    return urls



if __name__ == "__main__":
    main()

