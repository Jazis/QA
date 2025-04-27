import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS
from data.input_data.users import VALID_USERS_WITH_ROLES
from api.function_api import validate_json_keys, auth_token_function
import pytest


@allure.title('Admin user list')
def test_admin_user_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/user?ordering=-spend&date_start=2024-05-18&date_end=2024-05-19', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/user?date_end=2024-05-19&date_start=2024-05-18&ordering=-spend&page=2","previous":null,"results":{"total_sum":{"settled":980.0,"pending":810.0,"reversed_amount":183.0,"fx_fee":7.17,"cross_border_fee":14.47,"decline_fee":4.5,"spend":1656.14,"refund":160.0},"avg_transaction":58.539354838709684,"total_decline_rate":18.367346938775512,"total_decline_amount":117.0,"international":60.0')
    assert response.text().__contains__('"id":298,"avatar":null,"avg_transaction_amount":82.57142857142857,"company":{"id":168,"name":"red company","owner_type":"client"},"cross_border_fee":4.52,"decline_fee":1.5,"decline_rate":23.076923076923077,"decline_amount":39.0,"fx_fee":2.94,"international":60.0,"pending":214.0,"person":{"first_name":"red","last_name":"company","status":1,"role":1,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":48.0,"reversed_amount":61.0,"settled":355.0,"spend":529.96,"username":"redcompany@mail.ru"')
    assert response.text().__contains__('"id":301,"avatar":null,"avg_transaction_amount":141.48,"company":{"id":171,"name":"ruby rose","owner_type":"client"},"cross_border_fee":2.73,"decline_fee":0.0,"decline_rate":0.0,"decline_amount":0.0,"fx_fee":2.23,"international":50.0,"pending":0.0,"person":{"first_name":"ruby","last_name":"rose","status":1,"role":1,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":0.0,"reversed_amount":0.0,"settled":278.0,"spend":282.96000000000004,"username":"rubyrose@mail.ru"')
    assert response.text().__contains__('"id":302,"avatar":null,"avg_transaction_amount":60.010000000000005,"company":{"id":172,"name":"golden company","owner_type":"client"},"cross_border_fee":3.11,"decline_fee":0.0,"decline_rate":0.0,"decline_amount":0.0,"fx_fee":0.93,"international":75.0,"pending":214.0,"person":{"first_name":"golden","last_name":"company","status":1,"role":1,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":16.0,"reversed_amount":0.0,"settled":22.0,"spend":224.04000000000002,"username":"goldencompany@mail.ru"')
    assert response.text().__contains__('"id":297,"avatar":null,"avg_transaction_amount":34.628571428571426,"company":{"id":167,"name":"white company","owner_type":"client"},"cross_border_fee":1.72,"decline_fee":1.5,"decline_rate":23.076923076923077,"decline_amount":39.0,"fx_fee":0.14,"international":60.0,"pending":84.0,"person":{"first_name":"test","last_name":"Employee","status":1,"role":2,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":48.0,"reversed_amount":61.0,"settled":155.0,"spend":194.35999999999999,"username":"someemail@google.com"')
    assert response.text().__contains__('"id":299,"avatar":null,"avg_transaction_amount":85.18,"company":{"id":169,"name":"green company","owner_type":"client"},"cross_border_fee":1.43,"decline_fee":0.0,"decline_rate":0.0,"decline_amount":0.0,"fx_fee":0.93,"international":50.0,"pending":168.0,"person":{"first_name":"green","last_name":"company","status":1,"role":1'),('"limit_amount":200,"limit_spend":0.0},"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":170.36,"username":"greencompany@google.com"')
    assert response.text().__contains__('"id":303,"avatar":null,"avg_transaction_amount":28.428571428571427,"company":{"id":173,"name":"black company","owner_type":"client"},"cross_border_fee":0.0,"decline_fee":1.5,"decline_rate":23.076923076923077,"decline_amount":39.0,"fx_fee":0.0,"international":60.0,"pending":84.0,"person":{"first_name":"black","last_name":"company","status":1,"role":1,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":48.0,"reversed_amount":61.0,"settled":115.0,"spend":152.5,"username":"blackcompany@mail.ru"')


