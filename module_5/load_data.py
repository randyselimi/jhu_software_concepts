"""
This module provides functionality to connect to a PostgreSQL database, load data from a JSON file,
create necessary database tables, and insert data in batches.
"""

import json
import os
import re
import psycopg
from psycopg import OperationalError, sql

def create_connection():
    """
    Establish a connection to the PostgreSQL database.

    :return: Database connection instance.
    """
    url = (
        'postgresql://neondb_owner:xNsRPKjk36Oo@ep-curly-hall-a5y59slx.us-east-2.aws.neon.tech/neondb?sslmode=require'
    )
    connection = None
    try:
        connection = psycopg.connect(url)
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def load_json():
    """
    Load applicant data from 'applicant_data.json'.

    :return: A list of parsed application tuples.
    """
    if os.path.exists('applicant_data.json'):
        with open('applicant_data.json', 'r', encoding="utf-8") as json_file:
            data = json.load(json_file)
            applications = []
            for application in data:
                date_added = re.sub(r"Added on", "", application['dateAdded'])
                gpa = float(re.sub(r"GPA\s*", "", application['gpa'])) if application['gpa'] else 0
                gre = float(re.sub(r"GRE\s*", "", application['gre'])) if application['gre'] else 0
                gre_v = float(re.sub(r"GRE V\s*", "", application['greV'])) if application['greV'] else 0
                gre_aw = float(re.sub(r"GRE AW\s*", "", application['greAW'])) if application['greAW'] else 0

                parsed_application = (
                    application['program'],
                    application['notes'],
                    date_added,
                    application['url'],
                    application['resultStatus'],
                    application['programTerm'],
                    application['locationType'],
                    gpa,
                    gre,
                    gre_v,
                    gre_aw,
                    application['educationType'],
                )
                applications.append(parsed_application)
            return applications
    return []

def create_database(connection, query):
    """
    Execute a SQL query to create a table in the database.

    :param connection: The database connection.
    :param query: SQL query to create the table.
    """
    connection.autocommit = True
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

def batch_insert(applications, batch_size=1000):
    """
    Insert application data into the database in batches.

    :param applications: List of application records to insert.
    :param batch_size: Number of records to insert per batch.
    """
    # Template for inserting applications
    application_template = sql.SQL(
        "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )

    # Split the applications into batches
    for i in range(0, len(applications), batch_size):
        batch = applications[i:i + batch_size]
        insert_query = sql.SQL(
            "INSERT INTO {} ({}) VALUES {}"
        ).format(
            sql.Identifier('applications'),
            sql.SQL(', ').join(map(sql.Identifier, [
                'program', 'comments', 'date_added', 'url', 'status',
                'term', 'us_or_international', 'gpa', 'gre', 'gre_v', 'gre_aw', 'degree'
            ])),
            sql.SQL(', ').join([application_template] * len(batch))
        )

        data = [item for sublist in batch for item in sublist]  # Flatten the batch data for execution

        conn = create_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(insert_query, data)
            conn.commit()
            print(f"Batch of {len(batch)} records inserted successfully.")
        except OperationalError as e:
            print(f"The error '{e}' occurred during batch insert")
        finally:
            conn.close()

if __name__ == "__main__":
    CONNECTION = create_connection()

    POSTS_TABLE = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {} (
            {} SERIAL PRIMARY KEY,
            {} TEXT NOT NULL,
            {} TEXT,
            {} DATE,
            {} TEXT,
            {} TEXT,
            {} TEXT,
            {} FLOAT,
            {} FLOAT,
            {} FLOAT,
            {} FLOAT,
            {} TEXT
        );
    """).format(
        sql.Identifier('applications'),
        sql.Identifier('p_id'),
        sql.Identifier('program'),
        sql.Identifier('comments'),
        sql.Identifier('date_added'),
        sql.Identifier('url'),
        sql.Identifier('status'),
        sql.Identifier('term'),
        sql.Identifier('us_or_international'),
        sql.Identifier('gpa'),
        sql.Identifier('gre'),
        sql.Identifier('gre_v'),
        sql.Identifier('gre_aw'),
        sql.Identifier('degree')
    )

    create_database(CONNECTION, POSTS_TABLE)
    loaded_applications = load_json()
    if loaded_applications:
        batch_insert(loaded_applications)
