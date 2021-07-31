import json
import requests
from bs4 import BeautifulSoup


class QuotesScraper:
    url = "https://dailystoic.com/stoic-quotes/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    @staticmethod
    def getResults(ids):
        return QuotesScraper.soup.find(id=ids)

    @classmethod
    def scrape_quotes(cls):
        cnt = 0
        post_with_result = {}
        for i in range(0, 1000):
            ids = "post-" + str(i)

            results = cls.getResults(ids)
            if results is None:
                continue
            post_with_result[i] = ids
            cnt += 1
            job_elems = results.find_all("blockquote")
            quotes = {}
            for idx, job_elem in enumerate(job_elems):
                quote_elem = job_elem.find("p")
                if None in (quote_elem):
                    continue

                # Save quotes
                quotes[idx] = quote_elem.text.strip().split("\n")

    def quote_format(quotes):
        for _, value in quotes.items():
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
            with open("quotes.txt", "a") as textfile:
                with open("quotes.txt", "a") as file:
                    file.write(quotes + "\n")