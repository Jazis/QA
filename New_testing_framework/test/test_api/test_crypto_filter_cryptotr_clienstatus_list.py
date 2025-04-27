
import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter crypto transaction client status list')
def test_admin_filter_crypto_transaction_clientstatus_batch_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/clientstatus', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"id":"received_on_deposit","name":"Deposit Done"},{"id":"topup_from_credit","name":"Top-up from credit"},{"id":"in_the_way","name":"On the way"},{"id":"topup_done","name":"Top-up done"}]'


@allure.title('Not admin filter crypto transaction client status batch list')
def test_not_admin_filter_crypto_transaction_client_status_batch_list(auth_token_black_company,
                                                       api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/clientstatus', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter batch crypto transaction client status list without auth')
def test_filter_filter_batch_crypto_transaction_clientstatus_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/clientstatus'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED