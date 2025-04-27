import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED


@allure.title('Admin filter address token list')
def test_admin_filter_address_token_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/filter/address/token', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"id":1,"symbol":"USDT","type":"TRC-20","blockchain_id":1},{"id":6,"symbol":"USDT","type":"ERC-20","blockchain_id":2},{"id":5,"symbol":"USDC","type":"ERC-20","blockchain_id":2},{"id":4,"symbol":"string","type":"string","blockchain_id":null}]'


@allure.title('Not admin filter address token list')
def test_not_admin_filter_address_token_list(auth_token_black_company,
                                               api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/filter/address/token', headers=headers
    )

    assert response.status == 200


@allure.title('Filter address token list without auth')
def test_filter_address_token_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/address/token'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Filter address status list without auth wrong way')
def test_filter_address_token_list_without_auth_wrong_way(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filt/address/token'
    )
    assert response.status == 404