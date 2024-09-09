from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrape_data(numberOfPages): 
    scrapedPages = []
    for pageNumber in range(2, numberOfPages):
        url = "https://www.thegradcafe.com/survey/?page={pageNumber}&per_page=40".format(pageNumber=pageNumber)
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        resultsContainer = soup.find(id="results-container")
        resultCells = resultsContainer.find_all("div", class_="row mb-2")
        scrapedPages.append(resultCells)
    return scrapedPages
