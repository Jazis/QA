import uuid

import allure
from playwright.sync_api import APIRequestContext

from api.function_api import api_post_with_auth, api_post, api_post_pending_with_auth, api_request
from data.input_data.data_card import DECLINED, COUNTRY_GB, CURRENCY_USD, COUNTRY_US, PENDING, SETTLED, REVERSAL, REFUND, \
    CURRENCY_EUR, PENDING_REFUND, REVERSAL_EXPIRATION
from data.input_data.decline_reasons import APPROVED_SUCCES
from data.input_data.random_data import generate_random_float
from data.input_data.users import USER_RUBY_ROSE
from data.responses_texts import APPROVE_TRUE
from test.test_transactions.conftest import api_request_context, auth_token, CARD_LIMIT_DAY, send_auth


@allure.title("Transaction declined check status, daily")
def test_with_card_daily_decline_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response.status == 200
    response_json = response.json()
    id_before = response_json["results"]["data"][0]["id"]
    sum_before = response_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    api_post(api_request_context, n, CARD_LIMIT_DAY, DECLINED, COUNTRY_GB, CURRENCY_USD)

    response_after = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )

    assert response_after.status == 200
    response_json_after = response_after.json()
    id_after = response_json_after["results"]["data"][0]["id"]
    sum_after = response_json_after["results"]["data"][0]["amount"]
    status = response_json_after["results"]["data"][0]["status"]
    assert id_before < id_after
    assert sum_before != sum_after
    assert status == 'declined'


@allure.title("Transaction auth + declined check status, daily")
def test_with_card_daily_auth_decline_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response.status == 200
    response_json = response.json()
    id_before = response_json["results"]["data"][0]["id"]
    sum_before = response_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    auth = send_auth(api_request_context, n, CARD_LIMIT_DAY, '7311')

    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, DECLINED, COUNTRY_US, CURRENCY_USD)

    response_after = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_after.status == 200
    response_json_after = response_after.json()
    id_after = response_json_after["results"]["data"][0]["id"]
    sum_after = response_json_after["results"]["data"][0]["amount"]
    status = response_json_after["results"]["data"][0]["status"]
    assert id_before < id_after
    assert sum_before != sum_after
    assert status == 'declined'


@allure.title("Transaction auth + pending + settled check status, daily")
def test_with_card_daily_auth_pending_settled_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response.status == 200
    response_json = response.json()
    id_before = response_json["results"]["data"][0]["id"]
    sum_before = response_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    auth = send_auth(api_request_context, n, CARD_LIMIT_DAY, '7311')

    api_post_pending_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, PENDING, COUNTRY_US, CURRENCY_USD)

    response_pending = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_pending.status == 200
    response_json_pending = response_pending.json()
    id_pending = response_json_pending["results"]["data"][0]["id"]
    sum_pending = response_json_pending["results"]["data"][0]["amount"]
    status = response_json_pending["results"]["data"][0]["status"]
    assert id_before < id_pending
    assert sum_before != sum_pending
    assert status == 'pending'

    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, SETTLED, COUNTRY_US, CURRENCY_USD)

    response_settled = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_settled.status == 200
    response_json_settled = response_settled.json()
    id_settled = response_json_settled["results"]["data"][0]["id"]
    sum_settled = response_json_settled["results"]["data"][0]["amount"]
    status_settled = response_json_settled["results"]["data"][0]["status"]
    assert id_pending == id_settled
    assert sum_pending == sum_settled
    assert status_settled == 'settled'


