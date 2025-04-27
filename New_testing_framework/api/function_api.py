import uuid
from typing import Generator

import pytest
from playwright.sync_api import APIRequestContext, Playwright

from data.input_data.random_data import random_string
import json
from data.input_data.users import USER_01


def auth_token_function(request, api_request_context=None, username = None, password = None):
    api_request_context = request.getfixturevalue("api_request_context")
    data = {
        "username": username,
        "password": password
    }
    auth_login = api_request_context.post('/auth/login', data=data)
    assert auth_login.status == 200, "Authentication failed"
    auth_response = auth_login.json()

    token = auth_response['token']
    return token

# User_ru cards
@pytest.fixture(scope="session")
def auth_token(request, api_request_context: APIRequestContext) -> str:
    data = {
        "username": USER_01.login,
        "password": USER_01.password
    }
    auth_login = api_request_context.post('/auth/login', data=data)
    assert auth_login.status == 200, "Authentication failed"
    auth_response = auth_login.json()

    token = auth_response['token']
    return token


@pytest.fixture(scope="session")
def api_request_context(
        playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url='https://dev.api.devhost.io'
    )
    yield request_context
    request_context.dispose()


def api_post(api_request_context: APIRequestContext, sum, card, event, country, currency) -> None:
    data = {
        "id": str(uuid.uuid4()),
        "data": {
            "amount": sum,
            "idCard": 43359548,
            "network": "Master Card",
            "authCode": "5JWMZM",
            "cardGuid": card,
            "decisionBy": "Rize Ads",
            "authMessage": "Approved or completed successfully",
            "orderNumber": "lfkRqq",
            "currencyCode": "USD",
            "merchantName": "Rize Ads",
            "cardAcceptorMcc": "7311",
            "cardAcceptorMid": "420429000200589",
            "availableBalance": 499903.24,
            "cardAcceptorCity": "Menlo Park CA",
            "cardAcceptorName": "FACEBK ADS",
            "merchantIdentifier": "14e92235-7a12-4301-a36b-5cf00f590b14",
            "authorizationAmount": 2.0,
            "cardAcceptorCountry": country,
            "authorizationCurrencyCode": currency
        },
        "subject": "14e92235-7a12-4301-a36b-5cf00f510b14",
        "eventTime": "2023-09-26T14:45:43.1054533Z",
        "eventType": event,
        "dataVersion": "1"
    }

    auth_data = api_request_context.post('/webhook/connexpay', data=data)
    assert auth_data.status == 200


def api_request(api_request_context: APIRequestContext, sum, card, message, event, country, currency) -> None:
    data = {
        "id": str(uuid.uuid4()),
        "data": {
            "amount": sum,
            "idCard": 43359548,
            "network": "Master Card",
            "authCode": "5JWMZM",
            "cardGuid": card,
            "decisionBy": "Rize Ads",
            "authMessage": message,
            "orderNumber": "lfkRqq",
            "currencyCode": "USD",
            "merchantName": "Rize Ads",
            "cardAcceptorMcc": "7311",
            "cardAcceptorMid": "420429000200589",
            "availableBalance": 499903.24,
            "cardAcceptorCity": "Menlo Park CA",
            "cardAcceptorName": "FACEBK ADS",
            "merchantIdentifier": "14e92235-7a12-4301-a36b-5cf00f590b14",
            "authorizationAmount": 2.0,
            "cardAcceptorCountry": country,
            "authorizationCurrencyCode": currency
        },
        "subject": "14e92235-7a12-4301-a36b-5cf00f510b14",
        "eventTime": "2023-09-26T14:45:43.1054533Z",
        "eventType": event,
        "dataVersion": "1"
    }

    response = api_request_context.post('/webhook/connexpay', data=data)
    assert response.status == 200
    assert response.text() == '"OK"'


def api_request_with_available_balance(api_request_context: APIRequestContext, sum, card, message, event, country, currency, balance) -> None:
    data = {
        "id": str(uuid.uuid4()),
        "data": {
            "amount": sum,
            "idCard": 43359548,
            "network": "Master Card",
            "authCode": "5JWMZM",
            "cardGuid": card,
            "decisionBy": "Rize Ads",
            "authMessage": message,
            "orderNumber": "lfkRqq",
            "currencyCode": "USD",
            "merchantName": "Rize Ads",
            "cardAcceptorMcc": "7311",
            "cardAcceptorMid": "420429000200589",
            "availableBalance": balance,
            "cardAcceptorCity": "Menlo Park CA",
            "cardAcceptorName": "FACEBK ADS",
            "merchantIdentifier": "14e92235-7a12-4301-a36b-5cf00f590b14",
            "authorizationAmount": 2.0,
            "cardAcceptorCountry": country,
            "authorizationCurrencyCode": currency
        },
        "subject": "14e92235-7a12-4301-a36b-5cf00f510b14",
        "eventTime": "2023-09-26T14:45:43.1054533Z",
        "eventType": event,
        "dataVersion": "1"
    }

    response = api_request_context.post('/webhook/connexpay', data=data)
    assert response.status == 200
    assert response.text() == '"OK"'

