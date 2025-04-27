import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS
from data.input_data.users import VALID_USERS_WITH_ROLES
from api.function_api import validate_json_keys, auth_token_function
import pytest


@allure.title('Admin company get available wallets')
def test_admin_company_get_available_wallets(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/address', headers=headers
    )
    assert response.status == 200
    assert response.text() == '{"count":3,"next":null,"previous":null,"results":{"total_sum":{"money_in":7220.0,"balance":8.851},"data":[{"id":5,"address":"NewAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":1,"name":"tron","code":"TRC-20"},"token_id":1,"company":{"id":222,"name":"dsef dsfdsg","owner_type":"client"},"account":{"id":231,"name":"dsef dsfdsg","company":{"id":222,"name":"dsef dsfdsg","owner_type":"client"},"number":"1055386"},"status":"active","amount":0,"balance":0},{"id":4,"address":"expense_addr","wallet":{"id":4,"name":"Expense","provider":3,"type":"expenses"},"blockchain":{"id":1,"name":"tron","code":"TRC-20"},"token_id":1,"company":null,"account":null,"status":"active","amount":0,"balance":8.851},{"id":1,"address":"SomeAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":2,"name":"ethereum","code":"ERC-20"},"token_id":1,"company":{"id":1,"name":"MTS","owner_type":"client"},"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},"status":"active","amount":7220.0,"balance":0}]}}'


@allure.title('Not admin company get available wallets')
def test_not_admin_company_get_available_wallets(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/address', headers=headers
    )
    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Company get available wallets without auth')
def test_company_get_available_wallets_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/address'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Admin company get available wallets filter by company and status')
def test_admin_company_get_available_wallets_filter_by_company_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/address?company=1&status=active', headers=headers
    )
    assert response.status == 200
    assert response.text() == '{"count":1,"next":null,"previous":null,"results":{"total_sum":{"money_in":4210.0,"balance":0.0},"data":[{"id":1,"address":"SomeAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":1,"name":"tron","code":"TRC-20"},"token_id":1,"company":{"id":1,"name":"MTS","owner_type":"client"},"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},"status":"active","amount":4210.0,"balance":0}]}}'


@allure.title('Admin company get available wallets filter by wrong company and status')
def test_admin_company_get_available_wallets_filter_by_company_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/address?company=11&status=active', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":0,"next":null,"previous":null,"results":{"total_sum":{"money_in":0.0,"balance":0.0},"data":[]}}'


@allure.title('Admin company get available wallets filter by wrong account and status')
def test_admin_company_get_available_wallets_filter_by_wrong_account_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/address?account=1', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":0,"next":null,"previous":null,"results":{"total_sum":{"money_in":0.0,"balance":0.0},"data":[]}}'


@allure.title('Admin company get available wallets filter by account and status')
def test_admin_company_get_available_wallets_filter_by_account_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/address?account=4&status=active', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":1,"next":null,"previous":null,"results":{"total_sum":{"money_in":7220.0,"balance":0.0},"data":[{"id":1,"address":"SomeAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":2,"name":"ethereum","code":"ERC-20"},"token_id":1,"company":{"id":1,"name":"MTS","owner_type":"client"},"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},"status":"active","amount":7220.0,"balance":0}]}}'


@allure.title('Admin company get available wallets filter by wrong token and status')
def test_admin_company_get_available_wallets_filter_by_wrong_token_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/address?token=20&status=', headers=headers
    )
    assert response.status == 400
    assert response.text() == '{"token":["Select a valid choice. 20 is not one of the available choices."],"status":["Select a valid choice.  is not one of the available choices."]}'


@allure.title('Admin company get available wallets filter by token and status')
def test_admin_company_get_available_wallets_filter_by_token_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/address?token=1&status=active', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":3,"next":null,"previous":null,"results":{"total_sum":{"money_in":7220.0,"balance":8.851},"data":[{"id":5,"address":"NewAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":1,"name":"tron","code":"TRC-20"},"token_id":1,"company":{"id":222,"name":"dsef dsfdsg","owner_type":"client"},"account":{"id":231,"name":"dsef dsfdsg","company":{"id":222,"name":"dsef dsfdsg","owner_type":"client"},"number":"1055386"},"status":"active","amount":0,"balance":0},{"id":4,"address":"expense_addr","wallet":{"id":4,"name":"Expense","provider":3,"type":"expenses"},"blockchain":{"id":1,"name":"tron","code":"TRC-20"},"token_id":1,"company":null,"account":null,"status":"active","amount":0,"balance":8.851},{"id":1,"address":"SomeAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":2,"name":"ethereum","code":"ERC-20"},"token_id":1,"company":{"id":1,"name":"MTS","owner_type":"client"},"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},"status":"active","amount":7220.0,"balance":0}]}}'


@allure.title('Admin company get available wallets filter by wrong token and status')
def test_admin_company_get_available_wallets_filter_by_wrong_token_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/address?blockchain=11&status=active', headers=headers
    )

    assert response.status == 400
    assert response.text() == '{"blockchain":["Select a valid choice. 11 is not one of the available choices."]}'


@allure.title('Admin company get available wallets filter by wrong wallet and status')
def test_admin_company_get_available_wallets_filter_by_wrong_wallet_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/address?wallet=12&status=active', headers=headers
    )
    assert response.status == 400
    assert response.text() == '{"wallet":["Select a valid choice. 12 is not one of the available choices."]}'


