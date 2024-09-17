import psycopg
from psycopg import OperationalError
import os
import json
import re

def create_connection():
    connection = None
    try:
        connection = psycopg.connect('postgresql://neondb_owner:xNsRPKjk36Oo@ep-curly-hall-a5y59slx.us-east-2.aws.neon.tech/neondb?sslmode=require')
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def load_json():
    if os.path.exists('applicant_data.json'):
        with open('applicant_data.json', 'r') as json_file:
            data = json.load(json_file)
            applications = []
            for application in data:
                dateAdded = re.sub(r"Added on", "", application['dateAdded'])
                gpa = 0
                if application['gpa']:
                    gpa = re.sub(r"GPA\s*", "", application['gpa'])
                gre = 0
                if application['gre']:
                    gre = re.sub(r"GRE\s*", "", application['gre'])
                greV = 0
                if application['greV']:
                    greV = re.sub(r"GRE V\s*", "", application['greV'])
                greAW=0
                if application['greAW']:
                    greAW = re.sub(r"GRE AW\s*", "", application['greAW'])

                parsedApplication = (
                    application['program'],
                    application['notes'], 
                    dateAdded,
                    application['url'], 
                    application['resultStatus'], 
                    application['programTerm'], 
                    application['locationType'], 
                    gpa,
                    gre, 
                    greV, 
                    greAW, 
                    application['educationType'], 
                                    )
                applications.append(parsedApplication)
            return applications

def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

def batch_insert(applications, batch_size=1000):
    # Make sure each record is wrapped in parentheses in the VALUES clause
    application_template = "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    # Split the applications into batches
    for i in range(0, len(applications), batch_size):
        batch = applications[i:i + batch_size]
        # Create query for the current batch
        application_records = ", ".join([application_template] * len(batch))
        
        insert_query = (
            f"INSERT INTO applications (program, comments, date_added, url, status, term, us_or_international, gpa, gre, gre_v, gre_aw, degree) VALUES {application_records}"
        )
        
        # Flatten the batch data for execution
        data = [item for sublist in batch for item in sublist]
        with psycopg.connect('postgresql://neondb_owner:xNsRPKjk36Oo@ep-curly-hall-a5y59slx.us-east-2.aws.neon.tech/neondb?sslmode=require') as conn:
                with conn.cursor() as cur:
                    cur.execute(insert_query, data)
                conn.commit()

if __name__ == "__main__":
    connection = create_connection()

    posts_table = """
        CREATE TABLE IF NOT EXISTS applications (
        p_id SERIAL PRIMARY KEY ,
        program TEXT NOT NULL,
        comments TEXT,
        date_added DATE,
        url TEXT,
        status TEXT,
        term TEXT,
        us_or_international TEXT,
        gpa FLOAT,
        gre FLOAT,
        gre_v FLOAT,
        gre_aw FLOAT,
        degree TEXT
        );
        """
    create_database(connection, posts_table)
    applications = load_json()
    batch_insert(applications)

