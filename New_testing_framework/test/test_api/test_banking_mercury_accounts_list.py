import allure
from playwright.sync_api import APIRequestContext


@allure.title('Admin banking mercury accounts')
def test_admin_banking_mercury_accounts(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/banking/mercury/accounts', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"success":true}'


@allure.title('Not admin banking mercury accounts')
def test_not_admin_banking_mercury_accounts(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/banking/mercury/accounts', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"success":true}'


