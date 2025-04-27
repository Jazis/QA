import allure
from playwright.sync_api import APIRequestContext


@allure.title('Get cash balance widgets without authorization')
def test_cash_balance_widgets_without_authorization(api_request_context: APIRequestContext) -> None:
    response = api_request_context.get(
        '/api/cash/balance/widgets'
    )
    assert response.status == 500 #может 401 ?


@allure.title('Get cash balance widgets')
def test_cash_balance_widgets(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/cash/balance/widgets?date_start=2024-12-08T21:00:00.000Z&date_end=2024-12-09T20:59:59.999Z', headers=headers
    )

    assert response.status == 200
    assert response.json()["intervals"][0]["index"] == 0
    assert response.json()["intervals"][0]["date"] == "2024-12-09T00:00:00.000000Z"
    assert response.json()["intervals"][0]["available_balance"] == 1004.65

    assert response.json()["intervals"][1]["index"] == 1
    assert response.json()["intervals"][1]["available_balance"] == 1004.65

    assert response.json()["current"]["available_balance"] == 1004.65
    assert response.json()["current"]["pending"] == 101.0