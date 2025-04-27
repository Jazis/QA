import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter transaction statuses list')
def test_admin_filter_transaction_company_statuses_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/transaction/statuses', headers=headers
    )
    
    assert response.status == 200
    assert response.text() == '[{"code":"settled","name":"entity.transactionStatus.settled"},{"code":"pending","name":"entity.transactionStatus.pending"},{"code":"reversed","name":"entity.transactionStatus.reversed"},{"code":"declined","name":"entity.transactionStatus.declined"},{"code":"refund","name":"entity.transactionStatus.refund"}]'


@allure.title('Not admin filter transaction statuses list')
def test_not_admin_filter_transaction_company_statuses_list(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/transaction/statuses', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter transaction statuses list without auth')
def test_filter_transaction_company_statuses_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/transaction/statuses'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
