import uuid

import pytest
from playwright.sync_api import APIRequestContext


@pytest.mark.usefixtures("send_auth_trans_user_limit_check")
def test_check_user_limit(api_request_context: APIRequestContext, send_auth_trans_user_limit_check) -> None:
    data = [
        {
            "id": send_auth_trans_user_limit_check,
            "data": {
                "amount": 200.0,
                "idCard": 43359548,
                "network": "Visa",
                "authCode": "5JWMZM",
                "cardGuid": "19a212da-bc2d-47a7-a809-04cf1082d98d", #id = 238 green company
                "decisionBy": "Rize Ads",
                "authMessage": "Approved or completed successfully",
                "orderNumber": "lfkRqq",
                "currencyCode": "USD",
                "merchantName": "Rize Ads",
                "cardAcceptorMcc": "7311",
                "cardAcceptorMid": "227205000067204",
                "availableBalance": 499903.24,
                "cardAcceptorCity": "Menlo Park CA",
                "cardAcceptorName": "FACEBK ADS",
                "merchantIdentifier": "14e92235-7a12-4301-a36b-5cf00f510b14",
                "authorizationAmount": 2.0,
                "cardAcceptorCountry": "US",
                "authorizationCurrencyCode": "USD"
            },

            "subject": "14e92235-7a12-4301-a36b-5cf00f510b14",
            "eventTime": "2023-09-26T14:45:43.1054533Z",
            "eventType": "purchase.card.auth.settled",
            "dataVersion": "1"
        }
    ]
    response = api_request_context.post(
        '/webhook/connexpay', data=data)

    assert response.status == 200
    assert response.text() == '"OK"'

    data2 = {
        "AVS": "NA NA",
        "amount": 150.0,
        "network": "Visa",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": "19a212da-bc2d-47a7-a809-04cf1082d98d", #id = 238 green company
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
        "cardAcceptorMid": "227205000067204",
        "availableBalance": 499975.0,
        "cardAcceptorCity": "650-5434800 CA",
        "cardAcceptorName": "FACEBK 38TQEZB6W2",
        "cardAcceptorState": "",
        "cardAcceptorCountry": "US",
        "localTransactionAmount": 5.0,
        "retrievalReferenceNumber": "406513423488",
        "localTransactionCurrencyCode": "840"
    }

    response2 = api_request_context.post(
        '/webhook/connexpay/auth', data=data2
    )
    assert response2.status == 200
    assert response2.text() == '{"approved":false}'

    data3 = [
        {
            "id": str(uuid.uuid4()),
            "data": {
                "amount": 12.0,
                "idCard": 43359548,
                "network": "Visa",
                "authCode": "5JWMZM",
                "cardGuid": "19a212da-bc2d-47a7-a809-04cf1082d98d", #id = 238 green company
                "decisionBy": "Rize Ads",
                "authMessage": "Approved or completed successfully",
                "orderNumber": "lfkRqq",
                "currencyCode": "USD",
                "merchantName": "Rize Ads",
                "cardAcceptorMcc": "7311",
                "cardAcceptorMid": "227205000067204",
                "availableBalance": 499903.24,
                "cardAcceptorCity": "Menlo Park CA",
                "cardAcceptorName": "FACEBK ADS",
                "merchantIdentifier": "14e92235-7a12-4301-a36b-5cf00f510b14",
                "authorizationAmount": 2.0,
                "cardAcceptorCountry": "US",
                "authorizationCurrencyCode": "USD",
                "precedingRelatedToken": send_auth_trans_user_limit_check
            },

            "subject": "14e92235-7a12-4301-a36b-5cf00f510b14",
            "eventTime": "2023-09-26T14:45:43.1054533Z",
            "eventType": "purchase.card.auth.declined",
            "dataVersion": "1"
        }
    ]
    response3 = api_request_context.post(
        '/webhook/connexpay', data=data3)

    assert response3.status == 200
    assert response3.text() == '"OK"'
