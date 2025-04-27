import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin batch widgets list')
def test_admin_batch_widgets_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch/widgets', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"loan":0.0,"swap":0.0,"offramp":2700.0,"bank_account":0.0}'


@allure.title('Admin batch widgets list filter by token')
def test_admin_batch_widgets_list_filter_by_token(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch/widgets?token=1', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"loan":0.0,"swap":0.0,"offramp":2700.0,"bank_account":0.0}'


@allure.title('Admin batch widgets list filter by wrong provider')
def test_admin_batch_widgets_list_filter_by_wrong_provider(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch/widgets?provider=3', headers=headers
    )

    assert response.status == 400
    assert response.text() == '{"provider":["Select a valid choice. 3 is not one of the available choices."]}'


@allure.title('Admin batch widgets list filter by provider')
def test_admin_batch_widgets_list_filter_by_provider(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch/widgets?provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"loan":0.0,"swap":0.0,"offramp":2700.0,"bank_account":0.0}'


@allure.title('Admin batch widgets list filter by date')
def test_admin_batch_widgets_list_filter_by_date(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch/widgets?date_start=2024-05-01&date_end=2024-07-01', headers=headers
    )

    assert response.status == 200
    assert response.text() =='{"loan":0.0,"swap":0.0,"offramp":0.0,"bank_account":0.0}'


@allure.title('Not admin batch widgets list')
def test_not_admin_batch_widgets_list(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/batch/widgets', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Batch widgets list without ayth')
def test_batch_widgets_list_without_auth(auth_token_black_company, api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/batch/widgets'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


