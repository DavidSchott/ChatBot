from flask import Blueprint
import download

main = Blueprint('main', __name__,static_folder='static', static_url_path='/static/main')
download.fetch()

from .routes import *
from .events import *
