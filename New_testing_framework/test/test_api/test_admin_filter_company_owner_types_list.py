
import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter company owner types list')
def test_admin_filter_company_owner_types_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/company/owner_types', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"code":"client","name":"entity.companyOwnerType.client"},{"code":"own","name":"entity.companyOwnerType.own"}]'


@allure.title('Admin filter company owner types list not admin')
def test_admin_filter_company_owner_types_list_not_admin(auth_login_user_data_ru,
                                                api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/company/owner_types', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin filter company owner types list without auth')
def test_admin_filter_company_owner_types_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/company/owner_types'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
