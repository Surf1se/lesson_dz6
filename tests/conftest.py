import pytest
import allure
from faker import Faker
from dotenv import load_dotenv
from utils.helpers import API_KEY, TOKEN
from playwright.sync_api import sync_playwright

load_dotenv()
fake = Faker()

@pytest.fixture()
def query():
    return {
'key': f'{API_KEY}',
'token': f'{TOKEN}'
  }

@pytest.fixture()
@allure.title("Генерация описания для карточки")
def description():
    desc = {"desc": fake.text(50)}
    allure.attach(str(desc), name="Данные карточки", attachment_type=allure.attachment_type.JSON)
    return desc

@pytest.fixture()
@allure.title("Генерация имени и описания для карточки")
def description_update():
    data = {
        "name": fake.word(),
        "desc": fake.text(50)
    }
    allure.attach(str(data), name="Данные карточки", attachment_type=allure.attachment_type.JSON)
    return data

@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    yield browser
    browser.close()
    playwright.stop()

