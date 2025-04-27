import allure
from playwright.sync_api import APIRequestContext

from data.input_data.random_data import random_numbers_bills
from api.function_api import validate_json_keys
from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS, NOT_FOUND, BILL_QUERY_DOESNT_EXITS, PAYMENT_FAILED_NOT_ENOUGH_MONEY
from data.input_data.users import VALID_USERS_WITH_ROLES
from api.function_api import validate_json_keys, auth_token_function
import pytest


@allure.title('Admin bill cancel')
def test_admin_bill_cancel(auth_token, api_request_context: APIRequestContext) -> None:
    n = random_numbers_bills()
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    data = {
            "bills": [
                n
            ]
    }
    response = api_request_context.post(
        '/api/admin/subscription/bill/cancel', headers=headers, data=data
    )
    assert response.status == 200
    assert response.text() == '{"status":"OK"}'


@allure.title('Admin bill cancel without body')
def test_admin_bill_cancel_without_body(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.post(
        '/api/admin/subscription/bill/cancel', headers=headers
    )
    assert response.status == 400
    assert response.text() == '{"bills":["This field is required."]}'


@allure.title('Not admin bill cancel')
def test_not_admin_bill_cancel(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    n = random_numbers_bills()
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    data = {
            "bills": [
                n
            ]
    }
    response = api_request_context.post(
        '/api/admin/subscription/bill/cancel', headers=headers, data=data
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Bill cancel without auth')
def test_bill_cancel_without_auth(api_request_context: APIRequestContext) -> None:
    n = random_numbers_bills()

    data = {
            "bills": [
                n
            ]
    }
    response = api_request_context.post(
        '/api/admin/subscription/bill/cancel', data=data
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Wrong bill cancel')
def test_wrong_bill_cancel(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    data = {
            "bills": [
                1000
            ]
    }
    response = api_request_context.post(
        '/api/admin/subscription/bill/cancel', headers=headers, data=data
    )

    assert response.status == 400
    assert response.text() == BILL_QUERY_DOESNT_EXITS


@allure.title('Admin bill pay account')
def test_admin_bill_pay_account(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/subscription/bill/pay_account/55', headers=headers
    )

    assert response.status == 200
    assert validate_json_keys(response.text(),'{"id":182,"name":"black company","number":"1025391"'),('"provider":2,"company_id":173,"owner_type":"client"}') == True


@allure.title('Admin wrong bill pay account')
def test_admin_wrong_bill_pay_account(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/subscription/bill/pay_account/1550', headers=headers
    )

    assert response.status == 404
    assert response.text() == NOT_FOUND


@allure.title('Not admin bill pay account')
def test_not_admin_bill_pay_account(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/subscription/bill/pay_account/55', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Bill pay account without auth')
def test_bill_pay_account_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/subscription/bill/pay_account/55'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Admin bill payout')
def test_admin_bill_payout(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    data = {
            "bills": [
                63
            ]
    }
    response = api_request_context.post(
        '/api/admin/subscription/bill/payout', headers=headers, data=data
    )
    assert response.status == 200
    assert response.text() == '{"status":"OK"}'


@allure.title('Admin bill payout not enough money')
def test_admin_bill_payout_not_enough_money(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    data = {
            "bills": [
                64
            ]
    }
    response = api_request_context.post(
        '/api/admin/subscription/bill/payout', headers=headers, data=data
    )

    assert response.status == 400
    assert response.text() == PAYMENT_FAILED_NOT_ENOUGH_MONEY


@allure.title('Admin bill payout without body')
def test_admin_bill_payout_without_body(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.post(
        '/api/admin/subscription/bill/payout', headers=headers
    )

    assert response.status == 400
    assert response.text() == '{"bills":["This field is required."]}'


@allure.title('Not admin bill payout')
def test_not_admin_bill_payout(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    data = {
        "bills": [
            64
        ]
    }
    response = api_request_context.post(
        '/api/admin/subscription/bill/payout', headers=headers, data=data
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Bill payout without auth')
def test_bill_payout_without_auth(api_request_context: APIRequestContext) -> None:

    data = {
        "bills": [
            64
        ]
    }
    response = api_request_context.post(
        '/api/admin/subscription/bill/payout',data=data
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Admin bills list')
def test_admin_bills_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/subscription/bills?date_start=2024-08-08&date_end=2024-08-09', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":6,"next":null,"previous":null,"results":{"total_sum":{"amount":100.0},"data":[{"id":104,"created_at":"2024-08-08T09:07:11.449888Z","paid_at":null,"canceled_at":"2024-08-09T05:49:13.613438Z","plan":2,"status":"canceled","billing_period_start":"2024-08-08T09:07:11.443187Z","billing_period_end":"2024-09-07T23:59:59Z","company":{"id":405,"name":"dehyXJ","owner_type":"client"},"amount":"371.00"},{"id":103,"created_at":"2024-08-08T09:05:31.501120Z","paid_at":null,"canceled_at":null,"plan":1,"status":"unpaid","billing_period_start":"2024-08-08T09:05:31.496790Z","billing_period_end":"2024-09-07T23:59:59.496790Z","company":{"id":405,"name":"dehyXJ","owner_type":"client"},"amount":"100.00"},{"id":102,"created_at":"2024-08-08T05:09:07.776674Z","paid_at":"2024-08-09T06:57:49.454650Z","canceled_at":null,"plan":1,"status":"paid","billing_period_start":"2024-08-08T05:09:07.771500Z","billing_period_end":"2024-09-07T23:59:59.771500Z","company":{"id":81,"name":"Leonard_Gulgowski45 + Dibbert","owner_type":"client"},"amount":"100.00"},{"id":101,"created_at":"2024-08-08T03:30:00.058764Z","paid_at":null,"canceled_at":null,"plan":3,"status":"unpaid","billing_period_start":"2024-08-08T23:59:59Z","billing_period_end":"2024-09-07T23:59:59Z","company":{"id":202,"name":"nmfdADSF retryty","owner_type":"client"},"amount":"600.00"},{"id":100,"created_at":"2024-08-08T03:30:00.054466Z","paid_at":null,"canceled_at":"2024-08-09T06:09:50.894952Z","plan":1,"status":"canceled","billing_period_start":"2024-08-08T23:59:59Z","billing_period_end":"2024-09-07T23:59:59Z","company":{"id":200,"name":"1398h 3476nmm","owner_type":"client"},"amount":"100.00"},{"id":99,"created_at":"2024-08-08T03:30:00.047929Z","paid_at":null,"canceled_at":null,"plan":3,"status":"unpaid","billing_period_start":"2024-08-08T23:59:59Z","billing_period_end":"2024-09-07T23:59:59Z","company":{"id":249,"name":"uyuytuyturyur","owner_type":"client"},"amount":"600.00"}]}}'


@allure.title('Admin bills list filter by id company')
def test_admin_bills_list_filter_by_id_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/subscription/bills?company=6&date_start=2024-06-05&date_end=2024-07-17', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":3,"next":null,"previous":null,"results":{"total_sum":{"amount":0.0},"data":[{"id":27,"created_at":"2024-06-17T03:30:00.035675Z","paid_at":null,"canceled_at":null,"plan":1,"status":"unpaid","billing_period_start":"2024-06-17T23:59:59Z","billing_period_end":"2024-07-17T23:59:59Z","company":{"id":6,"name":"ConnCompany","owner_type":"client"},"amount":"100.00"},{"id":20,"created_at":"2024-06-12T00:08:31.015684Z","paid_at":"2024-06-12T00:10:50.438067Z","canceled_at":"2025-01-17T23:13:38.994052Z","plan":1,"status":"canceled","billing_period_start":"2024-06-12T00:08:31.011596Z","billing_period_end":"2024-07-12T23:59:59.011596Z","company":{"id":6,"name":"ConnCompany","owner_type":"client"},"amount":"100.00"},{"id":2,"created_at":"2024-06-06T13:50:28.431730Z","paid_at":null,"canceled_at":"2024-11-04T07:11:14.216609Z","plan":3,"status":"canceled","billing_period_start":"2024-06-06T13:00:00Z","billing_period_end":"2024-07-06T13:00:00Z","company":{"id":6,"name":"ConnCompany","owner_type":"client"},"amount":"500.00"}]}}'


@allure.title('Admin bills list filter by id plan')
def test_admin_bills_list_filter_by_id_plan(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/subscription/bills?plan=1&date_start=2024-07-12&date_end=2024-07-17', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":1,"next":null,"previous":null,"results":{"total_sum":{"amount":0.0},"data":[{"id":51,"created_at":"2024-07-15T09:37:14.593771Z","paid_at":null,"canceled_at":"2024-09-27T12:36:00.395791Z","plan":1,"status":"canceled","billing_period_start":"2024-07-15T09:37:14.589140Z","billing_period_end":"2025-07-15T23:59:59.589140Z","company":{"id":340,"name":"5вкевапав пвапаврары","owner_type":"client"},"amount":"1000.00"}]}}'


@allure.title('Admin bills list filter by status')
def test_admin_bills_list_filter_by_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/subscription/bills?status=unpaid&date_start=2024-07-12&date_end=2024-07-17', headers=headers
    )

    assert response.status == 200
    assert validate_json_keys(response.text(),'"next":null,"previous":null,"results":{"total_sum":{"amount":0.0},"data":') == True
    assert validate_json_keys(response.text(),'{"id":52,"created_at":"2024-07-15T09:37:34.206884Z","paid_at":null,"canceled_at":null,"plan":3,"status":"unpaid","billing_period_start":"2024-07-15T09:37:34.200829Z","billing_period_end":"2025-07-15T23:59:59.589140Z","company":{"id":340,"name":"5вкевапав пвапаврары","owner_type":"client"},"amount":"6300.00"}') == True
    assert validate_json_keys(response.text(),'{"id":50,"created_at":"2024-07-13T03:30:00.055611Z","paid_at":null,"canceled_at":null,"plan":3,"status":"unpaid","billing_period_start":"2024-07-13T23:59:59.180946Z","billing_period_end":"2024-08-12T23:59:59.180946Z","company":{"id":210,"name":"trytud fhfghgfjgfj","owner_type":"client"},"amount":"600.00"}') == True
    assert validate_json_keys(response.text(),'{"id":49,"created_at":"2024-07-13T03:30:00.048447Z","paid_at":null,"canceled_at":null,"plan":2,"status":"unpaid","billing_period_start":"2024-07-13T23:59:59Z","billing_period_end":"2024-08-12T23:59:59Z","company":{"id":197,"name":"Subscrition check","owner_type":"client"},"amount":"471.00"}') == True
    assert validate_json_keys(response.text(),'{"id":48,"created_at":"2024-07-12T03:30:00.036284Z","paid_at":null,"canceled_at":null,"plan":2,"status":"unpaid","billing_period_start":"2024-07-12T23:59:59Z","billing_period_end":"2024-08-11T23:59:59Z","company":{"id":321,"name":"456867r 4656776tuyg","owner_type":"client"},"amount":"471.00"}]}}') == True


@allure.title('Admin bills list by search')
def test_admin_bills_list_filter_by_search(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/subscription/bills?date_start=2024-07-12&date_end=2024-07-17&search=check', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":1,"next":null,"previous":null,"results":{"total_sum":{"amount":0.0},"data":[{"id":49,"created_at":"2024-07-13T03:30:00.048447Z","paid_at":null,"canceled_at":null,"plan":2,"status":"unpaid","billing_period_start":"2024-07-13T23:59:59Z","billing_period_end":"2024-08-12T23:59:59Z","company":{"id":197,"name":"Subscrition check","owner_type":"client"},"amount":"471.00"}]}}'


@allure.title('Admin bills list order by amount')
def test_admin_bills_list_order_by_amount(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/subscription/bills?date_start=2024-07-12&date_end=2024-07-17&ordering=amount', headers=headers
    )

    assert response.status == 200
    assert validate_json_keys(response.text(),'{"count":6,"next":null,"previous":null,"results":{"total_sum":{"amount":0.0},"data"') == True
    assert validate_json_keys(response.text(),'{"id":48,"created_at":"2024-07-12T03:30:00.036284Z","paid_at":null,"canceled_at":null,"plan":2,"status":"unpaid","billing_period_start":"2024-07-12T23:59:59Z","billing_period_end":"2024-08-11T23:59:59Z","company":{"id":321,"name":"456867r 4656776tuyg","owner_type":"client"},"amount":"471.00"}') == True
    assert validate_json_keys(response.text(),'{"id":49,"created_at":"2024-07-13T03:30:00.048447Z","paid_at":null,"canceled_at":null,"plan":2,"status":"unpaid","billing_period_start":"2024-07-13T23:59:59Z","billing_period_end":"2024-08-12T23:59:59Z","company":{"id":197,"name":"Subscrition check","owner_type":"client"},"amount":"471.00"}') == True
    assert validate_json_keys(response.text(),'{"id":50,"created_at":"2024-07-13T03:30:00.055611Z","paid_at":null,"canceled_at":null,"plan":3,"status":"unpaid","billing_period_start":"2024-07-13T23:59:59.180946Z","billing_period_end":"2024-08-12T23:59:59.180946Z","company":{"id":210,"name":"trytud fhfghgfjgfj","owner_type":"client"},"amount":"600.00"}') == True
    assert validate_json_keys(response.text(),'{"id":53,"created_at":"2024-07-16T03:30:00.061213Z","paid_at":null,"canceled_at":"2025-01-17T21:17:53.563723Z","plan":3,"status":"canceled","billing_period_start":"2024-07-08T23:59:59Z","billing_period_end":"2024-08-07T23:59:59Z","company":{"id":196,"name":"testvvvvfg fdggr","owner_type":"client"},"amount":"600.00"}') == True
    assert validate_json_keys(response.text(),'{"id":51,"created_at":"2024-07-15T09:37:14.593771Z","paid_at":null,"canceled_at":"2024-09-27T12:36:00.395791Z","plan":1,"status":"canceled","billing_period_start":"2024-07-15T09:37:14.589140Z","billing_period_end":"2025-07-15T23:59:59.589140Z","company":{"id":340,"name":"5вкевапав пвапаврары","owner_type":"client"},"amount":"1000.00"}') == True
    assert validate_json_keys(response.text(),'{"id":52,"created_at":"2024-07-15T09:37:34.206884Z","paid_at":null,"canceled_at":null,"plan":3,"status":"unpaid","billing_period_start":"2024-07-15T09:37:34.200829Z","billing_period_end":"2025-07-15T23:59:59.589140Z","company":{"id":340,"name":"5вкевапав пвапаврары","owner_type":"client"},"amount":"6300.00"}]}}') == True


@allure.title('Admin bills list order by -amount filter by status')
def test_admin_bills_list_order_by__amount_filter_by_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/subscription/bills?status=unpaid&date_start=2024-07-12&date_end=2024-07-17&ordering=-amount', headers=headers
    )

    assert response.status == 200
    assert validate_json_keys(response.text(),'{"id":52,"created_at":"2024-07-15T09:37:34.206884Z","paid_at":null,"canceled_at":null,"plan":3,"status":"unpaid","billing_period_start":"2024-07-15T09:37:34.200829Z","billing_period_end":"2025-07-15T23:59:59.589140Z","company":{"id":340,"name":"5вкевапав пвапаврары","owner_type":"client"},"amount":"6300.00"}')
    assert validate_json_keys(response.text(),'{"id":50,"created_at":"2024-07-13T03:30:00.055611Z","paid_at":null,"canceled_at":null,"plan":3,"status":"unpaid","billing_period_start":"2024-07-13T23:59:59.180946Z","billing_period_end":"2024-08-12T23:59:59.180946Z","company":{"id":210,"name":"trytud fhfghgfjgfj","owner_type":"client"},"amount":"600.00"}')
    assert validate_json_keys(response.text(),'{"id":53,"created_at":"2024-07-16T03:30:00.061213Z","paid_at":null,"canceled_at":null,"plan":3,"status":"unpaid","billing_period_start":"2024-07-08T23:59:59Z","billing_period_end":"2024-08-07T23:59:59Z","company":{"id":196,"name":"testvvvvfg fdggr","owner_type":"client"},"amount":"600.00"}')
    assert validate_json_keys(response.text(),'{"id":48,"created_at":"2024-07-12T03:30:00.036284Z","paid_at":null,"canceled_at":null,"plan":2,"status":"unpaid","billing_period_start":"2024-07-12T23:59:59Z","billing_period_end":"2024-08-11T23:59:59Z","company":{"id":321,"name":"456867r 4656776tuyg","owner_type":"client"},"amount":"471.00"}')
    assert validate_json_keys(response.text(),'{"id":49,"created_at":"2024-07-13T03:30:00.048447Z","paid_at":null,"canceled_at":null,"plan":2,"status":"unpaid","billing_period_start":"2024-07-13T23:59:59Z","billing_period_end":"2024-08-12T23:59:59Z","company":{"id":197,"name":"Subscrition check","owner_type":"client"},"amount":"471.00"}]}}')


@allure.title('Not admin bills list')
def test_not_admin_bills_list(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/subscription/bills', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Bills list without auth')
def test_bills_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/subscription/bills'
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
            '/api/admin/subscription/bills', headers=headers
        )
    assert response.status == 200
    assert validate_json_keys(response.text(), '{"id":785,"created_at":"2025-01-24T06:14:27.900744Z","paid_at":null,"canceled_at":"2025-01-24T06:18:02.731375Z","plan":1,"status":"canceled","billing_period_start":"2025-01-24T06:14:27.895306Z","billing_period_end":"2025-02-23T23:59:59.895306Z","company":{"id":281,"name":"EQlMct","owner_type":"client"},"amount":"100.00"}') == True
    