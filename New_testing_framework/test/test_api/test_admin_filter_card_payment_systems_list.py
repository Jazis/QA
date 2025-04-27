
import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter card payment systems list')
def test_admin_filter_card_payment_systems_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/card/payment_systems', headers=headers
    )
   
    assert response.status == 200
    assert response.text() == '[{"code":"mc","name":"entity.paymentSystem.mc"},{"code":"visa","name":"entity.paymentSystem.visa"}]'


@allure.title('Admin filter card payment systems list not admin')
def test_admin_filter_card_payment_systems_list_not_admin(auth_login_user_data_ru,
                                                 api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/card/payment_systems', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin filter card payment systems list without auth')
def test_admin_filter_card_payment_systems_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/card/payment_systems'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED