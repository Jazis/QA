import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter address company')
def test_admin_filter_address_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/filter/address/company', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"id":2,"name":"Beeline","owner_type":"client"},{"id":222,"name":"dsef dsfdsg","owner_type":"client"},{"id":1,"name":"MTS","owner_type":"client"}]'


@allure.title('Not admin filter address company')
def test_not_admin_filter_address_company(auth_token_black_company,
                                               api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/filter/address/company', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter address company without auth')
def test_filter_address_company_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/address/company'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED

