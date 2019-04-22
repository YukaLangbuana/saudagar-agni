from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
import os

#APP
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yukalangbuana:yukalangbuana@localhost:5432/newagni'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

#DB
db = SQLAlchemy(app)

#API
api = Api(app)

#CORS
CORS(app)

import models, resources
#############################################################################
api.add_resource(resources.Query, '/api/query')
