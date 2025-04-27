import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter card users list')
def test_admin_filter_card_users_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/card/users', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('{"id":34,"person":{"first_name":"Conn","last_name":"User"}')
    assert response.text().__contains__('{"id":170,"person":{"first_name":"test","last_name":"test"}')
    assert response.text().__contains__('{"id":519,"person":{"first_name":"first-employee-check","last_name":"lastname"}')
    assert response.text().__contains__('{"id":295,"person":{"first_name":"Test","last_name":"Dashboard"}')
    assert response.text().__contains__('{"id":188,"person":{"first_name":"sfdsf","last_name":"fdsf"}')
    assert response.text().__contains__('{"id":113,"person":{"first_name":"тест","last_name":"ttesy"}')
    assert response.text().__contains__('{"id":515,"person":{"first_name":"yi879ouo","last_name":"gi8987iy"}')
    assert response.text().__contains__('{"id":627,"person":{"first_name":"test60987650999","last_name":"tesr409876543299999"}')


@allure.title('Admin filter card users list not admin')
def test_admin_filter_card_users_list_not_admin(auth_login_user_data_ru,
                                                   api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/card/users', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin filter card users list without auth')
def test_admin_filter_card_users_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/card/users'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
