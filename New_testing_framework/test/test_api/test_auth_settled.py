import allure
from playwright.sync_api import APIRequestContext

from api.function_api import api_post_auth_trans, api_post_with_auth
from data.input_data.data_card import SETTLED, COUNTRY_US, CURRENCY_USD
from test.test_api.conftest import VISA


@allure.title("Transaction auth settled")
def test_auth_settled(api_request_context: APIRequestContext) -> None:
    token = api_post_auth_trans(api_request_context, 10, VISA, '{"approved":true}')
    api_post_with_auth(api_request_context, token,10, VISA, SETTLED, COUNTRY_US, CURRENCY_USD)

