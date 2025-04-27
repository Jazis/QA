import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin move money to accounts list')
def test_admin_move_money_to_accounts_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":4,"name":"MTS","number":"1021481","balance"'),('"company_id":1,"provider":2,"owner_type":"client"')
    assert response.text().__contains__('"id":5,"name":"Beeline","number":"1038841","balance"'),('"company_id":2,"provider":2,"owner_type":"client"')
    assert response.text().__contains__('"id":6,"name":"Some New Company","number":"1039750","balance"'),('"company_id":3,"provider":2,"owner_type":"client"')


@allure.title('Admin move money to accounts list Qolo')
def test_admin_move_money_to_accounts_list_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?provider=5', headers=headers
    )
    assert response.status == 200
    assert response.text()


@allure.title('Not admin move money to accounts list')
def test_not_admin_move_money_to_accounts_list(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?provider=5', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Move money to accounts list without auth')
def test_move_money_to_accounts_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?provider=5'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Admin move money to accounts list filter deposit & company 1')
def test_admin_move_money_to_accounts_list_filter_deposit_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=deposit&provider=2&company=1', headers=headers
    )
    assert response.status == 200
    assert response.text().__contains__('[{"id":4,"name":"MTS","number":"1021481"'),('"provider":2,"company_id":1,"owner_type":"client"}]')


@allure.title('Admin move money to accounts list filter deposit & company 803 Qolo')
def test_admin_move_money_to_accounts_list_filter_deposit_company_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=deposit&provider=5&company=803', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":814,"name":"Clover Qolo","number":"5085666","balance"'), ('"company_id":803,"provider":5,"owner_type":"client"')


