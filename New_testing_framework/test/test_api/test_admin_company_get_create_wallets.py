import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS, SUCCESS
from data.input_data.random_data import random_numbers_choose_number


@allure.title('Admin company get available wallets')
def test_admin_company_get_available_wallets(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/company/1/available_crypto_wallets', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"available_wallets":[{"symbol":"USDT","type":"TRC-20","blockchain":"Tron"},{"symbol":"USDT","type":"ERC-20","blockchain":"Ethereum"}]}'


@allure.title('Not admin company get available wallets')
def test_not_admin_company_get_available_wallets(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/company/1/available_crypto_wallets', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Company get available wallets without auth')
def test_company_get_available_wallets_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/company/1/available_crypto_wallets'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Company create crypto-wallets')
def test_company_create_crypto_wallets(auth_token, api_request_context: APIRequestContext) -> None:
    id = random_numbers_choose_number()
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    data = {
        "symbol": "USDT",
        "type": "TRC-20"
    }

    response = api_request_context.post(
        f'/api/admin/company/{id}/create_crypto_address', headers=headers, data=data
    )
    assert response.status == 200
    assert response.text() == SUCCESS