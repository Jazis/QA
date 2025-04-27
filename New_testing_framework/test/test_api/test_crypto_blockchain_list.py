import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED


@allure.title('Admin crypto blockchain list')
def test_admin_crypto_blockchain_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/crypto/blockchain', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"id":1,"name":"Tron","code":"TRC-20"},{"id":2,"name":"Ethereum","code":"ERC-20"}]'


@allure.title('Not admin crypto blockchain list')
def test_not_admin_crypto_blockchain_list(auth_token_black_company,
                                                           api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/crypto/blockchain', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"id":1,"name":"Tron","code":"TRC-20"},{"id":2,"name":"Ethereum","code":"ERC-20"}]'


@allure.title('Crypto blockchain list without auth')
def test_crypto_blockchain_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/crypto/blockchain'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
