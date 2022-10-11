import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pyvirtualdisplay import Display
import json
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()    
options = [
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

driver.get('https://messmenu.epizy.com/')
d={}
d['date'] = driver.find_elements(by=selenium.webdriver.common.by.By.TAG_NAME, value='h3')[0].text
d['time'] = driver.find_elements(by=selenium.webdriver.common.by.By.TAG_NAME, value='h2')[0].text
d['occ'] = driver.find_elements(by=selenium.webdriver.common.by.By.TAG_NAME, value='h3')[1].text.encode("ascii", "ignore").decode()
li = driver.find_elements(by=selenium.webdriver.common.by.By.TAG_NAME, value='li')
d['li'] = [i.text for i in li]
if len(d['li'])==0:
    td = driver.find_elements(by=selenium.webdriver.common.by.By.TAG_NAME, value='td')
    d['td'] = {}
    for i in range(0,len(td)):
        if i % 2 == 0:
            d['td'][td[i].text] = td[i+1].text.encode("ascii", "ignore").decode().replace(" ", "")
driver.close()
with open('data.json', 'w') as outfile:
    json.dump(d, outfile, indent=4)
