import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter account companies')
def test_admin_filter_account_companies(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/account/companies', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":2,"name":"Beeline","owner_type":"client"')
    assert response.text().__contains__('"id":7,"name":"Microsoft","owner_type":"client"')
    assert response.text().__contains__('"id":9,"name":"test2","owner_type":"own"')
    assert response.text().__contains__('"id":14,"name":"GreatTraffic","owner_type":"client"')
    assert response.text().__contains__('"id":30,"name":"FirstReferee","owner_type":"client"')
    assert response.text().__contains__('"id":102,"name":"ere rtre","owner_type":"client"')
    assert response.text().__contains__('"id":173,"name":"black company","owner_type":"client"')
    assert response.text().__contains__('"id":165,"name":"BeGKroLput lESp","owner_type":"client"')
    assert response.text().__contains__('"id":387,"name":"GXIVas","owner_type":"client"')


@allure.title('Admin filter account companies without auth')
def test_admin_filter_account_companies_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/account/companies'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Admin filter account companies not admin')
def test_admin_filter_account_companies_not_admin(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/account/companies', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS

