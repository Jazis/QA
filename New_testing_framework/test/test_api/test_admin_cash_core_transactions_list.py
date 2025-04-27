import allure
from playwright.sync_api import APIRequestContext
from api.function_api import validate_json_keys, auth_token_function
from data.responses_texts import AUTH_NOT_PROVIDED
from data.input_data.users import VALID_USERS_WITH_ROLES
import pytest
from data.input_data.api.admin_cash_core_transactions_list import TRANSACTION_LIST
from utils.json_validation import validate_json_schema

@allure.title('Get admin cash core transactions without authorization')
def test_get_admin_cash_core_transactions_without_authorization(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/cash/core_transactions?cash_batch_id=178_spend_settled_2024-12-25'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Get admin cash core transactions wrong endpoint')
def test_get_admin_cash_core_transactions_wrong_endpoint(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/cash/core_trans?cash_batch_id=178_spend_settled_2024-12-25'
    )
    assert response.status == 404


@allure.title('Get admin cash core transactions not admin')
def test_get_admin_cash_core_transactions_not_admin(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/cash/core_transactions?cash_batch_id=178_spend_settled_2024-12-25', headers=headers
    )
    assert response.status == 403


@allure.title('Get admin cash core settled transactions')
@pytest.mark.parametrize("schema_name", TRANSACTION_LIST)
def test_get_admin_cash_core_settled_transactions(auth_token, api_request_context: APIRequestContext, schema_name) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/cash/core_transactions?cash_batch_id=4_spend_settled_2024-12-26', headers=headers
    )
    assert response.status == 200
    validate_json_schema(response.text(), schema_name)


@allure.title('Get admin cash core refund transactions')
@pytest.mark.parametrize("schema_name", TRANSACTION_LIST)
def test_get_admin_cash_core_refund_transactions(auth_token, api_request_context: APIRequestContext, schema_name) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/cash/core_transactions?cash_batch_id=4_refund_refund_2024-12-19', headers=headers
    )
    assert response.status == 200
    validate_json_schema(response.text(), schema_name)


@allure.title('Get admin cash core declined transactions')
def test_get_admin_cash_core_declined_transactions(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/cash/core_transactions?cash_batch_id=4_decline_fee_settled_2024-12-19', headers=headers
    )
    assert response.status == 200
    assert response.text() == '{"count":1,"next":null,"previous":null,"results":{"total_sum":{"spend":0.5,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.5},"data":[{"id":17144,"amount":"12.00","authorize_time":"2024-12-19T07:30:05.295777Z","card":{"id":509,"name":"null test 11","number":"0765","user":{"id":1,"email":"admin@admin.com","person":{"first_name":"Joe","last_name":"Dow"}},"payment_system":"mc"},"country":{"id":235,"name":"United Kingdom","code":"GB"},"cross_border_fee":0.0,"currency":"USD","decline_fee":0.5,"decline_reason":"The transaction was declined for an unknown reason.","description":"","direction":"out","fx_fee":0.0,"local_amount":2.0,"mcc":"7311","merchant_info":"FACEBK ADS","merchant_image":"https://dev.api.devhost.io/media/merchant_ico/facebook-dev.png","merchant_name":"Facebook-dev","refund_time":null,"reversed_time":null,"settled_time":null,"status":"declined","total":12.0,"user":{"id":1,"email":"admin@admin.com","person":{"first_name":"Joe","last_name":"Dow"}},"processed_time":null}],"date_start":"2024-12-19T07:30:05.295777Z","date_end":"2024-12-19T07:30:05.295777Z"}}'

@pytest.mark.parametrize("user", VALID_USERS_WITH_ROLES)
@pytest.mark.parametrize("schema_name", TRANSACTION_LIST)
def test_transaction_view(request, api_request_context: APIRequestContext, user, schema_name):
    token = auth_token_function(request=request, username = user.login, password = user.password)
    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
            '/api/admin/transaction', headers=headers
        )
    assert response.status == 200
    validate_json_schema(response.text(), schema_name)

@pytest.mark.parametrize("user", VALID_USERS_WITH_ROLES)
@pytest.mark.parametrize("schema_name", TRANSACTION_LIST)
def test_processed_transactions_view(request, api_request_context: APIRequestContext, user, schema_name):
    token = auth_token_function(request=request, username = user.login, password = user.password)
    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
            '/api/admin/cash/processed_transactions', headers=headers
        )
    assert response.status == 200
    validate_json_schema(response.text(), schema_name)
