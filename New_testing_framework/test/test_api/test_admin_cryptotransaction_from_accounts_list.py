import allure
from playwright.sync_api import APIRequestContext


@allure.title('Admin crypto transaction from accounts list filter by operation type & provider Deposit')
def test_admin_crypto_transaction_from_accounts_list_deposit(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction/from_accounts?operation=deposit&provider=2', headers=headers
    )
    assert response.status == 200
    assert response.json()[0]['id'] == 11
    assert response.json()[0]['name'] == 'Main – ConnexPay'
    assert response.json()[0]['number'] == '2000011'
    assert response.json()[0]['provider'] == 2
    assert response.json()[0]["company_id"] is None
    assert response.json()[0]["owner_type"] == "own"


@allure.title('Admin crypto transaction from accounts list filter by operation type & provider Withdrawal')
def test_admin_crypto_transaction_from_accounts_list_withdrawal(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction/from_accounts?operation=withdrawal&provider=2', headers=headers
    )
    assert response.status == 200
    assert response.text().__contains__('{"id":138,"name":"test do not change","number":"1018850","balance":1004.65,"company_id":129,"provider":2,"owner_type":"client"}')


@allure.title('Admin crypto transaction from accounts list filter by operation type & provider Credit Issue')
def test_admin_crypto_transaction_from_accounts_list_credit_issue(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/cryptotransaction/from_accounts?operation=credit_issue&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.json()[0]["id"] == 18
    assert response.json()[0]["name"] == "Credit – ConnexPay"
    assert response.json()[0]["number"] == "2000018"
    assert response.json()[0]["provider"] == 2
    assert response.json()[0]["company_id"] is None
    assert response.json()[0]["owner_type"] == "own"


@allure.title('Admin crypto transaction from accounts list filter by operation type & provider Credit Issue Wire')
def test_admin_crypto_transaction_from_accounts_list_credit_issue_wire(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/cryptotransaction/from_accounts?operation=credit_issue_wire&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.json()[0]["id"] == 18
    assert response.json()[0]["name"] == "Credit – ConnexPay"
    assert response.json()[0]["number"] == "2000018"
    assert response.json()[0]["provider"] == 2
    assert response.json()[0]["company_id"] is None
    assert response.json()[0]["owner_type"] == "own"


@allure.title('Admin crypto transaction from accounts list filter by operation type & provider Сredit Сlear')
def test_admin_crypto_transaction_from_accounts_list_credit_clear(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/cryptotransaction/from_accounts?operation=credit_clear&provider=2', headers=headers
    )

    assert response.json()[1]["id"] == 11
    assert response.json()[1]["name"] == "Main – ConnexPay"
    assert response.json()[1]["number"] == "2000011"
    assert response.json()[1]["provider"] == 2
    assert response.json()[1]["company_id"] is None
    assert response.json()[1]["owner_type"] == "own"

    assert response.json()[0]["id"] == 500
    assert response.json()[0]["name"] == "Netting – ConnexPay"
    assert response.json()[0]["number"] == "20000xx"
    assert response.json()[0]["provider"] == 2
    assert response.json()[0]["company_id"] is None
    assert response.json()[0]["owner_type"] == "own"


@allure.title('Admin crypto transaction from accounts list filter by operation type & provider Subscription')
def test_admin_crypto_transaction_from_accounts_list_subscription(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/cryptotransaction/from_accounts?operation=subscription&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('{"id":138,"name":"test do not change","number":"1018850","balance":1004.65,"company_id":129,"provider":2,"owner_type":"client"}')


@allure.title('Admin crypto transaction from accounts list filter by operation type & provider Money Outbound')
def test_admin_crypto_transaction_from_accounts_list_money_outbound(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/cryptotransaction/from_accounts?operation=money_outbound&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.json()[0]["id"] == 17
    assert response.json()[0]["name"] == "Fee – ConnexPay"
    assert response.json()[0]["number"] == "2000017"
    assert response.json()[0]["provider"] == 2
    assert response.json()[0]["company_id"] is None
    assert response.json()[0]["owner_type"] == "own"


@allure.title('Admin crypto transaction from accounts list filter by operation type & Revenue to main')
def test_admin_crypto_transaction_from_accounts_list_revenue_to_main(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/cryptotransaction/from_accounts?operation=revenue_to_main&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.json()[0]["id"] == 19
    assert response.json()[0]["name"] == "Revenue – ConnexPay"
    assert response.json()[0]["number"] == "2000019"
    assert response.json()[0]["provider"] == 2
    assert response.json()[0]["company_id"] is None
    assert response.json()[0]["owner_type"] == "own"


@allure.title('Admin crypto transaction from accounts list filter by operation type & Main to revenue')
def test_admin_crypto_transaction_from_accounts_list_main_to_revenue(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/cryptotransaction/from_accounts?operation=main_to_revenue&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.json()[0]["id"] == 11
    assert response.json()[0]["name"] == "Main – ConnexPay"
    assert response.json()[0]["number"] == "2000011"
    assert response.json()[0]["provider"] == 2
    assert response.json()[0]["company_id"] is None
    assert response.json()[0]["owner_type"] == "own"


@allure.title('Admin crypto transaction from accounts list filter by operation type & Internal_credit')
def test_admin_crypto_transaction_from_accounts_list_internal_credit(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/cryptotransaction/from_accounts?operation=internal_credit&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.json()[0]["id"] == 18
    assert response.json()[0]["name"] == "Credit – ConnexPay"
    assert response.json()[0]["number"] == "2000018"
    assert response.json()[0]["provider"] == 2
    assert response.json()[0]["company_id"] is None
    assert response.json()[0]["owner_type"] == "own"


@allure.title('Admin crypto transaction from accounts list filter by operation type & Netting')
def test_admin_crypto_transaction_from_accounts_list_netting(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/cryptotransaction/from_accounts?operation=netting&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('{"id":138,"name":"test do not change","number":"1018850","balance":1004.65,"company_id":129,"provider":2,"owner_type":"client"}')


@allure.title('Admin crypto transaction from accounts list filter by operation type & Gift')
def test_admin_crypto_transaction_from_accounts_list_gift(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/cryptotransaction/from_accounts?operation=gift&provider=2', headers=headers
    )
    assert response.status == 200
    assert response.json()[0]["id"] == 19
    assert response.json()[0]["name"] == "Revenue – ConnexPay"
    assert response.json()[0]["number"] == "2000019"
    assert response.json()[0]["provider"] == 2
    assert response.json()[0]["company_id"] is None
    assert response.json()[0]["owner_type"] == "own"


@allure.title('Admin crypto transaction from accounts list filter by operation type & inter account transfer')
def test_admin_crypto_transaction_from_accounts_list_inter_account_transfer(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/cryptotransaction/from_accounts?operation=inter-account-transfer&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('{"id":138,"name":"test do not change","number":"1018850","balance":1004.65,"company_id":129,"provider":2,"owner_type":"client"}')


@allure.title('Admin crypto transaction from accounts list filter by operation type & provider Deposit not admin')
def test_admin_crypto_transaction_from_accounts_list_deposit_not_admin(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/cryptotransaction/from_accounts?operation=deposit&provider=2', headers=headers
    )
    assert response.status == 403


@allure.title('Admin crypto transaction from accounts list filter by operation type & provider Deposit without auth')
def test_admin_crypto_transaction_from_accounts_list_deposit_without_auth(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    response = api_request_context.get(
        '/api/admin/cryptotransaction/from_accounts?operation=deposit&provider=2'
    )
    assert response.status == 401