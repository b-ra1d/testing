import requests
from bs4 import BeautifulSoup as Soup

r = requests.get('https://www.iamcook.ru/event/everyday')
soup = Soup(r.text, 'html.parser')

list = soup.find_all(class_="info")

for x in list:
  print(x.text)
