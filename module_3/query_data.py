import psycopg
from psycopg import OperationalError

def create_connection():
    connection = None
    try:
        connection = psycopg.connect('postgresql://neondb_owner:xNsRPKjk36Oo@ep-curly-hall-a5y59slx.us-east-2.aws.neon.tech/neondb?sslmode=require')
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

# Assuming a connection is established using the psycopg3 library
def execute_query(query):
    with psycopg.connect("postgresql://neondb_owner:xNsRPKjk36Oo@ep-curly-hall-a5y59slx.us-east-2.aws.neon.tech/neondb?sslmode=require") as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

# 1. How many entries do you have in your database who have applied for Fall 2024?
def count_entries_fall_2024():
    query = """
        SELECT COUNT(*) FROM applications WHERE term = 'Fall 2024';
    """
    results = execute_query(query)[0][0]

    return f"Applicant count: {results}"

# 2. What percentage of entries are from international students (not American or Other) (to two decimal places)?
def percentage_international_students_fall_2024():
    query = """
        SELECT (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM applications WHERE term = 'Fall 2024')) 
        FROM applications 
        WHERE term = 'Fall 2024' AND us_or_international = 'International';
    """
    results =  round(execute_query(query)[0][0], 2)
    return f"Percent International: {results}"


# 3. What is the average GPA, GRE, GRE V, GRE AW of applicants who provide these metrics?
def average_metrics_fall_2024():
    query = """
        SELECT 
            AVG(gpa), 
            AVG(gre), 
            AVG(gre_v), 
            AVG(gre_aw) 
        FROM applications 
        WHERE gpa > 0 AND gre > 0 and gre_v > 0 and gre_aw > 0
    """
    results = execute_query(query)[0]
    gpa = results[0]
    gre = results[1]
    gre_v = results[2]
    gre_aw = results[3]
    return f"Average GPA: {gpa}, Average GRE: {gre}, Average GRE V: {gre_v}, Average GRE AW: {gre_aw}"

# 4. What is the average GPA of American students in Fall 2024?
def average_gpa_american_fall_2024():
    query = """
        SELECT AVG(gpa) 
        FROM applications 
        WHERE term = 'Fall 2024' AND us_or_international = 'American' AND gpa > 0;
    """
    results =  execute_query(query)[0][0]
    return f"Average GPA American: {results}"

# 5. What percent of entries for Fall 2024 are Acceptances?
def percentage_acceptances_fall_2024():
    query = """
        SELECT (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM applications WHERE term = 'Fall 2024'))
        FROM applications 
        WHERE term = 'Fall 2024' AND status LIKE '%Accepted%';
    """
    results = round(execute_query(query)[0][0], 2)
    return f"Acceptance percent: {results}"

# 6. What is the average GPA of applicants who applied for Fall 2024 who are Acceptances?
def average_gpa_accepted_fall_2024():
    query = """
        SELECT AVG(gpa) 
        FROM applications 
        WHERE term = 'Fall 2024' AND status LIKE '%Accepted%' AND gpa > 0;
    """
    results = execute_query(query)[0][0]
    return f"Average GPA Acceptance: {results}"


# 7. How many entries are from applicants who applied to JHU for a master's degree in Computer Science?
def count_cs_masters_fall_2024():
    query = """
        SELECT COUNT(*) 
        FROM applications 
        WHERE term = 'Fall 2024' AND degree = 'Masters' AND program LIKE '%Computer Science, Johns Hopkins%';
    """
    results = execute_query(query)[0][0]
    return f"JHU Masters Computer Science count: {results}"

def execute_queries():
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
    print(execute_queries())
