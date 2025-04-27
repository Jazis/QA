import allure
from playwright.sync_api import APIRequestContext

from data.responses_texts import AUTH_NOT_PROVIDED, PERMISSIONS


@allure.title('Admin filter subscriptions companies list')
def test_admin_filter_subscriptions_companies_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        '/api/admin/filter/subscription/companies', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('"id":1,"name":"MTS","owner_type":"client"')
    assert response.text().__contains__('"id":6,"name":"ConnCompany","owner_type":"client"}'),('"id":81,"name":"Leonard_Gulgowski45 + Dibbert","owner_type":"client"')
    assert response.text().__contains__('"id":149,"name":"POgbGBXmNE gIfH","owner_type":"client"')
    assert response.text().__contains__('"id":165,"name":"BeGKroLput lESp","owner_type":"client"'),('"id":168,"name":"red company","owner_type":"client"')
    assert response.text().__contains__('"id":173,"name":"black company","owner_type":"client"')
    assert response.text().__contains__('"id":196,"name":"testvvvvfg fdggr","owner_type":"client"'), ('"id":197,"name":"Subscrition check","owner_type":"client"')
    assert response.text().__contains__('"id":198,"name":"subscrition test","owner_type":"client"'),('"id":199,"name":"subscr. test","owner_type":"client"')
    assert response.text().__contains__('"id":200,"name":"1398h 3476n","owner_type":"client"'),('"id":201,"name":"ki877 gfhghg","owner_type":"client"')
    assert response.text().__contains__('"id":202,"name":"nmfdADSF retryty","owner_type":"client"'),('"id":203,"name":"tesat rfgt5443","owner_type":"client"')
    assert response.text().__contains__('"id":206,"name":"hmhjgkhgk hkghkhkghk","owner_type":"client"'),('"id":210,"name":"trytud fhfghgfjgfj","owner_type":"client"')
    assert response.text().__contains__('"id":222,"name":"dsef dsfdsg","owner_type":"client"'),('"id":249,"name":"uyuytuyturyur","owner_type":"client"')
    assert response.text().__contains__('"id":258,"name":"kqrbRZ","owner_type":"client"'),('"id":307,"name":"KcWgPYvtUj cQMH","owner_type":"client"')
    assert response.text().__contains__('"id":321,"name":"456867r 4656776tuyg","owner_type":"client"'),('"id":322,"name":"company","owner_type":"client"')
    assert response.text().__contains__('"id":340,"name":"5вкевапав пвапаврары","owner_type":"client"'),('"id":361,"name":"caznjevZTp FshT","owner_type":"client"')
    assert response.text().__contains__('"id":366,"name":"ROhrlm","owner_type":"client"'),('"id":367,"name":"MJUuWF","owner_type":"client"')
    assert response.text().__contains__('"id":368,"name":"VYNvw_878978лоролролргнг89089890809890890890890898","owner_type":"client"')
    assert response.text().__contains__('"id":369,"name":"SuGiz","owner_type":"own"'),('"id":370,"name":"CkEmqQPYlV HIGg","owner_type":"client"')
    assert response.text().__contains__('"id":371,"name":"4546546","owner_type":"client"')
    assert response.text().__contains__('"id":376,"name":"eWbfPL","owner_type":"client"'),('"id":377,"name":"soNmKC","owner_type":"client"')
    assert response.text().__contains__('"id":378,"name":"uWOhLE","owner_type":"client"')
    assert response.text().__contains__('"id":379,"name":"string","owner_type":"client"'),('"id":380,"name":"ZgIoFU","owner_type":"client"')
    assert response.text().__contains__('"id":381,"name":"fiANtp","owner_type":"client"')
    assert response.text().__contains__('"id":384,"name":"LyRDBJ","owner_type":"client"'),('"id":385,"name":"CfTWIa","owner_type":"client"')
    assert response.text().__contains__('"id":386,"name":"HYOvCy","owner_type":"client"')
    assert response.text().__contains__('"id":388,"name":"FryDfPToVq zWlM","owner_type":"client"')


@allure.title('Filter subscriptions companies list not admin')
def test_admin_filter_subscriptions_companies_list_not_admin(auth_login_user_data_ru, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_login_user_data_ru}"
    }
    response = api_request_context.get(
        '/api/admin/filter/subscription/companies', headers=headers
    )

    assert response.status == 403
    assert response.text() == PERMISSIONS


@allure.title('Filter subscriptions companies list without auth')
def test_admin_filter_subscriptions_companies_list_without_auth(api_request_context: APIRequestContext) -> None:

    response = api_request_context.get(
        '/api/admin/filter/subscription/companies'
    )

    assert response.status == 401
    assert response.text() == AUTH_NOT_PROVIDED
