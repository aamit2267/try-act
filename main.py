import selenium
import selenium.webdriver
import chromedriver_autoinstaller
import json
chromedriver_autoinstaller.install()
driver = selenium.webdriver.Chrome("~/usr/bin/chromedriver")
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