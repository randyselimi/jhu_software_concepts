# an object of WSGI application 
from flask import render_template, Blueprint
from query_data import execute_queries

# create home blueprint and add route
bp = Blueprint("home", __name__, 
               template_folder='../templates')
@bp.route('/') 
def home(): 
    queries = execute_queries()
    print(queries)
    count_entries_fall_2024 = queries.get('count_entries_fall_2024')
    print(count_entries_fall_2024)
    return render_template('home.html', query=queries)
