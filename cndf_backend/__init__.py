from os import environ as env
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = env.get('APP_SECRET_KEY')

from cndf_backend import routes
