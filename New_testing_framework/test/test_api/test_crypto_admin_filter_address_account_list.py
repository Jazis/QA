import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter address account list')
def test_admin_filter_address_account_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/filter/address/account', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},{"id":231,"name":"dsef dsfdsg","company":{"id":222,"name":"dsef dsfdsg","owner_type":"client"},"number":"1055386"}]'


@allure.title('Not admin filter address account list')
def test_not_admin_filter_address_account_list(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/filter/address/account', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter address account list without auth')
def test_filter_address_account_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/address/account'
    )
    
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
