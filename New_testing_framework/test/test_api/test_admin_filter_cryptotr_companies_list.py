import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter crypto transaction companies list')
def test_admin_filter_crypto_transaction_companies_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/companies', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('{"id":43,"name":"TestAirtable","owner_type":"client"}')
    assert response.text().__contains__('{"id":841,"name":"Solo Qolo","owner_type":"client"}')
    assert response.text().__contains__('{"id":4,"name":"Tesla","owner_type":"client"}')
    assert response.text().__contains__('{"id":6,"name":"ConnCompany","owner_type":"client"}')
    assert response.text().__contains__('{"id":2,"name":"Beeline","owner_type":"client"}')
    assert response.text().__contains__('{"id":7,"name":"Microsoft","owner_type":"client"}')
    assert response.text().__contains__('{"id":1,"name":"MTS","owner_type":"client"}')
    assert response.text().__contains__('{"id":8,"name":"test1","owner_type":"client"}')
    assert response.text().__contains__('{"id":65,"name":"Test update","owner_type":"client"}')
    assert response.text().__contains__('{"id":37,"name":"SeventhReferee","owner_type":"client"}')



@allure.title('Not admin filter crypto transaction companies list')
def test_not_admin_filter_crypto_transaction_companies_list(auth_token_black_company,
                                                           api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/companies', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter cryptotransaction companies list without auth')
def test_filter_cryptotransaction_companies_list_without_auth(
        api_request_context: APIRequestContext) -> None:
    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/companies'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
