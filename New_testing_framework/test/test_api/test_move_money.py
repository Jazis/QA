import allure
from playwright.sync_api import APIRequestContext
from data.responses_texts import *
# from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS, GREATER_ZERO, NOT_ENOUGH_MONEY, DIFFERENT_PROVIDERS, INVALID_ACCOUNT_DEPOSIT, INVALID_OPERATION_DEPOSIT
from data.input_data.random_data import random_numbers


# credit Connex - 18
# credit Qolo - 807
# main Connex - 11, 847- Qolo
# netting Connex - 500, Qolo - 810
# revenue Connex - 19, Qolo - 816
# fee Connex - 17, Qolo - 808

class TestMoveMoney:
    @allure.title("Deposit with wrong id account")
    def test_move_money_wrong_account_deposit(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 7.99, "from_account": 5, "to_account": 7, "operation": "deposit"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == INVALID_ACCOUNT_DEPOSIT

    @allure.title("Deposit with not admin")
    def test_deposit_with_not_admin(self, auth_token_black_company, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token_black_company}"
        }
        data = {"amount": 2, "from_account": 2, "to_account": 5, "operation": "deposit"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 403
        assert response.text() == PERMISSIONS

    @allure.title("Deposit without auth")
    def test_deposit_without_auth(self, api_request_context: APIRequestContext) -> None:
        data = {
            "amount": 2, "from_account": 5, "to_account": 7, "operation": "deposit"}
        response = api_request_context.post(
            '/api/admin/move_money', data=data
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Wrong name of Deposit")
    def test_wrong_deposit(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2, "from_account": 11, "to_account": 5, "operation": "Deposit"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == INVALID_OPERATION_DEPOSIT

    @allure.title("Deposit")
    def test_deposit(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 30.67, "from_account": 11, "to_account": 5, "operation": "deposit"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Deposit Qolo")
    def test_deposit_qolo(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 20.999, "from_account": 847, "to_account": 813, "operation": "deposit"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Deposit with zero")
    def test_deposit_with_zero(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 0, "from_account": 2, "to_account": 5, "operation": "deposit"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Deposit with -5")
    def test_deposit_with_not_integer(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": -5, "from_account": 2, "to_account": 5, "operation": "deposit"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Deposit from credit")
    def test_deposit_from_credit(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 1, "from_account": 18, "to_account": 5, "operation": "deposit"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == INVALID_ACCOUNT_DEPOSIT

    @allure.title("Deposit not enough money")
    def test_deposit_not_enough_money(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2000000000000, "from_account": 11, "to_account": 5, "operation": "deposit"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == NOT_ENOUGH_MONEY

    @allure.title("Deposit different providers")
    def test_deposit_different_providers(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 1, "from_account": 11, "to_account": 807, "operation": "deposit"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == DIFFERENT_PROVIDERS

    @allure.title("Withdrawal with wrong id account")
    def test_move_money_withdrawal_wrong_account(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 5, "from_account": 6, "to_account": 7, "operation": "withdrawal"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == INVALID_ACCOUNT_WITHDRAWAL

    @allure.title("Withdrawal with not admin")
    def test_withdrawal_with_not_admin(self, auth_token_black_company, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token_black_company}"
        }
        data = {"amount": 45, "from_account": 5, "to_account": 7, "operation": "withdrawal"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 403
        assert response.text() == PERMISSIONS

    @allure.title("Withdrawal without auth")
    def test_withdrawal_without_auth(self, api_request_context: APIRequestContext) -> None:
        data = {"amount": 2, "from_account": 5, "to_account": 7, "operation": "withdrawal"}

        response = api_request_context.post(
            '/api/admin/move_money', data=data
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Wrong name of Withdrawal")
    def test_wrong_withdrawal(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2, "from_account": 11, "to_account": 5, "operation": "Withdrawal"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid operation: Withdrawal"}'

    @allure.title("Withdrawal")
    def test_withdrawal(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 5, "from_account": 4, "to_account": 11, "operation": "withdrawal"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Withdrawal Qolo")
    def test_withdrawal_qolo(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 1.1, "from_account": 545, "to_account": 847, "operation": "withdrawal"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Withdrawal same account")
    def test_withdrawal_same_account(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 3, "from_account": 813, "to_account": 813, "operation": "withdrawal"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"From account and To account can`t be the same"}'

    @allure.title("Withdrawal to credit")
    def test_withdrawal_to_credit(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 6, "from_account": 4, "to_account": 18, "operation": "withdrawal"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == INVALID_ACCOUNT_WITHDRAWAL

    @allure.title("Withdrawal with 0")
    def test_withdrawal_with_zero(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 0, "from_account": 4, "to_account": 2, "operation": "withdrawal"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Withdrawal with -10")
    def test_withdrawal_not_natural(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": -10, "from_account": 813, "to_account": 11, "operation": "withdrawal"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Withdrawal with different providers")
    def test_move_money_withdrawal_different_providers(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 5, "from_account": 4, "to_account": 847, "operation": "withdrawal"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == DIFFERENT_PROVIDERS

    @allure.title("Credit Issue (Legacy) with wrong id account")
    def test_move_money_wrong_account_credit_issue_legacy(self, auth_token,
                                                          api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2, "from_account": 5, "to_account": 7, "operation": "credit_issue"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid account types for Credit_issue operation"}'

    @allure.title("Credit Issue (Legacy) with not admin")
    def test_credit_issue_legacy_with_not_admin(self, auth_token_black_company,
                                                api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token_black_company}"
        }
        data = {"amount": 2, "from_account": 5, "to_account": 7, "operation": "credit_issue"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 403
        assert response.text() == PERMISSIONS

    @allure.title("Credit Issue (Legacy) without auth")
    def test_credit_issue_legacy_without_auth(self, api_request_context: APIRequestContext) -> None:
        data = {"amount": 2, "from_account": 5, "to_account": 7, "operation": "credit_issue"}

        response = api_request_context.post(
            '/api/admin/move_money', data=data
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Wrong Credit Issue (Legacy)")
    def test_wrong_credit_issue_legacy(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 3, "from_account": 11, "to_account": 5, "operation": "Credit_issue"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid operation: Credit_issue"}'

    @allure.title("Credit Issue (Legacy)")
    def test_credit_issue_legacy(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 5, "from_account": 18, "to_account": 4, "operation": "credit_issue"}

        response = api_request_context.post(
            "/api/admin/move_money", headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Credit Issue (Legacy) Qolo")
    def test_credit_issue_legacy_qolo(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2.555, "from_account": 807, "to_account": 813, "operation": "credit_issue"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Credit Issue (Legacy) not natural")
    def test_credit_issue_legacy_not_natural(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": -1.00, "from_account": 807, "to_account": 813, "operation": "credit_issue"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Credit Issue (Legacy) with zero")
    def test_credit_issue_legacy_with_zero(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 0, "from_account": 18, "to_account": 4, "operation": "credit_issue"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Credit Issue (Legacy) different providers")
    def test_credit_issue_legacy_different_providers(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 1, "from_account": 11, "to_account": 807, "operation": "credit_issue"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == DIFFERENT_PROVIDERS

    @allure.title("Credit Issue Wire with wrong id account")
    def test_move_money_wrong_account_credit_issue_wire(self, auth_token,
                                                        api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2, "from_account": 4, "to_account": 182, "operation": "credit_issue_wire"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )

        assert response.status == 400
        assert response.text() == '{"detail":"Invalid account types for Credit_issue_wire operation"}'

    @allure.title("Credit Issue Wire with not admin")
    def test_credit_issue_wire_with_not_admin(self, auth_token_black_company,
                                              api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token_black_company}"
        }
        data = {"amount": 2, "from_account": 5, "to_account": 7, "operation": "credit_issue_wire"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 403
        assert response.text() == PERMISSIONS

    @allure.title("Credit Issue Wire without auth")
    def test_credit_issue_wire_without_auth(self, api_request_context: APIRequestContext) -> None:
        data = {"amount": 2, "from_account": 5, "to_account": 7, "operation": "credit_issue_wire"}

        response = api_request_context.post(
            '/api/admin/move_money', data=data
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Wrong Credit Issue Wire")
    def test_wrong_credit_issue_wire(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2, "from_account": 11, "to_account": 5, "operation": "Credit_issue_wire"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid operation: Credit_issue_wire"}'

    @allure.title("Credit Issue Wire")
    def test_credit_issue_wire(self, auth_token, api_request_context: APIRequestContext) -> None:
        n = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": n, "from_account": 18, "to_account": 4, "operation": "credit_issue_wire"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Credit Issue Wire Qolo")
    def test_credit_issue_wire_qolo(self, auth_token, api_request_context: APIRequestContext) -> None:
        n = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": n, "from_account": 807, "to_account": 813, "operation": "credit_issue_wire"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Credit Issue Wire not natural")
    def test_credit_issue_wire_not_natural(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": -2, "from_account": 807, "to_account": 813, "operation": "credit_issue_wire"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Credit Issue Wire different providers")
    def test_credit_issue_wire_different_providers(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 4, "from_account": 807, "to_account": 4, "operation": "credit_issue_wire"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == DIFFERENT_PROVIDERS

    @allure.title("Credit Issue Wire with zero")
    def test_credit_issue_wire_with_zero(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 0, "from_account": 18, "to_account": 4, "operation": "credit_issue_wire"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Credit Issue Wire from main")
    def test_credit_issue_wire_from_main(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 1, "from_account": 11, "to_account": 4, "operation": "credit_issue_wire"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid account types for Credit_issue_wire operation"}'

    @allure.title("Credit Clear with wrong id account")
    def test_move_money_wrong_account_credit_clear(self, auth_token,
                                                   api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2, "from_account": 5, "to_account": 4, "operation": "credit_clear"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid account types for Credit_clear operation"}'

    @allure.title("Credit Clear with not admin")
    def test_credit_clear_with_not_admin(self, auth_token_black_company,
                                         api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token_black_company}"
        }
        data = {"amount": 2, "from_account": 2, "to_account": 18, "operation": "credit_clear"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 403
        assert response.text() == PERMISSIONS

    @allure.title("Credit Clear without auth")
    def test_credit_clear_without_auth(self, api_request_context: APIRequestContext) -> None:
        data = {"amount": 2, "from_account": 2, "to_account": 18, "operation": "credit_clear"}

        response = api_request_context.post(
            '/api/admin/move_money', data=data
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Wrong name of Credit Clear")
    def test_wrong_credit_clear(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2, "from_account": 11, "to_account": 18, "operation": "Credit_clear"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid operation: Credit_clear"}'

    @allure.title("Credit Clear")
    def test_credit_clear(self, auth_token, api_request_context: APIRequestContext) -> None:
        n = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": n, "from_account": 11, "to_account": 18, "operation": "credit_clear"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Credit Clear Qolo")
    def test_credit_clear_qolo(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2, "from_account": 847, "to_account": 807, "operation": "credit_clear"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Credit Clear not natural")
    def test_credit_clear_not_natural(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": -2, "from_account": 847, "to_account": 807, "operation": "credit_clear"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Credit Clear with zero")
    def test_credit_clear_with_zero(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 0, "from_account": 11, "to_account": 18, "operation": "credit_clear"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Credit Clear from Credit Qolo")
    def test_credit_clear_from_credit_qolo(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2, "from_account": 807, "to_account": 847, "operation": "credit_clear"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid account types for Credit_clear operation"}'

    @allure.title("Credit Clear different providers")
    def test_credit_clear_different_providers(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2, "from_account": 11, "to_account": 807, "operation": "credit_clear"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == DIFFERENT_PROVIDERS

    @allure.title("Subscription with wrong id account")
    def test_move_money_wrong_account_subscription(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2, "from_account": 4, "to_account": 15, "operation": "subscription"}
        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid account types for Subscription operation"}'

    @allure.title("Subscription with not admin")
    def test_subscription_with_not_admin(self, auth_token_black_company,
                                         api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token_black_company}"
        }
        data = {"amount": 2, "from_account": 4, "to_account": 19, "operation": "subscription"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 403
        assert response.text() == PERMISSIONS

    @allure.title("Subscription without auth")
    def test_subscription_without_auth(self, api_request_context: APIRequestContext) -> None:
        data = {"amount": 2.6, "from_account": 4, "to_account": 19, "operation": "subscription"}

        response = api_request_context.post(
            '/api/admin/move_money', data=data
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Wrong Subscription")
    def test_wrong_subscription(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 7, "from_account": 4, "to_account": 19, "operation": "Subscription"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid operation: Subscription"}'

    @allure.title("Subscription")
    def test_subscription(self, auth_token, api_request_context: APIRequestContext) -> None:
        n = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": n, "from_account": 4, "to_account": 19, "operation": "subscription"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Subscription Qolo")
    def test_subscription_qolo(self, auth_token, api_request_context: APIRequestContext) -> None:
        n = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": n, "from_account": 813, "to_account": 816, "operation": "subscription"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Subscription not natural")
    def test_subscription_not_natural(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": -2, "from_account": 813, "to_account": 816, "operation": "subscription"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Subscription with zero")
    def test_subscription_zero(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 0, "from_account": 4, "to_account": 19, "operation": "subscription"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Subscription from credit")
    def test_subscription_from_credit(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 9, "from_account": 18, "to_account": 5, "operation": "subscription"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid account types for Subscription operation"}'

    @allure.title("Subscription not enough money")
    def test_subscription_not_enough_money(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 20, "from_account": 366, "to_account": 19, "operation": "subscription"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == NOT_ENOUGH_MONEY

    @allure.title("Subscription different providers")
    def test_subscription_different_providers(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2, "from_account": 813, "to_account": 19, "operation": "subscription"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == DIFFERENT_PROVIDERS

    @allure.title("Fee to Main with wrong id account")
    def test_move_money_wrong_account_fee_to_main(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2, "from_account": 4, "to_account": 807, "operation": "money_outbound"}
        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == DIFFERENT_PROVIDERS

    @allure.title("Fee to Main with not admin")
    def test_fee_to_main_with_not_admin(self, auth_token_black_company,
                                        api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token_black_company}"
        }
        data = {"amount": 2, "from_account": 17, "to_account": 11, "operation": "money_outbound"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 403
        assert response.text() == PERMISSIONS

    @allure.title("Fee to Main without auth")
    def test_fee_to_main_without_auth(self, api_request_context: APIRequestContext) -> None:
        data = {"amount": 2, "from_account": 17, "to_account": 11, "operation": "money_outbound"}

        response = api_request_context.post(
            '/api/admin/move_money', data=data
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Wrong Fee to Main")
    def test_wrong_fee_to_main(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2, "from_account": 17, "to_account": 11, "operation": "Money_outbound"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid operation: Money_outbound"}'

    @allure.title("Fee to Main")
    def test_fee_to_main(self, auth_token, api_request_context: APIRequestContext) -> None:
        n = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": n, "from_account": 17, "to_account": 11, "operation": "money_outbound"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Fee to Main Qolo")
    def test_fee_to_main_qolo(self, auth_token, api_request_context: APIRequestContext) -> None:
        n = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": n, "from_account": 808, "to_account": 847, "operation": "money_outbound"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Fee to Main not natural")
    def test_fee_to_main_not_natural(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": -2, "from_account": 808, "to_account": 847, "operation": "money_outbound"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Fee to Main with zero")
    def test_fee_to_main_with_zero(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 0, "from_account": 17, "to_account": 11, "operation": "money_outbound"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Fee to Main from credit")
    def test_fee_to_main_from_credit(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 1, "from_account": 807, "to_account": 808, "operation": "money_outbound"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid account types for Money_outbound operation"}'

    @allure.title("Fee to Main not enough money")
    def test_fee_to_main_not_enough_money(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 1000000, "from_account": 17, "to_account": 11, "operation": "money_outbound"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == NOT_ENOUGH_MONEY

    @allure.title("Fee to Main different providers")
    def test_fee_to_main_different_providers(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 1, "from_account": 17, "to_account": 847, "operation": "money_outbound"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == DIFFERENT_PROVIDERS

    @allure.title("Revenue to Main with wrong id account")
    def test_move_money_wrong_account_revenue_to_main(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2, "from_account": 19, "to_account": 2000, "operation": "revenue_to_main"}
        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 500

    @allure.title("Revenue to Main with not admin")
    def test_revenue_to_main_with_not_admin(self, auth_token_black_company,
                                            api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token_black_company}"
        }
        data = {"amount": 3, "from_account": 19, "to_account": 11, "operation": "revenue_to_main"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 403
        assert response.text() == PERMISSIONS

    @allure.title("Revenue to Main without auth")
    def test_revenue_to_main_without_auth(self, api_request_context: APIRequestContext) -> None:
        data = {"amount": 5, "from_account": 19, "to_account": 11, "operation": "revenue_to_main"}

        response = api_request_context.post(
            '/api/admin/move_money', data=data
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Wrong Revenue to Main")
    def test_wrong_revenue_to_main(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 7, "from_account": 19, "to_account": 11, "operation": "Revenue_to_main"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid operation: Revenue_to_main"}'

    @allure.title("Revenue to Main")
    def test_revenue_to_main(self, auth_token, api_request_context: APIRequestContext) -> None:
        n = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": n, "from_account": 19, "to_account": 11, "operation": "revenue_to_main"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Revenue to Main Qolo")
    def test_revenue_to_main_qolo(self, auth_token, api_request_context: APIRequestContext) -> None:
        n = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": n, "from_account": 816, "to_account": 847, "operation": "revenue_to_main"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Revenue to Main with zero")
    def test_revenue_to_main_with_zero(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 0, "from_account": 816, "to_account": 847, "operation": "revenue_to_main"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Revenue to Main not natural")
    def test_revenue_to_main_not_natural(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": -10, "from_account": 816, "to_account": 847, "operation": "revenue_to_main"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Revenue to Main not enough money")
    def test_revenue_to_main_not_enough_money(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 10000, "from_account": 19, "to_account": 11, "operation": "revenue_to_main"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )

        assert response.status == 400
        assert response.text() == NOT_ENOUGH_MONEY

    @allure.title("Revenue to Main different providers")
    def test_revenue_to_main_different_providers(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 10000, "from_account": 19, "to_account": 847, "operation": "revenue_to_main"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )

        assert response.status == 400
        assert response.text() == DIFFERENT_PROVIDERS

    @allure.title("Main to Revenue with wrong id account")
    def test_move_money_wrong_account_main_to_revenue(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2, "from_account": 11, "to_account": 2999, "operation": "main_to_revenue"}
        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 500

    @allure.title("Main to Revenue with not admin")
    def test_main_to_revenue_with_not_admin(self, auth_token_black_company,
                                            api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token_black_company}"
        }
        data = {"amount": 2, "from_account": 11, "to_account": 19, "operation": "main_to_revenue"}
        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 403
        assert response.text() == PERMISSIONS

    @allure.title("Main to Revenue without auth")
    def test_main_to_revenue_without_auth(self, api_request_context: APIRequestContext) -> None:
        data = {
            "amount": 6, "from_account": 11, "to_account": 19, "operation": "main_to_revenue"}
        response = api_request_context.post(
            '/api/admin/move_money', data=data
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Wrong name of Main to Revenue")
    def test_wrong_main_to_revenue(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2.7, "from_account": 11, "to_account": 816, "operation": "Main_to_revenue"}
        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == DIFFERENT_PROVIDERS

    @allure.title("Main to Revenue")
    def test_main_to_revenue(self, auth_token, api_request_context: APIRequestContext) -> None:
        n = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": n, "from_account": 11, "to_account": 19, "operation": "main_to_revenue"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Main to Revenue Qolo")
    def test_main_to_revenue_qolo(self, auth_token, api_request_context: APIRequestContext) -> None:
        n = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": n, "from_account": 847, "to_account": 816, "operation": "main_to_revenue"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Main to Revenue with zero")
    def test_main_to_revenue_with_zero(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 0, "from_account": 847, "to_account": 816, "operation": "main_to_revenue"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Main to Revenue not natural")
    def test_main_to_revenue_not_natural(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": -10, "from_account": 847, "to_account": 816, "operation": "main_to_revenue"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Main to Revenue different providers")
    def test_main_to_revenue_different_providers(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 10, "from_account": 11, "to_account": 816, "operation": "main_to_revenue"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == DIFFERENT_PROVIDERS

    @allure.title("Main to Revenue from client")
    def test_main_to_revenue_from_client(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 1, "from_account": 4, "to_account": 11, "operation": "main_to_revenue"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid account types for Main_to_revenue operation"}'

    @allure.title("Gift with wrong id account")
    def test_move_money_wrong_account_gift(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 10, "from_account": 19, "to_account": 2000, "operation": "gift"}
        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 500

    @allure.title("Gift with not admin")
    def test_gift_with_not_admin(self, auth_token_black_company,
                                 api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token_black_company}"
        }
        data = {"amount": 11, "from_account": 19, "to_account": 11, "operation": "gift"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 403
        assert response.text() == PERMISSIONS

    @allure.title("Gift without auth")
    def test_gift_without_auth(self, api_request_context: APIRequestContext) -> None:
        data = {"amount": 12, "from_account": 19, "to_account": 5, "operation": "gift"}

        response = api_request_context.post(
            '/api/admin/move_money', data=data
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Wrong gift")
    def test_wrong_gift(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 22, "from_account": 19, "to_account": 4, "operation": "Gift"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid operation: Gift"}'

    @allure.title("Gift")
    def test_gift(self, auth_token, api_request_context: APIRequestContext) -> None:
        n = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": n, "from_account": 19, "to_account": 4, "operation": "gift"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Gift Qolo")
    def test_gift_qolo(self, auth_token, api_request_context: APIRequestContext) -> None:
        n = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": n, "from_account": 816, "to_account": 813, "operation": "gift"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Gift wrong accounts")
    def test_gift_wrong_accounts(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 2.7, "from_account": 813, "to_account": 816, "operation": "gift"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )

        assert response.status == 400
        assert response.text() == '{"detail":"Invalid account types for Gift operation"}'

    @allure.title("Gift with zero")
    def test_gift_with_zero(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 0, "from_account": 19, "to_account": 4, "operation": "gift"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Gift not natural")
    def test_gift_not_natural(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": -10, "from_account": 19, "to_account": 4, "operation": "gift"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Gift different providers")
    def test_gift_different_providers(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 10, "from_account": 816, "to_account": 4, "operation": "gift"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == DIFFERENT_PROVIDERS

    @allure.title("Inter Account Transfer with wrong id account")
    def test_move_money_wrong_account_inter_account_transfer(self, auth_token,
                                                             api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 7, "from_account": 4, "to_account": 1999, "operation": "inter-account-transfer"}
        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 500

    @allure.title("Inter Account Transfer with not admin")
    def test_inter_account_transfer_with_not_admin(self, auth_token_black_company,
                                                   api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token_black_company}"
        }
        data = {"amount": 4, "from_account": 4, "to_account": 5, "operation": "inter-account-transfer"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 403
        assert response.text() == PERMISSIONS

    @allure.title("Inter Account Transfer without auth")
    def test_inter_account_transfer_without_auth(self, api_request_context: APIRequestContext) -> None:
        data = {
            "amount": 6, "from_account": 4, "to_account": 5, "operation": "inter-account-transfer"}
        response = api_request_context.post(
            '/api/admin/move_money', data=data
        )
        assert response.status == 401
        assert response.text() == AUTH_NOT_PROVIDED

    @allure.title("Wrong Inter Account Transfer")
    def test_wrong_inter_account_transfer(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 20, "from_account": 4, "to_account": 5, "operation": "Inter-account-transfer"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == '{"detail":"Invalid operation: Inter-account-transfer"}'

    @allure.title("Inter Account Transfer")
    def test_inter_account_transfer(self, auth_token, api_request_context: APIRequestContext) -> None:
        n = random_numbers()
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": n, "from_account": 4, "to_account": 5, "operation": "inter-account-transfer"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 200

    @allure.title("Inter Account Transfer with zero")
    def test_inter_account_transfer_with_zero(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 0, "from_account": 5, "to_account": 4, "operation": "inter-account-transfer"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Inter Account Transfer not natural")
    def test_inter_account_transfer_not_natural(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": -10, "from_account": 5, "to_account": 4, "operation": "inter-account-transfer"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )

        assert response.status == 400
        assert response.text() == GREATER_ZERO

    @allure.title("Inter Account Transfer from main")
    def test_inter_account_transfer_from_main(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 10, "from_account": 11, "to_account": 4, "operation": "inter-account-transfer"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )

        assert response.status == 400
        assert response.text() == '{"detail":"Invalid account types for Inter-account-transfer operation"}'

    @allure.title("Inter Account Transfer different providers")
    def test_inter_account_transfer_different_providers(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        data = {"amount": 10, "from_account": 813, "to_account": 4, "operation": "inter-account-transfer"}

        response = api_request_context.post(
            '/api/admin/move_money', headers=headers, data=data
        )
        assert response.status == 400
        assert response.text() == DIFFERENT_PROVIDERS


