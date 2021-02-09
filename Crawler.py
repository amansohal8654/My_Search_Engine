import json
import requests
import re
import string
from bs4 import BeautifulSoup
# bas url 
first_url = "https://bola.kompas.com/"

# data fatching function
def featch(url):
    links = []
    documents = []
    try:
        # http request for given url
        response = requests.get(url)
        # errorn handling
    except response.exception.ConnectionError:
        print('Give URL : "%s" is not available!' % url)
    #parse content
    content = BeautifulSoup(response.text, 'html.parser')
    for i in content.find('div', {'class':'most__wrap'}).find_all('a'):
        i['href'] = i['href'] + '?page=all'
        links.append(i['href'])

    for i in links:
        # Make a request to the link
        r = requests.get(i)
    
        # Initialize BeautifulSoup object to parse the content 
        soup = BeautifulSoup(r.content, 'html.parser')
    
        # Retrieve all paragraphs and combine it as one
        sen = []
        for i in soup.find('div', {'class':'read__content'}).find_all('p'):
            sen.append(i.text)
            # Add the combined paragraphs to documents
        documents.append(' '.join(sen))
    
    docClean = []
    for d in documents:
        # Remove Unicode
        document_test = re.sub(r'[^\x00-\x7F]+', ' ', d)
        # Remove Mentions
        document_test = re.sub(r'@\w+', '', document_test)
        # Lowercase the document
        document_test = document_test.lower()
        # Remove punctuations
        document_test = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', document_test)
        # Lowercase the numbers
        document_test = re.sub(r'[0-9]', '', document_test)
        # Remove the doubled space
        document_test = re.sub(r'\s{2,}', ' ', document_test)
        docClean.append(document_test)
    return docClean


   

print(featch(first_url))