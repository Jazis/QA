import pytest
import allure
from playwright.sync_api import APIRequestContext
from data.input_data.deleted_endpoints import DELETED_ADMIN_ENDPOINTS


@allure.title('Check that deleted admin endpoints still be deleted')
@pytest.mark.parametrize('endpoint', DELETED_ADMIN_ENDPOINTS)
def test_deleted_admin_endpoints(auth_token, api_request_context: APIRequestContext, endpoint: str) -> None:
    """
    Test to ensure that deleted admin endpoints return a 404 status code.
    """
    headers = {'Authorization': f"Token {auth_token}"}
    response = api_request_context.get(endpoint, headers=headers)
    assert response.status == 404, f"Expected 404 for endpoint {endpoint}, but got {response.status}"
