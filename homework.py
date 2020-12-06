from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup
import re
import chromedriver_binary
import pandas as pd

# ハローワークインターネットサービスのURL
url = "https://itc-lms.ecc.u-tokyo.ac.jp/lms/task"

# 以下からご自分で使用しているChromeのバージョンに合ったChromeDriverをダウンロードして下さい
# https://chromedriver.chromium.org/downloads

# ChromeDriverをご自分のPCの任意の場所に保存して、以下のDRIVER_PATHに設定して下さい。
driver = webdriver.Chrome()
time.sleep(1)
driver.get(url)
driver.find_element_by_class_name("square_button").click()
time.sleep(1)
element=driver.find_element_by_id("userNameInput")
element.send_keys("5864340639")
element=driver.find_element_by_id("passwordInput")
element.send_keys("rYoshi3!")
driver.find_element_by_class_name("submit").click()
time.sleep(1)
"""
driver.find_element_by_id("sidemenu_open").click()
time.sleep(1)
driver.find_element_by_class_name("sidemenu_link_task").click()
time.sleep(1)
driver.get("https://itc-lms.ecc.u-tokyo.ac.jp/lms/task")

# 今見ているページをBeautifulSoupで解析
soup = BeautifulSoup(driver.page_source, "html.parser")

# 「求人」のテーブルを検索
tasks = soup.find_all("a")
print(tasks)
"""
df=pd.DataFrame(columns=["course","title","deadline"])

course=driver.find_elements_by_class_name("tasklist-course.break.course")
title_class=driver.find_elements_by_class_name("tasklist-title.answer-test.break")
deadline=driver.find_elements_by_class_name("tasklist-mobile-width-deadline.deadline")
for i,_ in enumerate(course):
    title=title_class[i*2].find_element_by_tag_name("a")
    if not(course[i].text=="電気電子情報実験・演習第二" and title.text!="課題6　マイクロプロセッサの設計と実装"):
        df.loc[i]=[course[i].text,title.text,deadline[i].text]        
print(df)