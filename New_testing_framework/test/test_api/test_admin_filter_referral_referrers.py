
import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter referral referrers')
def test_admin_filter_referral_referrers(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/referral/referrers', headers=headers
    )
    
    assert response.status == 200
    assert response.text().__contains__('"id":1,"name":"MTS","owner_type":"client"')
    assert response.text().__contains__('"id":6,"name":"ConnCompany","owner_type":"client"')


@allure.title('Admin filter referral referrers not admin')
def test_admin_filter_referral_referrers_not_admin(auth_login_user_data_ru,
                                                      api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/referral/referrers', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin filter referral referrers without auth')
def test_admin_filter_referral_referrers_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/referral/referrers'
    )
    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
