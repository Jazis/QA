from time import sleep

import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import UNABLE_TO_LOG
from data.input_data.random_data import random_string
from data.input_data.users import USER_01


class TestAuthUser:
    @allure.title("Login & pass same")
    def test_auth_pass_same(self, api_request_context: APIRequestContext) -> None:
        data = {
            "username": USER_01.login,
            "password": USER_01.login
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1)
        assert response.status == 400
        assert response.text() == UNABLE_TO_LOG

    @allure.title("Username caps")
    def test_auth_username_caps(self, api_request_context: APIRequestContext) -> None:
        data = {
            "username": USER_01.login,
            "password": "UDAK7NSV7WWCtJG"
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1)
        assert response.status == 400
        assert response.text() == UNABLE_TO_LOG

    @allure.title("Username & password caps")
    def test_auth_username_pass_caps(self, api_request_context: APIRequestContext) -> None:
        data = {
            "username": "ADMIN@ADMIN.COM",
            "password": USER_01.password
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1.5)
        assert response.status == 200

    @allure.title("Username with space")
    def test_auth_username_with_space(self, api_request_context: APIRequestContext) -> None:
        data = {
            "username": "a dmi n@admin.com",
            "password": USER_01.password
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1)
        assert response.status == 400
        assert response.text() == UNABLE_TO_LOG

    @allure.title("Password with space")
    def test_auth_passw_with_caps(self, api_request_context: APIRequestContext) -> None:
        data = {
            "username": USER_01.login,
            "password": "UDaK7nSV7WWCtjG"
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1)
        assert response.status == 400

    @allure.title("Login with space")
    def test_auth_login_with_caps(self, api_request_context: APIRequestContext) -> None:
        data = {
            "username": 'admiN@admin.com',
            "password": USER_01.password
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1.5)
        assert response.status == 200

    @allure.title("Login & password with space")
    def test_auth_login_passw_with_caps(self, api_request_context: APIRequestContext) -> None:
        data = {
            "username": 'adm iN@admin.com',
            "password": "UdAK7n SV 7WWCtjG"
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1)
        assert response.status == 400
        assert response.text() == UNABLE_TO_LOG

    @allure.title("Auth only username")
    def test_auth_only_username(self, api_request_context: APIRequestContext) -> None:
        data = {
            "username": USER_01.login
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"password":["This field is required."]}'

    @allure.title("Auth only password")
    def test_auth_only_password(self, api_request_context: APIRequestContext) -> None:
        data = {
            "password": USER_01.password
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1)
        assert response.status == 500

    @allure.title("Auth password random")
    def test_auth_pass_random(self, api_request_context: APIRequestContext) -> None:
        data = {
            "username": USER_01.login,
            "password": random_string(15)
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1)
        assert response.status == 400
        assert response.text() == UNABLE_TO_LOG

    @allure.title("Auth username random")
    def test_auth_username_random(self, api_request_context: APIRequestContext) -> None:
        data = {
            "username": random_string(15),
            "password": USER_01.password
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1)
        assert response.status == 400
        assert response.text() == UNABLE_TO_LOG

    @allure.title("Auth password null")
    def test_auth_password_null(self, api_request_context: APIRequestContext) -> None:
        data = {
            "username": USER_01.login,
            "password": ""
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"password":["This field may not be blank."]}'

    @allure.title("Auth username null")
    def test_auth_username_null(self, api_request_context: APIRequestContext) -> None:
        data = {
            "username": "",
            "password": USER_01.password
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"username":["This field may not be blank."]}'

    @allure.title("Auth username & password null")
    def test_auth_username_passw_null(self, api_request_context: APIRequestContext) -> None:
        data = {
            "username": "",
            "password": ""
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"username":["This field may not be blank."],"password":["This field may not be blank."]}'

    @allure.title("Auth username & only numbers")
    def test_auth_username_numbers(self, api_request_context: APIRequestContext) -> None:
        data = {
            "username": 12346789,
            "password": USER_01.password
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1)
        assert response.status == 500

    @allure.title("Auth username & only space")
    def test_auth_username_only_space(self, api_request_context: APIRequestContext) -> None:
        data = {
            "username": " ",
            "password": USER_01.password
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1)
        assert response.status == 400

    @allure.title("Auth successful")
    def test_auth_successfull(self, api_request_context: APIRequestContext) -> None:
        data = {
            "username": USER_01.login,
            "password": USER_01.password
        }
        response = api_request_context.post(
            '/auth/login', data=data)
        sleep(1)
        assert response.status == 200