@allure.title("Transaction auth + pending + reversed check status, daily")
def test_with_card_daily_auth_pending_reversed_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response.status == 200
    response_json = response.json()
    id_before = response_json["results"]["data"][0]["id"]
    sum_before = response_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    auth = send_auth(api_request_context, n, CARD_LIMIT_DAY, '7311')

    api_post_pending_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, PENDING, COUNTRY_US, CURRENCY_USD)

    response_pending = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_pending.status == 200
    response_json_pending = response_pending.json()
    id_pending = response_json_pending["results"]["data"][0]["id"]
    sum_pending = response_json_pending["results"]["data"][0]["amount"]
    status = response_json_pending["results"]["data"][0]["status"]
    assert id_before < id_pending
    assert sum_before != sum_pending
    assert status == 'pending'

    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, REVERSAL, COUNTRY_US, CURRENCY_USD)

    response_reversal = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_reversal.status == 200
    response_json_reversal = response_reversal.json()
    id_reversal = response_json_reversal["results"]["data"][0]["id"]
    sum_reversal = response_json_reversal["results"]["data"][0]["amount"]
    status_reversal = response_json_reversal["results"]["data"][0]["status"]
    assert id_pending == id_reversal
    assert sum_pending == sum_reversal
    assert status_reversal == 'reversed'


@allure.title("Transaction auth + pending + settled + refund check status, daily")
def test_with_card_daily_auth_pending_settled_refund_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response.status == 200
    response_json = response.json()
    id_before = response_json["results"]["data"][0]["id"]
    sum_before = response_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    auth = send_auth(api_request_context, n, CARD_LIMIT_DAY, '7311')
    api_post_pending_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, PENDING, COUNTRY_GB, CURRENCY_USD)

    response_pending = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_pending.status == 200
    response_json_pending = response_pending.json()
    id_pending = response_json_pending["results"]["data"][0]["id"]
    sum_pending = response_json_pending["results"]["data"][0]["amount"]
    status = response_json_pending["results"]["data"][0]["status"]
    assert id_before < id_pending
    assert sum_before != sum_pending
    assert status == 'pending'

    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, SETTLED, COUNTRY_GB, CURRENCY_USD)

    response_settled = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_settled.status == 200
    response_json_settled = response_settled.json()
    id_settled = response_json_settled["results"]["data"][0]["id"]
    sum_settled = response_json_settled["results"]["data"][0]["amount"]
    status_settled = response_json_settled["results"]["data"][0]["status"]
    assert id_pending == id_settled
    assert sum_pending == sum_settled
    assert status_settled == 'settled'

    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, REFUND, COUNTRY_GB, CURRENCY_USD)

    response_refund = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_refund.ok
    response_json_refund = response_refund.json()
    id_refund = response_json_refund["results"]["data"][0]["id"]
    sum_refund = response_json_refund["results"]["data"][0]["amount"]
    status_refund = response_json_refund["results"]["data"][0]["status"]
    assert id_refund > id_settled
    assert sum_refund == sum_settled
    assert status_refund == 'refund'


@allure.title("Transaction only auth, daily")
def test_with_card_daily_auth(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response.status == 200
    response_json = response.json()
    id_before = response_json["results"]["data"][0]["id"]
    sum_before = response_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    send_auth(api_request_context, n, CARD_LIMIT_DAY, '7311')

    response_after = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_after.status == 200
    response_json_after = response_after.json()
    id_after = response_json_after["results"]["data"][0]["id"]
    sum_after = response_json_after["results"]["data"][0]["amount"]
    assert id_before == id_after
    assert sum_before == sum_after


@allure.title("Transaction only settled check status, daily")
def test_with_card_daily_settled_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response.status == 200
    response_json = response.json()
    id_before = response_json["results"]["data"][0]["id"]
    sum_before = response_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    api_request(api_request_context, n, CARD_LIMIT_DAY, APPROVED_SUCCES, SETTLED, COUNTRY_GB, CURRENCY_USD)

    response_settled = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_settled.ok
    response_settled_json = response_settled.json()
    id_settled = response_settled_json["results"]["data"][0]["id"]
    sum_settled = response_settled_json["results"]["data"][0]["amount"]
    status = response_settled_json["results"]["data"][0]["status"]
    assert id_before < id_settled
    assert sum_before != sum_settled
    assert status == 'settled'


@allure.title("Transaction auth settled check status, daily")
def test_with_card_daily_auth_settled_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response.status == 200
    response_json = response.json()
    id_before = response_json["results"]["data"][0]["id"]
    sum_before = response_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    auth = send_auth(api_request_context, n, CARD_LIMIT_DAY, '7311')
    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, SETTLED, COUNTRY_GB, CURRENCY_EUR)

    response_settled = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_settled.status == 200
    response_settled_json = response_settled.json()
    id_settled = response_settled_json["results"]["data"][0]["id"]
    sum_settled = response_settled_json["results"]["data"][0]["amount"]
    status = response_settled_json["results"]["data"][0]["status"]
    assert id_before < id_settled
    assert sum_before != sum_settled
    assert status == 'settled'


