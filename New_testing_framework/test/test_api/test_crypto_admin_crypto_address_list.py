
import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED


@allure.title('Admin filter crypto address list')
def test_admin_filter_crypto_address_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/crypto/address', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"id":1,"address":"SomeAddress","blockchain_id":2,"token":{"id":1,"symbol":"USDT","type":"TRC-20","blockchain_id":1}}]'


@allure.title('Not admin filter crypto address list')
def test_not_admin_filter_crypto_address_list(auth_token_black_company,
                                                           api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/crypto/address', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[]'


@allure.title('Filter crypto address list without auth')
def test_filter_crypto_address_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/crypto/address'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Admin create crypto address list')
def test_admin_create_crypto_address_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    data = {
        "blockchain_id": 12,
        "wallet_type": "deposit"
    }

    response = api_request_context.post(
        '/api/crypto/address', headers=headers, data=data
    )
    
    assert response.status == 400
    assert response.text() == '{"non_field_errors":["Blockchain does not exist with the provided data"]}'


