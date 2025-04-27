import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter address blockchain list')
def test_admin_filter_address_blockchain_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/filter/address/blockchain', headers=headers
    )
    
    assert response.status == 200
    assert response.text() == '[{"id":1,"name":"tron","code":"TRC-20","is_active":true},{"id":2,"name":"ethereum","code":"ERC-20","is_active":true}]'


@allure.title('Not admin filter address blockchain list')
def test_not_admin_filter_address_blockchain_list(auth_token_black_company,
                                               api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/filter/address/blockchain', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter address blockchain list without auth')
def test_filter_address_blockchain_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/address/blockchain'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