@allure.title("Transaction auth pending check status, daily")
def test_with_card_daily_auth_pending_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response.status == 200
    response_json = response.json()
    id_before = response_json["results"]["data"][0]["id"]
    sum_before = response_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    auth = send_auth(api_request_context, n, CARD_LIMIT_DAY, '7311')
    api_post_pending_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, PENDING, COUNTRY_GB, CURRENCY_USD)

    response_pending = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_pending.status == 200
    response_json_pending = response_pending.json()
    id_pending = response_json_pending["results"]["data"][0]["id"]
    sum_pending = response_json_pending["results"]["data"][0]["amount"]
    status = response_json_pending["results"]["data"][0]["status"]
    assert id_before < id_pending
    assert sum_before != sum_pending
    assert status == 'pending'


@allure.title("Transaction auth reversed check status, daily")
def test_with_card_daily_auth_reversed_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response.status == 200
    response_before = response.json()
    id_before = response_before["results"]["data"][0]["id"]
    sum_before = response_before["results"]["data"][0]["amount"]
    n = generate_random_float()

    auth = send_auth(api_request_context, n, CARD_LIMIT_DAY, '7311')
    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, REVERSAL, COUNTRY_US, CURRENCY_USD)

    response_reversal = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_reversal.ok
    response_reversal_json = response_reversal.json()
    id_reversal = response_reversal_json["results"]["data"][0]["id"]
    sum_reversal = response_reversal_json["results"]["data"][0]["id"]
    status = response_reversal_json["results"]["data"][0]["status"]
    assert id_before < id_reversal
    assert sum_before != sum_reversal
    assert status == 'reversed'


@allure.title("Transaction auth pending refund check status, daily")
def test_with_card_daily_auth_pending_refund_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response_before = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_before.status == 200
    response_before_json = response_before.json()
    id_before = response_before_json["results"]["data"][0]["id"]
    sum_before = response_before_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    auth = send_auth(api_request_context, n, CARD_LIMIT_DAY, '7311')
    api_post_pending_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, PENDING, COUNTRY_GB, CURRENCY_USD)

    response_pending = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_pending.status == 200
    response_pending_json = response_pending.json()
    id_pending = response_pending_json["results"]["data"][0]["id"]
    sum_pending = response_pending_json["results"]["data"][0]["amount"]
    status_pending = response_pending_json["results"]["data"][0]["status"]
    assert id_before < id_pending
    assert sum_before != sum_pending
    assert status_pending == 'pending'

    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, REFUND, COUNTRY_GB, CURRENCY_USD)

    response_refund = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_refund.status == 200
    response_refund_json = response_refund.json()
    id_refund = response_refund_json["results"]["data"][1]["id"]
    sum_refund = response_refund_json["results"]["data"][1]["amount"]
    status_refund = response_refund_json["results"]["data"][1]["status"]
    assert id_pending < id_refund
    assert sum_pending == sum_refund
    assert status_refund == 'refund'


