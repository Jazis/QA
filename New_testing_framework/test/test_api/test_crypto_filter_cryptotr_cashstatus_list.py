
import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter crypto transaction cashstatus list')
def test_admin_filter_crypto_transaction_cashstatus_batch_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/cashstatus', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"id":"received_on_deposit","name":"Deposit"},{"id":"received_on_treasury","name":"Treasury"},{"id":"expenses_vault","name":"Expense"},{"id":"gas_vault","name":"Gas"},{"id":"swap","name":"Swap"},{"id":"offramp","name":"Offramp"},{"id":"bank_account","name":"Bank account"},{"id":"master_account","name":"Master account"},{"id":"received_on_trash","name":"Trash"},{"id":"transit","name":"Transit"}]'


@allure.title('Not admin filter crypto transaction cashstatus batch list')
def test_not_admin_filter_crypto_transaction_cashstatus_batch_list(auth_token_black_company,
                                                       api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/cashstatus', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter batch crypto transaction cashstatus list without auth')
def test_filter_filter_batch_crypto_transaction_cashstatus_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/cashstatus'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED