import allure
from playwright.sync_api import APIRequestContext


@allure.title('Company banners list')
def test_company_banners_list(auth_login_user_restricted_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_restricted_company}"
    }
    response = api_request_context.get(
        'api/banners/company', headers=headers
    )
    assert response.status == 200
    assert response.text() == '[{"id":4,"title":"entity.banner.restrictedStatusForAdmin.title","content":"entity.banner.restrictedStatusForAdmin.content","level":"destructive"}]'


@allure.title('Company banners empty list')
def test_company_banners_empty_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/banners/company', headers=headers
    )
    assert response.status == 200
    assert response.text() == '[]'


@allure.title('Company banners list without auth')
def test_company_banners_list_without_auth(auth_token, api_request_context: APIRequestContext) -> None:
    response = api_request_context.get(
        'api/banners/company'
    )
    assert response.status == 401
