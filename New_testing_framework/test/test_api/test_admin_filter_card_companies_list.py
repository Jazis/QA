import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter card companies list')
def test_admin_filter_card_companies_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/card/companies', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":2,"name":"Beeline","owner_type":"client"')
    assert response.text().__contains__('"id":12,"name":"456 ihiyhyigi h uiy8767jh sKjdfkhfowe8u0483 67","owner_type":"client"}')
    assert response.text().__contains__('"id":18,"name":"1232","owner_type":"client"')
    assert response.text().__contains__('"id":71,"name":"Last Test name тест","owner_type":"client"')
    assert response.text().__contains__('"id":163,"name":"ywQFNCisSu iTkd","owner_type":"client"')
    assert response.text().__contains__('"id":260,"name":"JoGgbU","owner_type":"client"')
    assert response.text().__contains__('"id":360,"name":"zvEwQfCDde wQLK","owner_type":"client"')
    assert response.text().__contains__('"id":396,"name":"sHSbOW","owner_type":"client"')


@allure.title('Admin filter card companies list not admin')
def test_admin_filter_card_companies_list_not_admin(auth_login_user_data_ru,
                                                   api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/card/companies', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin filter card companies list without auth')
def test_admin_filter_card_companies_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/card/companies'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
