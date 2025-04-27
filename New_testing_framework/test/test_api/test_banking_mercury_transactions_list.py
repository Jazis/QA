import allure
from playwright.sync_api import APIRequestContext


@allure.title('Banking Mercury accounts')
def test_banking_mercury_accounts(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/banking/mercury/transactions', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"success":true}'