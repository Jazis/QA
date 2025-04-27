
import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter batch status list')
def test_admin_filter_batch_status_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/filter/batch/status', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"id":"received_on_treasury","name":"Treasury"},{"id":"batch_released","name":"Card Provider"},{"id":"loan_issued","name":"Loan issued"},{"id":"loan_cleared","name":"Loan cleared"},{"id":"swap","name":"Swap"},{"id":"offramp","name":"Offramp"},{"id":"bank_account","name":"Bank account"},{"id":"netting","name":"Netting"},{"id":"transit","name":"Transit"},{"id":"pending","name":"Pending"},{"id":"canceled","name":"Canceled"},{"id":"credit_account","name":"Credit Account"}]'


@allure.title('Not admin filter batch status list')
def test_not_admin_filter_batch_status_list(auth_token_black_company,
                                             api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/filter/batch/status', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter batch status list without auth')
def test_filter_batch_status_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/batch/status'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Filter batch status list without auth wrong way')
def test_filter_batch_status_list_without_auth_wrong_way(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/batch/stat'
    )
    assert response.status == 404
    