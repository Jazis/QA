import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS
from data.input_data.api.admin_crypto_transaction_list import DATA
from utils.json_validation import validate_json_schema
import pytest

@allure.title('Admin crypto transaction list')
@pytest.mark.parametrize("schema_name", DATA)
def test_admin_crypto_transaction_list(auth_token, api_request_context: APIRequestContext, schema_name) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"next":null,"previous":null,"results"')
    assert response.text().__contains__('"total_amount"')
    assert response.text().__contains__('"total_topup":')
    assert response.text().__contains__('"total_fee":')
    validate_json_schema(response.text(), schema_name)

@allure.title('Admin crypto transaction list filter by company')
@pytest.mark.parametrize("schema_name", DATA)
def test_admin_crypto_transaction_list_filter_by_company(auth_token, api_request_context: APIRequestContext, schema_name) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction?company=6', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"count":6,"next":null,"previous":null,"results":{"total_amount":4410.0,"total_topup":3973.0,"total_fee":261.0')
    validate_json_schema(response.text(), schema_name)
    

@allure.title('Admin cryptotransaction list filter by status top up_from_credit')
@pytest.mark.parametrize("schema_name", DATA)
def test_admin_crypto_transaction_list_filter_by_status_top_up_from_credit(auth_token, api_request_context: APIRequestContext, schema_name) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction?client_status=topup_from_credit', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"next":null,"previous":null,"results":{"total_amount"')
    assert response.text().__contains__('"total_topup"')
    assert response.text().__contains__('"total_fee":')
    validate_json_schema(response.text(), schema_name)


@allure.title('Admin crypto transaction list filter by cash status received_on_treasury')
@pytest.mark.parametrize("schema_name", DATA)
def test_admin_crypto_transaction_list_filter_by_cash_status_received_on_treasury(auth_token, api_request_context: APIRequestContext, schema_name) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction?cash_status=received_on_treasury', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"next":null,"previous":null,"results":{"total_amount"')
    assert response.text().__contains__('"total_topup":')
    assert response.text().__contains__('"total_fee":')
    validate_json_schema(response.text(), schema_name)

@allure.title('Admin crypto transaction list filter by date')
@pytest.mark.parametrize("schema_name", DATA)
def test_admin_crypto_transaction_list_filter_by_date(auth_token, api_request_context: APIRequestContext, schema_name) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction?date_start=2024-01-10&date_end=2024-07-24', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"count":5,"next":null,"previous":null,"results":{"total_amount":4210.0,"total_topup":3953.0,"total_fee":257.0')
    validate_json_schema(response.text(), schema_name)

@allure.title('Admin crypto transaction list filter by batch')
@pytest.mark.parametrize("schema_name", DATA)
def test_admin_crypto_transaction_list_filter_by_batch(auth_token, api_request_context: APIRequestContext, schema_name) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction?batch=1', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"next":null,"previous":null,"results":{"total_amount"')
    assert response.text().__contains__('"total_topup":')
    assert response.text().__contains__('"total_fee":')
    validate_json_schema(response.text(), schema_name)



@allure.title('Admin crypto transaction list filter by wrong batch')
def test_admin_crypto_transaction_list_filter_by_wrong_batch(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction?batch=6789', headers=headers
    )

    assert response.status == 400
    assert response.text() == '{"batch":["Select a valid choice. 6789 is not one of the available choices."]}'


@allure.title('Admin crypto transaction list filter by wrong loan')
def test_admin_crypto_transaction_list_filter_by_wrong_loan(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction?loan=3', headers=headers
    )

    assert response.status == 400
    assert response.text() == '{"loan":["Select a valid choice. 3 is not one of the available choices."]}'


@allure.title('Admin crypto transaction list filter by wrong token')
def test_admin_crypto_transaction_list_filter_by_wrong_token(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction?token=102', headers=headers
    )

    assert response.status == 400
    assert response.text() == '{"token":["Select a valid choice. 102 is not one of the available choices."]}'


@allure.title('Admin crypto transaction list filter by token')
@pytest.mark.parametrize("schema_name", DATA)
def test_admin_crypto_transaction_list_filter_by_token(auth_token, api_request_context: APIRequestContext, schema_name) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction?token=1', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"total_topup":')
    assert response.text().__contains__('"total_fee":')
    validate_json_schema(response.text(), schema_name)

@allure.title('Admin crypto transaction list filter by search')
@pytest.mark.parametrize("schema_name", DATA)
def test_admin_crypto_transaction_list_filter_by_search(auth_token, api_request_context: APIRequestContext, schema_name) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction?search=ConnCompany', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"total_topup":')
    assert response.text().__contains__('"total_fee":')
    validate_json_schema(response.text(), schema_name)

@allure.title('Admin crypto transaction list filter by search - no results')
def test_admin_crypto_transaction_list_filter_by_search_no_results(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction?search=76tqwer', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":0,"next":null,"previous":null,"results":{"total_amount":0,"total_topup":0,"total_fee":0,"data":[]}}'


@allure.title('Admin crypto transaction list filter by topup_from_credit and received_on_deposit')
@pytest.mark.parametrize("schema_name", DATA)
def test_admin_crypto_transaction_list_filter_by_search_no_results(auth_token, api_request_context: APIRequestContext, schema_name) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction?client_status=topup_from_credit&cash_status=received_on_deposit', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"total_topup":')
    assert response.text().__contains__('"total_fee":')
    validate_json_schema(response.text(), schema_name)


@allure.title('Not admin crypto transaction list filter by topup_from_credit and received_on_deposit')
def test_not_admin_crypto_transaction_list_filter_by_search_no_results(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction?client_status=topup_from_credit&cash_status=received_on_deposit', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Crypto transaction list without auth')
def test_crypto_transaction_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/cryptotransaction'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED

