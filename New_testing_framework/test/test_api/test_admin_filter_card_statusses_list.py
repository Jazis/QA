
import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter card statuses list')
def test_admin_filter_card_statuses_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/card/statuses', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"id":-1,"name":"entity.cardStatus.closed"},{"id":0,"name":"entity.cardStatus.freeze"},{"id":1,"name":"entity.cardStatus.active"},{"id":2,"name":"entity.cardStatus.expired"}]'
    

@allure.title('Admin filter card statuses list not admin')
def test_admin_filter_card_statuses_list_not_admin(auth_login_user_data_ru,
                                                          api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/card/statuses', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin filter card statuses list without auth')
def test_admin_filter_card_statuses_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/card/statuses'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED