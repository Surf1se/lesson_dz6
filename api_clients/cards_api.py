import requests
from faker import Faker
from config.constant import url, idList
from tests.conftest import query, description

fake = Faker()

class CardsApi:

    def __init__(self, query):
        self.query = query

    def post_cards(self, query, description):
        query['name'] = f'{fake.word()}'
        query['idList'] = f'{idList}'
        response = requests.post(f'{url}', params=query, json=description)
        return response

    def get_cards(self, query, id_card):
        response = requests.get(f'{url}/{id_card}', params=query)
        return response

    def put_cards(self, query, id_card, description_update):
        response = requests.put(f'{url}/{id_card}', params=query, json=description_update)
        return response

    def delete_cards(self, query, id_card):
        response = requests.delete(f'{url}/{id_card}', params=query)
        return response
