from flask import Blueprint

v1 = Blueprint('v1', __name__)

from api.v1 import methods
