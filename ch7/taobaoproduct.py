from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
KEYWORD = 'iPad'

def index_page(page):
    """抓取索引页
    ：param page:页码
    """
    print('正在爬取第',page,'页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        if page > 1:
            input = wait.util(
                EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form > input'))
            )
