import selenium
from selenium import webdriver
import json
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

chromedriver_autoinstaller.install()

#Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument('--disable-dev-shm-usage')

#Run chrome
driver =  webdriver.Chrome('/home/<user>/chromedriver',chrome_options=chrome_options)

# do the code for your test
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