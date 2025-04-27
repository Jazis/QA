import allure
from playwright.sync_api import APIRequestContext


@allure.title('Admin plans list')
def test_admin_plans_list(auth_token, api_request_context: APIRequestContext) -> None:
    headers = {
        'Authorization': f"Token {auth_token}"
    }
    response = api_request_context.get(
        'api/admin/plans', headers=headers
    )

    assert response.status == 200
    assert response.text().__contains__('[{"name":"entity.tariff.basic.name","text":"entity.tariff.basic.text","features":[{"name":"entity.feature.cryptoTopUp","is_available":true,"value":"3%","is_default":true},{"name":"entity.feature.wireTopUp","is_available":true,"value":"3%","is_default":true},{"name":"entity.feature.usBins","is_available":true,"value":"3","is_default":true},{"name":"entity.feature.freeCards","is_available":true,"value":null,"is_default":true},{"name":"entity.feature.cardTransfer","is_available":true,"value":null,"is_default":false},{"name":"entity.feature.userLimits","is_available":true,"value":null,"is_default":false},{"name":"entity.feature.internationalBins","is_available":true,"value":null,"is_default":false}]')
    assert response.text().__contains__('"prices":[{"id":2,"amount":1000.0,"period":"annual"},{"id":1,"amount":100.0,"period":"monthly"}]},{"name":"entity.tariff.pro.name","text":"entity.tariff.pro.text","features":[{"name":"entity.feature.cryptoTopUp","is_available":true,"value":"2%","is_default":true},{"name":"entity.feature.wireTopUp","is_available":true,"value":"2%","is_default":true},{"name":"entity.feature.usBins","is_available":true,"value":"11","is_default":true},{"name":"entity.feature.freeCards","is_available":true,"value":null,"is_default":true},{"name":"entity.feature.cardTransfer","is_available":true,"value":null,"is_default":false},{"name":"entity.feature.userLimits","is_available":true,"value":null,"is_default":false},{"name":"entity.feature.internationalBins","is_available":true,"value":null,"is_default":false}]')
    assert response.text().__contains__('"prices":[{"id":3,"amount":471.0,"period":"monthly"}]},{"name":"entity.tariff.private.name","text":"entity.tariff.private.text","features":[{"name":"entity.feature.cryptoTopUp","is_available":true,"value":"2%","is_default":true},{"name":"entity.feature.wireTopUp","is_available":true,"value":"2%","is_default":true},{"name":"entity.feature.usBins","is_available":true,"value":"11","is_default":true},{"name":"entity.feature.freeCards","is_available":true,"value":null,"is_default":true},{"name":"entity.feature.cardTransfer","is_available":true,"value":null,"is_default":false},{"name":"entity.feature.userLimits","is_available":true,"value":null,"is_default":false},{"name":"entity.feature.internationalBins","is_available":true,"value":null,"is_default":false}]')
    assert response.text().__contains__('"prices":[{"id":4,"amount":600.0,"period":"monthly"}]}')
    assert response.text().__contains__('{"name":"entity.tariff.trial.name","text":"entity.tariff.trial.text","features":[{"name":"entity.feature.cryptoTopUp","is_available":true,"value":"2%","is_default":true},{"name":"entity.feature.wireTopUp","is_available":true,"value":"2%","is_default":true},{"name":"entity.feature.usBins","is_available":true,"value":"9","is_default":true},{"name":"entity.feature.freeCards","is_available":true,"value":null,"is_default":true},{"name":"entity.feature.cardTransfer","is_available":false,"value":null,"is_default":false},{"name":"entity.feature.userLimits","is_available":true,"value":null,"is_default":false},{"name":"entity.feature.internationalBins","is_available":false,"value":null,"is_default":false}]')
    assert response.text().__contains__('"prices":[{"id":5,"amount":0.0,"period":"biweekly"}]}]')
