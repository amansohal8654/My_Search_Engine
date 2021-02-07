import json
import requests
from bs4 import BeautifulSoup
# bas url 
first_url = "https://stackoverflow.com/questions"

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
    # extract question content
    description = content.findAll('div', {'class' : 'excerpt'})
    # extract question description
    links = content.findAll('a', {'class' : 'question-hyperlink'})

    #print(len(links), len(description))
    # loop over stack overflows question list
    for index in range(0, len(description)):
        # storing data
        question = {
            'title': links[index].text,
            'url' : links[index]['href'],
            'description' : description[index].text.strip().replace('\n', '')
        }
        #print data in json format
        print(json.dumps(question, indent = 2))

featch(first_url)