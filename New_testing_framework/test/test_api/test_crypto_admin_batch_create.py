import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


########### Дописать создание

@allure.title('Admin batch create with wrong address')
def test_admin_batch_create_with_wrong_address(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    data = {"ids": [
        4
    ],
        "address_id": 2,
        "address": "address",
        "provider_id": 3
    }

    response = api_request_context.post(
        '/api/admin/batch/batch', headers=headers, data=data
    )

    assert response.status == 400
    assert response.text() == '{"address_id":["Uncorrected address id"]}'


@allure.title('Not admin batch create with wrong address')
def test_admin_batch_create_with_wrong_address(auth_token_black_company,
                                               api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token_black_company}"
    }
    data = {"ids": [
        4
    ],
        "address_id": 2,
        "address": "address",
        "provider_id": 3
    }

    response = api_request_context.post(
        '/api/admin/batch/batch', headers=headers, data=data
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin batch create without auth')
def test_admin_batch_create_without_auth(api_request_context: APIRequestContext) -> None:
    data = {"ids": [
        4
    ],
        "address_id": 2,
        "address": "address",
        "provider_id": 3
    }

    response = api_request_context.post(
        '/api/admin/batch/batch', data=data
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
