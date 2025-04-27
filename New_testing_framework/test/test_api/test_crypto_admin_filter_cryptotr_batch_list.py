import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter crypto transaction batch list')
def test_admin_filter_crypto_transaction_batch_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/batch', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[1,4,5,8,9,10]'


@allure.title('Not admin filter crypto transaction batch list')
def test_not_admin_filter_crypto_transaction_batch_list(auth_token_black_company,
                                                       api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/batch', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter batch cryptotransaction list without auth')
def test_filter_batch_cryptotransaction_list_without_auth(api_request_context: APIRequestContext) -> None:
    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/batch'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
