Requests and parses college admission results from thegradcafe.com. This project complies with robots.txt

python run.py

Name: Randy Selimi
Module Info: Module 2 on 9/8/24
Approach: project split among 4 methods: scrape_data, clean_data, save_data, and load_data. scrape_data makes multiple requests to thegradcafe.com with a page size of 40. Each page is comprised of rows with college admission results that are passed into clean_data. clean_data traverses the HTML of each row in a fixed manner and creates an array of parsed objects literals. These object literals are converted into JSON and written to applicant_data.json in save_data. This JSON file is subsequently loaded and outputted in load_data.