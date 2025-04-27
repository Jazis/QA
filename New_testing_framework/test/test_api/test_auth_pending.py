import allure

from playwright.sync_api import APIRequestContext
from api.function_api import api_post_auth_trans, api_post_pending_with_auth
from data.input_data.data_card import PENDING, COUNTRY_US, CURRENCY_USD
from test.test_api.conftest import VISA


@allure.title("Transaction auth pending")
def test_auth_pending(api_request_context: APIRequestContext) -> None:
    token = api_post_auth_trans(api_request_context, 14.5, VISA, '{"approved":true}')
    api_post_pending_with_auth(api_request_context, token,  14.5, VISA, PENDING, COUNTRY_US, CURRENCY_USD)




