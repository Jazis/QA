from time import sleep

import allure
import pytest
from playwright.sync_api import Page, expect
from data.input_data.users import USER_01
from pages.pages import Pages
from steps import Steps
from utils.consts import DASHBOARD_REFERRALS_RANGE


class TestDashboardReferrals:
    @pytest.mark.skip("")
    @allure.title("Check page referrals")
    def test_check_page_referrals(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_REFERRALS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Referrals')
        expect(page.locator("//*[@data-test-id='tab']//div[contains(text(), 'All referrals')]")).to_be_visible()
        expect(page.locator("//*[@data-test-id='tab']//div[contains(text(), 'To be paid')]")).to_be_visible()
        expect(page.locator("//*[@data-test-id='tab']//div[contains(text(), 'Started')]")).to_be_visible()
        expect(page.locator("//*[@data-test-id='tab']//div[contains(text(), 'Closed')]")).to_be_visible()
        expect(page.locator("//input[@placeholder='Referral or referrer']")).to_be_visible()

        expect(page.locator("//*[@data-test-id='filters-filters']//span[contains(text(), 'Status')]")).to_be_visible()
        expect(page.locator('//*[@data-test-id="table-header"]//th[1]')).to_have_text('Referral')
        expect(page.locator('//*[@data-test-id="table-header"]//th[2]')).to_have_text('Status')
        expect(page.locator('//*[@data-test-id="table-header"]//th[3]')).to_have_text('Referrer')
        expect(page.locator('(//*[@data-test-id="item-with-pip"])[1]')).to_be_visible()

        pages.dashboard.first_name_company_at_table.check_text('GF399 – gfhgfj gfjghjghd')
        steps.dashboardSteps.check_status_in_row(page, '1', 'To be paid')
        expect(page.locator("(//td//*[contains(@class, 'display_flex align-items_center gap_2')])[1]")).to_have_text('170 – grey company')
        expect(page.locator("//*[@data-test-id='button']//span[contains(text(), 'Payout')]")).to_be_visible()
        expect(page.locator("(//div[contains(@class, 'display_flex align-items_center gap_3')])[3]")).to_have_text('NM202 – nmfdADSF retryty')

        steps.dashboardSteps.check_status_in_row(page, '3', 'Paid')
        steps.dashboardSteps.check_companies_referrals(page, '4', '1 – MTS')
        expect(page.locator("(//div[contains(@class, 'display_flex gap_1')])[2]")).to_have_text('$500.00paid on 2 Sept, 14:15')
        expect(page.locator("(//div[contains(@class, 'display_flex align-items_center gap_3')])[4]")).to_have_text('NE42 – New2Referee')

        steps.dashboardSteps.check_status_in_row(page, '4', 'Closed')
        expect(page.locator("(//td//*[contains(@class, 'display_flex align-items_center gap_2')])[4]")).to_have_text('6 – ConnCompany')
        pages.dashboard.table_pagination.check_text('6 referrals')
        expect(page.locator('(//*[@data-test-id="pip"])[1]')).to_have_css("color", "rgb(69, 143, 255)")
        expect(page.locator('(//*[@data-test-id="pip"])[2]')).to_have_css("color", "rgb(111, 198, 87)")
        expect(page.locator('(//*[@data-test-id="pip"])[4]')).to_have_css("color", "rgba(20, 21, 26, 0.6)")
        expect(page.locator('//*[@data-test-id="button"]//span[contains(text(), "Payout")]')).to_have_css("color", "rgb(255, 255, 255)")

    @pytest.mark.skip("")
    @allure.title("Search by referral")
    def test_search_by_referral(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_REFERRALS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Referrals')
        pages.dashboard.table_pagination.check_text('6 referrals')
        page.locator("//input[@placeholder='Referral or referrer']").fill('123f')
        pages.dashboard.table_pagination.check_text('1 referral')
        pages.dashboard.first_name_company_at_table.check_text('1239 – 123f')
        steps.dashboardSteps.check_status_in_row(page, '1', 'Paid')
        expect(page.locator("(//td//*[contains(@class, 'display_flex align-items_center gap_2')])[1]")).to_have_text('6 – ConnCompany')
        expect(page.locator("(//div[contains(@class, 'display_flex gap_1')])[1]")).to_have_text('$500.00paid on 26 Aug, 12:10')

    @pytest.mark.skip("")
    @allure.title("Filter by status")
    def test_filter_by_status(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_REFERRALS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Referrals')
        pages.dashboard.table_pagination.check_text('6 referrals')
        page.locator("//*[@data-test-id='filters-filters']//span[contains(text(), 'Status')]").click()
        steps.dashboardSteps.check_filters_referrals(page, 'Pending')
        steps.dashboardSteps.check_filters_referrals(page, 'Started')
        steps.dashboardSteps.check_filters_referrals(page, 'Denied')
        steps.dashboardSteps.check_filters_referrals(page, 'Closed')
        steps.dashboardSteps.check_filters_referrals(page, 'To be paid')
        steps.dashboardSteps.check_filters_referrals(page, 'Paid')
        page.locator("//*[@data-test-id='checkbox']//span[contains(text(), 'Closed')]").click()
        page.locator("//*[@data-test-id='checkbox']//span[contains(text(), 'To be paid')]").click()
        pages.dashboard.tag.check_text('Closed, To be paid')
        pages.dashboard.table_pagination.check_text('3 referrals')
        steps.dashboardSteps.check_status_in_row(page, '1', 'To be paid')
        steps.dashboardSteps.check_status_in_row(page, '2', 'Closed')
        steps.dashboardSteps.check_status_in_row(page, '3', 'Closed')

    @pytest.mark.skip("")
    @allure.title("Filter by referrer")
    def test_filter_by_referrer(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_REFERRALS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Referrals')
        pages.dashboard.table_pagination.check_text('6 referrals')
        page.locator('//*[@data-test-id="popper-activator"]//span[contains(text(), "Referrer")]').click()
        steps.dashboardSteps.check_filters_referrals(page, 'grey company')
        steps.dashboardSteps.check_filters_referrals(page, 'ConnCompany')
        steps.dashboardSteps.check_filters_referrals(page, 'ConnCompany')
        steps.dashboardSteps.check_filters_referrals(page, 'MTS')
        page.locator("//*[@data-test-id='checkbox']//span[contains(text(), 'MTS')]").click()
        pages.dashboard.table_pagination.check_text('2 referrals')
        pages.dashboard.tag.check_text('MTS')
        pages.dashboard.first_name_company_at_table.check_text('DS222 – dsef dsfdsg')
        expect(page.locator("(//div[contains(@class, 'display_flex align-items_center gap_3')])[2]")).to_have_text(
            'NM202 – nmfdADSF retryty')
        steps.dashboardSteps.check_companies_referrals(page, '2', '1 – MTS')
        steps.dashboardSteps.check_companies_referrals(page, '3', '1 – MTS')

    @pytest.mark.skip("")
    @allure.title("Check tab To be paid")
    def test_check_tab_to_be_paid(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_REFERRALS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Referrals')
        pages.dashboard.table_pagination.check_text('6 referrals')
        page.locator("//*[@data-test-id='tab']//div[contains(text(), 'To be paid')]").click()
        pages.dashboard.table_pagination.check_text('1 referral')
        pages.dashboard.tag.check_text('To be paid')
        pages.dashboard.first_name_company_at_table.check_text('GF399 – gfhgfj gfjghjghd')
        steps.dashboardSteps.check_status_in_row(page, '1', 'To be paid')
        steps.dashboardSteps.check_companies_referrals(page, '2', '170 – grey company')
        expect(page.locator("//*[@data-test-id='button']//span[contains(text(), 'Payout')]")).to_be_visible()

    @pytest.mark.skip("")
    @allure.title("Check tab Started")
    def test_check_tab_started(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_REFERRALS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Referrals')
        pages.dashboard.table_pagination.check_text('6 referrals')
        page.locator("//*[@data-test-id='tab']//div[contains(text(), 'Started')]").click()
        pages.dashboard.tag.check_text('Started')
        sleep(1.5)
        assert pages.dashboard.no_results.is_visible()
        assert pages.dashboard.text_change_filter.is_visible()
        pages.dashboard.btn_clear_filters.click()
        assert pages.dashboard.tag.is_not_on_page()
        pages.dashboard.table_pagination.check_text('6 referrals')

    @pytest.mark.skip("")
    @allure.title("Check tab Closed")
    def test_check_tab_closed(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_REFERRALS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Referrals')
        pages.dashboard.table_pagination.check_text('6 referrals')
        page.locator("//*[@data-test-id='tab']//div[contains(text(), 'Closed')]").click()
        pages.dashboard.tag.check_text('Closed')
        pages.dashboard.first_name_company_at_table.check_text('NE42 – New2Referee')
        expect(page.locator("(//div[contains(@class, 'display_flex align-items_center gap_3')])[2]")).to_have_text('NE40 – NewReferee')
        steps.dashboardSteps.check_status_in_row(page, '1', 'Closed')
        steps.dashboardSteps.check_status_in_row(page, '2', 'Closed')
        steps.dashboardSteps.check_companies_referrals(page, '2', '6 – ConnCompany')
        steps.dashboardSteps.check_companies_referrals(page, '3', '6 – ConnCompany')
        pages.dashboard.table_pagination.check_text('2 referrals')
