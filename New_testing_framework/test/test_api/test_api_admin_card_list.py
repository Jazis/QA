import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS
from data.input_data.users import VALID_USERS_WITH_ROLES
from api.function_api import validate_json_keys, auth_token_function
import pytest

@allure.title('Admin card')
def test_admin_card(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card?date_start=2024-05-18&date_end=2024-05-19', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/card?date_end=2024-05-19&date_start=2024-05-18&page=2","previous":null,"results":')
    assert response.text().__contains__('"id":242,"account":{"id":177,"name":"red company","company":{"id":168,"name":"red company","owner_type":"client"},"number":"1026728"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"531993","created_at":"2024-05-17T05:33:29.800348Z","cross_border_fee":4.52,"decline_fee":1.5,"frozen_by":null,"fx_fee":2.94,"limit":{"id":4,"name":"Monthly"')


@allure.title('Admin card without auth')
def test_admin_card_without_auth(api_request_context: APIRequestContext) -> None:
    response = api_request_context.get(
        '/api/admin/card?date_start=2024-05-18&date_end=2024-05-19')

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Admin card not admin')
def test_admin_card_not_admin(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/card?date_start=2024-05-18&date_end=2024-05-19', headers=headers)

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin card filter by account')
def test_admin_card_filter_by_account(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card?account=4&date_start=2024-05-18&date_end=2024-05-18', headers=headers)

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/card?account=4&date_end=2024-05-18&date_start=2024-05-18&page=2","previous":null,"results"')
    assert response.text().__contains__('"id":464,"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"433451","created_at":"2024-07-10T06:34:01.544856Z","cross_border_fee":0.0,"decline_fee":0.0,"frozen_by":null,"fx_fee":0.0')
    assert response.text().__contains__('{"id":485,"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"433451","created_at":"2024-11-01T07:06:51.530990Z","cross_border_fee":0.0,"decline_fee":0.0,"frozen_by":"client","fx_fee":0.0,"limit":{"id":1,"name":"No limit","days":0,"start_at":null},"limit_amount":500000,"limit_spend":null,"name":"","number":"9540","order_number":"IyIzpo","payment_system":"visa","pending":0.0,"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"status":-1,"user":{"id":176,"person":{"first_name":"wizSDea","last_name":"wizSDea"}},"provider":{"id":2,"name":"ConnexPay","stage":null}}')


@allure.title('Admin card filter by company')
def test_admin_card_filter_by_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card?company=4&date_start=2024-05-18&date_end=2024-05-19', headers=headers)

    assert response.status == 200
    assert response.text().__contains__('{"count":6,"next":null,"previous":null,"results"')
    assert response.text().__contains__('"id":55,"account":{"id":7,"name":"Tesla","company":{"id":4,"name":"Tesla","owner_type":"client"},"number":"1062148"},"billing_address":"Some Address","bin":"","created_at":"2023-08-14T14:36:55.425567Z","cross_border_fee":0.0,"decline_fee":0.0,"frozen_by":null,"fx_fee":0.0')
    assert response.text().__contains__('{"id":54,"account":null,"billing_address":"Some Address","bin":"","created_at":"2023-08-14T08:00:27.083004Z","cross_border_fee":0.0,"decline_fee":0.0,"frozen_by":null,"fx_fee":0.0,"limit":{"id":1,"name":"No limit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null,"name":"","number":"1638","order_number":"","payment_system":"mc","pending":0.0,"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"status":1,"user":{"id":26,"person":{"first_name":"Vova","last_name":"Ok"}},"provider":{"id":1,"name":"Core Pay","stage":null}}')


@allure.title('Admin card filter by status')
def test_admin_card_filter_by_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card?status=-1&date_start=2024-05-18&date_end=2024-05-19', headers=headers)

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/card?date_end=2024-05-19&date_start=2024-05-18&page=2&status=-1","previous":null,"results"')
    assert response.text().__contains__('{"id":483,"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"433451","created_at":"2024-10-29T09:43:04.757300Z","cross_border_fee":0.0,"decline_fee":0.0,"frozen_by":null,"fx_fee":0.0,"limit":{"id":1,"name":"No limit","days":0,"start_at":null},"limit_amount":500000,"limit_spend":null,"name":"","number":"6684","order_number":"QmELda","payment_system":"visa","pending":0.0,"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"status":-1,"user":{"id":1,"person":{"first_name":"Joe","last_name":"Dow"}},"provider":{"id":2,"name":"ConnexPay","stage":null}}')


@allure.title('Admin card filter by status 0')
def test_admin_card_filter_by_status_0(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card?status=0&date_start=2024-05-18&date_end=2024-05-19', headers=headers)

    assert response.status == 200
    assert response.text().__contains__('"next":null,"previous":null,"results"')
    assert response.text().__contains__('"id":199,"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"441112","created_at":"2024-05-09T10:40:28.904267Z","cross_border_fee":0.0,"decline_fee":0.0,"frozen_by":"client","fx_fee":0.0,"limit"')
    assert response.text().__contains__('{"id":162,"account":{"id":138,"name":"test do not change","company":{"id":129,"name":"test do not change","owner_type":"client"},"number":"1018850"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"489683000","created_at":"2024-04-17T05:49:18.067680Z","cross_border_fee":0.0,"decline_fee":0.0,"frozen_by":"client","fx_fee":0.0,"limit":{"id":1,"name":"No limit","days":0,"start_at":null},"limit_amount":50000,"limit_spend":null,"name":"23","number":"9542","order_number":"FWfdmC","payment_system":"visa","pending":0.0,"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"status":0,"user":{"id":190,"person":{"first_name":"test do not","last_name":"change"}},"provider":{"id":2,"name":"ConnexPay","stage":null}}')


@allure.title('Admin card filter by user')
def test_admin_card_filter_by_user(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card?user=168&date_start=2024-05-18&date_end=2024-05-19', headers=headers)

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/card?date_end=2024-05-19&date_start=2024-05-18&page=2&user=168","previous":null,"results":[{"id":464,"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"433451","created_at":"2024-07-10T06:34:01.544856Z","cross_border_fee":0.0,"decline_fee":0.0,"frozen_by":null,"fx_fee":0.0')
    assert response.text().__contains__('{"id":457,"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"433451","created_at":"2024-07-10T05:48:48.989855Z","cross_border_fee":0.0,"decline_fee":0.0,"frozen_by":null,"fx_fee":0.0,"limit":{"id":1,"name":"No limit","days":0,"start_at":null},"limit_amount":500000,"limit_spend":null,"name":"qudQhr","number":"9974","order_number":"ueDVWi","payment_system":"visa","pending":0.0,"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"status":1,"user":{"id":168,"person":{"first_name":"test","last_name":"test"}},"provider":{"id":2,"name":"ConnexPay","stage":null}}')
    assert response.text().__contains__('{"id":455,"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"531993","created_at":"2024-07-08T14:50:20.598052Z","cross_border_fee":0.0,"decline_fee":0.0,"frozen_by":null,"fx_fee":0.0,"limit":{"id":1,"name":"No limit","days":0,"start_at":null},"limit_amount":500000,"limit_spend":null,"name":"","number":"8009","order_number":"OmvzfO","payment_system":"mc","pending":0.0,"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"status":1,"user":{"id":168,"person":{"first_name":"test","last_name":"test"}},"provider":{"id":2,"name":"ConnexPay","stage":null}}')


@allure.title('Admin card filter by payment system')
def test_admin_card_filter_by_payment_system(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card?payment_system=mc&date_start=2024-05-18&date_end=2024-05-19', headers=headers)

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/card?date_end=2024-05-19&date_start=2024-05-18&page=2&payment_system=mc","previous":null,"results":[{"id":242,"account":{"id":177,"name":"red company","company":{"id":168,"name":"red company","owner_type":"client"},"number":"1026728"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"531993","created_at":"2024-05-17T05:33:29.800348Z","cross_border_fee":4.52,"decline_fee":1.5,"frozen_by":null,"fx_fee":2.94')
    assert response.text().__contains__('{"id":252,"account":{"id":176,"name":"white company","company":{"id":167,"name":"white company","owner_type":"client"},"number":"1047836"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"556150","created_at":"2024-05-17T05:46:31.474814Z","cross_border_fee":1.72,"decline_fee":1.5,"frozen_by":null,"fx_fee":0.14,"limit":{"id":1,"name":"No limit","days":0,"start_at":null},"limit_amount":500000,"limit_spend":null,"name":"employee","number":"9933","order_number":"RPkNOF","payment_system":"mc","pending":84.0,"refund":48.0,"reversed_amount":61.0,"settled":155.0,"spend":194.35999999999999,"status":1,"user":{"id":297,"person":{"first_name":"test","last_name":"Employee"}},"provider":{"id":2,"name":"ConnexPay","stage":null}}')


@allure.title('Admin card filter by limit')
def test_admin_card_filter_by_limit(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card?limit=1&date_start=2024-05-18&date_end=2024-05-19', headers=headers)

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/card?date_end=2024-05-19&date_start=2024-05-18&limit=1&page=2","previous":null,"results"')
    assert response.text().__contains__('{"id":252,"account":{"id":176,"name":"white company","company":{"id":167,"name":"white company","owner_type":"client"},"number":"1047836"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"556150","created_at":"2024-05-17T05:46:31.474814Z","cross_border_fee":1.72,"decline_fee":1.5,"frozen_by":null,"fx_fee":0.14,"limit":{"id":1,"name":"No limit","days":0,"start_at":null},"limit_amount":500000,"limit_spend":null,"name":"employee","number":"9933","order_number":"RPkNOF","payment_system":"mc","pending":84.0,"refund":48.0,"reversed_amount":61.0,"settled":155.0,"spend":194.35999999999999,"status":1,"user":{"id":297,"person":{"first_name":"test","last_name":"Employee"}},"provider":{"id":2,"name":"ConnexPay","stage":null}}')
    assert response.text().__contains__('{"id":248,"account":{"id":181,"name":"golden company","company":{"id":172,"name":"golden company","owner_type":"client"},"number":"1062075"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"556150","created_at":"2024-05-17T05:41:38.431698Z","cross_border_fee":0.72,"decline_fee":0.0,"frozen_by":null,"fx_fee":0.0,"limit":{"id":1,"name":"No limit","days":0,"start_at":null},"limit_amount":500000,"limit_spend":null,"name":"golden","number":"0007","order_number":"mKpzkc","payment_system":"mc","pending":0.0,"refund":16.0,"reversed_amount":0.0,"settled":22.0,"spend":6.719999999999999,"status":1,"user":{"id":302,"person":{"first_name":"golden","last_name":"company"}},"provider":{"id":2,"name":"ConnexPay","stage":null}}')


@allure.title('Admin card filter by limit = 4')
def test_admin_card_filter_by_limit_4(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card?limit=4&date_start=2024-05-18&date_end=2024-05-19', headers=headers)

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/card?date_end=2024-05-19&date_start=2024-05-18&limit=4&page=2","previous":null,"results":[{"id":242,"account":{"id":177,"name":"red company","company":{"id":168,"name":"red company","owner_type":"client"},"number":"1026728"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"531993","created_at":"2024-05-17T05:33:29.800348Z","cross_border_fee":4.52,"decline_fee":1.5,"frozen_by":null,"fx_fee":2.94')
    assert response.text().__contains__('{"id":249,"account":{"id":181,"name":"golden company","company":{"id":172,"name":"golden company","owner_type":"client"},"number":"1062075"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"433451","created_at":"2024-05-17T05:41:55.333053Z","cross_border_fee":2.39,"decline_fee":0.0,"frozen_by":null,"fx_fee":0.93,"limit":')
    assert response.text().__contains__('{"id":473,"account":{"id":231,"name":"dsef dsfdsg","company":{"id":222,"name":"dsef dsfdsg","owner_type":"client"},"number":"1055386"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"433451","created_at":"2024-10-23T09:47:30.735107Z","cross_border_fee":0.0,"decline_fee":0.0,"frozen_by":null,"fx_fee":0.0,"limit":{"id":4,"name"')


@allure.title('Admin filter by card search')
def test_admin_card_filter_by_search(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card?search=ipwvugk&date_start=2024-05-18&date_end=2024-05-19', headers=headers)

    assert response.status == 200
    assert response.text().__contains__('"next":null,"previous":null,"results":[{"id":464,"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"433451","created_at":"2024-07-10T06:34:01.544856Z","cross_border_fee":0.0,"decline_fee":0.0,"frozen_by":null,"fx_fee":0.0')
    assert response.text().__contains__('"name":"ipwvugk","number":"1132","order_number":"omHEpW","payment_system":"visa","pending":0.0,"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"status":-1,"user":{"id":168,"person":{"first_name":"test","last_name":"test"}},"provider":{"id":2,"name":"ConnexPay","stage":null}}]}')


@allure.title('Admin filter by payment system & order by created at')
def test_admin_card_by_payment_system_order_by_created_at(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/card?payment_system=visa&ordering=created_at&date_start=2024-05-18&date_end=2024-05-19', headers=headers)

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/card?date_end=2024-05-19&date_start=2024-05-18&ordering=created_at&page=2&payment_system=visa","previous":null,"results":')
    assert response.text().__contains__('[{"id":56,"account":{"id":9,"name":"ConnCompany","company":{"id":6,"name":"ConnCompany","owner_type":"client"},"number":"1015104"},"billing_address":"NewYork, Street 10","bin":"111111","created_at":"2023-08-14T14:59:07.346786Z","cross_border_fee":0.0,"decline_fee":0.0,"frozen_by":null,"fx_fee":0.0,"limit":{"id":1,"name":"No limit","days":0,"start_at":null},"limit_amount":1000,"limit_spend":null,"name":"","number":"5664","order_number":"","payment_system":"visa","pending":0.0,"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"status":1,"user":{"id":34,"person":{"first_name":"Conn","last_name":"User"}},"provider":{"id":2,"name":"ConnexPay","stage":null}}')
    assert response.text().__contains__('{"id":57,"account":{"id":9,"name":"ConnCompany","company":{"id":6,"name":"ConnCompany","owner_type":"client"},"number":"1015104"},"billing_address":"NewYork, Street 10","bin":"111111","created_at":"2023-08-14T15:09:02.819048Z","cross_border_fee":0.0,"decline_fee":0.0,"frozen_by":"client","fx_fee":0.0')
    assert response.text().__contains__('{"id":68,"account":{"id":9,"name":"ConnCompany","company":{"id":6,"name":"ConnCompany","owner_type":"client"},"number":"1015104"},"billing_address":"NewYork, Street 10","bin":"111111","created_at":"2023-08-15T16:19:28.384718Z","cross_border_fee":0.0,"decline_fee":0.0,"frozen_by":"client","fx_fee":0.0,"limit":{"id":1,"name":"No limit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null,"name":"Test 15","number":"9967","order_number":"","payment_system":"visa","pending":0.0,"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"status":0,"user":{"id":34,"person":{"first_name":"Conn","last_name":"User"}},"provider":{"id":2,"name":"ConnexPay","stage":null}}')

@pytest.mark.parametrize("user", VALID_USERS_WITH_ROLES)
def test_roles_view_card_list(request, api_request_context: APIRequestContext, user):
    token = auth_token_function(request=request, username = user.login, password = user.password)
    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
            '/api/admin/card', headers=headers
        )
    assert response.status == 200
    assert validate_json_keys(response.text(), '{"id":246,"account":{"id":180,"name":"ruby rose","company":{"id":171,"name":"ruby rose","owner_type":"client"},"number":"1029366"},"billing_address":"1007 N Orange Street, 4th Floor, Wilmington, Delaware, 19801","bin":"433451","created_at":"2024-05-17T05:39:37.487631Z","cross_border_fee":41.96,"decline_fee":13.5,"frozen_by":null,"fx_fee":7.61,"limit":{"id":5,"name":"Lifetime","days":999,"start_at":"2023-09-01T00:00:00Z"},"limit_amount":500,"limit_spend":null,"name":"ruby card lifetime","number":"7574","order_number":"GAwnHC","payment_system":"visa","pending":1864.56,"refund":1042.52,"reversed_amount":1279.02,"settled":2093.53,"spend":2978.64,"status":1,"user":{"id":301,"person":{"first_name":"ruby","last_name":"rose"}},"provider":{"id":2,"name":"ConnexPay","stage":null}}') == True
        
