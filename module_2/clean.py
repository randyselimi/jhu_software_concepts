import re

def clean_data(data):
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
            if parsedResult:
                parsedResults.append(parsedResult)
                print(parsedResult)
    return parsedResults