@allure.title("Transaction decline + auth check status, daily")
def test_with_card_daily_decline_auth_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)
    id = str(uuid.uuid4())

    headers = {
        'Authorization': f"Token {token}"
    }
    response_before = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_before.status == 200
    response_before_json = response_before.json()
    id_before = response_before_json["results"]["data"][0]["id"]
    sum_before = response_before_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    data = {
        "id": str(uuid.uuid4()),
        "data": {
            "amount": n,
            "idCard": 43359548,
            "network": "Master Card",
            "authCode": "5JWMZM",
            "cardGuid": CARD_LIMIT_DAY,
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
            "cardAcceptorCountry": "GB",
            "authorizationCurrencyCode": "EUR",
            "precedingRelatedToken": id
        },
        "subject": "14e92235-7a12-4301-a36b-5cf00f510b14",
        "eventTime": "2023-09-26T14:45:43.1054533Z",
        "eventType": DECLINED,
        "dataVersion": "1"
    }
    auth_data = api_request_context.post('/webhook/connexpay', data=data)
    assert auth_data.status == 200

    data = {
        "AVS": "NA NA",
        "amount": n,
        "network": "MasterCard",
        "CVVMatch": True,
        "authType": "Auth",
        "cardGuid": CARD_LIMIT_DAY,
        "currencyCode": "840",
        "transactionId": id,
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

    response_after = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_after.ok
    response_after_json = response_after.json()
    id_after = response_after_json["results"]["data"][0]["id"]
    sum_after = response_after_json["results"]["data"][0]["amount"]
    status = response_after_json["results"]["data"][0]["status"]
    assert id_before < id_after
    assert sum_before != sum_after
    assert status == 'declined'


@allure.title("Transaction auth + settled + pending check status, daily")
def test_with_card_daily_auth_settled_pending_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response_before = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_before.status == 200
    response_before_json = response_before.json()
    id_before = response_before_json["results"]["data"][0]["id"]
    sum_before = response_before_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    auth = send_auth(api_request_context, n, CARD_LIMIT_DAY, '7311')
    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, SETTLED, COUNTRY_GB, CURRENCY_USD)

    response_settled = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_settled.status == 200
    response_settled_json = response_settled.json()
    id_settled = response_settled_json["results"]["data"][0]["id"]
    sum_settled = response_settled_json["results"]["data"][0]["amount"]
    status_settled = response_settled_json["results"]["data"][0]["status"]
    assert id_before < id_settled
    assert sum_before != sum_settled
    assert status_settled == 'settled'

    api_post_pending_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, PENDING, COUNTRY_GB, CURRENCY_USD)

    response_pending = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_pending.status == 200
    response_pending_json = response_pending.json()
    id_pending = response_pending_json["results"]["data"][0]["id"]
    sum_pending = response_pending_json["results"]["data"][0]["amount"]
    status_pending = response_pending_json["results"]["data"][0]["status"]
    assert id_pending == id_settled
    assert sum_pending == sum_settled
    assert status_pending == status_settled


@allure.title("Transaction auth + reversed + pending check status, daily")
def test_with_card_daily_auth_reversed_pending_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response_before = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_before.status == 200
    response_before_json = response_before.json()
    id_before = response_before_json["results"]["data"][0]["id"]
    sum_before = response_before_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    auth = send_auth(api_request_context, n, CARD_LIMIT_DAY, '7311')
    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, REVERSAL, COUNTRY_GB, CURRENCY_USD)

    response_reversed = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_reversed.status == 200
    response_reversed_json = response_reversed.json()
    id_reversed = response_reversed_json["results"]["data"][0]["id"]
    sum_reversed = response_reversed_json["results"]["data"][0]["amount"]
    status_reversed = response_reversed_json["results"]["data"][0]["status"]
    assert id_before < id_reversed
    assert sum_before != sum_reversed
    assert status_reversed == 'reversed'

    api_post_pending_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, PENDING, COUNTRY_GB, CURRENCY_USD)

    response_pending = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_pending.status == 200
    response_pending_json = response_pending.json()
    id_pending = response_pending_json["results"]["data"][0]["id"]
    sum_pending = response_pending_json["results"]["data"][0]["amount"]
    status_pending = response_pending_json["results"]["data"][0]["status"]
    assert id_reversed == id_pending
    assert sum_reversed == sum_pending
    assert status_pending == status_reversed


