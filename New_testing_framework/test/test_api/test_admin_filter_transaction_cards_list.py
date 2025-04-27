import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import PERMISSIONS


@allure.title('Admin filter transaction cards list')
def test_admin_filter_transaction_cards_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/transaction/cards', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('{"id":18,"name":"Test","number":"4491","payment_system_code":"mc"}')
    assert response.text().__contains__('{"id":16,"name":"Test","number":"9567","payment_system_code":"mc"}')
    assert response.text().__contains__('{"id":30,"name":"08082023180033","number":"0355","payment_system_code":"mc"}')
    assert response.text().__contains__('{"id":25,"name":"Test Card 333","number":"1587","payment_system_code":"mc"}')
    assert response.text().__contains__('{"id":78,"name":"visa bin 408544007","number":"6869","payment_system_code":"visa"}')
    assert response.text().__contains__('{"id":366,"name":"1234567","number":"6320","payment_system_code":"mc"}')
    assert response.text().__contains__('{"id":177,"name":"IMzDNB","number":"0423","payment_system_code":"mc"}')



@allure.title('Filter transaction cards list not admin')
def test_not_admin_filter_transaction_cards_list(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/transaction/cards', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter transaction cards list without auth')
def test_not_admin_filter_transaction_cards_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/transaction/cards'
    )
    assert response.status == 401
