import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin user profile read')
def test_admin_user_profile_read(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/user/profile', headers=headers
    )
    assert response.status == 200
    assert response.text().__contains__('"id":1,"first_name":"Joe","last_name":"Dow","role":{"id":1,"name":"Admin"},"status":"Active","user_id":1,"avatar":"https://dev.api.devhost.io/media/CACHE/images/avatar/e830fa89535db19a09236eaff/543e164c7bbaeb8fe92c0b4cd73d8007.png","timezone":"Europe/Moscow"')


@allure.title('Not admin user profile read')
def test_not_admin_user_profile_read(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/user/profile', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('User profile read without auth')
def test_user_profile_read_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/user/profile'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED

