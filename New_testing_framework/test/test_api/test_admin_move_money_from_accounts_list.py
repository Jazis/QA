import re

import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS
from data.input_data.users import VALID_USERS_WITH_ROLES
from api.function_api import auth_token_function
import pytest

@allure.title('Admin move money from accounts')
def test_admin_move_money_from_accounts(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('{"id":4,"name":"MTS","number":"1021481"'), (
        '"provider":2,"company_id":1,"owner_type":"client"')
    assert response.text().__contains__('"id":5,"name":"Beeline","number":"1038841"'), (
        '"provider":2,"company_id":2,"owner_type":"client"')
    assert response.text().__contains__('"id":6,"name":"Some New Company","number":"1039750"'), (
        '"provider":2,"company_id":3,"owner_type":"client"')
    assert response.text().__contains__('"id":7,"name":"Tesla","number":"1062148"'), (
        '"provider":2,"company_id":4,"owner_type":"client"')
    assert response.text().__contains__('"id":8,"name":"New company 1","number":"1083293"'), (
        '"company_id":5,"owner_type":"client"')
    assert response.text().__contains__('"id":9,"name":"ConnCompany","number":"1015104"'), (
        '"provider":2,"company_id":6,"owner_type":"client"')


@allure.title('Admin move money from accounts Qolo')
def test_admin_move_money_from_accounts_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":813,"name":"Raven Qolo","number":"5028572","balance"'),('"company_id":802,"provider":5,"owner_type":"client"')


@allure.title('Not admin move money from accounts')
def test_not_admin_move_money_from_accounts(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?provider=2', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money deposit')
def test_admin_move_money_deposit(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=deposit&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('{"id":11,"name":"Main – ConnexPay","number":"2000011"'),('"company_id":null,"provider":2,"owner_type":"own"}')


@allure.title('Admin move money deposit Qolo')
def test_admin_move_money_deposit_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=deposit&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":847,"name":"Main – Qolo","number":"5000002","balance"'), ('"company_id":null,"provider":5,"owner_type":"own"')


@allure.title('Not admin move money deposit')
def test_not_admin_move_money_deposit(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=deposit&provider=2', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money withdrawal')
def test_admin_move_money_withdrawal(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=withdrawal&provider=2', headers=headers
    )
    print(response.text())
    assert response.status == 200
    assert response.text().__contains__('"id":4,"name":"MTS","number":"1021481"'), (
        '"provider":2,"company_id":1,"owner_type":"client"')
    assert response.text().__contains__('"id":7,"name":"Tesla","number":"1062148"'), (
        '"provider":2,"company_id":4,"owner_type":"client"')
    assert response.text().__contains__('"id":176,"name":"white company","number":"1047836"'), (
        '"company_id":167,"provider":2,"owner_type":"client"')


@allure.title('Admin move money withdrawal Qolo')
def test_admin_move_money_withdrawal_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=withdrawal&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":813,"name":"Raven Qolo","number":"5028572","balance"'), ('"company_id":802,"provider":5,"owner_type":"client"')


@allure.title('Not admin move money withdrawal')
def test_not_admin_move_money_withdrawal(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=withdrawal&provider=5', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money credit issue')
def test_admin_move_money_credit_issue(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=credit_issue&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('[{"id":18,"name":"Credit – ConnexPay","number":"2000018"'), (
        '"company_id":null,"provider":2,"owner_type":"own"}]')


@allure.title('Admin move money credit issue Qolo')
def test_admin_move_money_credit_issue_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=credit_issue&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":807,"name":"Credit – Qolo","number":"500007"'), ('"company_id":null,"provider":5,"owner_type":"own"')


@allure.title('Not admin move money credit issue')
def test_not_admin_move_money_credit_issue(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=credit_issue&provider=2', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money credit issue wire')
def test_admin_move_money_credit_issue_wire(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=credit_issue_wire&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('[{"id":18,"name":"Credit – ConnexPay","number":"2000018","balance"'), (
        '"company_id":null,"provider":2,"owner_type":"own"}]')


@allure.title('Admin move money credit issue wire Qolo')
def test_admin_move_money_credit_issue_wire_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=credit_issue_wire&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":807,"name":"Credit – Qolo","number":"500007","balance"'), ('"company_id":null,"provider":5,"owner_type":"own"')


@allure.title('Not admin move money credit issue wire')
def test_not_admin_move_money_credit_issue_wire(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=credit_issue_wire&provider=1', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money credit clear')
def test_admin_move_money_credit_clear(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=credit_clear&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('{"id":500,"name":"Netting – ConnexPay","number":"20000xx","balance":')
    assert response.text().__contains__('"company_id":null,"provider":2,"owner_type":"own"}')
    assert response.text().__contains__('{"id":11,"name":"Main – ConnexPay","number":"2000011","balance"')
    assert response.text().__contains__('"company_id":null,"provider":2,"owner_type":"own"}]')


@allure.title('Admin move money credit clear Qolo')
def test_admin_move_money_credit_clear_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=credit_clear&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":810,"name":"Netting – Qolo","number":"5000005","balance":'), ('"company_id":null,"provider":5,"owner_type":"own"')
    assert response.text().__contains__('"id":847,"name":"Main – Qolo","number":"5000002","balance"'), ('"company_id":null,"provider":5,"owner_type":"own"')


@allure.title('Not admin move money credit clear')
def test_not_admin_move_money_credit_clear(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=credit_clear&provider=2', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money subscription filter company MTS')
def test_admin_move_money_subscription_filter_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=subscription&provider=2&company=1', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('[{"id":4,"name":"MTS","number":"1021481"'), (
        '"provider":2,"company_id":1,"owner_type":"client"}]')


@allure.title('Admin move money subscription filter company Qolo Test')
def test_admin_move_money_subscription_filter_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=subscription&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":817,"name":"Qolo Test","number":"2092590","balance"'), ('"company_id":804,"provider":5,"owner_type":"client"')


@allure.title('Not admin move money subscription filter company MTS')
def test_not_admin_move_money_subscription_filter_company(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=subscription&provider=2&company=1', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money money outbound')
def test_admin_move_money_money_outbound(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=money_outbound&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('[{"id":17,"name":"Fee – ConnexPay","number":"2000017","balance"'), (
        '"company_id":null,"provider":2,"owner_type":"own"}]')


@allure.title('Admin move money money outbound Qolo')
def test_admin_move_money_money_outbound_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=money_outbound&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":808,"name":"Fee – Qolo","number":"5000006","balance"'), ('"company_id":null,"provider":5,"owner_type":"own"')


@allure.title('Not admin move money money outbound')
def test_not_admin_move_money_money_outbound(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=money_outbound&provider=5', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money revenue_to_main')
def test_admin_move_money_revenue_to_main(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=revenue_to_main&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('[{"id":19,"name":"Revenue – ConnexPay","number":"2000019","balance"'), (
        '"company_id":null,"provider":2,"owner_type":"own"}]')


@allure.title('Admin move money revenue_to_main Qolo')
def test_admin_move_money_revenue_to_main_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=revenue_to_main&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":816,"name":"Revenue – Qolo","number":"5000003","balance"'), ('"company_id":null,"provider":5,"owner_type":"own"')


@allure.title('Not admin move money revenue_to_main')
def test_not_admin_move_money_revenue_to_main(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=revenue_to_main&provider=2', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money main to revenue')
def test_admin_move_money_main_to_revenue(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=main_to_revenue&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":11,"name":"Main – ConnexPay","number":"2000011","balance"'), ('"company_id":null,"provider":2,"owner_type":"own"}')


@allure.title('Admin move money main to revenue Qolo')
def test_admin_move_money_main_to_revenue_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=main_to_revenue&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":847,"name":"Main – Qolo","number":"5000002","balance":'), ('"company_id":null,"provider":5,"owner_type":"own"')


@allure.title('Not admin move money main to revenue')
def test_not_admin_move_money_main_to_revenue(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=main_to_revenue&provider=2', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money internal credit')
def test_admin_move_money_internal_credit(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=internal_credit&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('[{"id":18,"name":"Credit – ConnexPay","number":"2000018","balance"'), (
        '"company_id":null,"provider":2,"owner_type":"own"}]')


@allure.title('Admin move money internal credit Qolo')
def test_admin_move_money_internal_credit_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=internal_credit&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":807,"name":"Credit – Qolo","number":"500007","balance"'), ('"company_id":null,"provider":5,"owner_type":"own"')


@allure.title('Not admin move money internal credit')
def test_not_admin_move_money_internal_credit(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=internal_credit&provider=2', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money netting')
def test_admin_move_money_netting(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=netting&provider=2', headers=headers
    )
    assert response.status == 200
    assert response.text().__contains__('[{"id":4,"name":"MTS","number":"1021481"'), (
        '"provider":2,"company_id":1,"owner_type":"client"}')
    assert response.text().__contains__('"id":5,"name":"Beeline","number":"1038841"'), (
        '"provider":2,"company_id":2,"owner_type":"client"')
    assert response.text().__contains__('"id":6,"name":"Some New Company","number":"1039750"'), (
        '"provider":2,"company_id":3,"owner_type":"client"')
    assert response.text().__contains__('"id":7,"name":"Tesla","number":"1062148"'), (
        '"provider":2,"company_id":4,"owner_type":"client"')
    assert response.text().__contains__('"id":8,"name":"New company 1","number":"1083293"'), (
        '"provider":2,"company_id":5,"owner_type":"client"')
    assert response.text().__contains__('"id":9,"name":"ConnCompany","number":"1015104"'), (
        '"provider":2,"company_id":6,"owner_type":"client"')
    assert response.text().__contains__('"id":24,"name":"The Tesla","number":"1071877"'), (
        '"provider":2,"company_id":15,"owner_type":"client"')
    assert response.text().__contains__('"id":138,"name":"test do not change","number":"1018850"'), (
        '"provider":2,"company_id":129,"owner_type":"client"')


@allure.title('Admin move money netting Qolo')
def test_admin_move_money_netting_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=netting&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":813,"name":"Raven Qolo","number":"5028572","balance"'), ('"company_id":802,"provider":5,"owner_type":"client"')


@allure.title('Not admin move money netting')
def test_not_admin_move_money_netting(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=netting&provider=2', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money gift')
def test_admin_move_money_gift(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=gift&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('[{"id":19,"name":"Revenue – ConnexPay","number":"2000019","balance"'), (
        '"company_id":null,"provider":2,"owner_type":"own"}]')


@allure.title('Admin move money gift Qolo')
def test_admin_move_money_gift_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=gift&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":816,"name":"Revenue – Qolo","number":"5000003","balance"'), ('"company_id":null,"provider":5,"owner_type":"own"')


@allure.title('Not admin move money gift')
def test_not_admin_move_money_gift(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=gift&provider=2', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money inter-account-transfer')
def test_admin_move_money_inter_account_transfer(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=inter-account-transfer&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":4,"name":"MTS","number":"1021481"'), (
        '"provider":2,"company_id":1,"owner_type":"client"')
    assert response.text().__contains__('"id":403,"name":"gfhgfj gfjghjghd","number":"2011600"'), (
        '"provider":2,"company_id":399,"owner_type":"client"')
    assert response.text().__contains__('"id":372,"name":"MJUuWF","number":"2094319"'), (
        '"provider":2,"company_id":367,"owner_type":"client"')


@allure.title('Admin move money inter-account-transfer Qolo')
def test_admin_move_money_inter_account_transfer_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=inter-account-transfer&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":813,"name":"Raven Qolo","number":"5028572","balance"'), ('"company_id":802,"provider":5,"owner_type":"client"')


@allure.title('Not admin move money inter-account-transfer')
def test_not_admin_move_money_inter_account_transfer(auth_login_user_data_ru,
                                                    api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/from_accounts?operation=inter-account-transfer&provider=2', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Move money without auth')
def test_move_money_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/move_money/from_accounts'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED

@allure.title("Role move money actions")
@pytest.mark.parametrize("user", VALID_USERS_WITH_ROLES)
def test_roles_move_money_actions(request, auth_token, api_request_context: APIRequestContext, user) -> None:
    token = auth_token_function(request=request, username = user.login, password = user.password)
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }
    if user.role == "Admin" or user.role == "Finance":
        data = {"amount":1,"from_account":11,"to_account":4,"operation":"deposit"}
        response = api_request_context.post(
                '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200
    if user.role == "Viewer" or user.role == "CS":
        data = {"amount":1,"from_account":11,"to_account":4,"operation":"deposit"}
        response = api_request_context.post(
                '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 403