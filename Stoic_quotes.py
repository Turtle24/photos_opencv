import json
import requests
from bs4 import BeautifulSoup

url = 'https://dailystoic.com/stoic-quotes/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# Get results from website post-347
def getResults(ids):
    return soup.find(id = ids)
    
    
# results = soup.find(id='post-347')   
# print(results.prettify())
cnt = 0 
post_with_result = {}
for i in range(0, 1000):
    ids = 'post-' + str(i)
    
    results = getResults(ids)
    if results is None:
        continue
    post_with_result[i] = ids
    cnt += 1
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
print(post_with_result)