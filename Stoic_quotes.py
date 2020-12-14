import json
import requests
from bs4 import BeautifulSoup

url = 'https://dailystoic.com/stoic-quotes/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='post-347')


#print(results.prettify())

job_elems = results.find_all('blockquote')
quotes = {}
for idx, job_elem in enumerate(job_elems):
    quote_elem = job_elem.find('p')
    if None in (quote_elem):
        continue

    # Save quotes
    quotes[idx] = quote_elem.text.strip().split("\n")

    # textfile = open('quotes.txt', 'w')
    # textfile.write(quote_elem.text.strip())
    # textfile.close()

for i in quotes.keys():
    print(i)