@allure.title("Transaction auth + pending + refund + settled check status, daily")
def test_with_card_daily_auth_pending_refund_settled_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response_before = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_before.status == 200
    response_before_json = response_before.json()
    id_before = response_before_json["results"]["data"][0]["id"]
    sum_before = response_before_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    auth = send_auth(api_request_context, n, CARD_LIMIT_DAY, '7311')
    api_post_pending_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, PENDING, COUNTRY_GB, CURRENCY_EUR)

    response_pending = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_pending.ok
    response_pending_json = response_pending.json()
    id_pending = response_pending_json["results"]["data"][0]["id"]
    sum_pending = response_pending_json["results"]["data"][0]["amount"]
    status_pending = response_pending_json["results"]["data"][0]["status"]
    assert id_before < id_pending
    assert sum_before != sum_pending
    assert status_pending == 'pending'

    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, REFUND, COUNTRY_GB, CURRENCY_EUR)

    response_refund = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_refund.ok
    response_refund_json = response_refund.json()
    id_refund = response_refund_json["results"]["data"][1]["id"]
    sum_refund = response_refund_json["results"]["data"][1]["amount"]
    status_refund = response_refund_json["results"]["data"][1]["status"]
    assert id_pending < id_refund
    assert sum_pending == sum_refund
    assert status_refund == 'refund'

    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, SETTLED, COUNTRY_GB, CURRENCY_EUR)

    response_settled = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_settled.ok
    response_settled_json = response_settled.json()
    id_settled = response_settled_json["results"]["data"][0]["id"]
    sum_settled = response_settled_json["results"]["data"][0]["amount"]
    status_settled = response_settled_json["results"]["data"][0]["status"]
    assert id_pending == id_settled
    assert sum_pending == sum_settled
    assert status_settled == 'settled'


@allure.title("Transaction auth + pending + reversed + settled check status, daily")
def test_with_card_daily_auth_pending_reversed_settled_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response_before = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_before.status == 200
    response_before_json = response_before.json()
    id_before = response_before_json["results"]["data"][0]["id"]
    sum_before = response_before_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    auth = send_auth(api_request_context, n, CARD_LIMIT_DAY, '7311')
    api_post_pending_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, PENDING, COUNTRY_GB, CURRENCY_EUR)

    response_pending = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_pending.ok
    response_pending_json = response_pending.json()
    id_pending = response_pending_json["results"]["data"][0]["id"]
    sum_pending = response_pending_json["results"]["data"][0]["amount"]
    status_pending = response_pending_json["results"]["data"][0]["status"]
    assert id_before < id_pending
    assert sum_before != sum_pending
    assert status_pending == 'pending'

    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, REVERSAL, COUNTRY_GB, CURRENCY_EUR)

    response_reversed = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_reversed.ok
    response_reversed_json = response_reversed.json()
    id_reversed = response_reversed_json["results"]["data"][0]["id"]
    sum_reversed = response_reversed_json["results"]["data"][0]["amount"]
    status_reversed = response_reversed_json["results"]["data"][0]["status"]
    assert id_pending == id_reversed
    assert sum_pending == sum_reversed
    assert status_reversed == 'reversed'

    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, SETTLED, COUNTRY_GB, CURRENCY_EUR)

    response_settled = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_settled.ok
    response_settled_json = response_settled.json()
    id_settled = response_settled_json["results"]["data"][0]["id"]
    sum_settled = response_settled_json["results"]["data"][0]["amount"]
    status_settled = response_settled_json["results"]["data"][0]["status"]
    assert id_reversed == id_settled
    assert sum_reversed == sum_settled
    assert status_settled == 'settled'


