import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin company ordering by avg transaction amount')
def test_admin_company_ordering_by_avg_transaction_amount(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/company?ordering=avg_transaction_amount&date_start=2024-05-18&date_end=2024-05-19', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/company?date_end=2024-05-19&date_start=2024-05-18&ordering=avg_transaction_amount&page=2","previous":null,"results":{"total_issued":1,"transactions_count":49,"avg_transaction":58.539354838709684,"total_decline_rate":18.367346938775512,"total_decline_amount":117.0,"international":60.0,"total_sum":{"money_in":0.0,"settled":980.0,"pending":810.0,"refund":160.0,"reversed_amount":183.0,"fx_fee":7.17,"cross_border_fee":14.47,"decline_fee":4.5,"spend":-1656.1400000000003}')
    assert response.text().__contains__('"id":7,"name":"Microsoft","status":"pending","tariff":null,"issued_cards":0,"transactions_count":0,"international":0.0,"avg_transaction_amount":0.0,"decline_rate":0.0,"decline_amount":0.0,"money_in":0.0,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":-0.0,"owner_type":"client","avatar":null}')
    assert response.text().__contains__('"id":8,"name":"test1","status":"pending","tariff":null,"issued_cards":0,"transactions_count":0,"international":0.0,"avg_transaction_amount":0.0,"decline_rate":0.0,"decline_amount":0.0,"money_in":0.0,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":-0.0,"owner_type":"client","avatar":null}')


