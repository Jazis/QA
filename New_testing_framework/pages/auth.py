from pages.base_page import BasePage
from widgets.button import Button
from widgets.input import Input

from playwright.async_api import Page
from playwright.sync_api import expect


class AuthPage(BasePage):
    def __init__(self) -> None:
        super().__init__()

        self.login_input = Input(selector=self._locators.auth.login)
        self.password_input = Input(selector=self._locators.auth.pass_word)
        self.login_button = Button(selector=self._locators.auth.login_button)
        self.title = Button(selector=self._locators.auth.title)

    def base_check(self, page: Page, language: str):

        locators = self._locators.auth
        texts = locators.base_elements[language]

        expect(page.get_by_text(texts["no_account"])).to_be_visible()
        expect(page.get_by_text(texts["request_invite"])).to_be_visible()
        expect(page.get_by_text(texts["forgot_password"])).to_be_visible()
        expect(page.get_by_text(texts["privacy_policy"])).to_be_visible()
        expect(page.get_by_text(texts["terms_of_use"])).to_be_visible()

        expect(page.locator(locators.header_logo)).to_be_visible()
        expect(page.locator(locators.footer_text)).to_be_visible()
