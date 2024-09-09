from urllib.request import urlopen
from bs4 import BeautifulSoup

# scrape pages of 40 results from thegradcafe.com
def scrape_data(numberOfPages): 
    scrapedPages = []
    iterator = 0
    for pageNumber in range(0, numberOfPages):
        print(iterator)
        iterator += 1
        url = "https://www.thegradcafe.com/survey/?page={pageNumber}&per_page=40".format(pageNumber=pageNumber)
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        # create a page of results and append it
        resultsContainer = soup.find(id="results-container")
        resultCells = resultsContainer.find_all("div", class_="row mb-2")
        scrapedPages.append(resultCells)
    return scrapedPages

if __name__ == "__main__":
    data = scrape_data(300)