@allure.title("Transaction auth + pending + settled + reversed check status, daily")
def test_with_card_daily_auth_pending_settled_reversed_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response_before = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_before.status == 200
    response_before_json = response_before.json()
    id_before = response_before_json["results"]["data"][0]["id"]
    sum_before = response_before_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    auth = send_auth(api_request_context, n, CARD_LIMIT_DAY, '7311')
    api_post_pending_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, PENDING, COUNTRY_US, CURRENCY_EUR)

    response_pending = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_pending.ok
    response_pending_json = response_pending.json()
    id_pending = response_pending_json["results"]["data"][0]["id"]
    sum_pending = response_pending_json["results"]["data"][0]["amount"]
    status_pending = response_pending_json["results"]["data"][0]["status"]
    assert id_before < id_pending
    assert sum_before != sum_pending
    assert status_pending == 'pending'

    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, SETTLED, COUNTRY_US, CURRENCY_EUR)

    response_settled = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_settled.ok
    response_settled_json = response_settled.json()
    id_settled = response_settled_json["results"]["data"][0]["id"]
    sum_settled = response_settled_json["results"]["data"][0]["amount"]
    status_settled = response_settled_json["results"]["data"][0]["status"]
    assert id_pending == id_settled
    assert sum_pending == sum_settled
    assert status_settled == 'settled'

    response_balance_before = api_request_context.get('/api/cash/accounts', headers=headers)
    assert response_balance_before.ok

    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, REVERSAL, COUNTRY_US, CURRENCY_EUR)

    response_reversal = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_reversal.ok
    response_reversal_json = response_reversal.json()
    id_reversal = response_reversal_json["results"]["data"][0]["id"]
    sum_reversal = response_reversal_json["results"]["data"][0]["amount"]
    status_reversal = response_reversal_json["results"]["data"][0]["status"]
    assert id_settled < id_reversal
    assert sum_settled == sum_reversal
    assert status_reversal == 'reversed'

    response_balance_after = api_request_context.get('/api/cash/accounts', headers=headers)
    assert response_balance_after.ok
    assert response_balance_before.text() == response_balance_after.text()


@allure.title("Transaction auth + pending + settled + reversed issue expiration check status, daily")
def test_with_card_daily_auth_pending_settled_reversed_issuerexpiration_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response_before = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_before.status == 200
    response_before_json = response_before.json()
    id_before = response_before_json["results"]["data"][0]["id"]
    sum_before = response_before_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    auth = send_auth(api_request_context, n, CARD_LIMIT_DAY, '7311')
    api_post_pending_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, PENDING, COUNTRY_US, CURRENCY_EUR)

    response_pending = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_pending.ok
    response_pending_json = response_pending.json()
    id_pending = response_pending_json["results"]["data"][0]["id"]
    sum_pending = response_pending_json["results"]["data"][0]["amount"]
    status_pending = response_pending_json["results"]["data"][0]["status"]
    assert id_before < id_pending
    assert sum_before != sum_pending
    assert status_pending == 'pending'

    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, SETTLED, COUNTRY_US, CURRENCY_EUR)

    response_settled = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_settled.ok
    response_settled_json = response_settled.json()
    id_settled = response_settled_json["results"]["data"][0]["id"]
    sum_settled = response_settled_json["results"]["data"][0]["amount"]
    status_settled = response_settled_json["results"]["data"][0]["status"]
    assert id_pending == id_settled
    assert sum_pending == sum_settled
    assert status_settled == 'settled'

    response_balance_before = api_request_context.get('/api/cash/accounts', headers=headers)
    assert response_balance_before.ok

    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, REVERSAL_EXPIRATION, COUNTRY_US, CURRENCY_EUR)

    response_reversal = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_reversal.ok
    response_reversal_json = response_reversal.json()
    id_reversal = response_reversal_json["results"]["data"][0]["id"]
    sum_reversal = response_reversal_json["results"]["data"][0]["amount"]
    status_reversal = response_reversal_json["results"]["data"][0]["status"]
    assert id_settled < id_reversal
    assert sum_settled == sum_reversal
    assert status_reversal == 'reversed'

    response_balance_after = api_request_context.get('/api/cash/accounts', headers=headers)
    assert response_balance_after.ok
    assert response_balance_before.text() == response_balance_after.text()


