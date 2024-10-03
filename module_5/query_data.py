"""
Creates a connection to the PostgreSQL database and executes various queries
to retrieve information about applicants.
"""

import psycopg
from psycopg import OperationalError, sql

def create_connection():
    """
    Creates a connection to the PostgreSQL database.

    :return: Database connection.
    :rtype: psycopg.Connection
    """
    connection = None
    try:
        # Attempt to connect to the PostgreSQL database
        connection = psycopg.connect('postgresql://neondb_owner:xNsRPKjk36Oo@ep-curly-hall-a5y59slx.us-east-2.aws.neon.tech/neondb?sslmode=require')
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        # Print an error message if the connection fails
        print(f"The error '{e}' occurred")
    return connection

def execute_query(query, params=None):
    """
    Execute a query on the database.

    :param query: The SQL query to execute.
    :type query: sql.Composable
    :param params: Optional parameters for the query.
    :type params: tuple
    :return: Query results.
    :rtype: list
    """
    # Establish a connection and execute the query
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute(query, params)  # Execute the provided query with optional parameters
        return cur.fetchall()  # Return all results

def count_entries_fall_2024():
    """
    Count the number of entries in the database for Fall 2024.

    :return: Number of applicants for Fall 2024.
    :rtype: str
    """
    # Query to count the number of entries with term 'Fall 2024'
    query = sql.SQL("SELECT COUNT(*) FROM applications WHERE term = %s LIMIT 1000")
    results = execute_query(query, ('Fall 2024',))[0][0]
    return f"Applicant count: {results}"

def percentage_international_students_fall_2024():
    """
    Calculate the percentage of international applicants for Fall 2024.

    :return: Percentage of international students.
    :rtype: str
    """
    # Query to calculate percentage of international applicants
    query = sql.SQL("""
        SELECT (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM applications WHERE term = %s)) 
        FROM applications 
        WHERE term = %s AND us_or_international = %s LIMIT 1000
    """)
    results = round(execute_query(query, ('Fall 2024', 'Fall 2024', 'International'))[0][0], 2)
    return f"Percent International: {results}"

def average_metrics_fall_2024():
    """
    Calculate the average GPA, GRE, GRE V, and GRE AW for applicants.

    :return: Average GPA, GRE, GRE V, GRE AW for Fall 2024 applicants.
    :rtype: str
    """
    # Query to calculate the average GPA, GRE, GRE V, GRE AW for all applicants who provided these metrics
    query = sql.SQL("""
        SELECT AVG(gpa), AVG(gre), AVG(gre_v), AVG(gre_aw) 
        FROM applications 
        WHERE gpa > 0 AND gre > 0 AND gre_v > 0 AND gre_aw > 0 LIMIT 1000
    """)
    results = execute_query(query)[0]
    gpa, gre, gre_v, gre_aw = results
    return f"Average GPA: {gpa}, Average GRE: {gre}, Average GRE V: {gre_v}, Average GRE AW: {gre_aw}"

def average_gpa_american_fall_2024():
    """
    Calculate the average GPA of American applicants for Fall 2024.

    :return: Average GPA for American applicants.
    :rtype: str
    """
    # Query to calculate the average GPA for American applicants for Fall 2024
    query = sql.SQL("""
        SELECT AVG(gpa) 
        FROM applications 
        WHERE term = %s AND us_or_international = %s AND gpa > 0 LIMIT 1000
    """)
    results = execute_query(query, ('Fall 2024', 'American'))[0][0]
    return f"Average GPA American: {results}"

def percentage_acceptances_fall_2024():
    """
    Calculate the percentage of acceptances for Fall 2024.

    :return: Percentage of accepted applicants.
    :rtype: str
    """
    # Query to calculate the percentage of applications that are accepted for Fall 2024
    query = sql.SQL("""
        SELECT (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM applications WHERE term = %s))
        FROM applications 
        WHERE term = %s AND status LIKE %s LIMIT 1000
    """)
    results = round(execute_query(query, ('Fall 2024', 'Fall 2024', '%Accepted%'))[0][0], 2)
    return f"Acceptance percent: {results}"

def average_gpa_accepted_fall_2024():
    """
    Calculate the average GPA of applicants who were accepted for Fall 2024.

    :return: Average GPA of accepted applicants.
    :rtype: str
    """
    # Query to calculate the average GPA for applicants who were accepted for Fall 2024
    query = sql.SQL("""
        SELECT AVG(gpa) 
        FROM applications 
        WHERE term = %s AND status LIKE %s AND gpa > 0 LIMIT 1000
    """)
    results = execute_query(query, ('Fall 2024', '%Accepted%'))[0][0]
    return f"Average GPA Acceptance: {results}"

def count_cs_masters_fall_2024():
    """
    Count the number of applicants who applied for a master's degree in Computer Science at JHU for Fall 2024.

    :return: Number of Computer Science master's degree applicants at JHU.
    :rtype: str
    """
    # Query to count the number of applicants for JHU's master's degree in Computer Science for Fall 2024
    query = sql.SQL("""
        SELECT COUNT(*) 
        FROM applications 
        WHERE term = %s AND degree = %s AND program LIKE %s LIMIT 1000
    """)
    results = execute_query(query, ('Fall 2024', 'Masters', '%Computer Science, Johns Hopkins%'))[0][0]
    return f"JHU Masters Computer Science count: {results}"

def execute_queries():
    """
    Execute all predefined queries and collect the results.

    :return: Dictionary containing the results of all queries.
    :rtype: dict
    """
    return {
        'count_entries_fall_2024': count_entries_fall_2024(),
        'percentage_international_students_fall_2024': percentage_international_students_fall_2024(),
        'average_metrics_fall_2024': average_metrics_fall_2024(),
        'average_gpa_american_fall_2024': average_gpa_american_fall_2024(),
        'percentage_acceptances_fall_2024': percentage_acceptances_fall_2024(),
        'average_gpa_accepted_fall_2024': average_gpa_accepted_fall_2024(),
        'count_cs_masters_fall_2024': count_cs_masters_fall_2024(),
    }

if __name__ == "__main__":
    # Execute all the queries and print the results
    print(execute_queries())