@allure.title('Admin move money to accounts list filter deposit')
def test_admin_move_money_to_accounts_list_filter_deposit(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=deposit&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('{"id":4,"name":"MTS","number":"1021481"'),('"provider":2,"company_id":1,"owner_type":"client"}')
    assert response.text().__contains__('{"id":5,"name":"Beeline","number":"1038841"'),('"provider":2,"company_id":2,"owner_type":"client"}')
    assert response.text().__contains__('{"id":6,"name":"Some New Company","number":"1039750"'),('"provider":2,"company_id":3,"owner_type":"client"}')
    assert response.text().__contains__('{"id":181,"name":"golden company","number":"1062075"'),('"provider":2,"company_id":172,"owner_type":"client"}')


@allure.title('Admin move money to accounts list filter withdrawal')
def test_admin_move_money_to_accounts_list_filter_withdrawal(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=withdrawal&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":11,"name":"Main – ConnexPay","number":"2000011","balance"'),('"company_id":null,"provider":2,"owner_type":"own"}')


@allure.title('Admin move money to accounts list filter withdrawal Qolo')
def test_admin_move_money_to_accounts_list_filter_withdrawal_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=withdrawal&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":847,"name":"Main – Qolo","number":"5000002","balance":'), ('"company_id":null,"provider":5,"owner_type":"own"')


@allure.title('Admin move money to accounts list filter withdrawal & company')
def test_admin_move_money_to_accounts_list_filter_withdrawal_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=withdrawal&company=1&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":11,"name":"Main – ConnexPay","number":"2000011","balance"'), ('"company_id":null,"provider":2,"owner_type":"own"')


@allure.title('Not admin move money to accounts list filter withdrawal & company')
def test_not_admin_move_money_to_accounts_list_filter_withdrawal_company(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=withdrawal&company=1&provider=2', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money to accounts list filter credit_issue & company')
def test_admin_move_money_to_accounts_list_filter_credit_issue_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=credit_issue&company=1&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":4,"name":"MTS","number":"1021481","balance"'), ('"company_id":1,"provider":2,"owner_type":"client"')


@allure.title('Admin move money to accounts list filter credit_issue')
def test_admin_move_money_to_accounts_list_filter_credit_issue(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=credit_issue&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":4,"name":"MTS","number":"1021481","balance"'), ('"company_id":1,"provider":2,"owner_type":"client"')
    assert response.text().__contains__('"id":5,"name":"Beeline","number":"1038841","balance"'), ('"company_id":2,"provider":2,"owner_type":"client"')
    assert response.text().__contains__('"id":6,"name":"Some New Company","number":"1039750","balance"'),('"company_id":3,"provider":2,"owner_type":"client"')


@allure.title('Admin move money to accounts list filter credit_issue Qolo')
def test_admin_move_money_to_accounts_list_filter_credit_issue_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=credit_issue&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":813,"name":"Raven Qolo","number":"5028572","balance"'), ('"company_id":802,"provider":5,"owner_type":"client"')
    assert response.text().__contains__('"id":814,"name":"Clover Qolo","number":"5085666","balance"'), ('"company_id":803,"provider":5,"owner_type":"client"')


@allure.title('Not admin move money to accounts list filter credit_issue')
def test_not_admin_move_money_to_accounts_list_filter_credit_issue(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=credit_issue&provider=5', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money to accounts list filter credit_issue_wire')
def test_admin_move_money_to_accounts_list_filter_credit_issue_wire(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=credit_issue_wire&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":4,"name":"MTS","number":"1021481","balance"'), ('"company_id":1,"provider":2,"owner_type":"client"')
    assert response.text().__contains__('"id":5,"name":"Beeline","number":"1038841","balance"'),('"company_id":2,"provider":2,"owner_type":"client"')


@allure.title('Admin move money to accounts list filter credit_issue_wire Qolo')
def test_admin_move_money_to_accounts_list_filter_credit_issue_wire_qolo(auth_token,
                                                                    api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=credit_issue_wire&provider=5', headers=headers
    )
    assert response.status == 200
    assert response.text().__contains__('"id":813,"name":"Raven Qolo","number":"5028572","balance"'), ('"company_id":802,"provider":5,"owner_type":"client"')
    assert response.text().__contains__('"id":814,"name":"Clover Qolo","number":"5085666","balance"'), ('"company_id":803,"provider":5,"owner_type":"client"')


@allure.title('Admin move money to accounts list filter credit_issue_wire and company')
def test_admin_move_money_to_accounts_list_filter_credit_issue_wire_and_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=credit_issue_wire&company=1&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('{"id":4,"name":"MTS","number":"1021481"'), ('"provider":2,"company_id":1,"owner_type":"client"}')


@allure.title('Not admin move money to accounts filter credit_issue_wire and company')
def test_not_admin_move_money_to_accounts_filter_credit_issue_wire_and_company(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=credit_issue_wire&provider=2', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money to accounts list filter credit_clear')
def test_admin_move_money_to_accounts_list_filter_credit_clear(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=credit_clear&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":18,"name":"Credit – ConnexPay","number":"2000018","balance"'), ('"company_id":null,"provider":2,"owner_type":"own"')


@allure.title('Admin move money to accounts money_outbound')
def test_admin_move_money_to_accounts_list_filter_money_outbound(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=money_outbound&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":11,"name":"Main – ConnexPay","number":"2000011","balance":'),('"company_id":null,"provider":2,"owner_type":"own"')


@allure.title('Admin move money to accounts money_outbound Qolo')
def test_admin_move_money_to_accounts_list_filter_money_outbound_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=money_outbound&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":847,"name":"Main – Qolo","number":"5000002","balance":'), ('"company_id":null,"provider":5,"owner_type":"own"')


@allure.title('Admin move money to accounts money_outbound and company')
def test_admin_move_money_to_accounts_list_filter_money_outbound_and_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=money_outbound&provider=2&company=1', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":11,"name":"Main – ConnexPay","number":"2000011","balance":'),('"company_id":null,"provider":2,"owner_type":"own"')


@allure.title('Not admin move money to accounts filter money_outbound and company')
def test_not_admin_move_money_to_accounts_filter_money_outbound_and_company(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=money_outbound&provider=2&company=1', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money to accounts revenue_to_main')
def test_admin_move_money_to_accounts_list_filter_revenue_to_main(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=revenue_to_main&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":11,"name":"Main – ConnexPay","number":"2000011","balance":'),('"company_id":null,"provider":2,"owner_type":"own"')


@allure.title('Admin move money to accounts revenue_to_main Qolo')
def test_admin_move_money_to_accounts_list_filter_revenue_to_main_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=revenue_to_main&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":847,"name":"Main – Qolo","number":"5000002","balance":'), ('"company_id":null,"provider":5,"owner_type":"own"')


@allure.title('Admin move money to accounts revenue_to_main and company')
def test_admin_move_money_to_accounts_list_filter_revenue_to_main_and_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=revenue_to_main&provider=2&company=1', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":11,"name":"Main – ConnexPay","number":"2000011","balance"'), ('"company_id":null,"provider":2,"owner_type":"own"')


@allure.title('Not admin move money to accounts filter revenue_to_main and company')
def test_not_admin_move_money_to_accounts_filter_revenue_to_main_and_company(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=revenue_to_main&provider=2&company=1', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money to accounts main_to_revenue and company')
def test_admin_move_money_to_accounts_list_filter_main_to_revenue_and_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=main_to_revenue&provider=2&company=1', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":19,"name":"Revenue – ConnexPay","number":"2000019","balance"'),('"company_id":null,"provider":2,"owner_type":"own"')


@allure.title('Admin move money to accounts main_to_revenue')
def test_admin_move_money_to_accounts_list_filter_main_to_revenue(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=main_to_revenue&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":19,"name":"Revenue – ConnexPay","number":"2000019","balance"'),('"company_id":null,"provider":2,"owner_type":"own"')


@allure.title('Admin move money to accounts main_to_revenue Qolo')
def test_admin_move_money_to_accounts_list_filter_main_to_revenue_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=main_to_revenue&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":816,"name":"Revenue – Qolo","number":"5000003","balance":'), ('"company_id":null,"provider":5,"owner_type":"own"')


@allure.title('Admin move money to accounts internal_credit and company')
def test_admin_move_money_to_accounts_list_filter_internal_credit_and_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=internal_credit&provider=2&company=1', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":11,"name":"Main – ConnexPay","number":"2000011","balance"'),('"company_id":null,"provider":2,"owner_type":"own"')


@allure.title('Admin move money to accounts internal_credit Qolo')
def test_admin_move_money_to_accounts_list_filter_internal_credit_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=internal_credit&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":847,"name":"Main – Qolo","number":"5000002","balance"'), ('"company_id":null,"provider":5,"owner_type":"own"')


@allure.title('Admin move money to accounts netting')
def test_admin_move_money_to_accounts_list_filter_netting(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=netting&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":500,"name":"Netting – ConnexPay","number":"20000xx","balance"'), ('"company_id":null,"provider":2,"owner_type":"own"')


@allure.title('Admin move money to accounts netting Qolo')
def test_admin_move_money_to_accounts_list_filter_netting_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=netting&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":810,"name":"Netting – Qolo","number":"5000005","balance":'), ('"company_id":null,"provider":5,"owner_type":"own"')


@allure.title('Admin move money to accounts gift & company')
def test_admin_move_money_to_accounts_list_filter_gift_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=gift&company=1&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('{"id":4,"name":"MTS","number":"1021481"'),('"provider":2,"company_id":1,"owner_type":"client"}')


@allure.title('Admin move money to accounts gift')
def test_admin_move_money_to_accounts_list_filter_gift(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=gift&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":6,"name":"Some New Company","number":"1039750","balance"'),('"company_id":3,"provider":2,"owner_type":"client"')
    assert response.text().__contains__('"id":803,"name":"QXIsbZET","number":"2095869","balance":'),('"company_id":798,"provider":2,"owner_type":"client"')


@allure.title('Admin move money to accounts gift Qolo')
def test_admin_move_money_to_accounts_list_filter_gift_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=gift&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":813,"name":"Raven Qolo","number":"5028572","balance"'), ('"company_id":802,"provider":5,"owner_type":"client"')
    assert response.text().__contains__('"id":814,"name":"Clover Qolo","number":"5085666","balance"'), ('"company_id":803,"provider":5,"owner_type":"client"')


@allure.title('Not admin move money to accounts gift')
def test_not_admin_move_money_to_accounts_filter_gift(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=gift&provider=5', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin move money to accounts inter-account-transfer & company')
def test_admin_move_money_to_accounts_list_filter_inter_account_transfer_company(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=inter-account-transfer&company=1&provider=2', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":4,"name":"MTS","number":"1021481","balance":'),('"company_id":1,"provider":2,"owner_type":"client"')


@allure.title('Admin move money to accounts inter-account-transfer Qolo')
def test_admin_move_money_to_accounts_list_filter_inter_account_transfer_qolo(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/move_money/to_accounts?operation=inter-account-transfer&provider=5', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":813,"name":"Raven Qolo","number":"5028572","balance"'), ('"company_id":802,"provider":5,"owner_type":"client"')
    assert response.text().__contains__('"id":814,"name":"Clover Qolo","number":"5085666","balance":'), ('"company_id":803,"provider":5,"owner_type":"client"')
