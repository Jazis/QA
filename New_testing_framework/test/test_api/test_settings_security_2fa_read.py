import allure
from playwright.sync_api import APIRequestContext


@allure.title('Api settings security without 2fa')
def test_api_settings_security_without_2fa(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/settings/security/2fa', headers=headers
    )
    assert response.status == 200
    assert response.text() == '{"totp_device":null,"recovery_codes":{"remaining_count":6,"default_count":6}}'


@allure.title('Api settings security with 2fa')
def test_api_settings_security_with_2fa(auth_login_user_with_2fa, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_with_2fa}"
    }
    response = api_request_context.get(
        '/api/settings/security/2fa', headers=headers
    )
    assert response.status == 401
