import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin move money operational types list')
def test_admin_move_money_operational_types_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/operation_types', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"code":"deposit","name":"Deposit"},{"code":"withdrawal","name":"Withdrawal"},{"code":"credit_issue","name":"Credit Issue (Legacy)"},{"code":"credit_issue_wire","name":"Credit Issue Wire"},{"code":"credit_clear","name":"Credit Clear"},{"code":"subscription","name":"Subscription"},{"code":"money_outbound","name":"Fee to Main"},{"code":"main_to_revenue","name":"Main to Revenue"},{"code":"revenue_to_main","name":"Revenue to Main"},{"code":"internal_credit","name":"Credit Internal"},{"code":"netting","name":"Netting"},{"code":"gift","name":"Gift"},{"code":"inter-account-transfer","name":"Inter Account Transfer"}]'


@allure.title('Not admin move money operational types list')
def test_not_admin_move_money_operational_types_list(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/operation_types', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Move money operational types list without auth')
def test_not_admin_move_money_operational_types_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/move_money/operation_types'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
