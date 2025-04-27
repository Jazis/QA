import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, SUCCESS, NOT_FOUND
from data.input_data.random_data import random_numbers_choose_number


@allure.title('Admin company change plan')
def test_admin_company_change_plan(auth_token, api_request_context: APIRequestContext) -> None:
    id = random_numbers_choose_number()

    headers = {
        'Authorization': f"Token {auth_token}"
    }
    data_1 = {
        "provider_id": 2
    }

    response = api_request_context.post(
        f'/api/admin/company/{id}/activate', headers=headers, data=data_1
    )

    assert response.status == 200


    headers_2 = {
        'Authorization': f"Token {auth_token}"
    }
    data = {
            "plan_id": 2
    }
    response_2 = api_request_context.post(
        f'/api/admin/company/{id}/change_plan', headers=headers_2, data=data
    )

    assert response_2.status == 200
    assert response_2.text() == SUCCESS


@allure.title('Admin company change plan without auth')
def test_admin_company_change_plan_without_auth(auth_token, api_request_context: APIRequestContext) -> None:
    id = random_numbers_choose_number()

    response = api_request_context.post(
        f'/api/admin/company/{id}/change_plan'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Admin company change plan wrong company')
def test_admin_company_change_plan_wrong_company(auth_token, api_request_context: APIRequestContext) -> None:

    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.post(
        f'/api/admin/company/1111/change_plan', headers=headers
    )
    assert response.status == 404


@allure.title('Admin company change plan wrong id plan')
def test_admin_company_change_plan_wrong_id_plan(auth_token, api_request_context: APIRequestContext) -> None:

    headers = {
        'Authorization': f"Token {auth_token}"
    }

    data = {
        "plan_id": 6
    }
    response = api_request_context.post(
        f'/api/admin/company/181/change_plan', headers=headers, data=data
    )
    assert response.status == 404
    assert response.text() == NOT_FOUND


@allure.title('Admin company subscription plans list')
def test_admin_company_subscription_plans_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/subscription/plans', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"id":1,"name":"entity.tariff.basic.name","code":"basic"},{"id":2,"name":"entity.tariff.pro.name","code":"pro"},{"id":3,"name":"entity.tariff.private.name","code":"private"}]'


@allure.title('Admin company subscription plans list without auth')
def test_admin_company_subscription_plans_list_without_auth(auth_token, api_request_context: APIRequestContext) -> None:
    response = api_request_context.get(
        '/api/admin/filter/subscription/plans'
    )
    
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED