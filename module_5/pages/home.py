"""
Defines a blueprint for the home route of the Flask application.
"""

# Import necessary modules
from flask import render_template, Blueprint
import query_data

# Create the home blueprint and add route
bp = Blueprint("home", __name__, template_folder='../templates')

@bp.route('/')
def home():
    """
    Render the home page with query data.
    """
    queries = query_data.execute_queries()
    count_entries_fall_2024 = queries.get('count_entries_fall_2024')
    print(queries)
    print(count_entries_fall_2024)
    return render_template('home.html', query=queries)
