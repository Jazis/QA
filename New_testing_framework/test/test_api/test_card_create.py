from time import sleep

import allure
import pytest
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED
from data.input_data.random_data import random_string
from data.input_data.api.card_create import DATA, DATA1
from utils.json_validation import validate_json_schema


class TestCardCreate:
    @pytest.mark.skip("")
    @allure.title("Create card")
    def test_create_card(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": random_string(5),
            "limit": 4,
            "limit_amount": 200000,
            "user": 392,
            "card_bin": 7
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 201
        assert response.text().__contains__("id")
        assert response.text().__contains__("created_at")
        assert response.text().__contains__("number")
        assert response.text().__contains__("name")
        assert response.text().__contains__("frozen_by")
        assert response.text().__contains__("limit")
        assert response.text().__contains__("limit_amount")
        assert response.text().__contains__("limit_spend")
        assert response.text().__contains__('"payment_system":"mc"')
        assert response.text().__contains__(
            '"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801"')
        assert response.text().__contains__(
            '"user":{"id":392,"email":"sderewrwf@mail.ru","person":{"first_name":"dsef","last_name":"dsfdsg"}}')
        assert response.text().__contains__('"status":1')
        assert response.text().__contains__('"settled":0.0')
        assert response.text().__contains__('"refund":0.0')
        assert response.text().__contains__('"pending":0.0')
        assert response.text().__contains__('"reversed_amount":0.0')
        assert response.text().__contains__('"fx_fee":0.0')
        assert response.text().__contains__('"cross_border_fee":0.0')
        assert response.text().__contains__('"decline_fee":0.0')
        assert response.text().__contains__('"spend":0.0')

    @allure.title("Create card wrong bin")
    def test_wrong_bin(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": " % *TEsT ()",
            "limit": 3,
            "limit_amount": 200000,
            "user": 392,
            "card_bin": 778
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"card_bin":["Invalid pk \\"778\\" - object does not exist."]}'

    @pytest.mark.skip("")
    @allure.title("Create card without bin")
    def test_without_bin(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": random_string(6),
            "limit": 3,
            "limit_amount": 200000,
            "user": 392
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 201
        assert response.text().__contains__("id")
        assert response.text().__contains__("created_at")
        assert response.text().__contains__("number")
        assert response.text().__contains__("name")
        assert response.text().__contains__("frozen_by")
        assert response.text().__contains__("limit")
        assert response.text().__contains__("limit_amount")
        assert response.text().__contains__("limit_spend")
        assert response.text().__contains__('"payment_system":"mc"')
        assert response.text().__contains__(
            '"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801"')
        assert response.text().__contains__(
            '"user":{"id":392,"email":"sderewrwf@mail.ru","person":{"first_name":"dsef","last_name":"dsfdsg"}}')
        assert response.text().__contains__('"status":1')
        assert response.text().__contains__('"settled":0.0')
        assert response.text().__contains__('"refund":0.0')
        assert response.text().__contains__('"pending":0.0')
        assert response.text().__contains__('"reversed_amount":0.0')
        assert response.text().__contains__('"fx_fee":0.0')
        assert response.text().__contains__('"cross_border_fee":0.0')
        assert response.text().__contains__('"decline_fee":0.0')
        assert response.text().__contains__('"spend":0.0')

    @allure.title("Create card with bin = 0")
    def test_without_bin_zero(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": random_string(6),
            "limit": 3,
            "limit_amount": 200000,
            "user": 392,
            "card_bin": 0
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"card_bin":["Invalid pk \\"0\\" - object does not exist."]}'

    @pytest.mark.skip("")
    @allure.title("Create card with bin = null")
    def test_without_bin_null(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": random_string(6),
            "limit": 3,
            "limit_amount": 200000,
            "user": 392,
            "card_bin": None
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 201
        assert response.text().__contains__("id")
        assert response.text().__contains__("created_at")
        assert response.text().__contains__("number")
        assert response.text().__contains__("name")
        assert response.text().__contains__("frozen_by")
        assert response.text().__contains__("limit")
        assert response.text().__contains__("limit_amount")
        assert response.text().__contains__("limit_spend")
        assert response.text().__contains__('"payment_system":"mc"')
        assert response.text().__contains__(
            '"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801"')
        assert response.text().__contains__(
            '"user":{"id":392,"email":"sderewrwf@mail.ru","person":{"first_name":"dsef","last_name":"dsfdsg"}}')
        assert response.text().__contains__('"status":1')
        assert response.text().__contains__('"settled":0.0')
        assert response.text().__contains__('"refund":0.0')
        assert response.text().__contains__('"pending":0.0')
        assert response.text().__contains__('"reversed_amount":0.0')
        assert response.text().__contains__('"fx_fee":0.0')
        assert response.text().__contains__('"cross_border_fee":0.0')
        assert response.text().__contains__('"decline_fee":0.0')
        assert response.text().__contains__('"spend":0.0')

    @allure.title("Create card with name more 50 sym.")
    def test_create_card_with_name_more_50_symbols(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": "kfjhgjdfkglkasjflsjdflksjfkldsjfkldsjfkldsjfklaffff",
            "limit": 2,
            "limit_amount": 200000,
            "user": 392,
            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"name":["Ensure this field has no more than 50 characters."]}'

    @allure.title("Create card without auth")
    def test_create_card_without_auth(self, api_request_context: APIRequestContext) -> None:
        data = {
            "name": "er54",
            "limit": 2,
            "limit_amount": 200000,
            "user": 392,
            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card',  data=data
        )
        sleep(1)
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Create card with  invalid (- 10) limit")
    def test_invalid_limit(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": "kfjhgjdfkglkasjflsjdflksjfkldsjfkldsjfkldsjfklaffff",
            "limit": -10,
            "limit_amount": 200000,
            "user": 392,
            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 400
        assert response.text() == ('{"name":["Ensure this field has no more than 50 '
                                   'characters."],"limit":["Invalid pk \\"-10\\" - object does not exist."]}')

    @allure.title("Create card with invalid limit = 0")
    def test_invalid_limit_zero(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": random_string(7),
            "limit": 0,
            "limit_amount": 200000,
            "user": 392,
            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"limit":["Invalid pk \\"0\\" - object does not exist."]}'

    @allure.title("Create card with invalid limit = 45")
    def test_invalid_limit(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": random_string(7),
            "limit": 45,
            "limit_amount": 200000,
            "user": 392,
            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"limit":["Invalid pk \\"45\\" - object does not exist."]}'

    @pytest.mark.skip("")
    @allure.title("Create card without row limit")
    def test_without_limit(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": random_string(7),
            "limit_amount": 200000,
            "user": 392,
            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 201
        assert response.text().__contains__("id")
        assert response.text().__contains__("created_at")
        assert response.text().__contains__("number")
        assert response.text().__contains__("name")
        assert response.text().__contains__("frozen_by")
        assert response.text().__contains__("limit")
        assert response.text().__contains__("limit_amount")
        assert response.text().__contains__("limit_spend")
        assert response.text().__contains__('"payment_system":"mc"')
        assert response.text().__contains__(
            '"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801"')
        assert response.text().__contains__(
            '"user":{"id":392,"email":"sderewrwf@mail.ru","person":{"first_name":"dsef","last_name":"dsfdsg"}}')
        assert response.text().__contains__('"status":1')
        assert response.text().__contains__('"settled":0.0')
        assert response.text().__contains__('"refund":0.0')
        assert response.text().__contains__('"pending":0.0')
        assert response.text().__contains__('"reversed_amount":0.0')
        assert response.text().__contains__('"fx_fee":0.0')
        assert response.text().__contains__('"cross_border_fee":0.0')
        assert response.text().__contains__('"decline_fee":0.0')
        assert response.text().__contains__('"spend":0.0')

    @pytest.mark.skip("")
    @allure.title("Create card with invalid limit = null")
    def test_invalid_limit(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": random_string(7),
            "limit": None,
            "limit_amount": 200000,
            "user": 392,
            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 201
        assert response.text().__contains__("id")
        assert response.text().__contains__("created_at")
        assert response.text().__contains__("number")
        assert response.text().__contains__("name")
        assert response.text().__contains__("frozen_by")
        assert response.text().__contains__("limit")
        assert response.text().__contains__("limit_amount")
        assert response.text().__contains__("limit_spend")
        assert response.text().__contains__('"payment_system":"mc"')
        assert response.text().__contains__(
            '"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801"')
        assert response.text().__contains__(
            '"user":{"id":392,"email":"sderewrwf@mail.ru","person":{"first_name":"dsef","last_name":"dsfdsg"}}')
        assert response.text().__contains__('"status":1')
        assert response.text().__contains__('"settled":0.0')
        assert response.text().__contains__('"refund":0.0')
        assert response.text().__contains__('"pending":0.0')
        assert response.text().__contains__('"reversed_amount":0.0')
        assert response.text().__contains__('"fx_fee":0.0')
        assert response.text().__contains__('"cross_border_fee":0.0')
        assert response.text().__contains__('"decline_fee":0.0')
        assert response.text().__contains__('"spend":0.0')
    @pytest.mark.skip("")
    @allure.title("Create card with amount and name null ")
    def test_card_with_amount_and_name_null(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": ' ',
            "limit": 1,
            "limit_amount": None,
            "user": 392,
            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 201
        assert response.text().__contains__("id")
        assert response.text().__contains__("created_at")
        assert response.text().__contains__("number")
        assert response.text().__contains__("name")
        assert response.text().__contains__("frozen_by")
        assert response.text().__contains__("limit")
        assert response.text().__contains__("limit_amount")
        assert response.text().__contains__("limit_spend")
        assert response.text().__contains__('"payment_system":"mc"')
        assert response.text().__contains__(
            '"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801"')
        assert response.text().__contains__(
            '"user":{"id":392,"email":"sderewrwf@mail.ru","person":{"first_name":"dsef","last_name":"dsfdsg"}}')
        assert response.text().__contains__('"status":1')
        assert response.text().__contains__('"settled":0.0')
        assert response.text().__contains__('"refund":0.0')
        assert response.text().__contains__('"pending":0.0')
        assert response.text().__contains__('"reversed_amount":0.0')
        assert response.text().__contains__('"fx_fee":0.0')
        assert response.text().__contains__('"cross_border_fee":0.0')
        assert response.text().__contains__('"decline_fee":0.0')
        assert response.text().__contains__('"spend":0.0')

    @allure.title("Create card with limit amount null")
    def test_card_with_limit_amount_null(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": ' ',
            "limit": 3,
            "limit_amount": None,
            "user": 392,
            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"status":"error","error_message":"Set to No limit if you want a value higher than 500000."}'

    @pytest.mark.skip("")
    @allure.title("Create card with limit & amount = 0")
    def test_create_card_with_limit_amount_0(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": '1234567',
            "limit": 2,
            "limit_amount": 0,
            "user": 392,
            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 201
        assert response.text().__contains__("id")
        assert response.text().__contains__("created_at")
        assert response.text().__contains__("number")
        assert response.text().__contains__("name")
        assert response.text().__contains__("frozen_by")
        assert response.text().__contains__("limit")
        assert response.text().__contains__("limit_amount")
        assert response.text().__contains__("limit_spend")
        assert response.text().__contains__('"payment_system":"mc"')
        assert response.text().__contains__(
            '"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801"')
        assert response.text().__contains__(
            '"user":{"id":392,"email":"sderewrwf@mail.ru","person":{"first_name":"dsef","last_name":"dsfdsg"}}')
        assert response.text().__contains__('"status":1')
        assert response.text().__contains__('"settled":0.0')
        assert response.text().__contains__('"refund":0.0')
        assert response.text().__contains__('"pending":0.0')
        assert response.text().__contains__('"reversed_amount":0.0')
        assert response.text().__contains__('"fx_fee":0.0')
        assert response.text().__contains__('"cross_border_fee":0.0')
        assert response.text().__contains__('"decline_fee":0.0')
        assert response.text().__contains__('"spend":0.0')

    @allure.title("Create card with limit & amount = -100")
    def test_create_card_with_limit_amount__100(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": '1234567',
            "limit": 2,
            "limit_amount": -100,
            "user": 1,
            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"status":"error","error_message":"Some error. Please try again later."}'

    @allure.title("Create card with big limit amount")
    def test_big_limit(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": random_string(6),
            "limit": 3,
            "limit_amount": 20000000000000,
            "user": 392,
            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"limit_amount":["Ensure this value is less than or equal to 2147483647."]}'

    @allure.title("Create card with null limit amount")
    def test_null_limit_amount(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": random_string(6),
            "limit": 3,
            "limit_amount": "",
            "user": 392,
            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"limit_amount":["A valid integer is required."]}'

    @allure.title("Create card with invalid user")
    def test_null_invalid_user(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": random_string(6),
            "limit": 3,
            "limit_amount": 250,
            "user": 3920,
            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"user":["Invalid pk \\"3920\\" - object does not exist."]}'

    @allure.title("Create card with user null")
    def test_null_user(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": random_string(6),
            "limit": 3,
            "limit_amount": 250,
            "user": None,
            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"user":["This field may not be null."]}'

    @allure.title("Create card with user name null")
    def test_null_user_name(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": None,
            "limit": 3,
            "limit_amount": 250,
            "user": 392,
            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"name":["This field may not be null."]}'

    @allure.title("Create card without user")
    def test_without_user(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": None,
            "limit": 3,
            "limit_amount": 250,

            "card_bin": 10
        }
        response = api_request_context.post(
            '/api/card', headers=headers, data=data
        )
        sleep(1)
        assert response.status == 400
        assert response.text() == '{"name":["This field may not be null."],"user":["This field is required."]}'

############ Card detail

    @allure.title("Card detail closed card")
    def test_card_detail_closed(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        response = api_request_context.get(
            '/api/card/273/detail', headers=headers
        )
        sleep(1)
        assert response.status == 200
        assert response.text() == '{"method":"direct","data":{"card_number":"4411126114228149","expiration_date":{"month":5,"year":25},"cvv":"909","cardholder":"Rize Ads"}}'

    @allure.title("Card detail active card")
    def test_card_detail_active(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        response = api_request_context.get(
            '/api/card/268/detail', headers=headers
        )
        sleep(1)
        assert response.status == 200
        assert response.text() == '{"method":"direct","data":{"card_number":"4411124268902981","expiration_date":{"month":5,"year":25},"cvv":"185","cardholder":"Rize Ads"}}'

    @allure.title("Card detail freeze card")
    def test_card_detail_freeze(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        response = api_request_context.get(
            '/api/card/113/detail', headers=headers
        )
        sleep(1)
        assert response.status == 200
        assert response.text() == '{"method":"direct","data":{"card_number":"5319930920567032","expiration_date":{"month":3,"year":25},"cvv":"091","cardholder":"Rize Ads"}}'

    @allure.title("Card detail wrong card")
    def test_card_detail_wrong_card(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        response = api_request_context.get(
            '/api/card/0/detail', headers=headers
        )
        sleep(1)
        assert response.status == 500

    @allure.title("Card detail wrong id card")
    def test_card_detail_wrong_id_card(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        response = api_request_context.get(
            '/api/card/-12/detail', headers=headers
        )
        sleep(1)
        assert response.status == 404

    @allure.title("Card filter by status -1")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_status__1(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?status=-1', headers=headers
        )
        sleep(1)
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Card filter by status 0")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_status_0(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?status=0', headers=headers
        )
        sleep(1)
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Card filter by status 1")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_status_1(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?status=1', headers=headers
        )

        sleep(1)
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Card filter by status 1 and ordering by created_at")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_status_1_ordering_by_created_at(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?status=1&ordering=created_at', headers=headers
        )
        sleep(1)
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Card filter by status 1 and ordering by -created_at")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_status_1_ordering_by__created_at(self, auth_login_user_data_ru,
                                                            api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?status=1&ordering=-created_at', headers=headers
        )

        sleep(1)
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Card filter by status 1 and ordering by spend")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_status_1_ordering_by_spend(self, auth_login_user_data_ru,
                                                            api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?status=1&ordering=spend', headers=headers
        )
        sleep(1)
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Card filter by status 1 and ordering by -spend")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_status_1_ordering_by__spend(self, auth_login_user_data_ru,
                                                       api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?status=1&ordering=-spend', headers=headers
        )
        sleep(1)
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Card filter by status 1 and ordering by status")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_status_1_ordering_by_status(self, auth_login_user_data_ru,
                                                       api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?status=1&ordering=status', headers=headers
        )

        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Card filter by status 1 and ordering by -status")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_status_1_ordering_by__status(self, auth_login_user_data_ru,
                                                        api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?status=1&ordering=-status', headers=headers
        )

        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Card filter by company")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_company(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?company=129', headers=headers
        )

        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Card filter by company and status -1")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_company_and_status(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?company=129&status=-1', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Card filter by bin")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_bin(self, auth_login_user_data_ru,api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?company=129&bin=22&user=190', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Card filter by card bin")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_card_bin(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?company=129&user=190&card_bin=15', headers=headers
        )

        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Card filter by search term")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_search_term(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?search=apple', headers=headers
        )

        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Card filter by start date")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_start_date(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?date_start=2024-04-19T06%3A09%3A28.044729Z', headers=headers
        )

        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
  
    @allure.title("Card filter by start date & status & page & ordering by created_at")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_start_date_status_page_ordering_created(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?status=1&ordering=-created_at&page=2&date_start=2024-04-19T06%3A09%3A28.044729Z', headers=headers
        )

        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        # assert response.text().__contains__('"count":28,"next":null,"previous":"https://dev.api.devhost.io/api/card?date_start=2024-04-19T06%3A09%3A28.044729Z&ordering=-created_at&status=1","results":[{"id":145,"created_at":"2024-04-17T05:33:34.342495Z","number":"6513","name":"taboola","frozen_by":null')
        # assert response.text().__contains__('{"id":143,"created_at":"2024-04-17T05:32:28.046321Z","number":"3495","name":"Facebook","frozen_by":null,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":10000,"limit_spend":null,"payment_system":"visa","billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","user":{"id":190,"email":"rtuuyhgfytr45fghfh@yandex.ru","person":{"first_name":"test do not","last_name":"change"}},"status":1,"settled":0.0,"refund":0.0,"pending":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":0.0,"bin":"404038","use_3ds":false}')

    @allure.title("Card filter by end date & status")
    @pytest.mark.parametrize("schema_name", DATA1)
    def test_filter_card_by_start_end_status(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card?status=-1&date_end=2024-04-19T06%3A09%3A28.044729Z', headers=headers
        )

        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get api card bins")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_api_card_bins(self, auth_login_user_data_ru,
                                             api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card/bins', headers=headers
        )
        assert response.status == 200
        # print(response.text())
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get api card transfer users")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_api_card_transfer_users(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/card/transfer/users', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get api cash total")
    def test_get_api_cash_total(self, auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/cash/total', headers=headers
        )
        assert response.status == 200
        assert response.text() == '{"balance":1004.65,"pending":101.0}'

    @allure.title("Get filter card bins")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_filter_card_bins(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/filter/card/bins', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Get filter card limits")
    def test_get_filter_card_limits(self, auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/filter/card/limits', headers=headers
        )
        assert response.status == 200
        assert response.text().__contains__('"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null')
        assert response.text().__contains__('"id":2,"name":"entity.cardLimit.daily","days":1')
        assert response.text().__contains__('"id":3,"name":"entity.cardLimit.weekly","days":7')
        assert response.text().__contains__('"id":4,"name":"entity.cardLimit.monthly","days":30')
        assert response.text().__contains__('"id":5,"name":"entity.cardLimit.lifetime","days":999,"start_at":"2023-09-01T00:00:00Z"')

    @allure.title("Get filter card statuses")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_filter_card_statuses(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/filter/card/statuses', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        # assert response.text() == '[{"code":-1,"name":"entity.cardStatus.closed"},{"code":0,"name":"entity.cardStatus.freeze"},{"code":1,"name":"entity.cardStatus.active"},{"code":2,"name":"entity.cardStatus.expired"}]'

    @allure.title("Get filter card users")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_filter_card_users(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/filter/card/users', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        # assert response.text() == '[{"id":190,"email":"rtuuyhgfytr45fghfh@yandex.ru","person":{"first_name":"test do not","last_name":"change"},"avatar":null},{"id":195,"email":"invaited@mail.ru","person":{"first_name":"invated","last_name":"emploee"},"avatar":null}]'

    @allure.title("Create card without authorize")
    def test_create_card_without_authorize(self, api_request_context: APIRequestContext) -> None:
        data = {
            "name": random_string(5),
            "limit": 1,
            "limit_amount": 200,
            "user": 5,
            "card_bin": 7
        }
        response = api_request_context.post(
            '/api/card', data=data
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED