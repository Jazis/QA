import pytest
from playwright.async_api import Page
from playwright.sync_api import expect

from data.input_data.users import USER_01, USER_UK, USER_EN, FAKE_VALID_USERS, FAKE_INVALID_USERS
from models.user import User
from pages.pages import Pages
from steps import Steps
from utils.consts import AUTH_URL, LOGIN_URL


class TestAuth:
    def test_change_theme(self, page: Page, pages: Pages, steps: Steps):
        page.goto(LOGIN_URL)
        pages.auth.login_input.fill(USER_01.login)
        pages.auth.password_input.fill(USER_01.password)
        pages.auth.login_button.click()
        pages.navigation.row_name.click()
        pages.navigation.my_profile.click()
        pages.settings_user.theme.click()
        pages.settings_user.theme_light.click()

    @pytest.mark.conf(locale="en-GB")
    def test_login_en(self, page: Page, pages: Pages, steps: Steps):
        page.goto(LOGIN_URL)
        pages.auth.base_check(page, "en-GB")
        pages.auth.login_input.fill(USER_EN.login)
        pages.auth.password_input.fill(USER_EN.password)
        pages.auth.login_button.click()
        expect(page.locator('//h1')).to_have_text("Cash")

    @pytest.mark.conf(locale="uk-UA")
    def test_login_uk(self, page: Page, pages: Pages, steps: Steps):
        page.goto(LOGIN_URL)
        pages.auth.base_check(page, "uk-UA")
        pages.auth.login_input.fill(USER_UK.login)
        pages.auth.password_input.fill(USER_UK.password)
        pages.auth.login_button.click()
        expect(page.locator('//h1')).to_have_text("Картки")

    @pytest.mark.conf(locale="ru-RU")
    def test_login_ru(self, page: Page, pages: Pages, steps: Steps):
        page.goto(LOGIN_URL)
        pages.auth.base_check(page, "ru-RU")
        pages.auth.login_input.fill(USER_01.login)
        pages.auth.password_input.fill(USER_01.password)
        pages.auth.login_button.click()
        expect(page.locator('//h1')).to_have_text("Счет")

    @pytest.mark.conf(locale="ru-RU")
    @pytest.mark.parametrize("user", FAKE_VALID_USERS)
    def test_auth_negative(self, page: Page, pages: Pages, steps: Steps, user: User):
        page.goto(LOGIN_URL)
        pages.auth.login_input.fill(user.login)
        pages.auth.password_input.fill(user.password)
        pages.auth.login_button.click()
        expect(page.locator('//*[contains(text(), "Unable to log in with provided credentials.")]'))

    @pytest.mark.browser_context_args(locale="ru-RU")
    @pytest.mark.parametrize("user", FAKE_INVALID_USERS)
    def test_validation_negative(self, page: Page, pages: Pages, steps: Steps, user: User):
        page.goto(AUTH_URL)
        pages.auth.login_input.fill(user.login)
        pages.auth.password_input.fill(user.password)
        pages.auth.login_button.click()
        expect(page.locator('//*[contains(text(), "Неверный email адрес")]'))

# TODO: дописать тесты на проверку ошибок на других локалях
