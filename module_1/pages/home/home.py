# an object of WSGI application 
from flask import render_template, Blueprint

# create home blueprint and add route
bp = Blueprint("home", __name__, 
               template_folder='../templates')
@bp.route('/') 
def home(): 
    return render_template('home.html', active_page="home")
