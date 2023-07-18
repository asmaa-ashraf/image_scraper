import requests
from bs4 import BeautifulSoup
import validators

def getdata(url):
    if not validators.url(url):
        url = input("The url you entered isn't a valid url.\nPlease,enter a valid url:")
        getdata(url)
    r = requests.get(url)
    return r.text

input_url = input('Please enter url to scrap images from:')
htmldata = getdata(input_url)
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])
