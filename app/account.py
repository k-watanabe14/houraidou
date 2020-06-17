from flask import Blueprint, request, render_template, flash, redirect, url_for, g
from werkzeug.exceptions import abort
from app.auth import login_required
from app import db
 
# Define the blueprint: 'register', set its url prefix: app.url/register
mod_account = Blueprint('account', __name__, url_prefix='/account')


@mod_account.route('/')
@login_required
def index():
    return render_template('account/index.html')
