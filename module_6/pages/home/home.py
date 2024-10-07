"""
Homepage for web app
"""
from flask import render_template, Blueprint

# create home blueprint and add route
bp = Blueprint("home", __name__,
               template_folder='../templates')
@bp.route('/')
def home():
    """
    Shows web app
    """
    return render_template('home.html', active_page="home")
