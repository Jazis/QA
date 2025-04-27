import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter transaction users list')
def test_admin_filter_transaction_users_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/transaction/users', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('{"id":295,"person":{"first_name":"Test","last_name":"Dashboard"}')
    assert response.text().__contains__('{"id":347,"person":{"first_name":"fbfgh","last_name":"hfghgfh"}')
    assert response.text().__contains__('{"id":184,"person":{"first_name":"Test","last_name":"Some"}')
    assert response.text().__contains__('{"id":188,"person":{"first_name":"sfdsf","last_name":"fdsf"}')
    assert response.text().__contains__('{"id":113,"person":{"first_name":"тест","last_name":"ttesy"}')
    assert response.text().__contains__('{"id":530,"person":{"first_name":"testyu7567","last_name":"test4654724"}')
    assert response.text().__contains__('{"id":4,"person":{"first_name":"Bill","last_name":"Hill"}')
    assert response.text().__contains__('{"id":21,"person":{"first_name":"Hhgr","last_name":"Gdyhr"}')
    assert response.text().__contains__('{"id":46,"person":{"first_name":"Oleg","last_name":"Velikiy"}')
    assert response.text().__contains__('{"id":95,"person":{"first_name":"onb1","last_name":"onb1"}')
    assert response.text().__contains__('{"id":180,"person":{"first_name":"SOme","last_name":"Token"}')
    assert response.text().__contains__('{"id":392,"person":{"first_name":"dsef","last_name":"dsfdsg"}')
    assert response.text().__contains__('{"id":2,"person":{"first_name":"Mue","last_name":"Cer"}')
    assert response.text().__contains__('{"id":341,"person":{"first_name":"subscrition","last_name":"test"}')
    assert response.text().__contains__('{"id":526,"person":{"first_name":"test098765","last_name":"tesr8765444"}')
    assert response.text().__contains__('{"id":311,"person":{"first_name":"5454","last_name":"9879"}')
    assert response.text().__contains__('{"id":70,"person":{"first_name":"Sixth","last_name":"Referee"}')
    assert response.text().__contains__('{"id":342,"person":{"first_name":"subscr.","last_name":"test"}')
    assert response.text().__contains__('{"id":19,"person":{"first_name":"Vlad","last_name":"Ok"}')


@allure.title('Not admin filter transaction users list')
def test_not_admin_filter_transaction_users_list(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/transaction/users', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter transaction users list without auth')
def test_filter_transaction_users_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/transaction/users'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
