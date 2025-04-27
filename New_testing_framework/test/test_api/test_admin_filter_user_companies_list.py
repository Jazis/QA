import allure
from playwright.sync_api import APIRequestContext


@allure.title('Admin filter user companies list')
def test_admin_filter_user_companies_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/filter/user/companies', headers=headers
    )
    assert response.status == 200
    assert response.text().__contains__('{"id":4,"name":"Tesla","owner_type":"client"}')


@allure.title('Not Admin filter user companies list')
def test_not_admin_filter_user_companies_list(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        'api/admin/filter/user/companies', headers=headers
    )
    assert response.status == 403


@allure.title('Admin filter user companies list without auth')
def test_not_admin_filter_user_companies_list_without_auth(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    response = api_request_context.get(
        'api/admin/filter/user/companies'
    )
    assert response.status == 401
