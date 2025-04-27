import allure
from playwright.sync_api import APIRequestContext


@allure.title('Api transactions widgets list')
def test_api_transactions_widgets_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/transaction/widgets?company=129', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('{"index":0,"start":"2023-08-01T00:00:00Z"')
    assert response.text().__contains__('"value":0.0}')
    assert response.text().__contains__('{"index":16,"start"')
    assert response.text().__contains__('{"index":22,"start"')
    assert response.text().__contains__('"value":')
    assert response.text().__contains__('{"index":14,"start":')
    assert response.text().__contains__('"value":')


@allure.title('Api transactions widgets list filter by reversed')
def test_api_transactions_widgets_list_filter_by_reversed(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/transaction/widgets?company=129&status=reversed', headers=headers
    )

    assert response.status == 200
    assert response.json()["transactions"]["intervals"][1]["index"] == 1
    assert response.json()["spend"]["total"] == 0.0
    assert response.json()["declined_transactions"]["total"] == 0.0
    assert response.json()["decline_amount"]["total"] == 0.0
    assert response.json()["decline_rate"]["total"] == None
    assert response.json()["decline_rate"]["intervals"] == None


@allure.title('Api transactions widgets list filter by declined')
def test_api_transactions_widgets_list_filter_by_declined(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/transaction/widgets?company=129&status=declined', headers=headers
    )

    assert response.status == 200
    assert response.json()["transactions"]["total"] == 2.0
    assert response.json()["spend"]["total"] == 1.0
    assert response.json()["declined_transactions"]["total"] == 2.0
    assert response.json()["decline_amount"]["total"] == 22
    assert response.json()["decline_rate"]["total"] == None
    assert response.json()["decline_rate"]["intervals"] == None




