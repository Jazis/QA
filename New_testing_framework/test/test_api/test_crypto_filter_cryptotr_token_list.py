
import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED


@allure.title('Admin filter crypto transaction token list')
def test_admin_filter_crypto_transaction_token_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/token', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"id":1,"symbol":"USDT","type":"TRC-20","blockchain_id":1},{"id":6,"symbol":"USDT","type":"ERC-20","blockchain_id":2},{"id":5,"symbol":"USDC","type":"ERC-20","blockchain_id":2},{"id":4,"symbol":"string","type":"string","blockchain_id":null}]'


@allure.title('Not admin filter crypto transaction token list')
def test_not_admin_filter_crypto_transaction_token_list(auth_token_black_company,
                                                           api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/token', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"id":1,"symbol":"USDT","type":"TRC-20","blockchain_id":1},{"id":6,"symbol":"USDT","type":"ERC-20","blockchain_id":2},{"id":5,"symbol":"USDC","type":"ERC-20","blockchain_id":2},{"id":4,"symbol":"string","type":"string","blockchain_id":null}]'


@allure.title('Filter batch crypto transaction token list without auth')
def test_filter_crypto_transaction_token_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/token'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
