import requests
from bs4 import BeautifulSoup

url = "https://www.diw.go.th/webdiw/search-factory/"

# Send a GET request to the website to retrieve the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the "prov" input element and set its value to "อุบลราชธานี"
prov_input = soup.find_all("input", attrs={"name": "provname"})

# print("Prov_input = ",prov_input)

prov_input.insert(0,'อุบลราชธานี')

# print("Prov_input insert val = ",prov_input)
# Find the "submit" input element
submit_input = sorted.find("input", attrs={"name": "Submit"})

# print("Submit_input =",submit_input)

# Submit the form
response = requests.post(url, data={
    "provname": prov_input["value"],
    "Submit": submit_input["value"],
})

# # You can now parse the response content to extract the information you need
soup = BeautifulSoup(response.content, "html.parser")
# # ...