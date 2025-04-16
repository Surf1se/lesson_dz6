from faker import Faker
from pages.base_page import BasePage

fake = Faker()


class BoardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'b/0Q8wyT8d/lngv'

    ADD_CARD_SELECTOR = '[data-list-id="67f9012dc529de4375817108"] .Sb_QqNKeadm2oq .IapUGb_Cq2VzSr button:has-text("Добавить карточку")'
    NAME_CARD_SELECTOR = '[data-testid="list-card-composer-textarea"]'
    ADD_BATTON_SELECTOR = 'button[data-testid="list-card-composer-add-card-button"]'
    OPEN_CARD_SELECTOR ='[data-testid="list-card"]'
    ARCHIVE_CARD_SELECTOR = '[data-testid="card-back-archive-button"]'
    DELETE_CARD_SELECTOR = '[data-testid="card-back-delete-card-button"]'
    APPROVE_DELETE_CARD_SELECTOR = '[data-testid="popover-confirm-button"]'


    def add_new_card(self):
        self.navigate_to()
        self.wait_for_selector_and_click(self.ADD_CARD_SELECTOR)
        self.wait_for_selector_and_fill(self.NAME_CARD_SELECTOR, fake.word())
        self.wait_for_selector_and_click(self.ADD_BATTON_SELECTOR)

    def delete_card(self):
        self.wait_for_selector_and_click(self.OPEN_CARD_SELECTOR)
        self.wait_for_selector_and_click(self.ARCHIVE_CARD_SELECTOR)
        self.wait_for_selector_and_click(self.DELETE_CARD_SELECTOR )
        self.wait_for_selector_and_click(self.APPROVE_DELETE_CARD_SELECTOR)
        self.wait_for_selector(self.ADD_CARD_SELECTOR)
