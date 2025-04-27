import allure
from playwright.sync_api import APIRequestContext

from api.function_api import api_post_auth_trans, api_post_with_auth
from data.input_data.data_card import DECLINED, CURRENCY_USD, COUNTRY_GB
from test.test_api.conftest import VISA


@allure.title("Transaction auth declined")
def test_auth_declined(api_request_context: APIRequestContext) -> None:
    token = api_post_auth_trans(api_request_context, 12, VISA, '{"approved":true}')
    api_post_with_auth(api_request_context, token, 12, VISA, DECLINED, COUNTRY_GB, CURRENCY_USD)



