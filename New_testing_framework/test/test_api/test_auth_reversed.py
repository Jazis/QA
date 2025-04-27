import allure
from playwright.sync_api import APIRequestContext
from api.function_api import api_post_auth_trans, api_post_with_auth

from test.test_api.conftest import VISA
from data.input_data.data_card import REVERSAL, CURRENCY_USD, COUNTRY_GB
from test.test_api.conftest import VISA


@allure.title("Transaction auth reversed")
def test_auth_reversed(api_request_context: APIRequestContext) -> None:
    token = api_post_auth_trans(api_request_context, 15, VISA, '{"approved":true}')
    api_post_with_auth(api_request_context, token, 25, VISA, REVERSAL, COUNTRY_GB, CURRENCY_USD)
