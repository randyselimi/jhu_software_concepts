# an object of WSGI application 
from flask import render_template, Blueprint

# create contact blueprint and add route
bp = Blueprint("contact", __name__, 
               template_folder='templates')
@bp.route('/contact')
def contact():
    return render_template('contact.html', active_page="contact")
