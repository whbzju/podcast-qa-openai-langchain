import requests
from bs4 import BeautifulSoup
import re

url = 'https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5jYXB0aXZhdGUuZm0vZ3JhZGllbnQtZGlzc2VudC8?sa=X&ved=2ahUKEwielruquML9AhUmhY4IHeKPDhgQ9sEGegQIARAG'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Find all divs with class 'zlb4lf'
divs = soup.find_all('div', {'class': 'oD3fme'})

for div in divs:
    # Get mp3 link
    jsdata = div.find('div', {'jscontroller': 'lExGmf'})
    pattern = r'jsdata="(.*?)\;(.*?)\;(.*?)"'
    match = re.search(pattern, str(jsdata))
    if match:
        mp3_link = match.group(2)
        print(mp3_link)

    # Get title
    title_div = div.find('div', {'class': 'e3ZUqe'})
    if title_div:
        print("find title div")
        title = title_div.text.strip()
        print(title)

    # Download mp3
    if mp3_link:
        response = requests.get(mp3_link)
        with open(f'{title}.mp3', 'wb') as f:
            f.write(response.content)

