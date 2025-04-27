import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED


@allure.title('Admin company disable and activate')
def test_admin_company_disable_and_activate(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    data = {
        "plan_id": 1,
        "provider_id": 2
    }
    response_active_1 = api_request_context.post(
        '/api/admin/company/198/activate', headers=headers, data=data
    )

    assert response_active_1.status == 200

    response_get = api_request_context.get(
        '/api/admin/company/198', headers=headers
    )

    assert response_get.status == 200



    response = api_request_context.post(
        '/api/admin/company/198/disable', headers=headers
    )

    assert response.status == 200
    assert response.text() == ''

    response_check = api_request_context.get(
        '/api/admin/company/198', headers=headers
    )

    assert response_check.status == 200

    data_activate = {
        "plan_id": 1,
        "provider_id": 2
    }
    response_active = api_request_context.post(
        '/api/admin/company/198/activate', headers=headers, data=data_activate
    )

    assert response_active.status == 200
    assert response_active.text() == ''

    response_get_active = api_request_context.get(
        '/api/admin/company/198', headers=headers
    )

    assert response_get_active.status == 200


@allure.title('Admin company disable without auth')
def test_admin_company_disable_without_auth(auth_token, api_request_context: APIRequestContext) -> None:
    response = api_request_context.post(
        '/api/admin/company/203/disable'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Admin company restrict without auth')
def test_admin_company_restrict_without_auth(auth_token, api_request_context: APIRequestContext) -> None:
    response = api_request_context.post(
        '/api/admin/company/203/restrict'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Admin company disable not admin')
def test_admin_company_disable_not_admin(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.post(
        '/api/admin/company/203/disable'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Admin company restrict not admin')
def test_admin_company_restrict_not_admin(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.post(
        '/api/admin/company/203/restrict'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED