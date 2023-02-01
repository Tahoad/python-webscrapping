# Imports, of course
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time
import pandas as pd
# from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

#Add Options Firefox
ffopt = FirefoxOptions()
ffopt.add_argument("--headless")
chmopt=ChromeOptions()
chmopt.add_argument("--headless")
# driver = webdriver.Firefox(options=opt)
driver = webdriver.Chrome(options=chmopt)

# Initialize a Firefox webdriver
# wait = WebDriverWait(driver,10)
# wait.until(EC.url_to_be('https://userdb.diw.go.th/results1.asp'))
# Grab the web page

url = "https://www.diw.go.th/webdiw/search-factory/"

driver.get(url)

# You'll use selenium.webdriver.support.ui.Select
# that we imported above to grab the Seelct element called 
# t_web_lookup__license_type_name, then select Acupuncturists

# We use .find_element_by_name here because we know the name
# txtProvname = Select(driver.find_element_by_name("provname"))
# txtProvname = Select(driver.find_element_by_name("provname"))
path_provname = '//input[@name="provname"]'
# path_btnsubmit = '//input[@name="Submit"]'
txtProvname = driver.find_element(By.XPATH,path_provname)
driver.implicitly_wait(7)
txtProvname.send_keys("อุบลราชธานี")
txtProvname.submit()

# driver.implicitly_wait(7) 
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

doc = BeautifulSoup(driver.page_source, "html.parser")

# print("Document = ",doc)
# rows = doc.find('table',)

# doc.find_all
h2 = doc.find_all("h2")
print("h2 = ",h2)
table = doc.find("table").find_all('tr',attrs={'bgcolor':"#FFFFFF"})
print("table = ",table)

warehouses =[]

for row in table:
    if 'style' in row.attrs:
        pass
    else:
        cells = row.find_all("td")
        warehouse = {
            'col1' : cells[0].text.replace("\n",""),
            'col2' : cells[1].text.replace("\n",""),
            'col3' : cells[2].text.replace("\n",""),
            'col4' : cells[3].text.replace("\n",""),
        }
        warehouses.append(warehouse)

print(warehouses)

# print(doc)

driver.close()

warehouses_df = pd.DataFrame(warehouses)
print(warehouses_df)

warehouses_df.to_csv("../warehouses.csv",index=False,encoding='utf-8-sig')