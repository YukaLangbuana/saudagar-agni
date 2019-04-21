import os
import json
from app import app
from app import db
from flask_restful import Resource
from flask import request 

class Query(Resource):

    def post(self):
        query = request.get_json()
        result = db.engine.execute(query['query']).fetchall()
        response = [dict(r) for r in result]
        return {
            "result": response
        }