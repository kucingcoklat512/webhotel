from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://DBhotel_catchthin:0d7c37a2b2e5cfb4baf665bdbadd64c7891a8f48@wowwx.h.filess.io:3305/DBhotel_catchthin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()