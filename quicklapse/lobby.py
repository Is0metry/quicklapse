import functools
from flask import (
    Blueprint, flash, g,redirect, render_template, request, session, url_for
)
from quicklapse.db import get_db

bp = Blueprint('lobby', __name__, url_prefix='/lobby')
@bp.route('/join', methods=('GET','POST'))
def joinGame():
    if request.method == 'POST':
        username = 