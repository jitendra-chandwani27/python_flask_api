from flask import Flask
from flask_restful import Resource, Api
import sqlite3
# from sqlite3 import Error
# import json
from flask import request
app = Flask(__name__)
api = Api(app)


class FindCapital(Resource):
    def get(self):
        country = request.args.get('cn')
        conn = sqlite3.connect("./database.db")
        with conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT Capital FROM findCapital WHERE Country = ?", (country,)
            )
            capital = cur.fetchone()
            if capital is None:
                return {'error': 'Invalid Country Found, Try Again'}
        return {'Country': country, 'Capital': capital[0]}


api.add_resource(FindCapital, '/')
if __name__ == '__main__':
    app.run(port=8000, debug=False, host='0.0.0.0')
