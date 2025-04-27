import allure
from playwright.sync_api import APIRequestContext
from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS
from data.input_data.users import VALID_USERS_WITH_ROLES
from api.function_api import validate_json_keys, auth_token_function
import pytest


@allure.title('Admin referral list')
def test_admin_referral_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/referral', headers=headers
    )

    assert response.status == 200
    assert validate_json_keys(response.text(),'{"id":33,"referee":{"id":989,"name":"test 948756849","owner_type":"client","account_number":"20227046"},"referrer":{"id":1,"name":"MTS","owner_type":"client","account_number":"1021481"},"referee_name":"test 948756849","status":"onboarded","created_at":"2025-01-14T11:52:43.452209Z","referrer_reward":0.0,"referee_reward":0.0}') == True
    assert validate_json_keys(response.text(),'{"id":32,"referee":{"id":973,"name":"solotest ru47","owner_type":"client","account_number":"20245388"},"referrer":{"id":1,"name":"MTS","owner_type":"client","account_number":"1021481"},"referee_name":"solotest ru47","status":"onboarded","created_at":"2025-01-11T07:56:19.934655Z","referrer_reward":0.0,"referee_reward":0.0}') == True
    assert validate_json_keys(response.text(),'{"id":31,"referee":{"id":972,"name":"Team Crypto","owner_type":"client","account_number":"20435131"},"referrer":{"id":1,"name":"MTS","owner_type":"client","account_number":"1021481"},"referee_name":"Team Crypto","status":"onboarded","created_at":"2025-01-09T13:14:50.591087Z","referrer_reward":0.0,"referee_reward":0.0}') == True
    assert validate_json_keys(response.text(),'{"id":30,"referee":{"id":664,"name":"do not activate","owner_type":"client","account_number":"2077080"},"referrer":{"id":169,"name":"green company","owner_type":"client","account_number":"1057766"},"referee_name":"do not activate","status":"onboarded","created_at":"2024-12-16T07:32:20.895087Z","referrer_reward":0.0,"referee_reward":0.0}') == True
    assert validate_json_keys(response.text(),'{"id":29,"referee":{"id":933,"name":"Solo Mts","owner_type":"client","account_number":"20940894"},"referrer":{"id":1,"name":"MTS","owner_type":"client","account_number":"1021481"},"referee_name":"Solo Mts","status":"denied","created_at":"2024-12-11T14:10:42.977531Z","referrer_reward":0.0,"referee_reward":0.0}') == True
    assert validate_json_keys(response.text(),'{"id":28,"referee":{"name":"Team qwertetret"},"referrer":{"id":1,"name":"MTS","owner_type":"client","account_number":"1021481"},"referee_name":"Team qwertetret","status":"denied","created_at":"2024-12-11T14:08:32.258210Z","referrer_reward":0.0,"referee_reward":0.0}') == True
    assert validate_json_keys(response.text(),'{"id":27,"referee":{"id":931,"name":"Ukr_1223","owner_type":"client","account_number":"50186753"},"referrer":{"id":1,"name":"MTS","owner_type":"client","account_number":"1021481"},"referee_name":"Ukr_1223","status":"closed","created_at":"2024-12-11T07:52:38.141356Z","referrer_reward":250.0,"referee_reward":250.0}') == True
    assert validate_json_keys(response.text(),'{"id":26,"referee":{"name":"Ukr_!"},"referrer":{"id":1,"name":"MTS","owner_type":"client","account_number":"1021481"},"referee_name":"Ukr_!","status":"denied","created_at":"2024-12-11T07:43:29.188444Z","referrer_reward":250.0,"referee_reward":250.0}') == True
    assert validate_json_keys(response.text(),'{"id":25,"referee":{"name":"Recommended"},"referrer":{"id":1,"name":"MTS","owner_type":"client","account_number":"1021481"},"referee_name":"Recommended","status":"denied","created_at":"2024-12-11T07:12:41.802378Z","referrer_reward":250.0,"referee_reward":250.0}') == True
    assert validate_json_keys(response.text(),'{"id":24,"referee":{"id":923,"name":"tetst iuiu","owner_type":"client","account_number":"20942647"},"referrer":{"id":1,"name":"MTS","owner_type":"client","account_number":"1021481"},"referee_name":"tetst iuiu","status":"onboarded","created_at":"2024-12-11T07:06:25.996099Z","referrer_reward":250.0,"referee_reward":250.0}') == True


