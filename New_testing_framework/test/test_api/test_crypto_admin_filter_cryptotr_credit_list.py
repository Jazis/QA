
import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter crypto transaction credit list')
def test_admin_filter_crypto_transaction_credit_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/credit', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85')


@allure.title('Not admin filter crypto transaction credit list')
def test_not_admin_filter_crypto_transaction_credit_list(auth_token_black_company,
                                                           api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/credit', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter batch crypto transaction credit list without auth')
def test_filter_batch_crypto_transaction_credit_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/cryptotransaction/credit'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
