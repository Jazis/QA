import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED


@allure.title('Get admin cash client types without authorization')
def test_get_admin_client_types_without_authorization(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/cash/client_types'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Get admin cash client types wrong endpoint')
def test_get_admin_client_types_wrong_endpoint(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/cash/clientypes'
    )
    assert response.status == 404


@allure.title('Get admin cash client types not admin')
def test_get_admin_cash_client_types_not_admin(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/cash/client_types', headers=headers
    )
    assert response.status == 403


@allure.title('Get admin cash client types admin')
def test_get_admin_cash_client_types_admin(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/cash/client_types', headers=headers
    )
    assert response.status == 200
    assert response.text() == '[{"code":"deposit","name":"entity.transactionType.deposit","is_visible":true},{"code":"deposit_wire","name":"entity.transactionType.depositWire","is_visible":true},{"code":"deposit_fee","name":"entity.transactionType.depositFee","is_visible":true},{"code":"spend","name":"entity.transactionType.spend","is_visible":true},{"code":"decline_fee","name":"entity.transactionType.declineFee","is_visible":true},{"code":"refund","name":"entity.transactionType.refund","is_visible":true},{"code":"referral","name":"entity.transactionType.referral","is_visible":false},{"code":"referrer","name":"entity.transactionType.referrer","is_visible":true},{"code":"bonus","name":"entity.transactionType.bonus","is_visible":true},{"code":"withdrawal","name":"entity.transactionType.withdrawal","is_visible":true},{"code":"subscription","name":"entity.transactionType.subscription","is_visible":true}]'


@allure.title('Get admin cash client types filter by company')
def test_get_admin_cash_client_types_filter_by_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/cash/client_types?company_ids=129', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"code":"deposit","name":"entity.transactionType.deposit","is_visible":true},{"code":"deposit_wire","name":"entity.transactionType.depositWire","is_visible":false},{"code":"deposit_fee","name":"entity.transactionType.depositFee","is_visible":true},{"code":"spend","name":"entity.transactionType.spend","is_visible":true},{"code":"decline_fee","name":"entity.transactionType.declineFee","is_visible":true},{"code":"refund","name":"entity.transactionType.refund","is_visible":true},{"code":"referral","name":"entity.transactionType.referral","is_visible":false},{"code":"referrer","name":"entity.transactionType.referrer","is_visible":false},{"code":"bonus","name":"entity.transactionType.bonus","is_visible":false},{"code":"withdrawal","name":"entity.transactionType.withdrawal","is_visible":false},{"code":"subscription","name":"entity.transactionType.subscription","is_visible":false}]'