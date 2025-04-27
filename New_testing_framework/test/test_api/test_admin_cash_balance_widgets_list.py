import allure
import pytest
from playwright.sync_api import APIRequestContext

from data.input_data.api.admin_cash_balance_widgets_data import CASH_BALANCE_FILTER_BY_COMPANIES, CASH_BALANCE
from utils.json_validation import validate_json_schema

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Get admin cash balance without authorization')
def test_get_admin_cash_balance_without_authorization(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/cash/balance/widgets?date_start=2024-10-11T21%3A00%3A00.000Z&date_end=2024-10-22T20%3A59%3A59.999Z'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Get admin cash balance wrong endpoint')
def test_get_admin_cash_balance_wrong_endpoint(api_request_context: APIRequestContext) -> None:
    response = api_request_context.get('/api/admin/cash/balance/widge')
    assert response.status == 404


@allure.title('Get admin cash balance transactions not admin')
def test_get_admin_cash_balance_not_admin(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {'Authorization': f"Token {auth_token_black_company}"}
    response = api_request_context.get('/api/admin/cash/balance/widgets', headers=headers)
    assert response.status == 403
    assert response.text() == PERMISSIONS


@pytest.mark.parametrize("url, schema_name", CASH_BALANCE)
@allure.title('Get admin cash balance')
def test_get_admin_cash_balance(auth_token, api_request_context: APIRequestContext, url: str, schema_name: str) -> None:
    headers = {'Authorization': f"Token {auth_token}"}
    response = api_request_context.get(url=url, headers=headers)
    response_data = response.json()
    assert response.status == 200
    validate_json_schema(response_data, schema_name)


@pytest.mark.parametrize("url, schema_name", CASH_BALANCE_FILTER_BY_COMPANIES)
@allure.title('Get admin cash balance filter by companies')
def test_get_admin_cash_balance_filter_by_companies(
        auth_token, api_request_context: APIRequestContext, url: str, schema_name: str) -> None:
    headers = {'Authorization': f"Token {auth_token}"}
    response = api_request_context.get(url=url, headers=headers)
    response_data = response.json()
    assert response.status == 200
    validate_json_schema(response_data, schema_name)
