import uuid
from typing import Generator

import pytest
from playwright.sync_api import APIRequestContext, Playwright, sync_playwright

from data.input_data.users import USER_RESTRICTED_COMPANY
from data.responses_texts import APPROVE_TRUE


# User_ru cards
@pytest.fixture(scope="session")
def auth_token(api_request_context: APIRequestContext) -> None:
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

    # print(f" var Token ^^ {token}")
    return token


@pytest.fixture(scope="session")
def auth_token_black_company(api_request_context: APIRequestContext) -> None:
    data = {
        "username": "blackCompany@mail.ru",
        "password": "BLaCKCOMPAny2010"
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
def auth_login_user_data_ru(api_request_context: APIRequestContext) -> None:
    data = {
        "username": "rtuuyhgfytr45fghfh@yandex.ru",
        "password": "Hihu&hjghgf#hJKIUY&*bJHH"
    }

    auth_login = api_request_context.post(
        '/auth/login', data=data
    )
    assert auth_login.ok
    auth_response = auth_login.json()

    token = auth_response['token']
    return token


@pytest.fixture(scope="session")
def auth_login_user_restricted_company(api_request_context: APIRequestContext) -> None:
    data = {
        "username": USER_RESTRICTED_COMPANY.login,
        "password": USER_RESTRICTED_COMPANY.password
    }

    auth_login = api_request_context.post(
        '/auth/login', data=data
    )
    assert auth_login.ok
    auth_response = auth_login.json()

    token = auth_response['token']
    return token


@pytest.fixture(scope="session")
def auth_login_user_with_2fa(api_request_context: APIRequestContext) -> None:
    data = {
        "username": "goldenCompany@mail.ru",
        "password": "GOLDEN_company202020"
    }

    auth_login = api_request_context.post(
        '/auth/login', data=data
    )
    assert auth_login.ok
    auth_response = auth_login.json()

    token = auth_response['token']
    return token


@pytest.fixture(scope="session")
def send_auth_trans_mc(api_request_context: APIRequestContext) -> None:
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


@pytest.fixture(scope="session")
def send_auth_trans_visa(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 1,
        "network": "Visa",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": "fe1ed4f7-4d5e-42ce-b6b8-7b398e973b09",
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
    token_auth = data['transactionId']
    return token_auth


@pytest.fixture(scope="session")
@pytest.mark.usefixtures("api_request_context")
def send_auth_trans_user_limit(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 21.0,
        "network": "Visa",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": "563adf5f-5632-4412-8562-f65993db7191", #id = 459
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
    assert response.text() == '{"approved":false}'
    token = data['transactionId']
    return token


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url='https://dev.api.devhost.io'
    )
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="session")
@pytest.mark.usefixtures("api_request_context")
def send_auth_trans_user_limit_check(api_request_context: APIRequestContext) -> None:
    data = {
        "AVS": "NA NA",
        "amount": 200.0,
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

    response = api_request_context.post(
        '/webhook/connexpay/auth', data=data
    )
    assert response.ok
    assert response.text() == APPROVE_TRUE
    token = data['transactionId']
    return token

@pytest.fixture(scope="session")
def playwright() -> Playwright:  # type: ignore
    with sync_playwright() as pw:
        yield pw


VISA = "1c1d3e34-6665-4db8-8ad1-fa06b62b2bb8" #USER_UK
MC = "34a602eb-8b75-4e18-9ff5-ab01dc043ebf"  # USER_RU user's card id 440 (rtyhgf5643)
VISA_TEST = "8f6a5eca-6abe-48fe-8343-355d6c857ada"  #test do not change 170
VISA_TRANS = "971b65f4-d8de-40b6-876d-706dd9af24b1" # USER_RU user's card 8009
CARD_EMPLOYEE = "2aa8221f-9bdd-48da-a38d-089d15d19f83"
#"acada330-30d7-4aa6-8315-ccc2d8791b2e" Test Dashboard
# white "fe1ed4f7-4d5e-42ce-b6b8-7b398e973b09"