@allure.title("Transaction only refund, daily")
def test_with_card_daily_only_refund(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response_before = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_before.ok
    response_before_json = response_before.json()
    id_before = response_before_json["results"]["data"][0]["id"]
    sum_before = response_before_json["results"]["data"][0]["amount"]
    n = generate_random_float()

    api_request(api_request_context, n, CARD_LIMIT_DAY, APPROVED_SUCCES, REFUND, COUNTRY_US, CURRENCY_EUR)

    response_refund = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_refund.ok
    response_refund_json = response_refund.json()
    id_refund = response_refund_json["results"]["data"][0]["id"]
    sum_refund = response_refund_json["results"]["data"][0]["amount"]
    status = response_refund_json["results"]["data"][0]["status"]
    assert id_before < id_refund
    assert sum_before != sum_refund
    assert status == 'refund'


@allure.title("Transaction auth + pending + refund + reversed check status, daily")
def test_with_card_daily_auth_pending_refund_reversed_check_status(api_request_context: APIRequestContext) -> None:
    token = auth_token(api_request_context, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password)

    headers = {
        'Authorization': f"Token {token}"
    }
    response_before = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_before.status == 200
    response_before_json = response_before.json()
    id_before = response_before_json["results"]["data"][0]["id"]
    sum_before = response_before_json["results"]["data"][0]["amount"]
    n = 1

    auth = send_auth(api_request_context, n, CARD_LIMIT_DAY, '7311')
    api_post_pending_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, PENDING_REFUND, COUNTRY_US, CURRENCY_EUR)

    response_pending = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_pending.ok
    response_pending_json = response_pending.json()
    id_pending = response_pending_json["results"]["data"][0]["id"]
    sum_pending = response_pending_json["results"]["data"][0]["amount"]
    assert id_before == id_pending
    assert sum_before == sum_pending


    api_request(api_request_context, n, CARD_LIMIT_DAY, APPROVED_SUCCES, REFUND, COUNTRY_US, CURRENCY_EUR)

    response_refund = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_refund.ok
    response_refund_json = response_refund.json()
    id_refund = response_refund_json["results"]["data"][0]["id"]
    sum_refund = response_refund_json["results"]["data"][0]["amount"]
    status = response_refund_json["results"]["data"][0]["status"]
    assert id_pending != id_refund
    assert sum_pending != sum_refund
    assert status == 'refund'

    response_balance_before = api_request_context.get('/api/cash/accounts', headers=headers)
    assert response_balance_before.ok

    api_post_with_auth(api_request_context, auth, n, CARD_LIMIT_DAY, REVERSAL, COUNTRY_US, CURRENCY_EUR)

    response_reversal = api_request_context.get(
        '/api/transaction?card=492', headers=headers
    )
    assert response_reversal.ok
    response_reversal_json = response_reversal.json()
    id_reversal = response_reversal_json["results"]["data"][0]["id"]
    sum_reversal = response_reversal_json["results"]["data"][0]["amount"]
    status_reversal = response_reversal_json["results"]["data"][0]["status"]
    assert id_refund == id_reversal
    assert sum_refund == sum_reversal
    assert status_reversal == 'refund'

    response_balance_after = api_request_context.get('/api/cash/accounts', headers=headers)
    assert response_balance_after.ok
    assert response_balance_before.text() == response_balance_after.text()

