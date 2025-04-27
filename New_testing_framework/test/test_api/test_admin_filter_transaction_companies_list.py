import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter transaction companies list')
def test_admin_filter_transaction_companies_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/transaction/companies', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('{"id":2,"name":"Beeline","owner_type":"client"}')
    assert response.text().__contains__('{"id":306,"name":"ENJauAxIkv PLpZ","owner_type":"client"}')
    assert response.text().__contains__('{"id":30,"name":"FirstReferee","owner_type":"client"}')
    assert response.text().__contains__('{"id":81,"name":"Leonard_Gulgowski45 + Dibbert","owner_type":"client"}')


@allure.title('Not admin filter transaction companies list')
def test_not_admin_filter_transaction_companies_list(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/transaction/companies', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter transaction companies list without auth')
def test_filter_transaction_companies_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/transaction/companies'
    )
    
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
