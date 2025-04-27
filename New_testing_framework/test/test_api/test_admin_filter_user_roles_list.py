import allure
from playwright.sync_api import APIRequestContext
from api.function_api import validate_json_keys
from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter user roles list')
def test_admin_filter_user_roles_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/user/roles', headers=headers
    )
    assert response.status == 200
    assert response.text() == '[{"id":1,"name":"Admin"},{"id":2,"name":"Employee"},{"id":3,"name":"Dashboard: Admin"},{"id":6,"name":"Dashboard: Viewer"},{"id":4,"name":"Dashboard: FInance"},{"id":5,"name":"Dashboard: CS"}]'


@allure.title('Not admin filter user roles list')
def test_not_admin_filter_user_roles_list(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/user/roles', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter user roles list without auth')
def test_filter_user_roles_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/user/roles'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED

    