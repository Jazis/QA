import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS
from data.input_data.users import VALID_USERS_WITH_ROLES
from api.function_api import auth_token_function, validate_json_keys
import pytest


@allure.title('Admin company get batch list')
def test_admin_company_get_batch_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"count":6,"next":null,"previous":null')
    assert response.text().__contains__('"id":8,"created_at":"2024-08-12T09:50:51.958561Z","status":"canceled","type":"loan","amount":"500.000000","amount_topup":"490.000000","token":1,"provider":3,"provider_name":"Fireblocks","history":[]},{"id":5,"created_at":"2024-03-26T13:25:29.740838Z","status":"offramp","type":"batch","amount":"2000.000000","amount_topup":"1800.000000","token":1,"provider":2,"provider_name":"ConnexPay","history":[]},{"id":4,"created_at":"2024-03-26T13:22:57.489349Z","status":"loan_cleared","type":"loan","amount":"10.000000","amount_topup":"8.000000","token":1,"provider":3,"provider_name":"Fireblocks","history":[]},{"id":1,"created_at":"2024-03-26T13:20:05.503066Z","status":"offramp","type":"batch","amount":"700.000000","amount_topup":"625.000000","token":1,"provider":2,"provider_name":"ConnexPay","history":[]}]}')


@allure.title('Admin company get batch list filter by batch')
def test_admin_company_get_batch_list_filter_by_batch(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch?id=1', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"count":1,"next":null,"previous":null')
    assert response.text().__contains__('"id":1,"created_at":"2024-03-26T13:20:05.503066Z","status":"offramp","type":"batch","amount":"700.000000","amount_topup":"625.000000","token":1,"provider":2,"provider_name":"ConnexPay","history":[]}]}')


