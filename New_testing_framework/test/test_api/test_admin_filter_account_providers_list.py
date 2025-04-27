import allure
from playwright.sync_api import APIRequestContext
from api.function_api import validate_json_keys
from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter account providers list')
def test_admin_filter_account_providers_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/account/providers', headers=headers
    )

    assert response.status == 200
    assert validate_json_keys(response.text(), '[{"id":2,"name":"ConnexPay","stage":null},{"id":5,"name":"Qolo","stage":null}]') == True


@allure.title('Admin filter account providers list not admin')
def test_admin_filter_account_providers_list_not_admin(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/account/providers', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin filter account providers list without auth')
def test_admin_filter_account_providers_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/account/providers'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED

