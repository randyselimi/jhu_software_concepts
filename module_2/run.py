import os
import json
from scrape import scrape_data
from clean import clean_data

def save_data(data):
    with open('applicant_data.json', 'w') as json_file:
        json.dump(data, json_file)

def load_data(data):
    if os.path.exists('applicant_data.json'):
        with open('applicant_data.json', 'r') as json_file:
            data = json.load(json_file)
            return data

# scrape and clean 12000 (300 * 40) results from thegradcafe.com
if __name__ == "__main__":
    data = scrape_data(300)
    data = clean_data(data)
    save_data(data)
    print(load_data(data))