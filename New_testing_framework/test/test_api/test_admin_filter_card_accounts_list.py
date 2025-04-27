
import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter card accounts list')
def test_admin_filter_card_accounts_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/card/accounts', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":23,"name":"GreatTraffic","company":{"id":14,"name":"GreatTraffic","owner_type":"client"},"number":"1096379"')
    assert response.text().__contains__('"id":26,"name":"1231","company":{"id":17,"name":"1231","owner_type":"client"')
    assert response.text().__contains__('"id":30,"name":"ComapnyCreated","company":{"id":21,"name":"ComapnyCreated","owner_type":"client"')
    assert response.text().__contains__('"id":43,"name":"FifthReferee","company":{"id":34,"name":"FifthReferee","owner_type":"client"},"number":"1010976"')
    assert response.text().__contains__('"id":67,"name":"onb1 onb1","company":{"id":58,"name":"onb1 onb1","owner_type":"client"},"number":"2085723"')


@allure.title('Admin filter card accounts list not admin')
def test_admin_filter_card_accounts_list_not_admin(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/card/accounts', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin filter card accounts list without auth')
def test_admin_filter_card_accounts_list_without_auth(api_request_context: APIRequestContext) -> None:
    response = api_request_context.get(
        '/api/admin/filter/card/accounts'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED