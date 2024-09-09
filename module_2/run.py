from urllib.request import urlopen
import json
from bs4 import BeautifulSoup
import re 

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


def clean_data(data):
    infoContainerMapping = {
        "programTerm": "Fall|Summer|Winter|Spring",
        "resultStatus": "Accepted|Rejected|Wait listed",
        "educationType": "PhD|Masters|MFA|MBA|JD|EdD|PsyD",
        "locationType": "International|American|Other",
        "gpa": "GPA",
        "gre": "GRE \d\d\d",
        "greV": "GRE V",
        "greAW": "GRE AW"
    }
    parsedResults = []
    for page in data:
        for resultCell in page:
            parsedResult = {}
            headerTag = resultCell.find("h6", class_="mt-3 fw-normal")
            if (headerTag):
                programSchoolText = headerTag.contents[0]
                parsedResult["program"] = programSchoolText
                notesTag = headerTag.contents[1]
                if (notesTag):
                    notesText = notesTag.contents[0] if len(notesTag.contents) else ''
                    parsedResult['notes'] = notesText        
            dateTag = resultCell.find("p", class_="mb-0 fst-italic")
            if (dateTag): 
                dateText = dateTag.contents[0]
                parsedResult['dateAdded'] = dateText
            print(resultCell)
            resultInfoContainer = resultCell.find("div", class_="mt-3")
            if resultInfoContainer:
                resultInfoCells = resultInfoContainer.find_all("span")
                for resultInfoCell in resultInfoCells:
                    infoText = resultInfoCell.contents[0]
                    for key in infoContainerMapping:
                        if key not in parsedResult: 
                            if re.findall(infoContainerMapping[key], infoText): parsedResult[key] = infoText.replace('\n', '').replace('\t', '').replace('Acceptedon', 'Accepted').replace('Rejectedon', 'Rejected')
                urlTag = resultInfoContainer.find("a")
                if (urlTag):
                    urlText = urlTag.attrs['href']
                    parsedResult["url"] = urlText
            parsedResults.append(parsedResult)
            print(parsedResult)
    return parsedResults

data = scrape_data(10)
data = clean_data(data)

with open('applicant_data.json', 'w') as json_file:
    json.dump(data, json_file)




    #each class="row mb-2"


        # if checkIfComments(resultCell):
        #     commentedResults.push(resultCell)
        #     break;






# def parseInfoContainer():


# def parseResultListingCell(resultCell):



        # each class="mt-3"
            # try result, date, 'X on 12 Jun'
            # try program date, Semester Y
            # try locationType, (International/American/Other)
            # try gpa, (GPA #.##)
            # try educationType, (PhD, Masters)
            # try gre, (GRE XXX)
            # try greV, (GRE V XXX)
            # try greAW, (GRE AW XXX)
            # try comments check (https://www.thegradcafe.com/result/938574#insticator-commenting, 1)
            # try url, (https://www.thegradcafe.com/result/938855)

# def checkIfComments(resultCell):
#     return 1




# class="Text-sc-1jeqstd-0 CommentText__CText-sc-urbev0-6 fCzisV" - comment text
# Text-sc-1jeqstd-0 CommentHeader__UserName-sc-5qytua-2 etXmVY - comment user name

# class Result:
#     def __init__(self, voice):


# @dataclass
# class Result:
#     detailedUrl: str
#     program: str
#     university: str
#     comments: list<str>
#     dateAdded: str
#     applicantStatus: str
#     applicantStatusDate: str
#     programDate: str
#     international: bool
#     mastersOrPHD: bool
#     gpa: str
#     gre: str
#     greAW: str
#     greV: str

    


