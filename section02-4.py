#Section 02-3
#파이썬 크롤링 기초
# lxml 함수 기초 사용법


import requests
import lxml.html from fromstring, tostring

def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인함수
    """
    # 세션 사용
    session = requests.Session()

    # 스크랩핑 대상 URL
    response = requests.get("https://www.naver.com")

    # 신문사 링크 딕셔너리 획득
    urls = scrape_news_list_page(response)

    # 딕셔너리 확인
    #print(urls)

    for url in urls:
         print(url)

def scrape_news_list_page(response):
    # URL 딕셔너리 선언
    urls= {}
    # 태그 정보 문자열 저장
    root = fromstring(response.content)


    for a in root.xpath('//ul[@class="api_list"]/li[@class="api_item"]/a[@class="api_link"]'):
        # a 구조 확인
        # print(a)

        # a 문자열 출력
        # print(tostring(a, pretty_print=True))

        name , url = extract_contents(a)
        # 딕셔너리 삽입
        urls[name] = url

    # return urls

def extract_contents(dom):
    # 링크주소
    link = dom.get("href")

    # 신문사 명
    name = dom.xpath('./img')[0].get('alt') #xpath('./img')

    return name, link

if __name__ == "__main__":
    main()

