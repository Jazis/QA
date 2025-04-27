import allure
from playwright.sync_api import APIRequestContext

from data.input_data.random_data import random_string, random_numbers
from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS

class TestAdminCompanyPartialUpdate:
    @allure.title('Admin company partial update')
    def test_admin_company_partial_update(self, auth_token, api_request_context: APIRequestContext) -> None:
        name = random_string(6)
        cards = random_numbers()
        balance = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": name,
            "cards_quantity_limit": cards,
            "use_decline_fee": "false",
            "critical_balance": balance
        }
        response = api_request_context.patch(
            '/api/admin/company/127', headers=headers, data=data
        )

        assert response.status == 200
        assert response.json()["id"] == 127
        assert response.json()["created_at"] == "2024-04-15T10:01:05.961655Z"
        assert response.json()["name"] == name
        assert response.json()["cards_quantity_limit"] == cards
        assert response.json()["use_decline_fee"] == False
        assert response.json()["critical_balance"] == balance
        assert response.json()["subscription"]["id"] == 14
        assert response.json()["subscription"]["plan"]["id"] == 1
        assert response.json()["subscription"]["plan"]["name"] == "Basic Monthly"
        assert response.json()["subscription"]["plan"]["code"] == "basic_monthly"
        assert response.json()["subscription"]["plan"]["price"] == f"{100}.00"
        assert response.json()["subscription"]["plan"]["period"] == "Monthly - 30"
        assert response.json()["subscription"]["plan"]["tariff"]["id"] == 1
        assert response.json()["subscription"]["plan"]["tariff"]["name"] == "Basic"
        assert response.json()["subscription"]["plan"]["tariff"]["code"] == "basic"
        assert response.json()["subscription"]["plan"]["tariff"]["crypto_topup_fee"] == 3.0
        assert response.json()["subscription"]["plan"]["tariff"]["wire_topup_fee"] == 3.0
        assert response.json()["subscription"]["plan"]["tariff"]["available_bins_count"] == 3
        assert response.json()["subscription"]["plan"]["tariff"]["is_international_bins"] == False
        assert response.json()["subscription"]["plan"]["tariff"]["is_free_cards"] == True
        assert response.json()["subscription"]["status"] == "Active"
        assert response.json()["subscription"]["started_at"] == "2024-04-15T10:01:05.961655Z"
        assert response.json()["subscription"]["expires_at"] == None
        assert response.json()["subscription"]["ended_at"] == None
        assert response.json()["wallet_addresses"] == []
        assert response.json()["status"] == "active"


    @allure.title('Admin company partial update name')
    def test_admin_company_partial_update_name(self, auth_token, api_request_context: APIRequestContext) -> None:
        name = random_string(6)
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "name": name
        }
        response = api_request_context.patch(
            '/api/admin/company/125', headers=headers, data=data
        )
        assert response.status == 200
        assert response.json()["id"] == 125
        assert response.json()["created_at"] == "2024-04-12T07:53:35.753605Z"
        assert response.json()["name"] == name
        assert response.json()["cards_quantity_limit"] == 50
        assert response.json()["use_decline_fee"] == False
        assert response.json()["critical_balance"] == 100.0 #f"{100}.00"
        assert response.json()["subscription"]["id"] == 13
        assert response.json()["subscription"]["plan"]["id"] == 1
        assert response.json()["subscription"]["plan"]["name"] == "Basic Monthly"
        assert response.json()["subscription"]["plan"]["code"] == "basic_monthly"
        assert response.json()["subscription"]["plan"]["price"] == f"{100}.00"
        assert response.json()["subscription"]["plan"]["period"] == "Monthly - 30"
        assert response.json()["subscription"]["plan"]["tariff"]["id"] == 1
        assert response.json()["subscription"]["plan"]["tariff"]["name"] == "Basic"
        assert response.json()["subscription"]["plan"]["tariff"]["code"] == "basic"
        assert response.json()["subscription"]["plan"]["tariff"]["crypto_topup_fee"] == 3.00
        assert response.json()["subscription"]["plan"]["tariff"]["wire_topup_fee"] == 3.00
        assert response.json()["subscription"]["plan"]["tariff"]["available_bins_count"] == 3
        assert response.json()["subscription"]["plan"]["tariff"]["is_international_bins"] == False
        assert response.json()["subscription"]["plan"]["tariff"]["is_free_cards"] == True
        assert response.json()["subscription"]["status"] == "Active"
        assert response.json()["subscription"]["started_at"] == "2024-04-12T07:53:35.753605Z"
        assert response.json()["subscription"]["expires_at"] == None
        assert response.json()["subscription"]["ended_at"] == None
        assert response.json()["wallet_addresses"] == []
        assert response.json()["status"] == "active"


    @allure.title('Admin company partial update cards_quantity_limit')
    def test_admin_company_partial_update_cards_quantity_limit(self, auth_token, api_request_context: APIRequestContext) -> None:
        cards_quantity_limit = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "cards_quantity_limit": cards_quantity_limit
        }
        response = api_request_context.patch(
            '/api/admin/company/144', headers=headers, data=data
        )

        assert response.status == 200
        assert response.json()["id"] == 144
        assert response.json()["created_at"] == "2024-04-26T09:34:09.524084Z"
        assert response.json()["name"] == "test r"
        assert response.json()["cards_quantity_limit"] == cards_quantity_limit
        assert response.json()["use_decline_fee"] == False
        assert response.json()["critical_balance"] == 100.0 #f"{100}.00"
        assert response.json()["subscription"]["id"] == 16
        assert response.json()["subscription"]["plan"]["id"] == 1
        assert response.json()["subscription"]["plan"]["name"] == "Basic Monthly"
        assert response.json()["subscription"]["plan"]["code"] == "basic_monthly"
        assert response.json()["subscription"]["plan"]["price"] == f"{100}.00"
        assert response.json()["subscription"]["plan"]["period"] == "Monthly - 30"
        assert response.json()["subscription"]["plan"]["tariff"]["id"] == 1
        assert response.json()["subscription"]["plan"]["tariff"]["name"] == "Basic"
        assert response.json()["subscription"]["plan"]["tariff"]["code"] == "basic"
        assert response.json()["subscription"]["plan"]["tariff"]["crypto_topup_fee"] == 3.00
        assert response.json()["subscription"]["plan"]["tariff"]["wire_topup_fee"] == 3.00
        assert response.json()["subscription"]["plan"]["tariff"]["available_bins_count"] == 3
        assert response.json()["subscription"]["plan"]["tariff"]["is_international_bins"] == False
        assert response.json()["subscription"]["plan"]["tariff"]["is_free_cards"] == True
        assert response.json()["subscription"]["status"] == "Active"
        assert response.json()["subscription"]["started_at"] == "2024-04-26T09:35:48.841652Z"
        assert response.json()["subscription"]["expires_at"] == None
        assert response.json()["subscription"]["ended_at"] == None
        assert response.json()["wallet_addresses"] == []
        assert response.json()["status"] == "active"


    @allure.title('Admin company partial update use_decline_fee')
    def test_admin_company_partial_update_use_decline_fee(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "use_decline_fee": True
        }
        response = api_request_context.patch(
            '/api/admin/company/165', headers=headers, data=data
        )
        assert response.status == 200
        assert response.json()["id"] == 165
        assert response.json()["created_at"] == "2024-05-15T07:38:34.540356Z"
        assert response.json()["name"] == "BeGKroLput lESp"
        assert response.json()["cards_quantity_limit"] == 50
        assert response.json()["use_decline_fee"] == True
        assert response.json()["critical_balance"] == 100.0 #f"{100}.00"
        assert response.json()["activated_at"] == "2024-08-20T07:52:31.482859Z"
        assert response.json()["subscription"]["id"] == 29
        assert response.json()["subscription"]["plan"]["id"] == 3
        assert response.json()["subscription"]["plan"]["name"] == "Pro Monthly"
        assert response.json()["subscription"]["plan"]["code"] == "pro_monthly"
        assert response.json()["subscription"]["plan"]["price"] == f"{471}.00"
        assert response.json()["subscription"]["plan"]["period"] == "Monthly - 30"
        assert response.json()["subscription"]["plan"]["tariff"]["id"] == 2
        assert response.json()["subscription"]["plan"]["tariff"]["name"] == "Pro"
        assert response.json()["subscription"]["plan"]["tariff"]["code"] == "pro"
        assert response.json()["subscription"]["plan"]["tariff"]["crypto_topup_fee"] == 2.00
        assert response.json()["subscription"]["plan"]["tariff"]["wire_topup_fee"] == 2.00
        assert response.json()["subscription"]["plan"]["tariff"]["available_bins_count"] == 11
        assert response.json()["subscription"]["plan"]["tariff"]["is_international_bins"] == False
        assert response.json()["subscription"]["plan"]["tariff"]["is_free_cards"] == True
        assert response.json()["subscription"]["status"] == "Active"
        assert response.json()["wallet_addresses"] == []
        assert response.json()["status"] == "active"


    @allure.title('Admin company partial update critical_balance')
    def test_admin_company_partial_update_critical_balance(self, auth_token, api_request_context: APIRequestContext) -> None:
        balance = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "critical_balance": balance
        }
        response = api_request_context.patch(
            '/api/admin/company/166', headers=headers, data=data
        )

        assert response.status == 200
        assert response.json()["id"] == 166
        assert response.json()["created_at"] == "2024-05-16T10:08:28.375810Z"
        assert response.json()["name"] == "Test Dashboard"
        assert response.json()["cards_quantity_limit"] == 509
        assert response.json()["use_decline_fee"] == False
        assert response.json()["critical_balance"] == balance #f"{balance}.00"
        assert response.json()["activated_at"] == "2025-01-28T05:53:59.861434Z"
        assert response.json()["subscription"]["id"] == 19
        assert response.json()["subscription"]["plan"]["id"] == 1
        assert response.json()["subscription"]["plan"]["name"] == "Basic Monthly"
        assert response.json()["subscription"]["plan"]["code"] == "basic_monthly"
        assert response.json()["subscription"]["plan"]["price"] == f"{100}.00"
        assert response.json()["subscription"]["plan"]["period"] == "Monthly - 30"
        assert response.json()["subscription"]["plan"]["tariff"]["id"] == 1
        assert response.json()["subscription"]["plan"]["tariff"]["name"] == "Basic"
        assert response.json()["subscription"]["plan"]["tariff"]["code"] == "basic"
        assert response.json()["subscription"]["plan"]["tariff"]["crypto_topup_fee"] == 3.00
        assert response.json()["subscription"]["plan"]["tariff"]["wire_topup_fee"] == 3.00
        assert response.json()["subscription"]["plan"]["tariff"]["available_bins_count"] == 3
        assert response.json()["subscription"]["plan"]["tariff"]["is_international_bins"] == False
        assert response.json()["subscription"]["plan"]["tariff"]["is_free_cards"] == True
        assert response.json()["subscription"]["status"] == "Active"
        assert response.json()["wallet_addresses"] == []
        assert response.json()["status"] == "active"


    @allure.title('Admin company partial update without auth')
    def test_admin_company_partial_update_without_auth(self, api_request_context: APIRequestContext) -> None:
        data = {
            "critical_balance": 100
        }
        response = api_request_context.patch(
            '/api/admin/company/166', data=data
        )

        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED


    @allure.title('Admin company partial update not admin')
    def test_admin_company_partial_update_not_admin(self, auth_token, api_request_context: APIRequestContext) -> None:

        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "critical_balance": 55
        }
        response = api_request_context.patch(
            '/api/admin/company/166', headers=headers, data=data
        )

        assert response.status == 403
        assert response.text() == PERMISSIONS

