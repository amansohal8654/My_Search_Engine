import requests
from bs4 import BeautifulSoup

first_url = "https://stackoverflow.com/questions"

response = requests.get(first_url)
content = BeautifulSoup(response.text, 'html.parser')
links = content.findAll('a', {'class' : 'question-hyperlink'})

print(links)