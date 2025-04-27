import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter company statuses list')
def test_admin_filter_company_statuses_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/company/statuses', headers=headers
    )
    assert response.status == 200
    assert response.text() == '[{"code":"pending","name":"entity.companyStatus.pending"},{"code":"qualified","name":"entity.companyStatus.qualified"},{"code":"disabled","name":"entity.companyStatus.disabled"},{"code":"restricted","name":"entity.companyStatus.restricted"},{"code":"active","name":"entity.companyStatus.active"}]'


@allure.title('Admin filter company statuses list not admin')
def test_admin_filter_company_statuses_list_not_admin(auth_login_user_data_ru,
                                                      api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/company/statuses', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin filter company statuses list without auth')
def test_admin_filter_company_statuses_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/company/statuses'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
