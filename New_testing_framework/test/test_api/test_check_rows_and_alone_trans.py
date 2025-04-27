import uuid
from time import sleep

import allure
from playwright.sync_api import APIRequestContext

from api.function_api import api_request
from data.responses_texts import APPROVE_TRUE
from data.input_data.data_card import PENDING, COUNTRY_US, CURRENCY_USD, DECLINED
from data.input_data.decline_reasons import APPROVED_SUCCES
from test.test_api.conftest import MC


@allure.title("Transaction pending_zero")
def test_webhook_pending_zero(api_request_context: APIRequestContext) -> None:
    api_request(api_request_context, 0, MC, APPROVED_SUCCES, PENDING, COUNTRY_US, CURRENCY_USD)


@allure.title("Transaction declined")
def test_webhook_declined(api_request_context: APIRequestContext) -> None:
    api_request(api_request_context, 11.6, MC, APPROVED_SUCCES, DECLINED, COUNTRY_US, CURRENCY_USD)


@allure.title("Transaction auth card acceptor country ru")
def test_auth_card_acceptor_country_ru(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
        "cardAcceptorMid": "420429000200589",
        "availableBalance": 499975.0,
        "cardAcceptorCity": "650-5434800 CA",
        "cardAcceptorName": "FACEBK 38TQEZB6W2",
        "cardAcceptorState": "",
        "cardAcceptorCountry": "RU",
        "localTransactionAmount": 5.0,
        "retrievalReferenceNumber": "406513423488",
        "localTransactionCurrencyCode": "840"
    }

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )
    sleep(1)
    assert response.status == 200
    assert response.text() == APPROVE_TRUE


@allure.title("Check random rows")
def test_check_random_rows(api_request_context: APIRequestContext) -> None:
    data = {
        "cardAcceptorName": "FACEBK 38TQEZB6W2",
        "availableBalance": 499975.0,
        "amount": 1.0,
        "localTransactionCurrencyCode": "840",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
        "cardAcceptorMid": "420429000200589",
        "network": "MasterCard",
        "cardAcceptorCity": "650-5434800 CA",
        "AVS": "NA NA",
        "cardAcceptorState": "",
        "cardAcceptorCountry": "RU",
        "localTransactionAmount": 5.0,
        "retrievalReferenceNumber": "406513423488"
    }
    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )
    sleep(1)
    assert response.status == 200
    assert response.text() == APPROVE_TRUE


@allure.title("Check currency code empty")
def test_check_currency_cod_empty(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,
        "currencyCode": " ",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
        "cardAcceptorMid": "420429000200589",
        "availableBalance": 499975.0,
        "cardAcceptorCity": "650-5434800 CA",
        "cardAcceptorName": "FACEBK 38TQEZB6W2",
        "cardAcceptorState": "",
        "cardAcceptorCountry": "RU",
        "localTransactionAmount": 5.0,
        "retrievalReferenceNumber": "406513423488",
        "localTransactionCurrencyCode": "840"
    }

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )
    sleep(1)
    assert response.status == 500
    assert response.status_text == 'Internal Server Error'


@allure.title("Check without currency code")
def test_without_currency_cod(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,

        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
        "cardAcceptorMid": "420429000200589",
        "availableBalance": 499975.0,
        "cardAcceptorCity": "650-5434800 CA",
        "cardAcceptorName": "FACEBK 38TQEZB6W2",
        "cardAcceptorState": "",
        "cardAcceptorCountry": "RU",
        "localTransactionAmount": 5.0,
        "retrievalReferenceNumber": "406513423488",
        "localTransactionCurrencyCode": "840"
    }

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )
    sleep(1)
    assert response.status == 200
    assert response.status_text == 'OK'


@allure.title("Check another method")
def test_check_another_method(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
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

    response = api_request_context.get(
        '/webhook/connexpay/auth', data=data
    )
    sleep(1)
    assert response.status == 405
    assert response.text() == '{"detail":"Method \\"GET\\" not allowed."}'


@allure.title("Check wrong endpoint")
def test_check_wrong_endpoint(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
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
        '/webhookk/connexpay', data=data
    )
    sleep(1)
    assert response.status == 404


@allure.title("Check short wrong endpoint")
def test_check_short_wrong_endpoint(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
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
        '/webhook/', data=data
    )
    sleep(1)
    assert response.status == 404


@allure.title("Check currency not available")
def test_currency_not_available(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
        "cardAcceptorMid": "420429000200589",
        "availableBalance": 499975.0,
        "cardAcceptorCity": "650-5434800 CA",
        "cardAcceptorName": "FACEBK 38TQEZB6W2",
        "cardAcceptorState": "",
        "cardAcceptorCountry": "KZ",
        "localTransactionAmount": 5.0,
        "retrievalReferenceNumber": "406513423488",
        "localTransactionCurrencyCode": "398"
    }

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )
    sleep(1)
    assert response.status == 200
    assert response.text() == '{"approved":false}'


@allure.title("Check currency not available usa")
def test_currency_not_available_usa(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
        "cardAcceptorMid": "420429000200589",
        "availableBalance": 499975.0,
        "cardAcceptorCity": "650-5434800 CA",
        "cardAcceptorName": "FACEBK 38TQEZB6W2",
        "cardAcceptorState": "",
        "cardAcceptorCountry": "USA",
        "localTransactionAmount": 5.0,
        "retrievalReferenceNumber": "406513423488",
        "localTransactionCurrencyCode": "840"
    }

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )
    sleep(1)
    assert response.status == 200
    assert response.text() == '{"approved":false}'


@allure.title("Check card acceptor empty")
def test_card_acceptor_empty(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
        "cardAcceptorMid": "420429000200589",
        "availableBalance": 499975.0,
        "cardAcceptorCity": "650-5434800 CA",
        "cardAcceptorName": "FACEBK 38TQEZB6W2",
        "cardAcceptorState": "",
        "cardAcceptorCountry": "",
        "localTransactionAmount": 5.0,
        "retrievalReferenceNumber": "406513423488",
        "localTransactionCurrencyCode": "840"
    }

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )
    sleep(1)
    assert response.status == 200
    assert response.text() == '{"approved":false}'


@allure.title("Check currency code is empty")
def test_currency_code_is_empty(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
        "cardAcceptorMid": "420429000200589",
        "availableBalance": 499975.0,
        "cardAcceptorCity": "650-5434800 CA",
        "cardAcceptorName": "FACEBK 38TQEZB6W2",
        "cardAcceptorState": "",
        "cardAcceptorCountry": "US",
        "localTransactionAmount": 5.0,
        "retrievalReferenceNumber": "406513423488",
        "localTransactionCurrencyCode": " "
    }

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )
    sleep(1)
    assert response.status == 200
    assert response.text() == '{"approved":false}'


@allure.title("Check long currency code")
def test_currency_code_long(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
        "cardAcceptorMid": "420429000200589",
        "availableBalance": 499975.0,
        "cardAcceptorCity": "650-5434800 CA",
        "cardAcceptorName": "FACEBK 38TQEZB6W2",
        "cardAcceptorState": "",
        "cardAcceptorCountry": "US",
        "localTransactionAmount": 5.0,
        "retrievalReferenceNumber": "406513423488",
        "localTransactionCurrencyCode": "9780"
    }

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )
    sleep(1)
    assert response.status == 200
    assert response.text() == '{"approved":false}'


@allure.title("Check short currency code")
def test_currency_code_short(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
        "cardAcceptorMid": "420429000200589",
        "availableBalance": 499975.0,
        "cardAcceptorCity": "650-5434800 CA",
        "cardAcceptorName": "FACEBK 38TQEZB6W2",
        "cardAcceptorState": "",
        "cardAcceptorCountry": "US",
        "localTransactionAmount": 5.0,
        "retrievalReferenceNumber": "406513423488",
        "localTransactionCurrencyCode": "9"
    }

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )
    sleep(1)
    assert response.status == 200
    assert response.text() == '{"approved":false}'


@allure.title("Check currency code is not available")
def test_us_currency_code_not_available(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
        "cardAcceptorMid": "420429000200589",
        "availableBalance": 499975.0,
        "cardAcceptorCity": "650-5434800 CA",
        "cardAcceptorName": "FACEBK 38TQEZB6W2",
        "cardAcceptorState": "",
        "cardAcceptorCountry": "US",
        "localTransactionAmount": 5.0,
        "retrievalReferenceNumber": "406513423488",
        "localTransactionCurrencyCode": "398"
    }

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )
    sleep(1)
    assert response.status == 200
    assert response.text() == '{"approved":false}'


@allure.title("Check card acceptor is not available")
def test_card_acceptor_not_available(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
        "cardAcceptorMid": "420429000200589",
        "availableBalance": 499975.0,
        "cardAcceptorCity": "650-5434800 CA",
        "cardAcceptorName": "FACEBK 38TQEZB6W2",
        "cardAcceptorState": "",
        "cardAcceptorCountry": "EE",
        "localTransactionAmount": 5.0,
        "retrievalReferenceNumber": "406513423488",
        "localTransactionCurrencyCode": "840"
    }

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )
    sleep(1)
    assert response.status == 200
    assert response.text() == '{"approved":false}'


@allure.title("Check merchant is not allowed")
def test_merchant_not_allowed(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
        "cardAcceptorMid": "527021000200586",
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
    sleep(1)
    assert response.status == 200
    assert response.text() == '{"approved":false}'


@allure.title("Check merchant is empty")
def test_merchant_is_empty(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1.0,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": MC,
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": "7311",
        "cardAcceptorMid": "",
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
    sleep(1)
    assert response.status == 200
    assert response.text() == APPROVE_TRUE
