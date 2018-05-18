from flask import Flask
from flask_restful import Resource, Api
import sqlite3
from sqlite3 import Error
import json
app = Flask(__name__)
api = Api(app)

class FindCapital(Resource):
    def get(self):
        country=raw_input("Country : ")
        # try:
        #     conn = sqlite3.connect("/home/ranosys/sqlite-autoconf-3080100/database.db")
        #     with conn:
        #         cur=conn.cursor()
        #         cur.execute("SELECT Capital FROM findCapital WHERE Country = ?",(country,))
        #         capital = cur.fetchone()
        # except Error as e:
        #     print("Invalid country name")
        conn = sqlite3.connect("./database.db")
        with conn:
            cur=conn.cursor()
            cur.execute("SELECT Capital FROM findCapital WHERE Country = ?",(country,))
            capital = cur.fetchone()
        return {'Country':country, 'Capital':capital[0]}
api.add_resource(FindCapital, '/')
if __name__ == '__main__':
    app.run(port=8000,debug=False, host='0.0.0.0')
