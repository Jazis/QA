import allure
from playwright.sync_api import APIRequestContext
from api.function_api import validate_json_keys
import pytest
from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS
from data.input_data.users import VALID_USERS_WITH_ROLES
from api.function_api import validate_json_keys, auth_token_function

@allure.title('Admin card totals')
def test_admin_card_totals(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card/totals?date_start=2024-05-18&date_end=2024-05-19', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"cross_border_fee":14.47,"decline_fee":4.5,"fx_fee":7.17,"pending":810.0,"refund":160.0,"reversed_amount":183.0,"settled":980.0,"spend":1656.14}'


@allure.title('Admin card totals without authorization')
def test_admin_card_totals_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/card/totals'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
    
@pytest.mark.parametrize("user", VALID_USERS_WITH_ROLES)
def test_card_view(request, api_request_context: APIRequestContext, user):
    token = auth_token_function(request=request, username = user.login, password = user.password)
    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
            '/api/admin/card', headers=headers
        )
    assert response.status == 200
    assert validate_json_keys(response.text(), '{"id":246,"account":{"id":180,"name":"ruby rose","company":{"id":171,"name":"ruby rose","owner_type":"client"},"number":"1029366"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"433451","created_at":"2024-05-17T05:39:37.487631Z","cross_border_fee":41.96,"decline_fee":13.5,"frozen_by":null,"fx_fee":7.61,"limit":{"id":5,"name":"Lifetime","days":999,"start_at":"2023-09-01T00:00:00Z"},"limit_amount":500,"limit_spend":null,"name":"ruby card lifetime","number":"7574","order_number":"GAwnHC","payment_system":"visa","pending":1864.56,"refund":1042.52,"reversed_amount":1279.02,"settled":2093.53,"spend":2978.64,"status":1,"user":{"id":301,"person":{"first_name":"ruby","last_name":"rose"}},"provider":{"id":2,"name":"ConnexPay","stage":null}}') == True
        

@allure.title('Admin card totals not admin')
def test_admin_card_totals_not_admin(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/card/totals',  headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin card totals filter by account')
def test_admin_card_totals_filter_by_account(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card/totals?account=182&date_start=2024-05-18&date_end=2024-05-19',  headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"cross_border_fee":0.0,"decline_fee":1.5,"fx_fee":0.0,"pending":84.0,"refund":48.0,"reversed_amount":61.0,"settled":115.0,"spend":152.5}'


@allure.title('Admin card totals filter by company')
def test_admin_card_totals_filter_by_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card/totals?company=173&date_start=2024-05-18&date_end=2024-05-19',  headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"cross_border_fee":0.0,"decline_fee":1.5,"fx_fee":0.0,"pending":84.0,"refund":48.0,"reversed_amount":61.0,"settled":115.0,"spend":152.5}'


@allure.title('Admin card totals filter by status')
def test_admin_card_totals_filter_by_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card/totals?status=-1&date_start=2024-05-18&date_end=2024-05-19',  headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"cross_border_fee":0.0,"decline_fee":0.0,"fx_fee":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0}'


@allure.title('Admin card totals filter by status = 1')
def test_admin_card_totals_filter_by_status_1(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card/totals?status=1&date_start=2024-05-18&date_end=2024-05-19',  headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"cross_border_fee":14.47,"decline_fee":4.5,"fx_fee":7.17,"pending":810.0,"refund":160.0,"reversed_amount":183.0,"settled":980.0,"spend":1656.14}'


@allure.title('Admin card totals filter by user')
def test_admin_card_totals_filter_by_user(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card/totals?user=303&date_start=2024-05-18&date_end=2024-05-19',  headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"cross_border_fee":0.0,"decline_fee":1.5,"fx_fee":0.0,"pending":84.0,"refund":48.0,"reversed_amount":61.0,"settled":115.0,"spend":152.5}'


@allure.title('Admin card totals filter by payment system')
def test_admin_card_totals_filter_by_payment_system(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card/totals?payment_system=visa&date_start=2024-05-18&date_end=2024-05-19',  headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"cross_border_fee":7.51,"decline_fee":0.0,"fx_fee":4.09,"pending":428.0,"refund":0.0,"reversed_amount":0.0,"settled":333.0,"spend":772.5999999999999}'


@allure.title('Admin card totals filter by limit = 3')
def test_admin_card_totals_filter_by_limit_3(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card/totals?limit=3&date_start=2024-05-18&date_end=2024-05-19',  headers=headers
    )
    
    assert response.status == 200
    assert response.text() == '{"cross_border_fee":1.43,"decline_fee":0.0,"fx_fee":0.93,"pending":168.0,"refund":0.0,"reversed_amount":0.0,"settled":55.0,"spend":225.36}'

