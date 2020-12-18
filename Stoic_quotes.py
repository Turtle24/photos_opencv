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

for key, value in quotes.items():
    # Formatting 
    quotes = value[0].replace("“", '"')
    quotes = quotes.replace("”", '"')
    quotes = quotes.replace("–", "-")
    quotes = quotes.replace("\xa0", "")
    quotes = quotes.replace("’", "'")
    quotes = quotes.replace("—", "--")
    quotes = quotes.replace("…", "...")
    quotes = quotes.replace("‘", "...")
    # write to txt file
    textfile = open('quotes.txt', 'a')
    with open('quotes.txt', 'a') as file:
        file.write(quotes + '\n')
    # textfile.write(quotes + '\n')
    textfile.close()  