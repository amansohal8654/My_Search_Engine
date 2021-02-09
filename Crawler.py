import json
import requests
from bs4 import BeautifulSoup
# bas url 
first_url = "https://hackr.io/"
links = []
course = []
# data fatching function
def featch(url):
    try:
        # http request for given url
        response = requests.get(url)
        # errorn handling
    except response.exception.ConnectionError:
        print('Give URL : "%s" is not available!' % url)
    #parse content
    content = BeautifulSoup(response.text, 'html.parser')
    # extract question description
    link = content.find_all('a', {'class' : 'topic-grid-item'})
    for i in link:
        links.append(i['href'])

    r = requests.get(links[0])
    soup = BeautifulSoup(r.content, 'html.parser')
    data = soup.find("script").find_all("mainEntity")
    print(data)

featch(first_url)
#print(links)