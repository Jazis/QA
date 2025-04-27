import allure
from playwright.sync_api import APIRequestContext
from api.function_api import validate_json_keys
from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter user statuses list')
def test_admin_filter_user_statuses_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/user/statuses', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"id":-1,"name":"entity.userStatus.deleted"},{"id":0,"name":"entity.userStatus.invited"},{"id":1,"name":"entity.userStatus.active"},{"id":2,"name":"entity.userStatus.pending"}]'


@allure.title('Not admin filter user statuses list')
def test_not_admin_filter_user_statuses_list(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/user/statuses', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter user statuses list without auth')
def test_filter_user_statuses_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/user/statuses'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED




