from flask import Blueprint, render_template, redirect, url_for

error_pages_bp = Blueprint('error_pages_bp', __name__, template_folder='templates')

@error_pages_bp.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'), 404