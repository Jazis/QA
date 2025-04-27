import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin batch provider list')
def test_admin_batch_provider_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch/provider', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[]'


@allure.title('Not admin batch provider list')
def test_not_admin_batch_provider_list(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/batch/provider', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Batch provider list without auth')
def test_batch_provider_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/batch/provider'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED

