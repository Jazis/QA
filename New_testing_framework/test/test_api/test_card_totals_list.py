import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED


@allure.title('Card totals list')
def test_card_totals_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/card/totals', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"settled"')
    assert response.text().__contains__('"pending":')
    assert response.text().__contains__('"refund":')
    assert response.text().__contains__('"reversed_amount":')
    assert response.text().__contains__('"fx_fee":')
    assert response.text().__contains__('"cross_border_fee":')
    assert response.text().__contains__('"decline_fee":')
    assert response.text().__contains__('"spend":')


@allure.title('Card totals list without auth')
def test_card_totals_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/card/totals?date_start=2024-05-18&date_end=2024-06-20'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED


@allure.title('Card totals list filter by date')
def test_card_totals_list_filter_by_date(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/card/totals?date_start=2024-05-18&date_end=2024-06-20', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"settled":2152.0,"pending":2865.0,"refund":1466.0,"reversed_amount":1471.0,"fx_fee":8.53,"cross_border_fee":30.95,"decline_fee":31.0,"spend":3621.48}'


@allure.title('Card totals list filter by date and status')
def test_card_totals_list_filter_by_date_status(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }

    response = api_request_context.get(
        '/api/card/totals?status=1&date_start=2024-05-18&date_end=2024-06-20', headers=headers
    )

    assert response.status == 200
    assert response.text() == '{"settled":2003.0,"pending":2865.0,"refund":1445.0,"reversed_amount":1446.0,"fx_fee":8.53,"cross_border_fee":30.95,"decline_fee":27.0,"spend":3489.48}'
