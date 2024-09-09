import re
from scrape import scrape_data

# cleans pages of data where each page has college result postings
def clean_data(pagedData):
    # map between fields and regex
    infoContainerMapping = {
        "programTerm": "Fall|Summer|Winter|Spring",
        "resultStatus": "Accepted|Rejected|Wait listed|Interview",
        "educationType": "PhD|Masters|MFA|MBA|JD|EdD|PsyD",
        "locationType": "International|American|Other",
        "gpa": "GPA",
        "gre": "GRE \d\d\d",
        "greV": "GRE V",
        "greAW": "GRE AW"
    }
    parsedResults = []
    for page in pagedData:
        for resultCell in page:
            # initalize result
            parsedResult = {
                'program': None,
                'notes': None,
                'dateAdded': None,
                'programTerm': None,
                'resultStatus': None,
                'educationType': None,
                'locationType': None,
                'gpa': None,
                'gre': None,
                'greV': None,
                'greAW': None,
            }
            # parse the various tags to extract result information
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
            resultInfoContainer = resultCell.find("div", class_="mt-3")
            if resultInfoContainer:
                resultInfoCells = resultInfoContainer.find_all("span")
                for resultInfoCell in resultInfoCells:
                    infoText = resultInfoCell.contents[0]
                    for key in infoContainerMapping:
                        if re.findall(infoContainerMapping[key], infoText): parsedResult[key] = infoText.replace('\n', '').replace('\t', '').replace('Acceptedon', 'Accepted').replace('Rejectedon', 'Rejected')
                urlTag = resultInfoContainer.find("a")
                if (urlTag):
                    urlText = urlTag.attrs['href']
                    parsedResult["url"] = urlText
            if parsedResult['program']:
                parsedResults.append(parsedResult)
    return parsedResults

if __name__ == "__main__":
    data = scrape_data(300)
    data = clean_data(data)
