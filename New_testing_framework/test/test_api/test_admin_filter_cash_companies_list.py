
import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter cash companies list')
def test_admin_filter_cash_companies_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/cash/companies', headers=headers
    )

    assert response.text().__contains__('"id":2,"name":"Beeline","owner_type":"client"')
    assert response.text().__contains__('"id":5,"name":"New company 1","owner_type":"client"')
    assert response.text().__contains__('"id":4,"name":"Tesla","owner_type":"client"')
    assert response.text().__contains__('"id":81,"name":"Leonard_Gulgowski45 + Dibbert","owner_type":"client"')
    assert response.text().__contains__('"id":35,"name":"SixthReferee","owner_type":"client"')
    assert response.text().__contains__('"id":197,"name":"Subscrition check","owner_type":"client"')
    assert response.text().__contains__('"id":201,"name":"ki877 gfhghg","owner_type":"client"')
    assert response.text().__contains__('"id":353,"name":"uimrSx","owner_type":"client"')
    assert response.text().__contains__('"id":166,"name":"Test Dashboard","owner_type":"client"')
    assert response.text().__contains__('"id":381,"name":"fiANtp","owner_type":"client"')
    assert response.text().__contains__('"id":79,"name":"Franecki","owner_type":"client"')
    assert response.text().__contains__('"id":73,"name":"Genevieve Halvorson MD","owner_type":"client"')
    assert response.text().__contains__('"id":35,"name":"SixthReferee","owner_type":"client"')


@allure.title('Admin filter cash companies list not admin')
def test_admin_filter_cash_companies_list_not_admin(auth_login_user_data_ru,
                                                   api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/cash/companies', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin filter cash companies list without auth')
def test_admin_filter_cash_companies_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/cash/companies'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
