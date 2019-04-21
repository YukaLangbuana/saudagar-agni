import os
from app import app
from app import db
from flask_restful import Resource
import jsonify

class Query(Resource):

    def get(self):
        result = db.engine.execute("SELECT DISTINCT state FROM BUSINESS;").fetchall() 
        states = []
        for i in result:
            states.append(i[0])
        return {
            "states": states
        }
