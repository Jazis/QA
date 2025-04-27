import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter card limits list')
def test_admin_filter_card_limits_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/card/limits', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":2,"name":"Daily","days":1')
    assert response.text().__contains__('"id":1,"name":"No limit","days":0')
    assert response.text().__contains__('"id":4,"name":"Monthly","days":30')
    assert response.text().__contains__('"id":5,"name":"Lifetime","days":999')
    assert response.text().__contains__('"id":3,"name":"Weekly","days":7')


@allure.title('Admin filter card limits list not admin')
def test_admin_filter_card_limits_list_not_admin(auth_login_user_data_ru,
                                                 api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/card/limits', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin filter card limits list without auth')
def test_admin_filter_card_limits_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/card/limits'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
