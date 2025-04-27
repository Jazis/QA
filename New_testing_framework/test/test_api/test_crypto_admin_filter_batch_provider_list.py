
import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter batch provider list')
def test_admin_filter_batch_provider_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/admin/filter/batch/provider', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('{"id":2,"name":"ConnexPay","stage":null}')
    assert response.text().__contains__('{"id":3,"name":"Fireblocks","stage":null}')
    assert response.text().__contains__('{"id":4,"name":"Offramp Provider","stage":"offramp"}')
    assert response.text().__contains__('{"id":5,"name":"Qolo","stage":null}')


@allure.title('Not admin filter batch provider list')
def test_not_admin_filter_batch_provider_list(auth_token_black_company,
                                             api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }

    response = api_request_context.get(
        '/api/admin/filter/batch/provider', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter batch provider list without auth')
def test_filter_batch_provider_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/batch/provider'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Filter batch provider list without auth wrong way')
def test_filter_batch_provider_list_without_auth_wrong_way(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/batch/provid'
    )
    assert response.status == 404
    