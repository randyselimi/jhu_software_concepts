"""
Shows publications
"""
from flask import render_template, Blueprint

# create publications blueprint and add route
bp = Blueprint("publications", __name__,
               template_folder='templates')
@bp.route('/publications')
def publications():
    """
    Shows publications
    """
    return render_template('publications.html', active_page="publications")
