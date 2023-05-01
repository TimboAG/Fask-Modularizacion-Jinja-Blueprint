from flask import Flask
from web_personal.vistas import base

app = Flask(__name__)
app.register_blueprint(base)
