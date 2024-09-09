from scrape import scrape_data
from clean import clean_data
import json

def save_data(data):
    with open('./module_2/applicant_data.json', 'w') as json_file:
        json.dump(data, json_file)

def load_data(data):
    with open('./module_2/applicant_data.json', 'r') as json_file:
        data = json.load(json_file)
        print(data)
        return data

data = scrape_data(10)
data = clean_data(data)
save_data(data)
load_data(data)