###авторизация
def api_post_auth_trans(api_request_context: APIRequestContext, sum, card, text) -> None:
    data = {
        "AVS": "NA NA",
        "amount": sum,
        "network": "Visa",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": card,  # "2aa8221f-9bdd-48da-a38d-089d15d19f83",
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
    assert response.text() == text
    token = data['transactionId']
    return token


def api_post_pending_with_auth(api_request_context: APIRequestContext, token, sum, card, event, country,
                               currency) -> None:
    data = {
        "id": token,
        "data": {
            "amount": sum,
            "idCard": 43359548,
            "network": "Master Card",
            "authCode": "5JWMZM",
            "cardGuid": card,
            "decisionBy": "Rize Ads",
            "authMessage": "Approved or completed successfully",
            "orderNumber": "lfkRqq",
            "currencyCode": "USD",
            "merchantName": "Rize Ads",
            "cardAcceptorMcc": "7311",
            "cardAcceptorMid": "420429000200589",
            "availableBalance": 499903.24,
            "cardAcceptorCity": "Menlo Park CA",
            "cardAcceptorName": "FACEBK ADS",
            "merchantIdentifier": "14e92235-7a12-4301-a36b-5cf00f590b14",
            "authorizationAmount": 2.0,
            "cardAcceptorCountry": country,
            "authorizationCurrencyCode": currency
        },
        "subject": "14e92235-7a12-4301-a36b-5cf00f510b14",
        "eventTime": "2023-09-26T14:45:43.1054533Z",
        "eventType": event,
        "dataVersion": "1"
    }
    auth_data = api_request_context.post('/webhook/connexpay', data=data)
    assert auth_data.status == 200


def api_post_with_auth(api_request_context: APIRequestContext, token, sum, card, event, country, currency) -> None:
    data = {
        "id": str(uuid.uuid4()),
        "data": {
            "amount": sum,
            "idCard": 43359548,
            "network": "Master Card",
            "authCode": "5JWMZM",
            "cardGuid": card,
            "decisionBy": "Rize Ads",
            "authMessage": "Approved or completed successfully",
            "orderNumber": "lfkRqq",
            "currencyCode": "USD",
            "merchantName": "Rize Ads",
            "cardAcceptorMcc": "7311",
            "cardAcceptorMid": "420429000200589",
            "availableBalance": 499903.24,
            "cardAcceptorCity": "Menlo Park CA",
            "cardAcceptorName": "FACEBK ADS",
            "merchantIdentifier": "14e92235-7a12-4301-a36b-5cf00f590b14",
            "authorizationAmount": 2.0,
            "cardAcceptorCountry": country,
            "authorizationCurrencyCode": currency,
            "precedingRelatedToken": token
        },
        "subject": "14e92235-7a12-4301-a36b-5cf00f510b14",
        "eventTime": "2023-09-26T14:45:43.1054533Z",
        "eventType": event,
        "dataVersion": "1"
    }
    auth_data = api_request_context.post('/webhook/connexpay', data=data)
    assert auth_data.status == 200


def api_delete_invitation_user(auth_token, api_request_context: APIRequestContext, email) -> None:
    token = auth_token(api_request_context)
    headers = {
        'Authorization': f"Token {token}"
    }
    data = {
        "email": email
    }
    response = api_request_context.delete('/auth/account', headers=headers, data=data)

    assert response.status == 200
    assert response.text() == '{"status":"Invite and email deleted"}'


def api_create_company(api_request_context: APIRequestContext, name: object) -> None:
    data = {
        "email": random_string(7) + '@gmail.com',
        "password": random_string(8),
        "first_name": random_string(6),
        "last_name": random_string(4),
        "company_name": name,
        "telegram": "@telegram",
        "ga_id": random_string(4),
        "recaptcha": random_string(5),
        "answers": [
            1, 2, 3, 4, 5, 6, 9, 13
        ],
        "locale": "en-GB",
        "timezone": "UTC+03:3"
    }

    response = api_request_context.post(
        '/auth/onboarding', data=data
    )

    assert response.status == 201
    assert response.text().__contains__("token")


def api_move_money(api_request_context: APIRequestContext, amount, from_acc, to_acc, operation) -> None:
    data = {
        "username": "admin@admin.com",
        "password": "vnLmdAxGAa4ZPeA6"
    }

    auth_login = api_request_context.post(
        '/auth/login', data=data
    )
    assert auth_login.ok
    auth_response = auth_login.json()

    token = auth_response['token']

    headers = {'Authorization': f"Token {token}"}

    data_deposit = {
        "amount": amount, "from_account": from_acc, "to_account": to_acc, "operation": operation
    }
    response = api_request_context.post(
        '/api/admin/move_money', headers=headers, data=data_deposit
    )
    assert response.status == 200


def api_set_limit(api_request_context: APIRequestContext, login, password, id_card, limit_amount, limit) -> None:
    data = {
        "username": login,
        "password": password
    }

    auth_login = api_request_context.post(
        '/auth/login', data=data
    )
    assert auth_login.ok
    auth_response = auth_login.json()

    token = auth_response['token']

    headers = {'Authorization': f"Token {token}"}
    data_card = {
        "id": id_card, "limit_amount": limit_amount, "limit": limit
    }
    response = api_request_context.put(
        '/api/card', headers=headers, data=data_card
    )
    assert response.status == 200

def validate_json_keys(response = None, json_data = None):
    """
    Проверяет, содержит ли JSON-объект необходимые ключи.
    
    :param json_data: строка JSON или словарь
    :param resp_keys: список обязательных ключей, если None - используются все ключи из json_data
    :return: (bool, list) - True и пустой список, если все ключи есть, иначе False и список отсутствующих ключей
    """
    resp_keys = list(json.loads(response).keys())
    data_keys = list(json.loads(json_data).keys())
    if len(resp_keys) < 1:
        return False
    try:
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        
        if not isinstance(json_data, dict):
            raise ValueError("Данные должны быть словарем или корректной строкой JSON")
        
        # if resp_keys is None:
        #     resp_keys = list(resp_keys.keys())

        # json_str = json.dumps(json_data)
    
        for word in data_keys:
            if f"\"{word}\"" not in response:
                return False
        return True
    except (json.JSONDecodeError, ValueError) as e:
        print([str(e)])
        return False

