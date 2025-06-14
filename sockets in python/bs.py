from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.python.org"
response = urlopen(url)
html = response.read().decode()

soup = BeautifulSoup(html, "html.parser")
# Знайти всі заголовки новин на головній сторінці:
for item in soup.find_all("h2", class_="widget-title"):
    print(item.text)

# print(soup.prettify())