@allure.title('Admin company get available wallets filter by wallet and status')
def test_admin_company_get_available_wallets_filter_by_wallet_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/address?wallet=1&status=active', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":2,"next":null,"previous":null,"results":{"total_sum":{"money_in":7220.0,"balance":0.0},"data":[{"id":5,"address":"NewAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":1,"name":"tron","code":"TRC-20"},"token_id":1,"company":{"id":222,"name":"dsef dsfdsg","owner_type":"client"},"account":{"id":231,"name":"dsef dsfdsg","company":{"id":222,"name":"dsef dsfdsg","owner_type":"client"},"number":"1055386"},"status":"active","amount":0,"balance":0},{"id":1,"address":"SomeAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":2,"name":"ethereum","code":"ERC-20"},"token_id":1,"company":{"id":1,"name":"MTS","owner_type":"client"},"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},"status":"active","amount":7220.0,"balance":0}]}}'


@allure.title('Admin company get available wallets filter by type wallet and status')
def test_admin_company_get_available_wallets_filter_by_type_wallet_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/address?status=active&wallet_type=client', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":2,"next":null,"previous":null,"results":{"total_sum":{"money_in":7220.0,"balance":0.0},"data":[{"id":5,"address":"NewAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":1,"name":"tron","code":"TRC-20"},"token_id":1,"company":{"id":222,"name":"dsef dsfdsg","owner_type":"client"},"account":{"id":231,"name":"dsef dsfdsg","company":{"id":222,"name":"dsef dsfdsg","owner_type":"client"},"number":"1055386"},"status":"active","amount":0,"balance":0},{"id":1,"address":"SomeAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":2,"name":"ethereum","code":"ERC-20"},"token_id":1,"company":{"id":1,"name":"MTS","owner_type":"client"},"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},"status":"active","amount":7220.0,"balance":0}]}}'


@allure.title('Admin company get available wallets filter by search and status')
def test_admin_company_get_available_wallets_filter_by_search_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/address?status=active&search=Some', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"count":1,"next":null,"previous":null,"results":{"total_sum":{"money_in":7220.0,"balance":0.0},"data":[{"id":1,"address":"SomeAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":2,"name":"ethereum","code":"ERC-20"},"token_id":1,"company":{"id":1,"name":"MTS","owner_type":"client"},"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},"status":"active","amount":7220.0,"balance":0}]}}'


@allure.title('Admin company get available wallets filter by date and status')
def test_admin_company_get_available_wallets_filter_by_date_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/address?status=active&date_start=2024-05-05&date_end=2024-06-05', headers=headers
    )
    assert response.status == 200
    assert response.text() == '{"count":3,"next":null,"previous":null,"results":{"total_sum":{"money_in":0.0,"balance":8.851},"data":[{"id":5,"address":"NewAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":1,"name":"tron","code":"TRC-20"},"token_id":1,"company":{"id":222,"name":"dsef dsfdsg","owner_type":"client"},"account":{"id":231,"name":"dsef dsfdsg","company":{"id":222,"name":"dsef dsfdsg","owner_type":"client"},"number":"1055386"},"status":"active","amount":0,"balance":0},{"id":4,"address":"expense_addr","wallet":{"id":4,"name":"Expense","provider":3,"type":"expenses"},"blockchain":{"id":1,"name":"tron","code":"TRC-20"},"token_id":1,"company":null,"account":null,"status":"active","amount":0,"balance":8.851},{"id":1,"address":"SomeAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":2,"name":"ethereum","code":"ERC-20"},"token_id":1,"company":{"id":1,"name":"MTS","owner_type":"client"},"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"client"},"number":"1021481"},"status":"active","amount":0,"balance":0}]}}'


@allure.title('Not admin company get available wallets filter by date and status')
def test_not_admin_company_get_available_wallets_filter_by_date_status(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/address?status=active&date_start=2024-05-05&date_end=2024-06-05', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Company get available wallets without auth')
def test_not_admin_company_get_available_wallets_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/address?status=active&date_start=2024-05-05&date_end=2024-06-05'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
    
@pytest.mark.parametrize("user", VALID_USERS_WITH_ROLES)
def test_roles_view_crypto_admin_address(request, api_request_context: APIRequestContext, user):
    token = auth_token_function(request=request, username = user.login, password = user.password)
    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
            '/api/admin/address', headers=headers
        )
    assert response.status == 200
    assert validate_json_keys(response.text(), '{"count":2,"next":null,"previous":null,"results":{"total_sum":{"money_in":0.0,"balance":0.0},"data":[{"id":5,"address":"NewAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":1,"name":"tron","code":"TRC-20"},"token_id":1,"company":{"id":841,"name":"Solo Qolo","owner_type":"client"},"account":{"id":856,"name":"Solo Qolo","company":{"id":841,"name":"Solo Qolo","owner_type":"client"},"number":"5042764"},"status":"active","amount":0,"balance":0},{"id":1,"address":"SomeAddress","wallet":{"id":1,"name":"DEPOSIT","provider":3,"type":"deposit"},"blockchain":{"id":2,"name":"ethereum","code":"ERC-20"},"token_id":1,"company":{"id":1,"name":"MTS","owner_type":"own"},"account":{"id":4,"name":"MTS","company":{"id":1,"name":"MTS","owner_type":"own"},"number":"1021481"},"status":"active","amount":0,"balance":0}]}}') == True
    