import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


########### Дописать создание

@allure.title('Admin batch create with exist id')
def test_admin_batch_create_with_exist_id(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    data = {"ids":
        [
            5
        ],
        "batch_id": 1,
        "operation": "issue"
    }

    response = api_request_context.post(
        '/api/admin/batch/credit', headers=headers, data=data
    )

    assert response.status == 400
    assert response.text() == '{"status":"error","error_message":"This transaction already has a credit transfer, please check (credit_id: 61)"}'


@allure.title('Admin batch create with wrong transaction id')
def test_admin_batch_create_with_wrong_transaction_id(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    data = {"ids":
        [
            590
        ],
        "batch_id": 1,
        "operation": "issue"
    }

    response = api_request_context.post(
        '/api/admin/batch/credit', headers=headers, data=data
    )

    assert response.status == 400
    assert response.text() == '{"status":"error","error_message":"Uncorrected crypto_transaction id"}'


@allure.title('Admin batch create with wrong operation')
def test_admin_batch_create_with_wrong_operation(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    data = {"ids":
        [
            590
        ],
        "batch_id": 1,
        "operation": "netting"
    }

    response = api_request_context.post(
        '/api/admin/batch/credit', headers=headers, data=data
    )

    assert response.status == 400
    assert response.text() == '{"operation":["\\"netting\\" is not a valid choice."]}'


@allure.title('Not admin batch create')
def test_not_admin_batch_create(auth_token_black_company, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    data = {"ids":
        [
            5
        ],
        "batch_id": 1,
        "operation": "issue"
    }

    response = api_request_context.post(
        '/api/admin/batch/credit', headers=headers, data=data
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Batch create without auth')
def test_batch_create_without_auth(api_request_context: APIRequestContext) -> None:

    data = {"ids":
        [
            5
        ],
        "batch_id": 1,
        "operation": "issue"
    }

    response = api_request_context.post(
        '/api/admin/batch/credit', data=data
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Not admin batch create without body')
def test_not_admin_batch_create_without_body(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.post(
        '/api/admin/batch/credit', headers=headers
    )

    assert response.status == 400
    assert response.text() == '{"operation":["This field is required."]}'
