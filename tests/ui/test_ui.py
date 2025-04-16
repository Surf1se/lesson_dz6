import allure
from faker import Faker
from tests.conftest import browser
from pages.board_page import BoardPage
from pages.login_page import LoginPage
from utils.helpers import USERNAME, PASSWORD


fake=Faker()
@allure.title("Проверка создания и удаления карточки через UI")
def test_create_card(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    board_page = BoardPage(page)

    login_page.login('vys777@fabricoak.com', f'{PASSWORD}') #если возвращать переменную из .env выводит только первые 5 символов
    board_page.add_new_card()
    board_page.delete_card()
