import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter subscriptions statuses list')
def test_admin_filter_subscriptions_statuses_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/subscription/statuses', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"code":"unpaid","name":"entity.subscriptionBillStatus.unpaid"},{"code":"paid","name":"entity.subscriptionBillStatus.paid"},{"code":"failed","name":"entity.subscriptionBillStatus.failed"},{"code":"canceled","name":"entity.subscriptionBillStatus.canceled"}]'


@allure.title('Filter subscriptions statuses list not admin')
def test_filter_subscriptions_statuses_list_not_admin(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/subscription/statuses', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter subscriptions statuses list without auth')
def test_filter_subscriptions_statuses_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/subscription/statuses'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
