import allure
from playwright.sync_api import APIRequestContext
from api.function_api import validate_json_keys
from data.responses_texts import AUTH_NOT_PROVIDED
from data.input_data.random_data import random_string
from utils.json_validation import validate_json_schema
from data.input_data.api.users import DATA
import pytest

class TestUsers:

    @allure.title("Cash total")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_api_cash(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/cash/total', headers=headers
        )
        assert response.status == 200
        assert response.text() == '{"balance":1004.65,"pending":101.0}'

    @allure.title("Cash total without authentication")
    def test_get_total_cash_without_auth(self, api_request_context: APIRequestContext) -> None:
        response = api_request_context.get(
            '/api/cash/total'
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Cash types")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_api_cash_types(self, auth_token, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        response = api_request_context.get(
            '/api/filter/cash/types', headers=headers
        )
        assert response.status == 200
        print(response.text())
        validate_json_schema(response.text(), schema_name)

    @allure.title("Filter referral statuses")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_filter_referral_statuses(self, auth_token, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        response = api_request_context.get(
            '/api/filter/referral/statuses', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Filter transaction cards")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_filter_transaction_cards(self, auth_login_user_data_ru,
                                          api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/filter/transaction/cards', headers=headers
        )
        validate_json_schema(response.text(), schema_name)

    @allure.title("Filter transaction cards without authentication")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_filter_transaction_cards_without_authentication(self, api_request_context: APIRequestContext, schema_name) -> None:
        response = api_request_context.get(
            '/api/filter/transaction/cards'
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED
        validate_json_schema(response.text(), schema_name)

    @allure.title("Filter transaction statuses")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_filter_transaction_statuses(self, auth_token, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        response = api_request_context.get(
            '/api/filter/transaction/statuses', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Filter transaction users")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_filter_transaction_users(self, auth_login_user_data_ru,
                                          api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/filter/transaction/users', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Filter transaction users statuses")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_filter_transaction_users(self, auth_token, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        response = api_request_context.get(
            '/api/filter/user/statuses', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get referral campaigns")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_referral_campaigns(self, auth_token, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        response = api_request_context.get(
            '/api/referral/campaigns', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get referral campaigns without auth")
    def test_get_referral_campaigns_without_auth(self, api_request_context: APIRequestContext) -> None:
        response = api_request_context.get(
            '/api/referral/campaigns'
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Get referral program")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_referral_program(self, auth_token, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        response = api_request_context.get(
            '/api/referral/program', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get transaction")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_transaction(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get transaction without auth")
    def test_get_transaction_without_auth(self, api_request_context: APIRequestContext) -> None:
        response = api_request_context.get(
            '/api/transaction'
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Get transaction second page")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_transaction_second_page(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?page=2', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Get transaction 3d page")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_transaction_3_page(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?page=3', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get transactions settled")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_transactions_settled(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?status=settled', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get transactions pending")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_transactions_pending(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?status=pending', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get transactions pending 2d page")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_transactions_pending_second_page(self, auth_login_user_data_ru,
                                                  api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?page=2&status=pending', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get transactions reversed")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_transactions_reversed(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?status=reversed', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get transactions declined")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_transactions_declined(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?status=declined', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get transactions refund")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_transactions_refund(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?status=refund', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Filter by user transactions settled")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_filter_by_user_transactions_settled(self, auth_login_user_data_ru,
                                                 api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?status=settled&user=195', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Filter by card transactions settled")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_filter_by_card_transactions_settled(self, auth_login_user_data_ru,
                                                 api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?status=settled&card=170', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Filter by transactions reversed and date")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_filter_by_transactions_reversed_and_date(self, auth_login_user_data_ru,
                                                      api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?status=reversed&date_start=2024-04-18T06%3A57%3A56.156901Z', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Filter by search term transactions date")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_filter_by_search_term_transactions_date(self, auth_login_user_data_ru,
                                                     api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?search=faceb&date_start=2024-04-21T21:00:00.000Z&date_end=2024-04-22T20:59:59.999Z&page=1&ordering=-authorize_time', headers=headers
        )

        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Filter by transactions pending & card ordering by authorize time")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_filter_by_transactions_pending_card_ordering_authorize_time(self, auth_login_user_data_ru,
                                                                         api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?status=pending&card=173&ordering=authorize_time', headers=headers
        )

        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Filter by transactions pending & card ordering by - authorize time")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_filter_by_transactions_pending_card_ordering__authorize_time(self, auth_login_user_data_ru,
                                                                          api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?status=pending&card=173&ordering=-authorize_time', headers=headers
        )

        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Filter by transactions pending & card ordering by amount")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_filter_by_transactions_pending_card_ordering_amount(self, auth_login_user_data_ru,
                                                                 api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?status=pending&card=173&ordering=amount', headers=headers
        )

        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Filter by transactions settled & card ordering by - amount")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_filter_by_transactions_settled_card_ordering__amount(self, auth_login_user_data_ru,
                                                                  api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?status=settled&card=173&ordering=-amount', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Filter by transactions settled & card ordering by status")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_filter_by_transactions_settled_card_ordering_status(self, auth_login_user_data_ru,
                                                                 api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?status=settled&card=170&ordering=status', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Filter by transactions settled & card ordering by - status")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_filter_by_transactions_settled_card_ordering__status(self, auth_login_user_data_ru,
                                                                  api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction?status=refund&ordering=-status', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get transactions by id pending")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_filter_by_id_transactions_pending(self, auth_login_user_data_ru,
                                               api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction/4144', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get transactions by id settled cross_border_fee")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_filter_by_id_transactions_settled_cross_border_fee(self, auth_login_user_data_ru,
                                                                api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction/4107', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get transactions by id settled fx_fee")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_filter_by_id_transactions_settled_fx_fee(self, auth_login_user_data_ru,
                                                      api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction/4137', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get transactions by id reversed")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_filter_by_id_transactions_reversed(self, auth_login_user_data_ru,
                                                api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction/4088', headers=headers
        )
        assert response.status == 200
        assert validate_json_keys(response.text(),'{"id":4088,"amount":1.0,"authorize_time":"2024-04-18T06:49:01.661837Z","card":{"id":170,"name":"test","number":"6980","user":{"id":190,"email":"rtuuyhgfytr45fghfh@yandex.ru","person":{"first_name":"test do not","last_name":"change"}},"payment_system":"mc"},"country":"US","cross_border_fee":0.0,"currency":"USD","decline_fee":0.0,"decline_reason":null,"direction":"out","fx_fee":0.0,"local_amount":2.0,"mcc":"7311","merchant_info":"FACEBK ADS","merchant_image":"https://dev.api.devhost.io/media/merchant_ico/facebook-dev.png","merchant_name":"Facebook-dev","refund_time":null,"reversed_time":"2024-04-18T06:50:44.462472Z","settled_time":null,"status":"reversed","user":{"id":190,"email":"rtuuyhgfytr45fghfh@yandex.ru","person":{"first_name":"test do not","last_name":"change"}}}') == True

    @allure.title("Get transactions by id declined")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_filter_by_id_transactions_declined(self, auth_login_user_data_ru,
                                                api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction/4099', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get transactions by id refund")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_filter_by_id_transactions_refund(self, auth_login_user_data_ru,
                                              api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/transaction/4130', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get user info")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_user_info(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get user info without auth")
    def test_get_user_info_no_auth(self, auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
        response = api_request_context.get(
            '/api/user'
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Get info by id company")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_info_by_id_company(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user?company=129', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Get info by id company without auth")
    def test_get_info_by_id_company_without_auth(self, auth_login_user_data_ru,
                                                 api_request_context: APIRequestContext) -> None:
        response = api_request_context.get(
            '/api/user?company=129'
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Get info by id company and status 0")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_info_by_id_company_and_status_0(self, auth_login_user_data_ru,
                                                 api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user?company=129&status=0', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get info by id company and status 1 ordering by date joined")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_info_by_id_company_and_status_0_ordering_by_date_joined(self, auth_login_user_data_ru,
                                                                         api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user?company=129&status=1&ordering=date_joined', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get info by id company and status 1 ordering by decline_rate")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_info_by_id_company_and_status_1_ordering_by_decline_rate(self, auth_login_user_data_ru,
                                                                          api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user?company=129&status=1&ordering=decline_rate', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get info by id company and status 1 ordering by - decline_rate")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_info_by_id_company_and_status_1_ordering_by__decline_rate(self, auth_login_user_data_ru,
                                                                           api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user?company=129&status=1&ordering=-decline_rate', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get info by id company and ordering by first_name")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_info_by_id_company_ordering_by_first_name(self, auth_login_user_data_ru,
                                                           api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user?company=129&ordering=person__first_name', headers=headers
        )

        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Get info by id company and ordering by spend")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_info_by_id_company_ordering_by_spend(self, auth_login_user_data_ru,
                                                      api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user?company=129&ordering=spend', headers=headers
        )

        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Get info by id company and ordering by -spend")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_info_by_id_company_ordering_by__spend(self, auth_login_user_data_ru,
                                                       api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user?company=129&ordering=-spend', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Get info by id company and ordering by -person__last_name")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_info_by_id_company_ordering_by__person__last_name(self, auth_login_user_data_ru,
                                                                   api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user?company=129&ordering=-person__last_name', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Get info by id company and date start")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_info_by_id_company_date_start(self, auth_login_user_data_ru,
                                               api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user?company=129&date_start=2024-06-17T00%3A00%3A00Z', headers=headers
        )

        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Get info by search")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_info_by_search(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user?company=129&search=test', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Get info by id company and status -1")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_info_by_id_company_and_status__1(self, auth_login_user_data_ru,
                                                  api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user?company=129&status=-1', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Get user limits")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_user_limits(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user/limits', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Get user roles")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_user_roles(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user/roles', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get user - admin info")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_user_admin_info(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user/190', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get user profile")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_user_profile(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user/profile', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get user profile without auth")
    def test_get_user_profile_without_auth(self, api_request_context: APIRequestContext) -> None:
        response = api_request_context.get(
            '/api/user/profile'
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Get user info emploee")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_user_info_emploee(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user/195', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)

    @allure.title("Get user info invited admin")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_user_info_invited_admin(self, auth_login_user_data_ru, api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user/212', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)
        
    @allure.title("Get user info invited employee")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_get_user_info_invited_employee(self, auth_login_user_data_ru,
                                           api_request_context: APIRequestContext, schema_name) -> None:
        headers = {
            'Authorization': f"Token {auth_login_user_data_ru}"
        }
        response = api_request_context.get(
            '/api/user/211', headers=headers
        )
        assert response.status == 200
        validate_json_schema(response.text(), schema_name)


    @allure.title("Partial update user")
    @pytest.mark.parametrize("schema_name", DATA)
    def test_partial_update_user(self, auth_token, api_request_context: APIRequestContext, schema_name) -> None:
        last_name = random_string(5)
        first_name = random_string(8)
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {
            "person": {
                "first_name": first_name,
                "last_name": last_name,
                "role": 1,
                "limit": 2,
                "limit_amount": 2147483647
            }
        }
        response = api_request_context.patch(
            '/api/user/362', headers=headers, data=data
        )
        assert response.status == 403
        assert response.text() == '{"detail":"You do not have permission to perform this action."}'