@allure.title('Admin company without auth')
def test_admin_company_without_auth(api_request_context: APIRequestContext) -> None:
    response = api_request_context.get(
        '/api/admin/company'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Admin company with not admin')
def test_admin_company_with_not_admin(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/company', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin company filter by status ordering by decline amount')
def test_admin_company_filter_by_status_ordering_by_decline__amount(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/company?status=pending&ordering=-decline_amount&date_start=2024-05-18&date_end=2024-05-19', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/company?date_end=2024-05-19&date_start=2024-05-18&ordering=-decline_amount&page=2&status=pending","previous":null,"results":{"total_issued":0,"transactions_count":0,"avg_transaction":0.0,"total_decline_rate":0.0,"total_decline_amount":0.0,"international":0.0,"total_sum":{"money_in":0.0,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":-0.0}')
    assert response.text().__contains__('{"id":7,"name":"Microsoft","status":"pending","tariff":null,"issued_cards":0,"transactions_count":0,"international":0.0,"avg_transaction_amount":0.0,"decline_rate":0.0,"decline_amount":0.0,"money_in":0.0,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":-0.0,"owner_type":"client","avatar":null}')
    assert response.text().__contains__('{"id":8,"name":"test1","status":"pending","tariff":null,"issued_cards":0,"transactions_count":0,"international":0.0,"avg_transaction_amount":0.0,"decline_rate":0.0,"decline_amount":0.0,"money_in":0.0,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":-0.0,"owner_type":"client","avatar":null}')


@allure.title('Admin company filter by status active ordering by decline rate & page = 2')
def test_admin_company_filter_by_status_active_ordering_by_decline_rate_page_2(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/company?status=active&ordering=decline_rate&page=2&date_start=2024-05-18&date_end=2024-05-19', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/company?date_end=2024-05-19&date_start=2024-05-18&ordering=decline_rate&page=3&status=active","previous":"https://dev.api.devhost.io/api/admin/company?date_end=2024-05-19&date_start=2024-05-18&ordering=decline_rate&status=active","results":{"total_issued":1,"transactions_count":49,"avg_transaction":58.53935483870968,"total_decline_rate":18.367346938775512,"total_decline_amount":117.0,"international":60.0,"total_sum":{"money_in":0.0,"settled":980.0,"pending":810.0,"refund":160.0,"reversed_amount":183.0,"fx_fee":7.17,"cross_border_fee":14.47,"decline_fee":4.5,"spend":-1656.14}')
    assert response.text().__contains__('"id":165,"name":"BeGKroLput lESp","status":"active","tariff":"Pro","issued_cards":0,"transactions_count":0,"international":0.0,"avg_transaction_amount":0.0,"decline_rate":0.0,"decline_amount":0.0,"money_in":0.0,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":-0.0,"owner_type":"client","avatar":null}')
    assert response.text().__contains__('{"id":166,"name":"Test Dashboard","status":"active","tariff":"Pro","issued_cards":0,"transactions_count":0,"international":0.0,"avg_transaction_amount":0.0,"decline_rate":0.0,"decline_amount":0.0,"money_in":0.0,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":-0.0,"owner_type":"client","avatar":null}')


@allure.title('Admin company filter by owner type ordering by international')
def test_admin_company_filter_by_owner_type_ordering_by_international(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/company?owner_type=client&ordering=international&date_start=2024-05-18&date_end=2024-05-19', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/company?date_end=2024-05-19&date_start=2024-05-18&ordering=international&owner_type=client&page=2","previous":null,"results":{"total_issued":1,"transactions_count":49,"avg_transaction":58.53935483870968,"total_decline_rate":18.367346938775512,"total_decline_amount":117.0,"international":60.0,"total_sum":{"money_in":0.0,"settled":980.0,"pending":810.0,"refund":160.0,"reversed_amount":183.0,"fx_fee":7.17,"cross_border_fee":14.47,"decline_fee":4.5,"spend":-1656.14')
    assert response.text().__contains__('"id":1,"name":"MTS","status":"active","tariff":"Pro","issued_cards":0,"transactions_count":0,"international":0.0,"avg_transaction_amount":0.0,"decline_rate":0.0,"decline_amount":0.0,"money_in":0.0,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":-0.0,"owner_type":"client","avatar":null')
    assert response.text().__contains__('"id":2,"name":"Beeline","status":"active","tariff":null,"issued_cards":0,"transactions_count":0,"international":0.0,"avg_transaction_amount":0.0,"decline_rate":0.0,"decline_amount":0.0,"money_in":0.0,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":-0.0,"owner_type":"client","avatar":null')


@allure.title('Admin company filter by search ordering by issued cards')
def test_admin_company_filter_by_search_ordering_by_issued_cards(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/company?search=Beeline&ordering=-issued_cards&date_start=2024-05-18&date_end=2024-05-19', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":1,"next":null,"previous":null,"results":{"total_issued":0,"transactions_count":0,"avg_transaction":0.0,"total_decline_rate":0.0,"total_decline_amount":0.0,"international":0.0,"total_sum":{"money_in":0.0,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":-0.0},"data":[{"id":2,"name":"Beeline","status":"active","tariff":null,"issued_cards":0,"transactions_count":0,"international":0.0,"avg_transaction_amount":0.0,"decline_rate":0.0,"decline_amount":0.0,"money_in":0.0,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":-0.0,"owner_type":"client","avatar":null}]}}'


@allure.title('Admin company ordering by money_in page = 5')
def test_admin_company_ordering_by_money_in(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/company?ordering=money_in&page=5&date_start=2024-05-18&date_end=2024-05-19', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/company?date_end=2024-05-19&date_start=2024-05-18&ordering=money_in&page=6","previous":"https://dev.api.devhost.io/api/admin/company?date_end=2024-05-19&date_start=2024-05-18&ordering=money_in&page=4","results":{"total_issued":1,"transactions_count":49,"avg_transaction":58.539354838709684,"total_decline_rate":18.367346938775512,"total_decline_amount":117.0,"international":60.0,"total_sum":{"money_in":0.0,"settled":980.0,"pending":810.0,"refund":160.0,"reversed_amount":183.0,"fx_fee":7.17,"cross_border_fee":14.47,"decline_fee":4.5,"spend":-1656.1400000000003}')
    assert response.text().__contains__('{"id":329,"name":"test546547yu 56456rtytfhfgn","status":"active","tariff":"Trial","issued_cards":0,"transactions_count":0,"international":0.0,"avg_transaction_amount":0.0,"decline_rate":0.0,"decline_amount":0.0,"money_in":0.0,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":-0.0,"owner_type":"client","avatar":null}')


@allure.title('Admin company ordering by -name page = 4')
def test_admin_company_ordering_by__name(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/company?ordering=-name&page=2&date_start=2024-05-18&date_end=2024-05-18', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/company?date_end=2024-05-18&date_start=2024-05-18&ordering=-name&page=3","previous":"https://dev.api.devhost.io/api/admin/company?date_end=2024-05-18&date_start=2024-05-18&ordering=-name","results":{"total_issued":0,"transactions_count":0,"avg_transaction":0.0,"total_decline_rate":0.0,"total_decline_amount":0.0,"international":0.0,"total_sum":{"money_in":0.0,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":-0.0}')
    assert response.text().__contains__('{"id":619,"name":"xLqtOCJD","status":"restricted","tariff":"Basic","issued_cards":0,"transactions_count":0,"international":0.0,"avg_transaction_amount":0.0,"decline_rate":0.0,"decline_amount":0.0,"money_in":0.0,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":-0.0,"owner_type":"client","avatar":null}')


@allure.title('Admin company some filter ordering by spend')
def test_admin_company_some_filter_ordering_by_spend(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/company?status=active&owner_type=client&ordering=-spend&date_start=2024-05-18&date_end=2024-05-19', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"next":"https://dev.api.devhost.io/api/admin/company?date_end=2024-05-19&date_start=2024-05-18&ordering=-spend&owner_type=client&page=2&status=active","previous":null,"results":{"total_issued":1,"transactions_count":49,"avg_transaction":58.53935483870968,"total_decline_rate":18.367346938775512,"total_decline_amount":117.0,"international":60.0,"total_sum":{"money_in":0.0,"settled":980.0,"pending":810.0,"refund":160.0,"reversed_amount":183.0,"fx_fee":7.17,"cross_border_fee":14.47,"decline_fee":4.5,"spend":-1656.14}')
    assert response.text().__contains__('"id":1,"name":"MTS","status":"active","tariff":"Pro","issued_cards":0,"transactions_count":0,"international":0.0,"avg_transaction_amount":0.0,"decline_rate":0.0,"decline_amount":0.0,"money_in":0.0,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":-0.0,"owner_type":"client","avatar":null}')
    assert response.text().__contains__('{"id":2,"name":"Beeline","status":"active","tariff":null,"issued_cards":0,"transactions_count":0,"international":0.0,"avg_transaction_amount":0.0,"decline_rate":0.0,"decline_amount":0.0,"money_in":0.0,"settled":0.0,"pending":0.0,"refund":0.0,"reversed_amount":0.0,"fx_fee":0.0,"cross_border_fee":0.0,"decline_fee":0.0,"spend":-0.0,"owner_type":"client","avatar":null}')
