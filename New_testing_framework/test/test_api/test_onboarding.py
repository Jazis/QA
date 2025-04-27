import allure
import pytest
from playwright.sync_api import APIRequestContext

from data.responses_texts import ENTER_VALID_EMAIL
from data.input_data.random_data import random_string


class TestOnboarding:
    @allure.title("Onboarding polls with referral")
    def test_onboarding_polls_with_referral(self, api_request_context: APIRequestContext) -> None:
        response = api_request_context.get(
            '/auth/onboarding/referrer?referral_code=WAqUzx'
        )
        assert response.status == 200
        assert response.text() == '{"id":6,"name":"ConnCompany"}'

    @allure.title("Get onboarding polls")
    def test_onboarding_polls(self, api_request_context: APIRequestContext) -> None:
        response = api_request_context.get(
            '/auth/onboarding/polls'
        )
        assert response.status == 200
        assert response.text() == '[{"id":1,"text":"poll.question.advertisingNetworks.title","multiple":true,"answers":[{"id":1,"text":"poll.question.advertisingNetworks.answer.facebook.content","image":"https://dev.api.devhost.io/media/answer_ico/facebook-ads.png"},{"id":2,"text":"poll.question.advertisingNetworks.answer.google.content","image":"https://dev.api.devhost.io/media/answer_ico/google-ads.png"},{"id":3,"text":"poll.question.advertisingNetworks.answer.tikTok.content","image":"https://dev.api.devhost.io/media/answer_ico/tiktok-ads.png"},{"id":4,"text":"poll.question.advertisingNetworks.answer.microsoft.content","image":"https://dev.api.devhost.io/media/answer_ico/microsoft-ads.png"},{"id":5,"text":"poll.question.advertisingNetworks.answer.taboola.content","image":"https://dev.api.devhost.io/media/answer_ico/taboola.png"},{"id":6,"text":"poll.question.advertisingNetworks.answer.other.content","image":"https://dev.api.devhost.io/media/answer_ico/other.png"}]},{"id":2,"text":"poll.question.monthlySpend.title","multiple":false,"answers":[{"id":7,"text":"poll.question.monthlySpend.answer.under10000.content","image":null},{"id":8,"text":"poll.question.monthlySpend.answer.10000-30000.content","image":null},{"id":9,"text":"poll.question.monthlySpend.answer.30000-50000.content","image":null},{"id":10,"text":"poll.question.monthlySpend.answer.50000-100000.content","image":null},{"id":11,"text":"poll.question.monthlySpend.answer.over100000.content","image":null}]},{"id":3,"text":"poll.question.team.title","multiple":false,"answers":[{"id":12,"text":"poll.question.team.answer.team.content","image":null},{"id":13,"text":"poll.question.team.answer.solo.content","image":null}]}]'

    @allure.title("Successful polls response solo")
    def test_successful_polls_response_solo(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 13
            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 200
        assert response.text() == '{"is_qualified":true,"is_team":false}'

    @allure.title("Onboarding create lead")
    def test_onboarding_create_lead(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": random_string(8),
            "first_name": random_string(6),
            "last_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 13
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }

        response = api_request_context.post(
            '/auth/onboarding', data=data
        )

        assert response.status == 201
        assert response.text().__contains__("token")

    @allure.title("Get onboarding manager")
    @pytest.mark.usefixtures("auth_token", "api_request_context")
    def test_onboarding_manager(self, auth_token, api_request_context: APIRequestContext) -> None:
        headers = {
            'Authorization': f"Token {auth_token}"
        }
        response = api_request_context.get(
            '/api/onboarding', headers=headers
        )

        assert response.status == 200
        assert response.text().__contains__('"id":1,"name":"Your Manager"')
        assert response.text().__contains__('"telegram":"https://t.me/some_telegram"},"referral_campaign":null')

    @allure.title("Successful polls response company")
    def test_successful_polls_response_company(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ]
        }

        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 200
        assert response.text() == '{"is_qualified":true,"is_team":true}'

    @allure.title("Create team company")
    def test_create_team_company(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": random_string(8),
            "first_name": random_string(6),
            "last_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )

        assert response.status == 201
        assert response.text().__contains__("token")
        assert response.text().__contains__("id")
        assert response.text().__contains__("username")

    @allure.title("Get polls with referral")
    def test_polls_with_referral(self, api_request_context: APIRequestContext) -> None:
        response = api_request_context.get(
            '/auth/onboarding/referrer?referral_code=DvTAIk'
        )
        assert response.status == 200
        assert response.text() == '{"id":1,"name":"MTS"}'

    @allure.title("Onboarding_polls_check_texts")
    def test_onboarding_polls_check_texts(self, api_request_context: APIRequestContext) -> None:
        response = api_request_context.get(
            '/auth/onboarding/polls'
        )
        assert response.status == 200
        assert response.text() == '[{"id":1,"text":"poll.question.advertisingNetworks.title","multiple":true,"answers":[{"id":1,"text":"poll.question.advertisingNetworks.answer.facebook.content","image":"https://dev.api.devhost.io/media/answer_ico/facebook-ads.png"},{"id":2,"text":"poll.question.advertisingNetworks.answer.google.content","image":"https://dev.api.devhost.io/media/answer_ico/google-ads.png"},{"id":3,"text":"poll.question.advertisingNetworks.answer.tikTok.content","image":"https://dev.api.devhost.io/media/answer_ico/tiktok-ads.png"},{"id":4,"text":"poll.question.advertisingNetworks.answer.microsoft.content","image":"https://dev.api.devhost.io/media/answer_ico/microsoft-ads.png"},{"id":5,"text":"poll.question.advertisingNetworks.answer.taboola.content","image":"https://dev.api.devhost.io/media/answer_ico/taboola.png"},{"id":6,"text":"poll.question.advertisingNetworks.answer.other.content","image":"https://dev.api.devhost.io/media/answer_ico/other.png"}]},{"id":2,"text":"poll.question.monthlySpend.title","multiple":false,"answers":[{"id":7,"text":"poll.question.monthlySpend.answer.under10000.content","image":null},{"id":8,"text":"poll.question.monthlySpend.answer.10000-30000.content","image":null},{"id":9,"text":"poll.question.monthlySpend.answer.30000-50000.content","image":null},{"id":10,"text":"poll.question.monthlySpend.answer.50000-100000.content","image":null},{"id":11,"text":"poll.question.monthlySpend.answer.over100000.content","image":null}]},{"id":3,"text":"poll.question.team.title","multiple":false,"answers":[{"id":12,"text":"poll.question.team.answer.team.content","image":null},{"id":13,"text":"poll.question.team.answer.solo.content","image":null}]}]'

    @allure.title("Onboarding under_10000_team")
    def test_under_10000_team(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                2, 4, 6, 7, 12
            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 200
        assert response.text() == '{"is_qualified":false,"is_team":true}'

    @allure.title("Double id of money")
    def test_double_id_of_money(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                2, 8, 9, 13
            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 400
        assert response.text() == '{"answers":["Invalid answers"]}'

    @allure.title("Missed id of team solo")
    def test_missed_id_of_team_solo(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                2, 8, 9, 13
            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 400
        assert response.text() == '{"answers":["Invalid answers"]}'

    @allure.title("Successful 10000_30000 team")
    def test_successful_10000_30000_team(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                1, 2, 3, 4, 5, 6, 8, 12
            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 200
        assert response.text() == '{"is_qualified":true,"is_team":true}'

    @allure.title("30000_50000 team")
    def test_30000_50000_team(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                4, 6, 9, 12
            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 200
        assert response.text() == '{"is_qualified":false,"is_team":true}'

    @allure.title("50000_100000_team")
    def test_50000_100000_team(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                1, 6, 10, 12
            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 200
        assert response.text() == '{"is_qualified":true,"is_team":true}'

    @allure.title("over100000_team")
    def test_over100000_team(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                3, 4, 5, 6, 11, 12
            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 200
        assert response.text() == '{"is_qualified":false,"is_team":true}'

    @allure.title("under_10000_solo")
    def test_under_10000_solo(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                2, 4, 6, 7, 13
            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 200
        assert response.text() == '{"is_qualified":false,"is_team":false}'

    @allure.title("Create 10000_30000 solo")
    def test_10000_30000_solo(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                1, 2, 3, 4, 5, 6, 8, 13
            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 200
        assert response.text() == '{"is_qualified":true,"is_team":false}'

    @allure.title("Create 30000_50000 solo")
    def test_30000_50000_solo(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                13, 4, 6, 9
            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 200
        assert response.text() == '{"is_qualified":false,"is_team":false}'

    @allure.title("Create over_100000 solo")
    def test_over_100000_solo(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                6, 4, 5, 3, 11, 13
            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 200
        assert response.text() == '{"is_qualified":false,"is_team":false}'

    @allure.title("Create 50000_100000 solo")
    def test_50000_100000_solo(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                1, 6, 10, 13
            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 200
        assert response.text() == '{"is_qualified":true,"is_team":false}'

    @allure.title("Post invalid id of network")
    def test_invalid_id_of_network(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                0, 1, 2, 3, 4, 7, 12
            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 400
        assert response.text() == '{"answers":["Invalid pk \\"0\\" - object does not exist."]}'

    @allure.title("Post missed id of money")
    def test_missed_id_of_money(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                2, 4, 5, 6, 13
            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 400
        assert response.text() == '{"answers":["Invalid answers"]}'

    @allure.title("Post double id of team & solo")
    def test_double_id_of_team_solo(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [
                4, 5, 6, 10, 12, 13
            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 400
        assert response.text() == '{"answers":["Invalid answers"]}'

    @allure.title("Post missed all id")
    def test_missed_all_id(self, api_request_context: APIRequestContext) -> None:
        data = {
            "answers": [

            ]
        }
        response = api_request_context.post(
            '/auth/onboarding/polls/response', data=data
        )
        assert response.status == 400
        assert response.text() == '{"answers":["This list may not be empty."]}'

    ###############Onboarding Check Rows When create Company
    @allure.title("Post wrong email")
    def test_email_wrong(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + 'gmail.com',
            "password": random_string(8),
            "first_name": random_string(6),
            "last_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == ENTER_VALID_EMAIL

    @allure.title("Post wrong email")
    def test_email_wrong_2(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": "testin@g*((*)&!@$!$!$#mail.ru",
            "password": random_string(8),
            "first_name": random_string(6),
            "last_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == ENTER_VALID_EMAIL

    @allure.title("Post empty email")
    def test_email_empty(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": " ",
            "password": random_string(8),
            "first_name": random_string(6),
            "last_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400

    @allure.title("Post wrong email")
    def test_email_wrong_3(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": "tes@tin@gmail.ru",
            "password": random_string(8),
            "first_name": random_string(6),
            "last_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == ENTER_VALID_EMAIL

    @allure.title("Post email with space")
    def test_email_with_space(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": "tes tin@gmail.ru",
            "password": random_string(8),
            "first_name": random_string(6),
            "last_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == ENTER_VALID_EMAIL

    @allure.title("Post email wrong")
    def test_email_wrong_4(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": "cv#$%^&^&&()*&(7899uigfrdszsdfghyyt@djgkdffdszx.tyuti",
            "password": random_string(8),
            "first_name": random_string(6),
            "last_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == ENTER_VALID_EMAIL

    @allure.title("Post email long")
    def test_long_email(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": "cvbgfrdseruyuyuiyyut7898789nbfvcdrewsdfghujnbvcxzsdfgtrewqasdfv@ghdgfjhdjgkdfjsgdfgruetyeuriwerupweruwpqwcnwjnkjhjghjghjgjhggytvutyctrex23dsfdszx.tyuti",
            "password": random_string(8),
            "first_name": random_string(6),
            "last_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == ENTER_VALID_EMAIL

    @allure.title("Post min length password")
    def test_min_length_pass(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": "1234567",
            "first_name": random_string(6),
            "last_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )

        assert response.status == 400
        assert response.text() == '{"password":["This password is too short. It must contain at least 8 characters.","This password is too common.","This password is entirely numeric."]}'

    @allure.title("Post big length password")
    def test_big_length_pass(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": random_string(40),
            "first_name": random_string(6),
            "last_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )

        assert response.status == 201
        assert response.text().__contains__("user")
        assert response.text().__contains__("token")

    @allure.title("Post password only numeric")
    def test_pass_only_numeric(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": "1234567847684565765",
            "first_name": random_string(6),
            "last_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == '{"password":["This password is entirely numeric."]}'

    @allure.title("Password too comon")
    def test_paasword_too_common(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": "qwerty1234",
            "first_name": random_string(6),
            "last_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == '{"password":["This password is too common."]}'

    @allure.title("Password with spaces")
    def test_paasword_with_space(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": random_string(3) + " " + random_string(4),
            "first_name": random_string(6),
            "last_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )

        assert response.status == 201
        assert response.text().__contains__("id")
        assert response.text().__contains__("token")
        assert response.text().__contains__("username")

    @allure.title("Company name min length")
    def test_company_name_min_length(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": random_string(8),
            "first_name": random_string(6),
            "last_name": random_string(4),
            "company_name": random_string(2),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )

        assert response.status == 400
        assert response.text() == '{"company_name":["Company name must be at least 3 characters long"]}'

    @allure.title("Company name max length")
    def test_company_name_max_length(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": random_string(8),
            "first_name": random_string(6),
            "last_name": random_string(4),
            "company_name": "evfdb fg gfhfdghfghjdfgh ghgfhdfgjghjdgjhfghtyuetu tyu rt yr tr  er ewrwerwelrmweljkr lmeoirehgru irjfierfioeuieurioeutioewuruweouwqieuwiqejwjh fdjkfhjdhgjfshgjfdhgjfdhgk vbvbvbvbvbbvvhbfjdhdjgfdjkfhjksahfjksdhfjkdshf ",
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == '{"company_name":["Company name must be at most 50 characters long"]}'

    @allure.title("Last name - max length")
    def test_last_name_max_length(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": random_string(8),
            "first_name": random_string(6),
            "last_name": "ghghfgjhgjghj gfhgfhgfhdfghfghfgh ghghgjghjhgjdjg nbvnbvmnbmhjhgjtytryt bgfhfghgjhgjghjhgjhgjhgjdghjhg",
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == '{"last_name":["Last name must be at most 24 characters long"]}'

    @allure.title("First name - empty row & without last name")
    def test_first_name_empty_row(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": random_string(8),
            "first_name": "",
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == '{"first_name":["This field may not be blank."],"last_name":["This field is required."]}'

    @allure.title("Last name - empty row")
    def test_last_name_empty_row(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": random_string(8),
            "first_name": random_string(6),
            "last_name": "",
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == '{"last_name":["This field may not be blank."]}'

    @allure.title("First name - max length")
    def test_first_name_max_length(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": random_string(8),
            "first_name": "ghghfgjhgjghj gfhgfhgfhdfghfghfgh ghghgjghjhgjdjg nbvnbvmnbmhjhgjtytryt bgfhfghgjhgjghjhgjhgjhgjdghjhg",
            "last_name": random_string(6),
            "company_name": random_string(6),
            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == '{"first_name":["First name must be at most 24 characters long"]}'

    @allure.title("Create without telegram & first_name")
    def test_create_without_telegram_first_name(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": random_string(6),
            "last_name": random_string(6),
            "company_name": random_string(6),
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == '{"first_name":["This field is required."],"telegram":["This field is required."]}'

    @allure.title("Check @ telegram")
    def test_check_tegram_row(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": random_string(9),
            "last_name": random_string(6),
            "first_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == ''

    @allure.title("Create without company name")
    def test_create_without_company_name(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": random_string(9),
            "last_name": random_string(6),
            "first_name": random_string(4),

            "telegram": "@telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == '{"company_name":["This field is required."]}'

    @allure.title("Create without ga_id")
    def test_create_without_ga_id(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": random_string(9),
            "last_name": random_string(6),
            "first_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "telegram",

            "recaptcha": random_string(5),
            "answers": [
                1, 2, 3, 4, 5, 6, 9, 12
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 201

    @allure.title("Create with empty answers")
    def test_create_with_empty_answers(self, api_request_context: APIRequestContext) -> None:
        data = {
            "email": random_string(7) + '@gmail.com',
            "password": random_string(9),
            "last_name": random_string(6),
            "first_name": random_string(4),
            "company_name": random_string(6),
            "telegram": "telegram",
            "ga_id": random_string(4),
            "recaptcha": random_string(5),
            "answers": [
            ],
            "locale": "en-GB",
            "timezone": "UTC+03:3",
            "referral_code": "75"
        }
        response = api_request_context.post(
            '/auth/onboarding', data=data
        )
        assert response.status == 400
        assert response.text() == '{"answers":["This list may not be empty."]}'


