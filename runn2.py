from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

main_url = 'https://www.baemin.com/list/%ED%94%BC%EC%9E%90/%EC%84%9C%EC%9A%B8_%EC%84%9D%EC%B4%8C%EB%8F%99'

#####################################################################
# 브라우저 가동
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(main_url)
# ID가 'loadData'인 요소 div의 모든 자식들(div) => 업체 1개에 대한 진입 정보다
# 페이지 로딩이 즉각적으로 되지는 않는다!!
driver.implicitly_wait(10)
time.sleep(2)
# 로드된 페이지를 DOM 객체로 받아낸다 
html = driver.page_source
# DOM 객체 완성
urls = list()
soup = BeautifulSoup(html, "html.parser")
for link in soup.find_all(onclick=re.compile("fn_mv_shopInfo")):
    if "onclick" in link.attrs:
        str = link.attrs["onclick"]
        if not "#review" in str:
            str = str.replace('fn_mv_shopInfo(', '')
            str = str.replace('\'', '')
            str = str.replace(');', '')
            addr = str.split(',')
            # 데이터를 리스트에 추가
            urls.append("https://www.baemin.com/shop/%s/%s" % (addr[0], addr[1]))            
        
        #print( link.attrs["onclick"] )
        
# https://www.baemin.com/shop/업체관리번호/업체명 => url 리스트를 구성하시오
print( urls )
# 페이지를 계속 루프 돌면서 -> 방문 -> 스크레치 -> 정제 -> 디비입력 -> 다음~>
def loop(visits, index):
    driver.get(visits[index])
    driver.implicitly_wait(10)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    # 스크레치 or 크롤링
    #    # 데이터 정제
    #    # 디비 작업
    #        # 다음 턴
    #        loop(visits, ++index)


loop(urls, 0)





