@allure.title('Admin user list filter by company')
def test_admin_user_list_filter_by_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/user?company=171&date_start=2024-05-18&date_end=2024-05-19', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"count":2,"next":null,"previous":null,"results":{"total_sum":{"settled":278.0,"pending":0.0,"reversed_amount":0.0,"fx_fee":2.23,"cross_border_fee":2.73,"decline_fee":0.0,"spend":282.96000000000004,"refund":0.0},"avg_transaction":141.48,"total_decline_rate":0.0,"total_decline_amount":0.0,"international":50.0')
    assert response.text().__contains__('"id":301,"avatar":null,"avg_transaction_amount":141.48,"company":{"id":171,"name":"ruby rose","owner_type":"client"},"cross_border_fee":2.73,"decline_fee":0.0,"decline_rate":0.0,"decline_amount":0.0,"fx_fee":2.23,"international":50.0,"pending":0.0,"person":{"first_name":"ruby","last_name":"rose","status":1,"role":1,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":0.0,"reversed_amount":0.0,"settled":278.0,"spend":282.96000000000004,"username":"rubyrose@mail.ru"}')


@allure.title('Admin user list filter by role and status')
def test_admin_user_list_filter_by_role_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/user?role=1&status=-1&date_start=2024-05-18&date_end=2024-05-19', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":4,"next":null,"previous":null,"results":{"total_sum":{"settled":0.0,"pending":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":0.0,"refund":0.0},"avg_transaction":0.0,"total_decline_rate":0.0,"total_decline_amount":0.0,"international":0.0,"data":[{"id":513,"avatar":null,"avg_transaction_amount":0.0,"company":{"id":1,"name":"MTS","owner_type":"client"},"cross_border_fee":0.0,"decline_fee":0.0,"decline_rate":0.0,"decline_amount":0.0,"fx_fee":0.0,"international":0.0,"pending":0.0,"person":{"first_name":"rytytu","last_name":"vbnvbnghjfjty","status":-1,"role":1,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"username":"trhy6765876867udtyjtyju@mail.ru"},{"id":512,"avatar":null,"avg_transaction_amount":0.0,"company":{"id":1,"name":"MTS","owner_type":"client"},"cross_border_fee":0.0,"decline_fee":0.0,"decline_rate":0.0,"decline_amount":0.0,"fx_fee":0.0,"international":0.0,"pending":0.0,"person":{"first_name":"emp3465","last_name":"rgrter45","status":-1,"role":1,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"username":"rgrgtt5ytru78769768r67@mail.com"},{"id":511,"avatar":null,"avg_transaction_amount":0.0,"company":{"id":1,"name":"MTS","owner_type":"client"},"cross_border_fee":0.0,"decline_fee":0.0,"decline_rate":0.0,"decline_amount":0.0,"fx_fee":0.0,"international":0.0,"pending":0.0,"person":{"first_name":"qewrt","last_name":"qwert567","status":-1,"role":1,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"username":"dfgrty5642@hjnyjdytjn.com"},{"id":186,"avatar":null,"avg_transaction_amount":0.0,"company":{"id":1,"name":"MTS","owner_type":"client"},"cross_border_fee":0.0,"decline_fee":0.0,"decline_rate":0.0,"decline_amount":0.0,"fx_fee":0.0,"international":0.0,"pending":0.0,"person":{"first_name":"last","last_name":"first","status":-1,"role":1,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"username":"lasttest@mai.tu"}]}}'


