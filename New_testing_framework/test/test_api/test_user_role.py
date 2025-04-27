import allure
from data.input_data.users import VALID_USERS_WITH_ROLES
from data.input_data.api.user_role import USER_ROLE
from api.function_api import auth_token_function
from data.responses_texts import PERMISSIONS
from utils.json_validation import validate_json_schema
import pytest
from playwright.sync_api import APIRequestContext, Playwright

@pytest.mark.parametrize("url, schema_name", USER_ROLE)
@pytest.mark.parametrize("user", VALID_USERS_WITH_ROLES)
def test_user_role_company_edit(request, api_request_context: APIRequestContext, user, url, schema_name):
    token = auth_token_function(request=request, username = user.login, password = user.password)
    headers = {
        'Authorization': f"Token {token}",
        'Content-Type': 'application/json'
    }
    data = {"cards_quantity_limit":50}
    response = api_request_context.patch(
        url, headers=headers, data=data
    )
    assert response.status == 200
    validate_json_schema(response.text(), schema_name)
    
@pytest.mark.parametrize("user", VALID_USERS_WITH_ROLES)
def test_user_role_company_edit(request, api_request_context: APIRequestContext, user):
    token = auth_token_function(request=request, username = user.login, password = user.password)
    headers = {
        'Authorization': f"Token {token}",
        'Content-Type': 'application/json'
    }
    data = {"name":"qwe qwe","email":"qwe@qwe.qwe","card_provider":2,"owner_type":"client"}
    response = api_request_context.post(
            '/api/admin/company', headers=headers, data=data
    )
    if user.role == "Finance" or user.role == "Viewer":
        assert response.status == 403
    else:
        assert response.status in (200, 400) 