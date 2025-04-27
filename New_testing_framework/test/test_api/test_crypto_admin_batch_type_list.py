
import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter batch type list')
def test_admin_filter_batch_type_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/filter/batch/type', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"id":"loan","name":"Loan"},{"id":"batch","name":"Batch"},{"id":"netting","name":"Netting"}]'


@allure.title('Not admin filter batch type list')
def test_not_admin_filter_batch_type_list(auth_token_black_company,
                                           api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/filter/batch/type', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter batch type list without auth')
def test_filter_filter_batch_type_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/batch/type'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED

