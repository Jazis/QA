import allure
from playwright.sync_api import APIRequestContext
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from data.responses_texts import PERMISSIONS
from utils.json_validation import validate_json_schema
from data.input_data.api.admin_cash_core_transactions_list import TRANSACTION_LIST
import pytest 
from data.input_data.api.users import DATA

@allure.title('Get admin processed transactions without authorization')
def test_get_admin_processed_transactions_without_authorization(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/cash/processed_transactions'
    )
    assert response.status == 401


@allure.title('Get admin processed transactions wrong endpooint')
def test_get_admin_processed_wrong_endpoint(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/cash/processed_transac'
    )
    assert response.status == 404


@allure.title('Get admin processed transactions not admin')
def test_get_admin_processed_transactions_not_admin(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/cash/processed_transactions', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Get admin processed transactions')
@pytest.mark.parametrize("schema_name", DATA)
def test_get_admin_processed_transactions(auth_token, api_request_context: APIRequestContext, schema_name) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/cash/processed_transactions?date_start=2024-12-11T21:00:00.000Z&date_end=2024-12-22T20:59:59.999Z', headers=headers
    )
    response_data = response.json()
    assert response.status == 200
    validate_json_schema(response.text(), schema_name)


@allure.title('Get admin processed transactions filter by account')
@pytest.mark.parametrize("schema_name", DATA)
def test_get_admin_processed_transactions_filter_by_account(auth_token, api_request_context: APIRequestContext, schema_name) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/cash/processed_transactions?account_id=183&date_start=2024-10-11T21:00:00.000Z&date_end=2024-10-22T20:59:59.999Z', headers=headers
    )
    response_data = response.json()
    assert response.status == 200
    validate_json_schema(response.text(), schema_name)