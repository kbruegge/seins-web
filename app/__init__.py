__author__ = 'mackaiver'

from flask import Flask

app = Flask(__name__)
from app import view
