from quote_creator.quote_scraper import QuotesScraper


def main():
    results = QuotesScraper.getResults()
    quotes = QuotesScraper.scrape_quotes(results)
    QuotesScraper.quote_format(quotes)

if __name__ == "main":
    main()