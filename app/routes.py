from flask import Blueprint
from app import db

bp = Blueprint('main', __name__)


@bp.route('/')
def home():
    return "Hello!"
