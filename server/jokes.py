import sqlite3
import json
import requests
from flask_restful import Resource, request

from settings import Settings


class Jokes(Resource):
    def get(self):
        conn = sqlite3.connect(Settings.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT text FROM jokes ORDER BY random() LIMIT 1;')
        response = {
            'text': f'{cursor.fetchall()[0][0]}'
            }
        conn.close()
        return response, 200
