import uuid

import allure

from playwright.sync_api import APIRequestContext

from data.responses_texts import APPROVE_TRUE


@allure.title("Check available = true mcc code")
def test_check_mcc_code_available_true(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 45,
        "network": "Visa",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": "2aa8221f-9bdd-48da-a38d-089d15d19f83",
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

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )

    assert response.ok
    assert response.text() == APPROVE_TRUE


@allure.title("Check available = false mcc code")
def test_check_mcc_code_available_false(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 45,
        "network": "Visa",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": "2aa8221f-9bdd-48da-a38d-089d15d19f83",
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "5045",
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

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )

    assert response.ok
    assert response.text() == '{"approved":false}'


@allure.title("Check empty mcc code")
def test_check_empty_mcc_code(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 45,
        "network": "Visa",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": "2aa8221f-9bdd-48da-a38d-089d15d19f83",
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": " ",
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

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )

    assert response.ok
    assert response.text() == '{"approved":false}'


@allure.title("Check without row mcc code")
def test_check_without_mcc_code(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 45,
        "network": "Visa",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": "2aa8221f-9bdd-48da-a38d-089d15d19f83",
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),

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

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )

    assert response.ok
    assert response.text() == '{"approved":false}'


@allure.title("Check wrong card acceptor mcc")
def test_wrong_card_acceptor_mcc(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": "2aa8221f-9bdd-48da-a38d-089d15d19f83",
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "999",
        "cardAcceptorMid": "420429000200589",
        "availableBalance": 499975.0,
        "cardAcceptorCity": "650-5434800 CA",
        "cardAcceptorName": "FACEBK 38TQEZB6W2",
        "cardAcceptorState": "",
        "cardAcceptorCountry": "EN",
        "localTransactionAmount": 5.0,
        "retrievalReferenceNumber": "406513423488",
        "localTransactionCurrencyCode": "840"
    }

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )

    assert response.status == 200
    assert response.text() == '{"approved":false}'