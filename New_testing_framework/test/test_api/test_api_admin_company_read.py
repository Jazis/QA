import allure
from playwright.sync_api import APIRequestContext
from data.responses_texts import PERMISSIONS, NOT_FOUND
from data.input_data.users import VALID_USERS_WITH_ROLES
from api.function_api import validate_json_keys, auth_token_function
from utils.json_validation import validate_json_schema
import pytest
from data.input_data.api.api_admin_company_read import COMPANY_READ


@allure.title('Admin company by id')
def test_admin_company_by_id(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/company/129', headers=headers
    )

    assert response.status == 200
    # validate_json_schema(response.text(), schema_name)
    assert validate_json_keys(response.text(),'{"id":129,"created_at":"2024-04-17T05:20:50.908082Z","name":"test do not change","cards_quantity_limit":150,"use_decline_fee":true,"critical_balance":100.0,"activated_at":"2024-04-17T05:22:30Z","disabled_at":null,"subscription":{"id":18,"plan":{"id":3,"name":"Pro Monthly","code":"pro_monthly","default":false,"price":"471.00","period":"Monthly - 30","tariff":{"id":2,"name":"Pro","code":"pro","crypto_topup_fee":2.0,"wire_topup_fee":2.0,"available_bins_count":11,"is_international_bins":false,"is_free_cards":true}},"status":"Active","started_at":"2024-04-17T05:22:30Z","expires_at":null,"ended_at":null},"wallet_addresses":[],"status":"active","owner_type":"client","provider":{"id":2,"name":"ConnexPay","stage":null}}') == True 


@allure.title('Admin company by wrong id')
def test_admin_company_by_wrong_id(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/company/129000', headers=headers
    )

    assert response.status == 404
    assert response.text() == NOT_FOUND


@allure.title('Admin company by id not admin')
def test_admin_company_by_id_not_admin(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/company/129', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin company by id without auth')
def test_admin_company_by_id_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/company/129'
    )

    assert response.status == 401

@pytest.mark.parametrize("user", VALID_USERS_WITH_ROLES)
def test_roles_view(request, api_request_context: APIRequestContext, user):
    token = auth_token_function(request=request, username = user.login, password = user.password)
    headers = {
        'Authorization': f"Token {token}"
    }
    response = api_request_context.get(
            '/api/admin/company', headers=headers
        )
    assert response.status == 200
    assert validate_json_keys(response.text(), '{"id":171,"name":"ruby rose","status":"active","tariff":"Pro","issued_cards":5,"transactions_count":1296,"international":58.767772511848335,"avg_transaction_amount":1340.5428129032257,"decline_rate":18.595679012345677,"decline_amount":11608.47,"money_in":1102100.0,"settled":528066.22,"pending":510208.41,"refund":13507.64,"reversed_amount":13981.97,"fx_fee":85.7,"cross_border_fee":325.31,"decline_fee":108.5,"spend":-1025286.5,"owner_type":"client","avatar":null}') == True
    