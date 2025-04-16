import allure
from faker import Faker
from config.constant import idBoard
from api_clients.cards_api import CardsApi
from tests.conftest import query, description, description_update

fake = Faker()


class TestCards:

    card_api = CardsApi(query)

    @allure.title("Создание новой карточки")
    def test_create_card(self, query, description):
        response_post = TestCards.card_api.post_cards(query, description)
        assert response_post.status_code == 200, f"Ошибка создания карточки Status Code: {response_post.status_code}, {response_post.text}"

        id_card = response_post.json().get("id")
        response_get = TestCards.card_api.get_cards(query, id_card)
        assert response_get.status_code == 200, f"Не удалось получить данные созданной карточки Status Code: {response_get.status_code}"
        assert response_get.json().get("name") == query["name"], "Карточка создается  с неверным заголовком"
        assert response_get.json().get("desc") == description["desc"], "Карточка создается  с неверным описанием"
        assert response_get.json().get("idBoard") == idBoard, "Карточка привязывается к неверной доске"

        TestCards.card_api.delete_cards(query, id_card)

    @allure.title("Обновление описания карточки")
    def test_update_card(self, query, description, description_update):
        response_post = TestCards.card_api.post_cards(query, description)
        assert response_post.status_code == 200, f"Ошибка создания карточки Status Code: {response_post.status_code}"

        id_card = response_post.json().get("id")
        response_put = TestCards.card_api.put_cards(query, id_card, description_update)
        assert response_put.status_code == 200, f"Ошибка удаления карточки Status Code: {response_put.status_code}"

        response_get = TestCards.card_api.get_cards(query, id_card)
        assert response_put.json().get("name") == response_get.json().get("name"), "Имя карточки не обновилось"
        assert response_put.json().get("desc") == response_get.json().get("desc"), "Описание карточки не обновилось"

        TestCards.card_api.delete_cards(query, id_card)

    @allure.title("Удаление карточки")
    def test_delete_cards(self, query, description):
        response_post = TestCards.card_api.post_cards(query, description)
        assert response_post.status_code == 200, f"Ошибка создания карточки Status Code: {response_post.status_code}"

        id_card = response_post.json().get("id")
        response_delete = TestCards.card_api.delete_cards(query, id_card)
        assert response_delete.status_code == 200, f"Ошибка удаления карточки Status Code: {response_delete.status_code}"

        response_get = TestCards.card_api.get_cards(query, id_card)
        assert  response_get.status_code == 404, "Карточка не удалилась"
