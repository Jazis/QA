
import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter account types list')
def test_admin_filter_account_types_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/account/types', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"id":1,"name":"entity.accountType.main"},{"id":2,"name":"entity.accountType.credit"},{"id":3,"name":"entity.accountType.virtual"},{"id":5,"name":"entity.accountType.fee"},{"id":6,"name":"entity.accountType.revenue"},{"id":7,"name":"Netting"}]'


@allure.title('Admin filter account types list not admin')
def test_admin_filter_account_types_list_not_admin(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/account/types', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin filter account types list without auth')
def test_admin_filter_account_types_list_without_auth(api_request_context: APIRequestContext) -> None:
    response = api_request_context.get(
        '/api/admin/filter/account/types'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED