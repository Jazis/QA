import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED


@allure.title('Get filter cash client types without authorization')
def test_get_filter_cash_client_types_without_authorization(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/filter/cash/client_types?account_id=4'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Get filter cash client types')
def test_get_filter_cash_client_types(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/filter/cash/client_types?acc_id=129', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"code":"deposit","name":"entity.transactionType.deposit","is_visible":false},{"code":"deposit_wire","name":"entity.transactionType.depositWire","is_visible":false},{"code":"deposit_fee","name":"entity.transactionType.depositFee","is_visible":false},{"code":"spend","name":"entity.transactionType.spend","is_visible":false},{"code":"decline_fee","name":"entity.transactionType.declineFee","is_visible":false},{"code":"refund","name":"entity.transactionType.refund","is_visible":false},{"code":"referral","name":"entity.transactionType.referral","is_visible":false},{"code":"referrer","name":"entity.transactionType.referrer","is_visible":false},{"code":"bonus","name":"entity.transactionType.bonus","is_visible":false},{"code":"withdrawal","name":"entity.transactionType.withdrawal","is_visible":false},{"code":"subscription","name":"entity.transactionType.subscription","is_visible":false}]'


@allure.title('Get filter cash client types wrong id')
def test_get_filter_cash_client_types_wrong_id(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/filter/cash/client_types?acc_id=40000', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"code":"deposit","name":"entity.transactionType.deposit","is_visible":false},{"code":"deposit_wire","name":"entity.transactionType.depositWire","is_visible":false},{"code":"deposit_fee","name":"entity.transactionType.depositFee","is_visible":false},{"code":"spend","name":"entity.transactionType.spend","is_visible":false},{"code":"decline_fee","name":"entity.transactionType.declineFee","is_visible":false},{"code":"refund","name":"entity.transactionType.refund","is_visible":false},{"code":"referral","name":"entity.transactionType.referral","is_visible":false},{"code":"referrer","name":"entity.transactionType.referrer","is_visible":false},{"code":"bonus","name":"entity.transactionType.bonus","is_visible":false},{"code":"withdrawal","name":"entity.transactionType.withdrawal","is_visible":false},{"code":"subscription","name":"entity.transactionType.subscription","is_visible":false}]'
