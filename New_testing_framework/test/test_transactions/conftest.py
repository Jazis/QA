import uuid
from typing import Generator

import pytest
from playwright.sync_api import APIRequestContext, Playwright, sync_playwright

from data.responses_texts import APPROVE_TRUE


def auth_token(api_request_context: APIRequestContext, user_name, user_pass) -> None:
    data = {
        "username": user_name,
        "password": user_pass
    }

    auth_login = api_request_context.post(
        '/auth/login', data=data
    )
    assert auth_login.ok
    auth_response = auth_login.json()

    token = auth_response['token']
    # print(f" var Token ^^ {token}")
    return token


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url='https://dev.api.devhost.io'
    )
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="session")
def playwright() -> Playwright:  # type: ignore
    with sync_playwright() as pw:
        yield pw


def send_auth(api_request_context: APIRequestContext, sum, card, mcc) -> None:
    data = {
        "AVS": "NA NA",
        "amount": sum,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": card,
        "currencyCode": "840",
        "transactionId": str(uuid.uuid4()),
        "cardAcceptorMcc": mcc,
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
    token_auth = data['transactionId']
    return token_auth


CARD_NO_LIMIT = '0c64dbb4-03b9-483f-98ff-fc24b9c8c11f'  #ruby rose #486

CARD_LIFETIME = '1ca94303-4cfc-4871-9c82-b41ec1ea3377' #ruby rose #7574

CARD_MONTHLY = 'ab00cfe6-009b-4f8c-bb43-c32731c8d3df' #ruby rose  4217

CARD_WEEKLY = '1169ac76-6b86-4bb5-8c03-583d6b6445e0'   # ruby rose 247

CARD_LIMIT_DAY = 'f402faa8-65d3-4dd5-974c-6a19a7951e04' # ruby rose 492