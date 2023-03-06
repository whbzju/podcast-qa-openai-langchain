import requests
from bs4 import BeautifulSoup
import re

#url = 'https://podcasts.google.com/feed/XXX'
url = 'https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5jYXB0aXZhdGUuZm0vZ3JhZGllbnQtZGlzc2VudC8?sa=X&ved=2ahUKEwielruquML9AhUmhY4IHeKPDhgQ9sEGegQIARAG'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Find all divs with class 'zlb4lf'
divs = soup.find_all('div', {'class': 'zlb4lf'})

mp3_links = []

# Loop over all matching divs to extract the mp3 links
for div in divs:
    jsdata = div.find('div', {'jscontroller': 'lExGmf'})
    
    if jsdata:
        pattern = r'jsdata="(.*?)\;(.*?)\;(.*?)"'
        match = re.search(pattern, str(jsdata))

        if match:
            mp3_link = match.group(2)
            mp3_links.append(mp3_link)

print('total number:', len(mp3_links))
print('\n'.join(mp3_links))