@allure.title('Admin user list filter by search and status')
def test_admin_user_list_filter_by_status_search(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/user?role=1&status=1&search=gold&date_start=2024-05-18&date_end=2024-05-19', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":1,"next":null,"previous":null,"results":{"total_sum":{"settled":22.0,"pending":214.0,"reversed_amount":0.0,"fx_fee":0.93,"cross_border_fee":3.11,"decline_fee":0.0,"spend":224.04000000000002,"refund":16.0},"avg_transaction":60.010000000000005,"total_decline_rate":0.0,"total_decline_amount":0.0,"international":75.0,"data":[{"id":302,"avatar":null,"avg_transaction_amount":60.010000000000005,"company":{"id":172,"name":"golden company","owner_type":"client"},"cross_border_fee":3.11,"decline_fee":0.0,"decline_rate":0.0,"decline_amount":0.0,"fx_fee":0.93,"international":75.0,"pending":214.0,"person":{"first_name":"golden","last_name":"company","status":1,"role":1,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":16.0,"reversed_amount":0.0,"settled":22.0,"spend":224.04000000000002,"username":"goldencompany@mail.ru"}]}}'


@allure.title('Admin user list filter by status and page = 2')
def test_admin_user_list_filter_by_status_page_2(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/user?status=1&ordering=-spend&page=2&date_start=2024-05-18&date_end=2024-05-19', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/user?date_end=2024-05-19&date_start=2024-05-18&ordering=-spend&page=3&status=1","previous":"https://dev.api.devhost.io/api/admin/user?date_end=2024-05-19&date_start=2024-05-18&ordering=-spend&status=1","results":{"total_sum":{"settled":980.0,"pending":810.0,"reversed_amount":183.0,"fx_fee":7.17,"cross_border_fee":14.47,"decline_fee":4.5,"spend":1656.14,"refund":160.0},"avg_transaction":58.53935483870968,"total_decline_rate":18.367346938775512,"total_decline_amount":117.0,"international":60.0,"data":[{"id":61,"avatar":null,"avg_transaction_amount":0.0,"company":{"id":26,"name":"Some Referee 3","owner_type":"client"},"cross_border_fee":0.0,"decline_fee":0.0,"decline_rate":0.0,"decline_amount":0.0,"fx_fee":0.0,"international":0.0,"pending":0.0,"person":{"first_name":"Some","last_name":"Referee","status":1,"role":1,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"username":"some3@referee.com"}')
    assert response.text().__contains__('{"id":64,"avatar":null,"avg_transaction_amount":0.0,"company":{"id":29,"name":"FirstReferrer","owner_type":"client"},"cross_border_fee":0.0,"decline_fee":0.0,"decline_rate":0.0,"decline_amount":0.0,"fx_fee":0.0,"international":0.0,"pending":0.0,"person":{"first_name":"First","last_name":"Referrer","status":1,"role":1,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"username":"first@referrer.com"}')
    assert response.text().__contains__('{"id":65,"avatar":null,"avg_transaction_amount":0.0,"company":{"id":30,"name":"FirstReferee","owner_type":"client"},"cross_border_fee":0.0,"decline_fee":0.0,"decline_rate":0.0,"decline_amount":0.0,"fx_fee":0.0,"international":0.0,"pending":0.0,"person":{"first_name":"First","last_name":"Referee","status":1,"role":1,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"username":"first@referee.com"}')
    assert response.text().__contains__('{"id":67,"avatar":null,"avg_transaction_amount":0.0,"company":{"id":32,"name":"ThirdReferee","owner_type":"client"},"cross_border_fee":0.0,"decline_fee":0.0,"decline_rate":0.0,"decline_amount":0.0,"fx_fee":0.0,"international":0.0,"pending":0.0,"person":{"first_name":"Third","last_name":"Referee","status":1,"role":1,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"username":"third@referee.com"}')
    assert response.text().__contains__('{"id":68,"avatar":null,"avg_transaction_amount":0.0,"company":{"id":33,"name":"FourthReferee","owner_type":"client"},"cross_border_fee":0.0,"decline_fee":0.0,"decline_rate":0.0,"decline_amount":0.0,"fx_fee":0.0,"international":0.0,"pending":0.0,"person":{"first_name":"Fourth","last_name":"Referee","status":1,"role":1,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"username":"fourth@referee.com"}')
    assert response.text().__contains__('"refund":0.0,"reversed_amount":0.0,"settled":0.0,"spend":0.0,"username":"russianlanguige@mail.ru"}]}}')


@allure.title('Not admin user list')
def test_not_admin_user_list(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/user?status=1&ordering=-spend&page=2&date_start=2024-05-18&date_end=2024-05-19', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('User list without auth')
def test_user_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/user?status=1&ordering=-spend&page=2&date_start=2024-05-18&date_end=2024-05-19'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED

@pytest.mark.parametrize("user", VALID_USERS_WITH_ROLES)
def test_roles_view_user_list(request, api_request_context: APIRequestContext, user):
    token = auth_token_function(request=request, username = user.login, password = user.password)
    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
            '/api/admin/user', headers=headers
        )
    assert response.status == 200
    assert validate_json_keys(response.text(), '{"id":296,"avatar":null,"avg_transaction_amount":57.6986301369863,"company":{"id":167,"name":"white company","owner_type":"client"},"cross_border_fee":0.0,"decline_fee":0.0,"decline_rate":0.0,"decline_amount":0.0,"fx_fee":0.0,"international":0.0,"pending":0.0,"person":{"first_name":"white","last_name":"company","status":1,"role":1,"limit":{"id":1,"name":"entity.cardLimit.noLimit","days":0,"start_at":null},"limit_amount":0,"limit_spend":null},"refund":0.0,"reversed_amount":0.0,"settled":4212.0,"spend":4212.0,"username":"whitecompany@mail.ru"}') == True
    