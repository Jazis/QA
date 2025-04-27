import allure
from playwright.sync_api import APIRequestContext
import pytest
from data.responses_texts import AUTH_NOT_PROVIDED
from data.input_data.random_data import random_string
from utils.json_validation import validate_json_schema
from data.input_data.api.settings import SETTINGS

class TestSettings:
    @allure.title("Settings billing payments")
    @pytest.mark.parametrize("schema_name", SETTINGS)
    def test_get_settings_billing_payments(self, auth_token_black_company, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_token_black_company}"
        }
        response = api_request_context.get(
            '/api/settings/billing/payments', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        

    @allure.title("Settings billing subscription")
    @pytest.mark.parametrize("schema_name", SETTINGS)
    def test_get_settings_billing_subscription(self, auth_login_user_data_ru,
                                               api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/settings/billing/subscription', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Settings bins")
    @pytest.mark.parametrize("schema_name", SETTINGS)
    def test_get_settings_bins(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/settings/bins', headers=headers
        )

        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        # assert response.text().__contains__('{"card_bin":"559292","currency":"USD","country":"US","is_global":false,"c3ds_enabled":false,"type":"Credit","payment_system":"mc","payment_system_name":"MasterCard","segment":"basic","segment_name":"Basic","category":"Commercial","fx_fee_percentage":0.01,"fx_fee_const":0.0,"cross_border_fee_percentage":0.01,"cross_border_fee_const":0.5}')
        # assert response.text().__contains__('{"card_bin":"489683","currency":"USD","country":"US","is_global":false,"c3ds_enabled":false,"type":"Prepaid","payment_system":"visa","payment_system_name":"Visa","segment":"private","segment_name":"Private","category":"Commercial","fx_fee_percentage":0.01,"fx_fee_const":0.0,"cross_border_fee_percentage":0.01,"cross_border_fee_const":0.5}')
        # assert response.text().__contains__('{"card_bin":"531993","currency":"USD","country":"US","is_global":false,"c3ds_enabled":false,"type":"Credit","payment_system":"mc","payment_system_name":"MasterCard","segment":null,"segment_name":null,"category":"Commercial","fx_fee_percentage":0.01,"fx_fee_const":0.0,"cross_border_fee_percentage":0.01,"cross_border_fee_const":0.5}')
        # assert response.text().__contains__('{"card_bin":"519075","currency":"USD","country":"US","is_global":false,"c3ds_enabled":false,"type":"Credit","payment_system":"mc","payment_system_name":"MasterCard","segment":null,"segment_name":null,"category":"Commercial","fx_fee_percentage":0.01,"fx_fee_const":0.0,"cross_border_fee_percentage":0.01,"cross_border_fee_const":0.5}')
        # assert response.text().__contains__('{"card_bin":"556371","currency":"USD","country":"US","is_global":false,"c3ds_enabled":false,"type":"Credit","payment_system":"mc","payment_system_name":"MasterCard","segment":null,"segment_name":null,"category":"Commercial","fx_fee_percentage":0.01,"fx_fee_const":0.0,"cross_border_fee_percentage":0.01,"cross_border_fee_const":0.5}')
        # assert response.text().__contains__('{"card_bin":"553437","currency":"INT","country":"US","is_global":true,"c3ds_enabled":false,"type":"Credit","payment_system":"mc","payment_system_name":"MasterCard","segment":null,"segment_name":null,"category":"Commercial","fx_fee_percentage":0,"fx_fee_const":0,"cross_border_fee_percentage":0,"cross_border_fee_const":0}')

    @allure.title("Settings company")
    @pytest.mark.parametrize("schema_name", SETTINGS)
    def test_get_settings_company(self, auth_token, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        response = api_request_context.get(
            '/api/settings/company', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Settings company without auth")
    def test_get_settings_company_without_auth(self, api_request_context: APIRequestContext) -> None:
        response = api_request_context.get(
            '/api/settings/company'
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Settings plans")
    @pytest.mark.parametrize("schema_name", SETTINGS)
    def test_get_settings_plans(self, auth_token, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        response = api_request_context.get(
            '/api/settings/plans', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        # assert response.text() == '[{"name":"entity.tariff.basic.name","text":"entity.tariff.basic.text","features":[{"name":"entity.feature.cryptoTopUp","is_available":true,"value":"3%","is_default":true},{"name":"entity.feature.wireTopUp","is_available":true,"value":"3%","is_default":true},{"name":"entity.feature.usBins","is_available":true,"value":"2","is_default":true},{"name":"entity.feature.freeCards","is_available":true,"value":null,"is_default":true},{"name":"entity.feature.cardTransfer","is_available":true,"value":null,"is_default":false},{"name":"entity.feature.userLimits","is_available":true,"value":null,"is_default":false},{"name":"entity.feature.internationalBins","is_available":false,"value":null,"is_default":false}],"is_current":false,"prices":[{"amount":1000.0,"period":"annual"},{"amount":100.0,"period":"monthly"}]},{"name":"entity.tariff.pro.name","text":"entity.tariff.pro.text","features":[{"name":"entity.feature.cryptoTopUp","is_available":true,"value":"2%","is_default":true},{"name":"entity.feature.wireTopUp","is_available":true,"value":"2%","is_default":true},{"name":"entity.feature.usBins","is_available":true,"value":"10","is_default":true},{"name":"entity.feature.freeCards","is_available":true,"value":null,"is_default":true},{"name":"entity.feature.cardTransfer","is_available":true,"value":null,"is_default":false},{"name":"entity.feature.userLimits","is_available":true,"value":null,"is_default":false},{"name":"entity.feature.internationalBins","is_available":true,"value":null,"is_default":false}],"is_current":true,"prices":[{"amount":471.0,"period":"monthly"}]},{"name":"entity.tariff.private.name","text":"entity.tariff.private.text","features":[{"name":"entity.feature.cryptoTopUp","is_available":true,"value":"2%","is_default":true},{"name":"entity.feature.wireTopUp","is_available":true,"value":"2%","is_default":true},{"name":"entity.feature.usBins","is_available":true,"value":"10","is_default":true},{"name":"entity.feature.freeCards","is_available":true,"value":null,"is_default":true},{"name":"entity.feature.cardTransfer","is_available":true,"value":null,"is_default":false},{"name":"entity.feature.userLimits","is_available":true,"value":null,"is_default":false},{"name":"entity.feature.internationalBins","is_available":true,"value":null,"is_default":false}],"is_current":false,"prices":[{"amount":600.0,"period":"monthly"}]}]'

    @allure.title("Settings user")
    @pytest.mark.parametrize("schema_name", SETTINGS)
    def test_get_settings_user(self, auth_token_black_company, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_token_black_company}"
        }
        response = api_request_context.get(
            '/api/settings/user', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        # assert response.text().__contains__('{"email":"blackcompany@mail.ru","first_name":"black","last_name":"company","locale":"en-GB","avatar":null,"timezone":"Europe/Moscow","theme":{"type":')

    @allure.title("Invite new user wrong role")
    def test_invite_new_user_wrong_role(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "email": "email@email.ru",
            "role": "rtfdews",
            "limit": 3,
            "limit_amount": 300
        }
        response = api_request_context.post(
            '/auth/account', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"status":"error","error_message":"No email"}'

    @allure.title("Invite new user wrong limit")
    def test_invite_new_user_wrong_limit(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "email": "email@email.ru",
            "role": "1",
            "limit": 300,
            "limit_amount": 300
        }
        response = api_request_context.post(
            '/auth/account', headers=headers, data=data
        )
        assert response.status == 400

    @allure.title("Invite new user big limit")
    def test_invite_new_user_big_limit(self, auth_token, api_request_context: APIRequestContext) -> None:
        email = random_string(4) + '@gmail.com'
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "email": email,
            "role": "2",
            "limit": 4,
            "limit_amount": 300000
        }
        response = api_request_context.post(
            '/auth/account', headers=headers, data=data
        )

        assert response.status == 200
        assert response.text() == '{"create":true,"send":true}'

    @allure.title("Invite new user admin")
    def test_invite_user_admin_(self, auth_token, api_request_context: APIRequestContext) -> None:
        email = random_string(4) + '@gmail.com'
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "email": email,
            "role": "1",
            "limit": 4,
            "limit_amount": 300
        }
        response = api_request_context.post(
            '/auth/account', headers=headers, data=data
        )
        assert response.status == 200
        assert response.text() == '{"create":true,"send":true}'

    # Падает из-за https://linear.app/devhost/issue/B-571
    @allure.title("Invite new user with wrong role")
    def test_invite_new_user_wrong_role(self, auth_token, api_request_context: APIRequestContext) -> None:
        email = random_string(4) + '@gmail.com'
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "email": email,
            "role": "904",
            "limit": 4,
            "limit_amount": 300
        }
        response = api_request_context.post(
            '/auth/account', headers=headers, data=data
        )
        assert response.status == 500

    # Падает из-за https://linear.app/devhost/issue/B-572
    @allure.title("Invite new user with negative limit amount")
    def test_invite_new_user_with_negative_limit_amount(self, auth_token,
                                                        api_request_context: APIRequestContext) -> None:
        email = random_string(4) + '@gmail.com'
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "email": email,
            "role": "2",
            "limit": 3,
            "limit_amount": - 3000
        }
        response = api_request_context.post(
            '/auth/account', headers=headers, data=data
        )
        assert response.status == 500

    # Падает из-за https://linear.app/devhost/issue/B-572
    @allure.title("Invite new user with limit amount = 0")
    def test_invite_new_user_with_limit_amount_zero(self, auth_token, api_request_context: APIRequestContext) -> None:
        email = random_string(4) + '@gmail.com'
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "email": email,
            "role": "2",
            "limit": 2,
            "limit_amount": 0
        }
        response = api_request_context.post(
            '/auth/account', headers=headers, data=data
        )
        assert response.status == 500

    @allure.title("Invite new user with same email address")
    def test_invite_new_user_with_same_email_address(self, auth_token, api_request_context: APIRequestContext) -> None:
        email = 'admin@admin.com'
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "email": email,
            "role": "2",
            "limit": 2,
            "limit_amount": 10
        }
        response = api_request_context.post(
            '/auth/account', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"email":["User with this email already exist. Status: Active"]}'

    @allure.title("Invite new user - admin with same email address")
    def test_invite_new_user_admin_with_same_email_address(self, auth_token,
                                                           api_request_context: APIRequestContext) -> None:
        email = 'admin@admin.com'
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "email": email,
            "role": "1",
            "limit": 2,
            "limit_amount": 10
        }
        response = api_request_context.post(
            '/auth/account', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"email":["User with this email already exist. Status: Active"]}'

    @allure.title("Invite new user without authorize")
    def test_invite_new_user_without_authorize(self, api_request_context: APIRequestContext) -> None:
        email = 'admin@admin.com'

        data = {
            "email": email,
            "role": "1",
            "limit": 2,
            "limit_amount": 10
        }
        response = api_request_context.post(
            '/auth/account', data=data
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Invite new user without email")
    def test_invite_new_user_without_email(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "role": "1",
            "limit": 2,
            "limit_amount": 10
        }
        response = api_request_context.post(
            '/auth/account', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"email":["This field is required."]}'

    @allure.title("Invite new user without role")
    def test_invite_new_user_without_role(self, auth_token, api_request_context: APIRequestContext) -> None:
        email = 'admin12345@admin.com'
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "email": email,
            "limit": 2,
            "limit_amount": 10
        }
        response = api_request_context.post(
            '/auth/account', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"role":["This field is required."]}'

    @allure.title("Invite new user without limit")
    def test_invite_new_user_without_limit(self, auth_token, api_request_context: APIRequestContext) -> None:
        email = 'admin12345@admin.com'
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "email": email,
            "role": "1",
            "limit_amount": 10
        }
        response = api_request_context.post(
            '/auth/account', headers=headers, data=data
        )
        assert response.status == 200
        assert response.text() == '{"create":true,"send":true}'

    @allure.title("Remove new user without limit")
    def test_remove_new_user_without_limit(self, auth_token, api_request_context: APIRequestContext) -> None:
        email = 'admin12345@admin.com'
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "email": 'admin12345@admin.com'
        }
        response = api_request_context.delete(
            '/auth/account', headers=headers, data=data
        )
        assert response.status == 200
        assert response.text() == '{"status":"Invite and email deleted"}'

    # Должен падать из-за https://linear.app/devhost/issue/B-572
    @allure.title("Invite new user without limit amount")
    def test_invite_new_user_without_limit_amount(self, auth_token, api_request_context: APIRequestContext) -> None:
        email = 'admin12345@admin.com'
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "email": email,
            "role": "1",
            "limit": 2
        }
        response = api_request_context.post(
            '/auth/account', headers=headers, data=data
        )
        assert response.status == 200
        assert response.text() == '{"create":true,"send":true}'

    @allure.title("Remove new user")
    def test_remove_new_user(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }

        data = {
            "email": 'admin12345@admin.com'
        }
        response = api_request_context.delete(
            '/auth/account', headers=headers, data=data
        )
        assert response.status == 200
        assert response.text() == '{"status":"Invite and email deleted"}'

    @allure.title("Log out all")
    def test_log_out_all(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        response = api_request_context.post(
            '/auth/logoutall', headers=headers
        )
        assert response.status == 204

    @allure.title("Settings filter billing transaction types list")
    def test_filter_billing_transaction_types_list(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        response = api_request_context.get(
            '/api/settings/filter/billing/transaction/types', headers=headers
        )
        assert response.status == 200
        assert response.text() == '[{"code":"subscription","name":"entity.transactionType.subscription"}]'

    @allure.title("Settings billing payments without authorization")
    def test_get_settings_billing_payments_without_authorization(self, api_request_context: APIRequestContext) -> None:
        response = api_request_context.get(
            '/api/settings/billing/payments'
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED
