import allure
from playwright.sync_api import expect

from models.user import User
from steps._base import BaseSteps


class AuthSteps(BaseSteps):
    @allure.step('Fill login and password as user "{1}" and click enter')
    def authorize(self, user: User):
        self.pages.auth.login_input.fill(user.login)
        self.pages.auth.password_input.fill(user.password)
        self.pages.auth.login_button.click()

    @allure.step('Check title')
    def check_title(self):
        self.pages.auth.title.is_visible()

    @allure.step('Fill login and password and click enter')
    def authorize_in_test(self, page, login, password, title):
        page.locator("//input[@id='username']").fill(login)
        page.locator("//input[@id='password']").fill(password)
        page.locator("//button[contains(@class, 'button styles_container')]").click()
        expect(page.locator("//h1")).to_have_text(title)