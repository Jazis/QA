import allure
from playwright.sync_api import Page

from data.input_data.users import USER_01
from pages.pages import Pages
from steps import Steps
from utils.consts import DASHBOARD_ORDERING_SPEND_RANGE
##############Переписать
#Переписать с учетом Qolo
class TestDashboardAccounts:
    @allure.title("Check page account")
    def test_check_account(self, page: Page, pages: Pages,
                           steps: Steps, playwright):
        page.goto(DASHBOARD_ORDERING_SPEND_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Accounts')
        assert pages.dashboard.button_move_money.is_visible()
        assert pages.dashboard.client_balance.is_visible()
        assert pages.dashboard.credit_balance.is_visible()
        assert pages.dashboard.master_balance.is_visible()
        assert pages.dashboard.clients.is_visible()
        assert pages.dashboard.operational.is_visible()
        assert pages.dashboard.user_name.is_visible()
        assert pages.dashboard.filter_status.is_visible()
        assert pages.dashboard.filter_company.is_visible()

    @allure.title("Check titles row")
    def test_check_titles_row(self, page: Page, pages: Pages,
                              steps: Steps, playwright):
        page.goto(DASHBOARD_ORDERING_SPEND_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Accounts')
        steps.universalSteps.check_one_row_in_table(page, '1', "CompanyAcc. numberStatusBeg. balanceMoney inMoney outSpendEnd balance")

    @allure.title("Check total row table")
    def test_check_total_row_table(self, page: Page, pages: Pages,
                                   steps: Steps, playwright):
        page.goto(DASHBOARD_ORDERING_SPEND_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Accounts')
        pages.dashboard.total_row_table.check_text("18 May – 19 May$186,684$0$0($1,656)$185,028")

    @allure.title("Check total spend")
    def test_check_total_spend(self, page: Page, pages: Pages,
                               steps: Steps, playwright):
        page.goto(DASHBOARD_ORDERING_SPEND_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Accounts')
        page.locator("(//th//*[@data-test-id = 'popper-activator'])[6]").click()
        steps.dashboardSteps.check_total_spend(page)

    @allure.title("Check each row table")
    def test_check_each_row_table(self, page: Page, pages: Pages,
                                  steps: Steps, playwright):
        page.goto(DASHBOARD_ORDERING_SPEND_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Accounts')
        steps.dashboardSteps.check_each_row_table_accounts(page)

    @allure.title("Check each row in total")#######################
    def test_check_total_each_row_table(self, page: Page, pages: Pages,
                                        steps: Steps, playwright):
        page.goto(DASHBOARD_ORDERING_SPEND_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Accounts')
        steps.dashboardSteps.check_total_rows_companies(page)

    @allure.title("Check operational in total row")
    def test_check_operational_total_row(self, page: Page, pages: Pages,
                                         steps: Steps, playwright):
        page.goto(DASHBOARD_ORDERING_SPEND_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Accounts')
        pages.dashboard.operational.click()
        pages.dashboard.total_row_table.check_text("18 May – 19 May($403,785)$0$0($403,785)")



    @allure.title("Check each row in operational")
    def test_check_each_row_operational(self, page: Page, pages: Pages,
                                        steps: Steps, playwright):
        page.goto(DASHBOARD_ORDERING_SPEND_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Accounts')
        pages.dashboard.operational.click()
        steps.dashboardSteps.check_each_row_table_accounts_operational(page)

    @allure.title("Filter by status and company")
    def test_filter_by_status_and_company(self, page: Page, pages: Pages,
                                        steps: Steps, playwright):
        page.goto(DASHBOARD_ORDERING_SPEND_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Accounts')
        pages.dashboard.filter_status.click()
        page.locator("//label//span[contains(text(), 'Active')]").click()
        pages.dashboard.filter_status.click()
        pages.dashboard.filter_company.click()
        page.locator("//*[@data-test-id='checkbox']//span[contains(text(), '7 – Microsoft')]").click()
        pages.dashboard.filter_company.click()
        pages.dashboard.first_name_company_at_table.check_text('7 – Microsoft')
        pages.dashboard.tag.check_text('Active')
        pages.dashboard.tag_2.check_text('7 – Microsoft')
        pages.dashboard.table_pagination.check_text('1 account')

    @allure.title("Sort by Beg. balance")
    def test_sort_by_beg_balance(self, page: Page, pages: Pages,
                                          steps: Steps, playwright):
        page.goto(DASHBOARD_ORDERING_SPEND_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Accounts')
        pages.dashboard.first_name_company_at_table.check_text('168 – red company')
        page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Beg. balance")]').click()
        page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Beg. balance")]').click()
        pages.dashboard.first_name_company_at_table.check_text('45 – TestAirtable3')

    @allure.title("Sort by Money in")
    def test_sort_by_money_in(self, page: Page, pages: Pages,
                                 steps: Steps, playwright):
        page.goto(DASHBOARD_ORDERING_SPEND_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Accounts')
        pages.dashboard.first_name_company_at_table.check_text('168 – red company')
        page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Money in")]').click()
        pages.dashboard.first_name_company_at_table.check_text('2 – Beeline')

    @allure.title("Sort by Money out")
    def test_sort_by_money_out(self, page: Page, pages: Pages,
                              steps: Steps, playwright):
        page.goto(DASHBOARD_ORDERING_SPEND_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Accounts')
        pages.dashboard.first_name_company_at_table.check_text('168 – red company')
        page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Money out")]').click()
        pages.dashboard.first_name_company_at_table.check_text('2 – Beeline')

    @allure.title("Sort by spend and End balance")
    def test_sort_by_spend_end_balance(self, page: Page, pages: Pages,
                               steps: Steps, playwright):
        page.goto(DASHBOARD_ORDERING_SPEND_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Accounts')
        pages.dashboard.first_name_company_at_table.check_text('168 – red company')
        page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Spend")]').click()
        pages.dashboard.first_name_company_at_table.check_text('2 – Beeline')
        page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "End balance")]').click()
        pages.dashboard.first_name_company_at_table.check_text('1 – MTS')
