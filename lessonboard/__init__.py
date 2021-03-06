from flask import Flask
from lessonboard.models import db

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)


import lessonboard.views
