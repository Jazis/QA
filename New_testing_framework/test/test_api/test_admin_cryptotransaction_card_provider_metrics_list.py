import allure
from playwright.sync_api import APIRequestContext
from jsonschema import validate
from jsonschema.exceptions import ValidationError

@allure.title('Admin crypto transaction card provider metrics')
def test_admin_crypto_transaction_card_provider_metrics(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/cryptotransaction/card-provider/metrics', headers=headers
    )
    assert response.status == 200
    assert response.text() == '[{"id":1,"name":"Core Pay","topups_count":1},{"id":2,"name":"ConnexPay","topups_count":9},{"id":5,"name":"Qolo","topups_count":2}]'


@allure.title('Admin crypto transaction currencies prices')
def test_admin_crypto_transaction_currencies_prices(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/cryptotransaction/currencies/prices', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"usdt"')
    assert response.text().__contains__('"usdc"')


@allure.title('Admin crypto transaction gas station')
def test_admin_crypto_transaction_gas_station(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/cryptotransaction/gas-station', headers=headers
    )
    assert response.status == 200
    assert response.text().__contains__('"tron"')
    assert response.text().__contains__('"ethereum"')


@allure.title('Admin crypto transaction widgets')
def test_admin_crypto_transaction_widgets(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/cryptotransaction/widgets', headers=headers
    )
    assert response.status == 200
    response_data = response.json()
    schema = {
        "type": "object",
        "properties": {
            "treasury_usdt_trc_amount": {
                "type": "number",
                "minimum": 0
            },
            "usdt_trc_count": {
                "type": "integer",
                "minimum": 0
            },
            "treasury_usdt_erc_amount": {
                "type": "number",
                "minimum": 0
            },
            "usdt_erc_count": {
                "type": "integer",
                "minimum": 0
            },
            "treasury_usdc_erc_amount": {
                "type": "number",
                "minimum": 0
            },
            "usdc_erc_count": {
                "type": "integer",
                "minimum": 0
            },
            "expense_amount": {
                "type": "number",
                "minimum": 0
            },
            "deposit_count": {
                "type": "integer",
                "minimum": 0
            }
        },
        "required": [
            "treasury_usdt_trc_amount",
            "usdt_trc_count",
            "treasury_usdt_erc_amount",
            "usdt_erc_count",
            "treasury_usdc_erc_amount",
            "usdc_erc_count",
            "expense_amount",
            "deposit_count"
        ],
        "additionalProperties": False
    }
    try:
        validate(instance=response_data, schema=schema)
        print("JSON соответствует схеме")
    except ValidationError as e:
        print("Ошибка валидации:", e)


@allure.title('Admin crypto transaction card provider')
def test_admin_crypto_transaction_card_provider(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/filter/cryptotransaction/card-provider', headers=headers
    )
    assert response.status == 200
    assert response.text() == '[{"id":2,"name":"ConnexPay","stage":null},{"id":5,"name":"Qolo","stage":null}]'

