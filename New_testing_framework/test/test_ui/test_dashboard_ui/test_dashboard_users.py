import allure
from playwright.sync_api import Page, expect
from data.input_data.users import USER_01
from pages.pages import Pages
from steps import Steps
from utils.consts import DASHBOARD_URL, DASHBOARD_URL_ETALON_RANGE


class TestDashboardUsers:
    @allure.title("Check users page")
    def test_check_users(self, page: Page, pages: Pages,
                         steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        assert pages.dashboard.title_users.is_visible()
        assert pages.dashboard.filter_company.is_visible()
        assert pages.dashboard.filter_by_role.is_visible()
        assert pages.dashboard.filter_status.is_visible()

    @allure.title("Check title table")
    def test_check_title_table(self, page: Page, pages: Pages,
                               steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        expect(page.locator("//thead")).to_have_text(
            "NameRoleEmailIDStatusLimitCompanySpendAvg. Tx amountDecline rateDeclinedInternational18 May – 19 May$1,656.14$58.5418.4%$117.0060.0% ")

    @allure.title("Check total spend users")
    def test_check_total_spend_users(self, page: Page, pages: Pages,
                                     steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        page.locator("(//th//*[@data-test-id = 'info-popover-activator']//div)[2]").click()
        steps.dashboardSteps.check_total_spend(page)

    @allure.title("Check each row table users")
    def test_check_each_row_table_users(self, page: Page, pages: Pages,
                                        steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        steps.dashboardSteps.check_each_row_users(page)

    @allure.title("Check first row in total spend")
    def test_check_first_row_in_total_spend(self, page: Page, pages: Pages,
                                         steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        page.locator("//span[contains(text(), '$529.96')]").hover()
        page.locator("(//td//*[@data-test-id = 'floating-activator'])[1]").click()
        pages.dashboard.info_popover.check_text('Settled$355.00Pending$214.00Reversed$61.00Refund$48.00Cross-border fee$4.52Decline fee$1.50FX fee$2.94')

    @allure.title("Check total spend second row")
    def test_check_total_spend_second_row(self, page: Page, pages: Pages,
                                          steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        page.locator("//span[contains(text(), '$282.96')]").hover()
        page.locator("(//td//*[@data-test-id = 'floating-activator'])[2]").click()
        pages.dashboard.info_popover.check_text('Settled$278.00Cross-border fee$2.73FX fee$2.23')

    @allure.title("Check total spend third row")
    def test_check_total_spend_third_row(self, page: Page, pages: Pages,
                                         steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        page.locator("//span[contains(text(), '$224.04')]").hover()
        page.locator("(//td//*[@data-test-id = 'floating-activator'])[3]").click()
        pages.dashboard.info_popover.check_text('Settled$22.00Pending$214.00Refund$16.00Cross-border fee$3.11FX fee$0.93')

    @allure.title("Check fourth row in total spend")
    def test_check_total_spend_fourth_row(self, page: Page, pages: Pages,
                                          steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        page.locator("//span[contains(text(), '$194.36')]").hover()
        page.locator("(//td//*[@data-test-id = 'floating-activator'])[4]").click()
        pages.dashboard.info_popover.check_text('Settled$155.00Pending$84.00Reversed$61.00Refund$48.00Cross-border fee$1.72Decline fee$1.50FX fee$0.14')

    @allure.title("Check five row in total spend")
    def test_check_total_spend_five_row(self, page: Page, pages: Pages,
                                        steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        page.locator("//span[contains(text(), '$170.36')]").hover()
        page.locator("(//td//*[@data-test-id = 'floating-activator'])[5]").click()
        pages.dashboard.info_popover.check_text('Pending$168.00Cross-border fee$1.43FX fee$0.93')

    @allure.title("Check total spend in sixth row")
    def test_check_total_spend_six_row(self, page: Page, pages: Pages,
                                       steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        page.locator("//span[contains(text(), '$152.50')]").hover()
        page.locator("(//td//*[@data-test-id = 'floating-activator'])[6]").click()
        pages.dashboard.info_popover.check_text('Settled$115.00Pending$84.00Reversed$61.00Refund$48.00Decline fee$1.50')

    @allure.title("Check total spend in seventh row")
    def test_check_total_spend_seven_row(self, page: Page, pages: Pages,
                                         steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        page.locator("//span[contains(text(), '$101.96')]").hover()
        page.locator("(//td//*[@data-test-id = 'floating-activator'])[7]").click()
        pages.dashboard.info_popover.check_text('Settled$55.00Pending$46.00Cross-border fee$0.96')

    @allure.title("Check all names")
    def test_check_all_names(self, page: Page, pages: Pages,
                             steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        steps.dashboardSteps.check_all_names_users(page)

    @allure.title("Check all emails")
    def test_check_all_emails(self, page: Page, pages: Pages,
                              steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        steps.dashboardSteps.check_all_emails_users(page)

    @allure.title("Check all roles")
    def test_check_all_roles(self, page: Page, pages: Pages,
                             steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        steps.dashboardSteps.check_all_roles_users(page)

    @allure.title("Check all statuses")
    def test_check_all_statuses(self, page: Page, pages: Pages,
                                steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        steps.dashboardSteps.check_all_statuses_users(page)

    @allure.title("Check all limits")
    def test_check_all_limits(self, page: Page, pages: Pages,
                              steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        steps.dashboardSteps.check_all_limits_users(page)

    @allure.title("Check all companies")
    def test_check_all_companies(self, page: Page, pages: Pages,
                                 steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        steps.dashboardSteps.check_all_companies_users(page)

    @allure.title("Check all spend")
    def test_check_all_spend(self, page: Page, pages: Pages,
                             steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        steps.dashboardSteps.check_all_spend_users(page)

    @allure.title("Check all avx amount")
    def test_check_all_avx_amount(self, page: Page, pages: Pages,
                                  steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        steps.dashboardSteps.check_all_avg_amount_users(page)

    @allure.title("Check all decline rates")
    def test_check_all_decline_rate(self, page: Page, pages: Pages,
                                    steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=3000)
        steps.dashboardSteps.check_all_decline_rate_users(page)

    @allure.title("Check all internationals")
    def test_check_all_international(self, page: Page, pages: Pages,
                                     steps: Steps, playwright):
        page.goto(DASHBOARD_URL_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.users.click()
        pages.dashboard.title_users.is_on_page(timeout=2500)
        steps.dashboardSteps.check_all_decline_international_users(page)
