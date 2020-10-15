import json
import requests
from flask_restful import Resource, request

from settings import Settings


class Weather(Resource):
    def get(self):
        args = request.args
        if 'City' in args:
            city = args['City']
        else:
            city = 'Moscow'
        response = requests.get(
            'http://api.openweathermap.org/data/2.5/weather',
            params={
                'q': f'{city}',
                'appid': f'{Settings.weather_token}',
                'units': 'metric'
            })
        response = json.loads(response.text)['main']['temp']
        return f'Текущая погода в городе {city} - {response}', 200
