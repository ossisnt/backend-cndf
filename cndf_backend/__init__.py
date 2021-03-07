from os import environ as env
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = env.get('APP_SECRET_KEY')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

from cndf_backend import routes
