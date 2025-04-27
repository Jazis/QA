import allure
from playwright.sync_api import APIRequestContext


@allure.title('Get processed transactions without authorization')
def test_get_processed_transactions_without_authorization(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/cash/processed_transactions?account_id=4'
    )

    assert response.status == 500 #может 401 ?


@allure.title('Get processed transactions with another user authorization')
def test_get_processed_transactions_with_another_user_authorization(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/cash/processed_transactions?account_id=173', headers=headers
    )

    assert response.status == 400
    assert response.text() == "{\"error\":\"You don't have access to account 173\"}"


@allure.title('Get processed transactions')
def test_get_processed_transactions_user(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/cash/processed_transactions?date_start=2024-12-11T21:00:00.000Z&date_end=2024-12-22T20:59:59.999Z&account_id=182', headers=headers
    )
    assert response.status == 200
    assert response.json()["count"] == 7
    assert response.json()["results"]["total_sum"]["total_amount"] == 478.8
    assert response.json()["results"]["total_sum"]["end_balance"] == 5311.97
    assert response.json()["results"]["total_sum"]["deposit"] == 1544
    assert response.json()["results"]["total_sum"]["wire_deposit"] == 0
    assert response.json()["results"]["total_sum"]["deposit_fee"] == 0
    assert response.json()["results"]["total_sum"]["settled"] == -10.2
    assert response.json()["results"]["total_sum"]["fx_fee"] == 0
    assert response.json()["results"]["total_sum"]["cross_border_fee"] == 0
    assert response.json()["results"]["total_sum"]["decline_fee"] == -1
    assert response.json()["results"]["total_sum"]["refund"] == 17
    assert response.json()["results"]["total_sum"]["refund_fx_fee"] == 0
    assert response.json()["results"]["total_sum"]["refund_cross_border_fee"] == 0
    assert response.json()["results"]["total_sum"]["gift"] == 0
    assert response.json()["results"]["total_sum"]["withdrawal"] == 0
    assert response.json()["results"]["total_sum"]["subscription"] == -1071
    assert response.json()["results"]["total_sum"]["beg_balance"] == 4833.17

    assert response.json()["results"]["data"][0]["id"] == 10723
    assert response.json()["results"]["data"][0]["subtype"] == "topup_virtual"
    assert response.json()["results"]["data"][0]["client_type"] == "deposit"
    assert response.json()["results"]["data"][0]["amount"] == 1500
    assert response.json()["results"]["data"][0]["count"] == 1
    assert response.json()["results"]["data"][0]["settled_at"] == "2024-12-18T09:21:24.141610Z"
    assert response.json()["results"]["data"][0]["status"] == "settled"
    assert response.json()["results"]["data"][0]["updated_at"] == "2024-12-18T09:21:24.141709Z"
    assert response.json()["results"]["data"][0]["date"] == "2024-12-18T00:00:00.000000Z"
    assert response.json()["results"]["data"][0]["fx_fee"] == 0
    assert response.json()["results"]["data"][0]["cross_border_fee"] == 0
    assert response.json()["results"]["data"][0]["decline_fee"] == 0
    assert response.json()["results"]["data"][0]["payment_amount"] == 1500
    assert response.json()["results"]["data"][0]["batch"] == "1734513684350"
    assert response.json()["results"]["data"][0]["is_aggregated"] == False

    assert response.json()["results"]["data"][5]["id"] == 4765
    assert response.json()["results"]["data"][5]["subtype"] == "spend"
    assert response.json()["results"]["data"][5]["client_type"] == "spend"
    assert response.json()["results"]["data"][5]["amount"] == -10.2
    assert response.json()["results"]["data"][5]["count"] == 1
    assert response.json()["results"]["data"][5]["settled_at"] == "2024-12-16T00:00:00.000000Z"
    assert response.json()["results"]["data"][5]["status"] == "unclosed"
    assert response.json()["results"]["data"][5]["updated_at"] == "2024-12-18T07:49:12.998670Z"
    assert response.json()["results"]["data"][5]["date"] == "2024-12-16T00:00:00.000000Z"
    assert response.json()["results"]["data"][5]["fx_fee"] == 0
    assert response.json()["results"]["data"][5]["cross_border_fee"] == 0
    assert response.json()["results"]["data"][5]["decline_fee"] == 0
    assert response.json()["results"]["data"][5]["payment_amount"] == -10.2
    assert response.json()["results"]["data"][5]["batch"] == "182_spend_settled_2024-12-16"
    assert response.json()["results"]["data"][5]["is_aggregated"] == True





