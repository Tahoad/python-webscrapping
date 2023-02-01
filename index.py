from bs4 import BeautifulSoup
import requests

# url = "https://stackpython.co/courses"

url = "https://www.diw.go.th/webdiw/search-factory/"

res = requests.get(url)

res.encoding="utf-8"

print(res.status_code)

if(res.status_code == 200):
    print("Successfully")
elif res.status_code == 404:
    print("Not Found")

soup = BeautifulSoup(res.text,'html.parser')

input_list = []

# print(soup.prettify())

# print(soup.find_all('input'))

print(soup.find_all(attrs={"name" : "provname"}))


# inputs = soup.find_all('input')
# for i in inputs:
#     obj = i.string
#     input_list.append(obj)
#     print(obj)    