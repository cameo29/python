from selenium import webdriver
from bs4 import BeautifulSoup
import time
main_url = 'https://www.naver.com'

#####################################################################
# 브라우저 가동
driver = webdriver.PhantomJS(executable_path='C:\\Users\\edu\\node_modules\\phantomjs\\bin\\phantomjs')
#driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(main_url)
time.sleep(2)
driver.save_screenshot('1.png')
# 검색어 넣기
driver.find_element_by_id('query').send_keys('수능')
driver.find_element_by_id('search_btn').click()
time.sleep(2)
driver.save_screenshot('2.png')