@allure.title('Admin referral list filter status')
def test_admin_referral_list_filter_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/referral?status=paid', headers=headers
    )

    assert response.status == 200
    assert validate_json_keys(response.text(),'{"id":7,"referee":{"id":222,"name":"dsef dsfdsg","owner_type":"client","account_number":"1055386"},"referrer":{"id":1,"name":"MTS","owner_type":"client","account_number":"1021481"},"referee_name":"dsef dsfdsg","status":"paid","started_at":"2024-06-18T06:52:36Z","ended_at":"2024-06-18T06:52:36Z","paid_at":"2024-10-11T05:47:19.251672Z","referrer_reward":250.0,"referee_reward":250.0}') == True
    assert validate_json_keys(response.text(),'{"id":6,"referee":{"id":202,"name":"nmfdADSF retryty","owner_type":"client","account_number":"1022765"},"referrer":{"id":1,"name":"MTS","owner_type":"client","account_number":"1021481"},"referee_name":"nmfdADSF retryty","status":"paid","started_at":"2024-06-10T07:01:26Z","ended_at":null,"paid_at":"2024-09-02T11:15:49.152387Z","referrer_reward":250.0,"referee_reward":250.0}') == True
    assert validate_json_keys(response.text(),'{"id":2,"referee":{"id":39,"name":"123f","owner_type":"client","account_number":"1022893"},"referrer":{"id":6,"name":"ConnCompany","owner_type":"client","account_number":"1015104"},"referee_name":"123f","status":"paid","started_at":"2024-01-22T22:14:15.327745Z","ended_at":"2024-01-22T22:24:28.378609Z","paid_at":"2024-08-26T09:10:56.206600Z","referrer_reward":250.0,"referee_reward":250.0}') == True


@allure.title('Admin referral list filter by search')
def test_admin_referral_list_filter_by_search(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/referral?search=gfjghjghd', headers=headers
    )

    assert response.status == 200
    assert validate_json_keys(response.text(),'{"id":8,"referee":{"id":399,"name":"gfhgfj gfjghjghd","owner_type":"client","account_number":"2011600"},"referrer":{"id":170,"name":"grey company","owner_type":"client","account_number":"1041407"},"referee_name":"gfhgfj gfjghjghd","status":"to_be_paid","started_at":"2024-08-07T11:17:51.213215Z","ended_at":null,"paid_at":"2024-10-14T06:39:09.075746Z","referrer_reward":250.0,"referee_reward":250.0}') == True


@allure.title('Not admin referral list')
def test_not_admin_referral_list(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    response = api_request_context.get(
        '/api/admin/referral', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Referral list without auth')
def test_referral_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/referral'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED

@pytest.mark.parametrize("user", VALID_USERS_WITH_ROLES)
def test_roles_view_referral(request, api_request_context: APIRequestContext, user):
    token = auth_token_function(request=request, username = user.login, password = user.password)
    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
            '/api/admin/company', headers=headers
        )
    assert response.status == 200
    assert validate_json_keys(response.text(), '{"id":171,"name":"ruby rose","status":"active","tariff":"Pro","issued_cards":5,"transactions_count":1296,"international":58.767772511848335,"avg_transaction_amount":1340.5428129032257,"decline_rate":18.595679012345677,"decline_amount":11608.47,"money_in":1102100.0,"settled":528066.22,"pending":510208.41,"refund":13507.64,"reversed_amount":13981.97,"fx_fee":85.7,"cross_border_fee":325.31,"decline_fee":108.5,"spend":-1025286.5,"owner_type":"client","avatar":null}') == True
    