@allure.title('Admin company get batch list filter by wrong batch')
def test_admin_company_get_batch_list_filter_by_wrong_batch(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch?id=3500', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":0,"next":null,"previous":null,"results":[]}'


@allure.title('Admin company get batch list filter by loan')
def test_admin_company_get_batch_list_filter_by_loan(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch?type=loan', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"count":4,"next":null,"previous":null')
    assert response.text().__contains__('"id":8,"created_at":"2024-08-12T09:50:51.958561Z","status":"canceled","type":"loan","amount":"500.000000","amount_topup":"490.000000","token":1,"provider":3,"provider_name":"Fireblocks","history":[]},{"id":4,"created_at":"2024-03-26T13:22:57.489349Z","status":"loan_cleared","type":"loan","amount":"10.000000","amount_topup":"8.000000","token":1,"provider":3,"provider_name":"Fireblocks","history":[]}]}')


@allure.title('Admin company get batch list filter by netting')
def test_admin_company_get_batch_list_filter_by_netting(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch?type=netting', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":0,"next":null,"previous":null,"results":[]}'


@allure.title('Admin company get batch list filter by status offramp')
def test_admin_company_get_batch_list_filter_by_status_offramp(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch?status=offramp', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"count":2,"next":null,"previous":null')
    assert response.text().__contains__('"id":5,"created_at":"2024-03-26T13:25:29.740838Z","status":"offramp","type":"batch","amount":"2000.000000","amount_topup":"1800.000000","token":1,"provider":2,"provider_name":"ConnexPay","history":[]},{"id":1,"created_at":"2024-03-26T13:20:05.503066Z","status":"offramp","type":"batch","amount":"700.000000","amount_topup":"625.000000","token":1,"provider":2,"provider_name":"ConnexPay","history":[]}]}')


@allure.title('Admin company get batch list filter by token')
def test_admin_company_get_batch_list_filter_by_token(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch?token=1', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"count":6,"next":null,"previous":null')
    assert response.text().__contains__('"id":5,"created_at":"2024-03-26T13:25:29.740838Z","status":"offramp","type":"batch","amount":"2000.000000","amount_topup":"1800.000000","token":1,"provider":2,"provider_name":"ConnexPay","history":[]},{"id":4,"created_at":"2024-03-26T13:22:57.489349Z","status":"loan_cleared","type":"loan","amount":"10.000000","amount_topup":"8.000000","token":1,"provider":3,"provider_name":"Fireblocks","history":[]},{"id":1,"created_at":"2024-03-26T13:20:05.503066Z","status":"offramp","type":"batch","amount":"700.000000","amount_topup":"625.000000","token":1,"provider":2,"provider_name":"ConnexPay","history":[]}]}')


@allure.title('Admin company get batch list filter by wrong token')
def test_admin_company_get_batch_list_filter_by_wrong_token(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch?token=187', headers=headers
    )

    assert response.status == 400
    assert response.text() == '{"token":["Select a valid choice. 187 is not one of the available choices."]}'


@allure.title('Admin company get batch list filter by wrong provider')
def test_admin_company_get_batch_list_filter_by_wrong_provider(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch?provider=346', headers=headers
    )

    assert response.status == 400
    assert response.text() == '{"provider":["Select a valid choice. 346 is not one of the available choices."]}'


@allure.title('Admin company get batch list filter by provider')
def test_admin_company_get_batch_list_filter_by_provider(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch?provider=3', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"count":4,"next":null,"previous":null')
    assert response.text().__contains__('"id":8,"created_at":"2024-08-12T09:50:51.958561Z","status":"canceled","type":"loan","amount":"500.000000","amount_topup":"490.000000","token":1,"provider":3,"provider_name":"Fireblocks","history":[]},{"id":4,"created_at":"2024-03-26T13:22:57.489349Z","status":"loan_cleared","type":"loan","amount":"10.000000","amount_topup":"8.000000","token":1,"provider":3,"provider_name":"Fireblocks","history":[]}]}')


@allure.title('Admin company get batch list filter by date')
def test_admin_company_get_batch_list_filter_by_date(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/batch?date_start=2024-03-26&date_end=2024-07-09', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"count":3,"next":null,"previous":null')
    assert response.text().__contains__('"id":5,"created_at":"2024-03-26T13:25:29.740838Z","status":"offramp","type":"batch","amount":"2000.000000","amount_topup":"1800.000000","token":1,"provider":2,"provider_name":"ConnexPay","history":[]},{"id":4,"created_at":"2024-03-26T13:22:57.489349Z","status":"loan_cleared","type":"loan","amount":"10.000000","amount_topup":"8.000000","token":1,"provider":3,"provider_name":"Fireblocks","history":[]},{"id":1,"created_at":"2024-03-26T13:20:05.503066Z","status":"offramp","type":"batch","amount":"700.000000","amount_topup":"625.000000","token":1,"provider":2,"provider_name":"ConnexPay","history":[]}]}')


@allure.title('Not admin company get batch list')
def test_not_admin_company_get_batch_list(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/batch', headers=headers
    )
    
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Company get batch list without auth')
def test_company_get_batch_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/batch'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED

@pytest.mark.parametrize("user", VALID_USERS_WITH_ROLES)
def test_roles_view_crypto_admin_address(request, api_request_context: APIRequestContext, user):
    token = auth_token_function(request=request, username = user.login, password = user.password)
    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
            '/api/admin/address', headers=headers
        )
    assert response.status == 200
    assert validate_json_keys(response.text(), '{"count":2,"next":null,"previous":null,"results":{"total_sum":{"money_in":0.0,"balance":0.0},"data":[{"id":5,"address":"NewAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":1,"name":"tron","code":"TRC-20"},"token_id":1,"company":{"id":841,"name":"Solo Qolo","owner_type":"client"},"account":{"id":856,"name":"Solo Qolo","company":{"id":841,"name":"Solo Qolo","owner_type":"client"},"number":"5042764"},"status":"active","amount":0,"balance":0},{"id":1,"address":"SomeAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":2,"name":"ethereum","code":"ERC-20"},"token_id":1,"company":{"id":1,"name":"MTS","owner_type":"own"},"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"own"},"number":"1021481"},"status":"active","amount":0,"balance":0}]}}') == True
    