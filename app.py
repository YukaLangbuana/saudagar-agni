from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

#APP
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yukalangbuana:yukalangbuana@localhost:5432/newagni'

#DB
db = SQLAlchemy(app)

#API
api = Api(app)

#CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

import models, resources
#############################################################################

api.add_resource(resources.Query, '/api/query')

@app.route("/")
def hello():
    result = db.engine.execute("SELECT DISTINCT state FROM BUSINESS;").fetchall() 
    return  str(result)