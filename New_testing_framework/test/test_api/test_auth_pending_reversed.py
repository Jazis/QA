import uuid
from time import sleep

import allure
from playwright.sync_api import APIRequestContext

from api.function_api import api_post_auth_trans
from test.test_api.conftest import VISA


@allure.title("Transaction auth pending reversed")
def test_auth_pending_reversed(api_request_context: APIRequestContext) -> None:
    token = api_post_auth_trans(api_request_context, 5, VISA, '{"approved":true}')

    data = [
        {
            "id": token,
            "data": {
                "amount": 11.0,
                "idCard": 43359548,
                "network": "Mastercard",
                "authCode": "5JWMZM",
                "cardGuid": VISA,
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
            "eventType": "purchase.card.auth.approved",
            "dataVersion": "1"
        }
    ]
    response = api_request_context.post(
        '/webhook/connexpay', data=data)
    sleep(2)
    assert response.status == 200
    assert response.text() == '"OK"'

    data2 = [
        {
            "id": str(uuid.uuid4()),
            "data": {
                "amount": 11.0,
                "idCard": 43359548,
                "network": "Mastercard",
                "authCode": "5JWMZM",
                "cardGuid": VISA,
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
                "precedingRelatedToken": token
            },

            "subject": "14e92235-7a12-4301-a36b-5cf00f510b14",
            "eventTime": "2023-09-26T14:45:43.1054533Z",
            "eventType": "purchase.card.auth.reversal.settled",
            "dataVersion": "1"
        }
    ]
    response2 = api_request_context.post(
        '/webhook/connexpay', data=data2)
    sleep(2)
    assert response2.status == 200
    assert response2.text() == '"OK"'
