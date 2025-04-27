import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter referral statuses list')
def test_admin_filter_referral_statuses_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/referral/statuses', headers=headers
    )

    assert response.status == 200
    assert response.text() == '[{"code":"waitlist","name":"entity.referralCampaignStatus.waitlist"},{"code":"onboarded","name":"entity.referralCampaignStatus.onboarded"},{"code":"denied","name":"entity.referralCampaignStatus.denied"},{"code":"closed","name":"entity.referralCampaignStatus.closed"},{"code":"to_be_paid","name":"entity.referralCampaignStatus.toBePaid"},{"code":"paid","name":"entity.referralCampaignStatus.paid"}]'


@allure.title('Filter referral statuses list not admin')
def test_filter_referral_statuses_list_not_admin(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/referral/statuses', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Admin filter referral statuses list without auth')
def test_filter_referral_statuses_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/referral/statuses'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
