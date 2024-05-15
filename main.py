from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import os
from time import sleep
import re
import random
from bs4 import BeautifulSoup

from requests import get
from getpass import getpass
username=input('enter username or email')

pssd=getpass('Password:')



thisDir=os.getcwd()
print(thisDir)
"/_internal/geckodriver.exe"
ff=wd.Firefox(executable_path=thisDir+"/_internal/geckodriver.exe")
ff.get('https://www.instagram.com/')
sleep(20)
ff.find_element(By.XPATH,'//input[@name="username"]').send_keys(username)
ff.find_element(By.XPATH,'//input[@name="password"]').send_keys(pssd)
ff.find_element(By.XPATH,'//button[@type="submit"]').click()
sleep(10)
ff.find_element(By.XPATH,'//div[contains(text(),"Not now")]').click()
sleep(8)
ff.find_element(By.XPATH,'//*[contains(text(),"Not Now")]').click()
sleep(10)

successful=0
def instgram_block(target,successful):
    ff.get(target)
    sleep(10)
    ff.find_element(By.XPATH,'//div[@class="x6s0dn4 x78zum5 xdt5ytf xl56j7k"]').click()
    sleep(10)
    block_button=ff.find_element(By.XPATH,'//button[@class="_a9-- _ap36 _a9-_"]')
    check=(block_button.text)
    if check !="Unblock":
        block_button.click()
        sleep(3)
        ff.find_element(By.XPATH,'//div[@class="x78zum5 xdt5ytf x1crbq5u xvrdyt3 x179zr98"]//button').click()
        print('blocked !')
        successful=successful+1
        print('successful blocks :{successful}')
    else:
        print('already blocked')
    return successful


linksurl='https://docs.google.com/spreadsheets/d/1_BOYkvDgXGIjcAl1ZdYNuxN6gV-lARKGW9TOhHPVAh4/htmlview'
site=get(linksurl).content
table_rows=BeautifulSoup(site).find('table',{"class":"waffle"}).find_all('tr')
for  index,row in enumerate(table_rows):
    print(f'finished {index/len(table_rows)*100}')
    
    try:
        separate_data=(row.find_all('td'))
        name=separate_data[0].text
        instgram=separate_data[1].text
        print(name,instgram)
        successful=instgram_block(instgram)
    except:
        pass
ff.close()
quit()


