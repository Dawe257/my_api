import sqlite3
from flask import Flask
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)


class Chat(Resource):
    # Получить последние 10 сообщений
    def get(self):
        conn = sqlite3.connect(Settings.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM messages ORDER BY ID DESC LIMIT 10;')
        sql_response = cursor.fetchall()
        response = {
        }
        for item in reversed(sql_response):
            response[item[0]] = {
                'author': item[1],
                'text': item[2],
                'date': item[3]
            }
        conn.close()
        return response, 200

    # Отправить сообщение
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('author')
        parser.add_argument('text')
        params = parser.parse_args()
        params = (params['author'], params['text'])
        conn = sqlite3.connect(Settings.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages(author, text, date)"
                       "VALUES(?, ?, datetime('now'))", params)
        conn.commit()
        conn.close()
        return params, 200


api.add_resource(Chat, "/chat")
if __name__ == '__main__':
    app.run(port=45965, debug=True)
