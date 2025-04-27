import allure
from playwright.sync_api import Page
from data.input_data.users import USER_01
from pages.pages import Pages
from steps import Steps
from utils.consts import DASHBOARD_URL_CARDS_ETALON_RANGE


class TestDashboardCards:
    @allure.title("Check page cards")
    def test_check_cards(self, page: Page, pages: Pages,
                         steps: Steps, playwright):
        page.goto(DASHBOARD_URL_CARDS_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cards')
        assert pages.dashboard.title_cards.is_visible()
        assert pages.dashboard.filter_account.is_visible()
        assert pages.dashboard.filter_company.is_visible()
        assert pages.dashboard.filter_by_user.is_visible()
        assert pages.dashboard.filter_status.is_visible()
        assert pages.dashboard.filter_network.is_visible()
        assert pages.dashboard.filter_limit.is_visible()

    #TODO:Написать тест на фильтрацию по провайдеру

    @allure.title("Check total row table")
    def test_check_total_row_table(self, page: Page, pages: Pages,
                                   steps: Steps, playwright):
        page.goto(DASHBOARD_URL_CARDS_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cards')
        pages.dashboard.total_row_table.check_text("18 May – 19 May$1,656.14")

    @allure.title("Check rows in total spend")
    def test_check_all_total_spend(self, page: Page, pages: Pages,
                                   steps: Steps, playwright):
        page.goto(DASHBOARD_URL_CARDS_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cards')
        page.locator("(//th//*[@data-test-id = 'floating-activator'])[2]").click()
        steps.dashboardSteps.check_total_spend(page)
        assert pages.dashboard.total_spend_sum.is_visible()

    @allure.title("Check each row table")
    def test_check_each_row_table(self, page: Page, pages: Pages,
                                  steps: Steps, playwright):
        page.goto(DASHBOARD_URL_CARDS_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cards')
        steps.dashboardSteps.check_cards_each_row_table(page)

    @allure.title("Check total spend")
    def test_check_total_spend(self, page: Page, pages: Pages,
                               steps: Steps, playwright):
        page.goto(DASHBOARD_URL_CARDS_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cards')
        page.locator("//span[contains(text(), '$529.96')]").hover()
        page.locator("(//td//*[@data-test-id = 'floating-activator'])[1]").hover()
        pages.dashboard.modal_info_in_row.check_text('Settled$355.00Pending$214.00Reversed$61.00Refund$48.00Cross-border fee$4.52Decline fee$1.50FX fee$2.94')

    @allure.title("Check total settled")
    def test_check_total_settled(self, page: Page, pages: Pages,
                                 steps: Steps, playwright):
        page.goto(DASHBOARD_URL_CARDS_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cards')
        page.locator("//span[contains(text(), '$227.96')]").hover()
        page.locator("(//td//*[@data-test-id = 'floating-activator'])[2]").click()
        pages.dashboard.modal_info_in_row.check_text('Settled$223.00Cross-border fee$2.73FX fee$2.23')

    @allure.title("Check total pending")
    def test_check_total_pending(self, page: Page, pages: Pages,
                                 steps: Steps, playwright):
        page.goto(DASHBOARD_URL_CARDS_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cards')
        page.locator("//span[contains(text(), '$217.32')]").hover()
        page.locator("(//td//*[@data-test-id = 'floating-activator'])[3]").click()
        pages.dashboard.modal_info_in_row.check_text('Pending$214.00Cross-border fee$2.39FX fee$0.93')

    @allure.title("Check total decline")
    def test_check_total_decline(self, page: Page, pages: Pages,
                                 steps: Steps, playwright):
        page.goto(DASHBOARD_URL_CARDS_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cards')
        page.locator("//span[contains(text(), '$152.50')]").hover()
        page.locator("(//td//*[@data-test-id = 'floating-activator'])[6]").click()
        pages.dashboard.modal_info_in_row.check_text('Settled$115.00Pending$84.00Reversed$61.00Refund$48.00Decline fee$1.50')

    @allure.title("Check total pending & settled")
    def test_check_total_pending_settled(self, page: Page, pages: Pages,
                                         steps: Steps, playwright):
        page.goto(DASHBOARD_URL_CARDS_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cards')
        page.locator("//span[contains(text(), '$101.96')]").hover()
        page.locator("(//td//*[@data-test-id = 'floating-activator'])[7]").click()
        pages.dashboard.modal_info_in_row.check_text('Settled$55.00Pending$46.00Cross-border fee$0.96')

    @allure.title("Check all companies")
    def test_check_all_companies(self, page: Page, pages: Pages,
                                 steps: Steps, playwright):
        page.goto(DASHBOARD_URL_CARDS_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cards')
        steps.dashboardSteps.check_companies_names_on_cards(page)

    @allure.title("Check all cards")
    def test_check_all_cards(self, page: Page, pages: Pages,
                             steps: Steps, playwright):
        page.goto(DASHBOARD_URL_CARDS_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cards')
        steps.dashboardSteps.check_cards_on_cards_page(page)

    @allure.title("Check all statuses")
    def test_check_all_status_cards(self, page: Page, pages: Pages,
                                    steps: Steps, playwright):
        page.goto(DASHBOARD_URL_CARDS_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cards')
        steps.dashboardSteps.check_status_on_cards_page(page)

    @allure.title("Check all bins and providers cards")
    def test_check_all_bins_providers_cards(self, page: Page, pages: Pages,
                                   steps: Steps, playwright):
        page.goto(DASHBOARD_URL_CARDS_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cards')
        steps.dashboardSteps.check_bins_on_cards_page(page)
        steps.dashboardSteps.check_providers_on_cards_page(page)

    @allure.title("Check all limits cards")
    def test_check_all_limits_cards(self, page: Page, pages: Pages,
                                   steps: Steps, playwright):
        page.goto(DASHBOARD_URL_CARDS_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cards')
        steps.dashboardSteps.check_limits_on_cards_page(page)

    @allure.title("Check all spend")
    def test_check_all_spend(self, page: Page, pages: Pages,
                                   steps: Steps, playwright):
        page.goto(DASHBOARD_URL_CARDS_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cards')
        steps.dashboardSteps.check_spend_on_cards_page(page)
