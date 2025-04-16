from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'home'

    USERNAME_SELECTOR = '#username'
    PASSWORD_SELECTOR = '#password'
    LOGIN_BUTTON_SELECTOR = 'a[data-uuid="MJFtCCgVhXrVl7v9HA7EH_login"].Buttonsstyles__Button-sc-1jwidxo-0.kTwZBr'
    CONTINUE_BUTTON_SELECTOR = '#login-submit'
    HOME_PAGE_SELECTOR = 'div.abpjlyqfUhVUJ4:has-text("Рабочие пространства")'

    def login(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_click(self.LOGIN_BUTTON_SELECTOR)
        self.wait_for_selector_and_fill(self.USERNAME_SELECTOR, username)
        self.wait_for_selector_and_click(self.CONTINUE_BUTTON_SELECTOR)
        self.wait_for_selector_and_fill(self.PASSWORD_SELECTOR, password)
        self.wait_for_selector_and_click(self.CONTINUE_BUTTON_SELECTOR)
        self.wait_for_selector(self.HOME_PAGE_SELECTOR)
