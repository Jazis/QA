import allure
from playwright.sync_api import APIRequestContext


@allure.title('Api cash')
def test_api_cash(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/cash', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":'), ('"created_at"')
    assert response.text().__contains__('"client_type":"subscription","description":"Pro"')
    assert response.text().__contains__('"amount":')
    assert response.text().__contains__('"client_type":"bonus","description":""')
    assert response.text().__contains__('"deposit_fee","description":""')
    assert response.text().__contains__('"client_type":"deposit_wire","description":""')
    assert response.text().__contains__('"client_type":"deposit","description":"","amount"')


@allure.title('Api cash filter by company')
def test_api_cash_filter_by_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/cash?company=3', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":0,"next":null,"previous":null,"results":[]}'


@allure.title('Api cash without auth')
def test_api_cash_without_auth(api_request_context: APIRequestContext) -> None:
    response = api_request_context.get(
        '/api/cash?company=3'
    )
    assert response.status == 401
