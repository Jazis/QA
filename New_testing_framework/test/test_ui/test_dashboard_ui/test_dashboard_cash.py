from time import sleep

import allure
from playwright.sync_api import Page, expect

from data.input_data.users import USER_01
from pages.pages import Pages
from steps import Steps
from utils.consts import DASHBOARD_CASH_ETALON_RANGE, DASHBOARD_URL, DASHBOARD_CASH_TODAY


class TestDashboardCash:
    @allure.title("Check page")
    def test_check_page(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_CASH_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cash')
        assert pages.dashboard.tab_all_transactions.is_visible()
        assert pages.dashboard.tab_deposits.is_visible()
        assert pages.dashboard.tab_withdrawals.is_visible()
        assert pages.dashboard.tab_subscriptions.is_visible()
        assert pages.dashboard.tab_referrals.is_visible()
        assert pages.dashboard.input_search.is_visible()
        assert pages.dashboard.filter_button_company.is_visible()
        assert pages.dashboard.filter_button_tx_type.is_visible()
        assert pages.dashboard.title_datetime.is_visible()
        assert pages.dashboard.title_amount.is_visible()
        assert pages.dashboard.title_tx_type.is_visible()
        assert pages.dashboard.title_company.is_visible()
        expect(page.get_by_text("1-25 of 49 transactions")).to_be_visible()
        pages.dashboard.date_at_table.check_text('10 Jun – 18 Jun')
        pages.dashboard.total_sum_at_table.check_text('$18,491.44')

    @allure.title("Check each row table")
    def test_check_each_row_table(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_CASH_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cash')
        steps.dashboardSteps.check_each_row_cash_page_1(page)
        pages.dashboard.button_next.click()
        steps.dashboardSteps.check_each_row_cash_page_2(page)
        expect(page.get_by_text("26-49 of 49 transactions")).to_be_visible()

    @allure.title("Check each row at deposits")
    def test_check_each_row_deposits(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_CASH_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cash')
        pages.dashboard.tab_deposits.click()
        assert pages.dashboard.filter_tag_deposit.is_on_page(timeout=1500)
        pages.dashboard.date_at_table.check_text('10 Jun – 18 Jun')
        pages.dashboard.total_sum_at_table.check_text('$18,492.00')
        steps.dashboardSteps.check_each_row_deposits(page)
        expect(page.get_by_text("1-25 of 29 transactions")).to_be_visible()
        pages.dashboard.button_next.click()
        steps.dashboardSteps.check_each_row_deposits_2(page)
        expect(page.get_by_text("26-29 of 29 transactions")).to_be_visible()

    @allure.title("Check each row at Withdrawals")
    def test_check_each_row_withdrawals(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_CASH_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cash')
        pages.dashboard.tab_withdrawals.click()
        assert pages.dashboard.filter_tag_withdrawal.is_on_page(timeout=1500)
        steps.dashboardSteps.check_each_row_withdrawals(page)
        expect(page.get_by_text("1 transaction")).to_be_visible()
        pages.dashboard.date_at_table.check_text('10 Jun – 18 Jun')
        pages.dashboard.total_sum_at_table.check_text('($50.00)')

    @allure.title("Check each row at Subscriptions")
    def test_check_each_row_subscriptions(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_CASH_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cash')
        pages.dashboard.tab_subscriptions.click()
        assert pages.dashboard.filter_tag_subscription.is_on_page(timeout=1500)
        steps.dashboardSteps.check_each_row_subscriptions(page)
        expect(page.get_by_text("6 transaction")).to_be_visible()
        pages.dashboard.date_at_table.check_text('10 Jun – 18 Jun')
        pages.dashboard.total_sum_at_table.check_text('($883.00)')

    @allure.title("Check each row at Referrals")
    def test_check_each_row_referral(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_CASH_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cash')
        pages.dashboard.tab_referrals.click()
        assert pages.dashboard.filter_tag_referral.is_on_page(timeout=1500)
        steps.dashboardSteps.check_each_row_referral(page)
        expect(page.get_by_text("4 transactions")).to_be_visible()
        pages.dashboard.date_at_table.check_text('10 Jun – 18 Jun')
        pages.dashboard.total_sum_at_table.check_text('$1,000.00')

    @allure.title("Search by name company")
    def test_search_by_name_company(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_CASH_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cash')
        pages.dashboard.input_search.fill("Mts")
        page.locator('//*[@data-test-id="button-link"]').is_visible(timeout=2500)
        steps.dashboardSteps.check_companies_after_search_mts(page)

    @allure.title("Search by id company")
    def test_search_by_id_company(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_CASH_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cash')
        pages.dashboard.input_search.fill(222)
        page.locator('//*[@data-test-id="button-link"]').is_visible(timeout=2500)
        steps.dashboardSteps.check_companies_after_search_222(page)
        page.locator('//*[@data-test-id="button-link"]').click()
        steps.dashboardSteps.check_each_row_cash_page_1(page)

    @allure.title("Filter by name company")
    def test_filter_by_company(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_CASH_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cash')
        pages.dashboard.filter_button_company.click()
        page.locator('(//*[@data-test-id="text-field"]//input)[2]').fill("dsef dsfdsg")
        page.locator('//*[@data-test-id="checkbox"]//span[contains(text(), "dsef dsfdsg")]').click()
        steps.dashboardSteps.check_companies_after_search_222(page)

    @allure.title("Filter by Tx type")
    def test_filter_by_tx_type(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_CASH_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cash')
        pages.dashboard.filter_button_tx_type.is_on_page(timeout=2000)
        pages.dashboard.filter_button_tx_type.click()
        page.locator("(//*[@data-test-id='checkbox']//span[contains(text(), 'Deposit')])[1]").click()
        steps.dashboardSteps.check_companies_filter_deposit(page)

    @allure.title("Filter by Tx type & company")
    def test_filter_by_tx_type_company(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_CASH_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cash')
        pages.dashboard.filter_button_company.click()
        page.locator('(//*[@data-test-id="text-field"]//input)[2]').fill("mts")
        page.locator('//*[@data-test-id="checkbox"]//span[contains(text(), "MTS")]').click()
        pages.dashboard.filter_button_tx_type.click()
        page.locator("//*[@data-test-id='checkbox']//span[contains(text(), 'Subscription')]").click()
        sleep(1)
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[1]")).to_have_text(
            '17 Jun, 09:58Pro Subscription1 – MTS($12.00)')
        pages.dashboard.total_sum_at_table.check_text('($12.00)')

    @allure.title("Not found results")
    def test_not_found_results_cash(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_CASH_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cash')
        page.locator('(//*[@data-test-id="text-field"]//input)[1]').fill("890765 eref")
        sleep(2)
        assert pages.dashboard.text_change_filter.is_visible()
        pages.dashboard.btn_clear_filters.click()
        expect(page.locator('//*[@data-test-id="text-field"]')).to_be_empty()

    @allure.title("Sort by Amount")
    def test_sort_by_amount(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_CASH_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cash')
        steps.dashboardSteps.check_each_row_cash_page_1(page)
        pages.dashboard.title_amount.click()
        sleep(2)
        steps.dashboardSteps.check_sort_by_amount_to_higest(page)
        pages.dashboard.title_amount.click()
        sleep(2)
        steps.dashboardSteps.check_sort_by_amount_to_lowest(page)

    @allure.title("Sort by Datetime")
    def test_sort_by_amount(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_CASH_ETALON_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Cash')
        steps.dashboardSteps.check_each_row_cash_page_1(page)
        pages.dashboard.title_datetime.click()
        sleep(2)
        steps.dashboardSteps.check_sort_by_datetime_to_oldest(page)
        pages.dashboard.title_datetime.click()
        sleep(2)
        steps.dashboardSteps.check_sort_by_datetime_to_newest(page)

    @allure.title("Move money deposit & check on cash page, ConnexPay")
    def test_make_deposit_check_on_cash_page_connex_pay(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        assert pages.dashboard.move_money_row_to.is_visible()
        sleep(2)
        expect(page.locator("//*[contains(text(), 'Main – ConnexPay')]")).to_be_visible()
        pages.dashboard.move_money_row_to.click()
        page.locator('(//button[@data-test-id="action"])[5]').click()
        pages.dashboard.input_amount.fill('10.00')
        pages.dashboard.move_money_btn_next.click()
        expect(page.get_by_text("Deposit • ConnexPay")).to_be_visible()
        expect(page.get_by_text("From")).to_be_visible()
        expect(page.locator("[data-test-id='modal-body']").get_by_text("To")).to_be_visible()
        expect(page.locator('(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[1]')).to_have_text('$10.00')
        expect(page.locator('(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[3]')).to_contain_text('Main – ConnexPay')
        expect(page.locator('(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[4]')).to_contain_text('ConnexPay')
        expect(page.locator('(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[5]')).to_contain_text('4 – Tesla')
        expect(page.locator('(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[6]')).to_contain_text('ConnexPay')
        pages.dashboard.move_money_btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("(//*[@data-test-id='modal-body']//span)[1]")).to_have_text('$10.00')
        expect(page.locator("(//*[@data-test-id='modal-body']//span)[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[@data-test-id='modal-body']//span)[2]")).to_have_text('Deposit • ConnexPay')
        expect(page.locator("(//*[@data-test-id='modal-body']//span)[3]")).to_have_text('From')
        expect(page.locator("(//*[contains(@class, 'min-width_0')])[1]")).to_have_text('Main – ConnexPayConnexPay')
        expect(page.locator("(//*[contains(@class, 'min-width_0')])[2]")).to_have_text('4 – TeslaConnexPay')
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.get_by_text("Deposit • ConnexPay")).to_be_visible()
        pages.dashboard.move_money_btn_go_dash.click()
        page.goto(DASHBOARD_CASH_TODAY)
        pages.dashboard.tx_type_first_row.check_text(" Deposit")
        pages.dashboard.company_name_first_row.check_text("4 – Tesla")
        pages.dashboard.amount_first_row.check_text('$10.00')

    @allure.title("Move money deposit & check on cash page, Qolo")
    def test_make_deposit_check_on_cash_page_qolo(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        sleep(1.5)
        assert pages.dashboard.modal_tab_qolo.is_visible()
        assert pages.dashboard.modal_tab_connexpay.is_visible()
        pages.dashboard.modal_tab_qolo.click()
        sleep(1.5)

        expect(page.locator("[data-test-id='modal-body']").get_by_text("Main – Qolo")).to_be_visible()
        pages.dashboard.move_money_row_to.click()
        page.locator('//*[@data-test-id="action"]//*[contains(text(), "540 – Qolo Test")]').click()
        pages.dashboard.input_amount.fill('10.00')
        pages.dashboard.move_money_btn_next.click()
        expect(page.get_by_text("Deposit • Qolo")).to_be_visible()
        expect(page.get_by_text("Review transfer details")).to_be_visible()
        expect(page.locator("[data-test-id='modal-body']").get_by_text("From")).to_be_visible()
        expect(page.locator("[data-test-id='modal-body']").get_by_text("To")).to_be_visible()
        expect(
            page.locator('(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[1]')).to_have_text(
            '$10.00')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[3]')).to_contain_text(
            'Main – Qolo')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[4]')).to_contain_text('Qolo')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[5]')).to_contain_text('540 – Qolo Test')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[6]')).to_contain_text('Qolo')
        pages.dashboard.move_money_btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("(//*[@data-test-id='modal-body']//span)[1]")).to_have_text('$10.00')
        expect(page.locator("(//*[@data-test-id='modal-body']//span)[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[@data-test-id='modal-body']//span)[2]")).to_have_text('Deposit • Qolo')
        expect(page.locator("(//*[@data-test-id='modal-body']//span)[3]")).to_have_text('From')
        expect(page.locator("(//*[contains(@class, 'min-width_0')])[1]")).to_have_text('Main – QoloQolo')
        expect(page.locator("(//*[contains(@class, 'min-width_0')])[2]")).to_have_text('540 – Qolo TestQolo')
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.get_by_text("Deposit • Qolo")).to_be_visible()
        pages.dashboard.move_money_btn_go_dash.click()
        page.goto(DASHBOARD_CASH_TODAY)
        pages.dashboard.tx_type_first_row.check_text(" Deposit")
        pages.dashboard.company_name_first_row.check_text("540 – Qolo Test")
        pages.dashboard.amount_first_row.check_text('$10.00')

    @allure.title("Move money. Make 'Withdrawal' transaction Connex Pay")
    def test_make_withdrawal_transaction_connex_pay(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.move_money_type_operation.click()
        page.locator('//*[contains(text(), "Withdrawal")]').click()
        sleep(2.5)
        expect(page.locator("[data-test-id='modal-body']").get_by_text("Main – ConnexPay")).to_be_visible()
        page.locator("(//*[contains(@class, 'styles_endContent')])[3]").click()
        page.locator('(//button[@data-test-id="action"])[2]').click()
        pages.dashboard.input_amount.fill('1.00')
        pages.dashboard.move_money_btn_next.click()
        expect(
            page.locator('(//*[@data-test-id="modal-body"])//span[contains(text(), "Withdrawal • ConnexPay")]')).to_be_visible()
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[1]')).to_have_text("$1.00")
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[3]')).to_contain_text(
            '2 – Beeline')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[4]')).to_contain_text('ConnexPay')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[5]')).to_contain_text(
            'Main – ConnexPay')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[6]')).to_contain_text('ConnexPay')
        pages.dashboard.move_money_btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color", "rgb(88, 182, 62)")
        expect(
            page.locator('(//*[@data-test-id="modal-body"])//span[contains(text(), "Withdrawal • ConnexPay")]')).to_be_visible()
        expect(page.locator(
            '(//*[@data-test-id="modal-body"]//span)[1]')).to_have_text("$1.00")
        pages.dashboard.move_money_btn_go_dash.click()
        page.goto(DASHBOARD_CASH_TODAY)
        pages.dashboard.tx_type_first_row.check_text("Withdrawal")
        pages.dashboard.company_name_first_row.check_text("2 – Beeline")
        pages.dashboard.amount_first_row.check_text("($1.00)")

    @allure.title("Move money. Make 'Withdrawal' transaction Qolo")
    def test_make_withdrawal_transaction_qolo(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.modal_tab_qolo.click()
        sleep(2)
        pages.dashboard.move_money_type_operation.click()
        page.locator('//*[contains(text(), "Withdrawal")]').click()
        sleep(1)
        expect(page.locator("[data-test-id='modal-body']").get_by_text("Main – Qolo")).to_be_visible()
        page.locator("(//*[contains(@class, 'styles_endContent')])[3]").click()
        page.locator('//*[@data-test-id="action"]//*[contains(text(), "540 – Qolo Test")]').click()
        pages.dashboard.input_amount.fill('1.00')
        pages.dashboard.move_money_btn_next.click()
        expect(
            page.locator(
                '(//*[@data-test-id="modal-body"])//span[contains(text(), "Withdrawal • Qolo")]')).to_be_visible()
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[1]')).to_have_text("$1.00")
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[3]')).to_contain_text(
            '540 – Qolo Test')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[4]')).to_contain_text(
            'Qolo')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[5]')).to_contain_text(
            'Main – Qolo')
        expect(page.locator(
                '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[6]')).to_contain_text(
            'Qolo')
        pages.dashboard.move_money_btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator(
            "(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css("color",
                                                                                                            "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color",
                                                                                                        "rgb(88, 182, 62)")
        expect(
            page.locator(
                '(//*[@data-test-id="modal-body"])//span[contains(text(), "Withdrawal • Qolo")]')).to_be_visible()
        expect(page.locator(
            '(//*[@data-test-id="modal-body"]//span)[1]')).to_have_text("$1.00")
        pages.dashboard.move_money_btn_go_dash.click()
        page.goto(DASHBOARD_CASH_TODAY)
        pages.dashboard.tx_type_first_row.check_text("Withdrawal")
        pages.dashboard.company_name_first_row.check_text("540 – Qolo Test")
        pages.dashboard.amount_first_row.check_text("($1.00)")

    @allure.title("Move money Credit Issue (Legacy) & check on cash page Connex Pay")
    def test_make_credit_issue_check_on_cash_page_connex_pay(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        sleep(1.5)
        pages.dashboard.move_money_type_operation.click()
        assert pages.dashboard.modal_tab_connexpay.is_visible()
        page.locator('//*[contains(text(), "Credit Issue (Legacy)")]').click()
        sleep(2)
        expect(page.locator("[data-test-id='modal-body']").get_by_text("Credit – ConnexPay")).to_be_visible()
        pages.dashboard.move_money_row_to.click()
        page.locator('(//button[@data-test-id="action"])[2]').click()
        pages.dashboard.input_amount.fill('1.5')
        pages.dashboard.move_money_btn_next.click()
        expect(page.get_by_text("Credit Issue (Legacy) • ConnexPay")).to_be_visible()
        expect(page.get_by_text("Review transfer details")).to_be_visible()
        expect(page.locator('(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[1]')).to_have_text(
            '$1.50')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[3]')).to_contain_text(
            'Credit – ConnexPay')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[4]')).to_contain_text(
            'ConnexPay')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[5]')).to_contain_text(
            '1 – MTS')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[6]')).to_contain_text(
            'ConnexPay')
        pages.dashboard.move_money_btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.get_by_text("Credit Issue (Legacy)")).to_be_visible()
        expect(page.locator('(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[1]')).to_have_text(
            '$1.50')
        pages.dashboard.move_money_btn_go_dash.click()
        page.goto(DASHBOARD_CASH_TODAY)
        pages.dashboard.tx_type_first_row.check_text(" Deposit")
        pages.dashboard.company_name_first_row.check_text("1 – MTS")
        pages.dashboard.amount_first_row.check_text('$1.50')

    @allure.title("Move money Credit Issue (Legacy) & check on cash page Qolo")
    def test_make_credit_issue_check_on_cash_page_qolo(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        sleep(1.5)
        pages.dashboard.modal_tab_qolo.click()
        pages.dashboard.move_money_type_operation.click()
        assert pages.dashboard.modal_tab_connexpay.is_visible()
        page.locator('//*[contains(text(), "Credit Issue (Legacy)")]').click()
        sleep(2)
        expect(page.locator("[data-test-id='modal-body']").get_by_text("Credit – Qolo")).to_be_visible()
        pages.dashboard.move_money_row_to.click()
        page.locator('//*[@data-test-id="action"]//*[contains(text(), "540 – Qolo Test")]').click()
        pages.dashboard.input_amount.fill('1.8')
        pages.dashboard.move_money_btn_next.click()
        expect(page.get_by_text("Credit Issue (Legacy) • Qolo")).to_be_visible()
        expect(page.get_by_text("Review transfer details")).to_be_visible()
        expect(
            page.locator('(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[1]')).to_have_text(
            '$1.80')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[3]')).to_contain_text(
            'Credit – Qolo')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[4]')).to_contain_text(
            'Qolo')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[5]')).to_contain_text(
            '540 – Qolo Test')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[6]')).to_contain_text(
            'Qolo')
        pages.dashboard.move_money_btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css(
            "color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color",
                                                                                                    "rgb(88, 182, 62)")
        expect(page.get_by_text("Credit Issue (Legacy) • Qolo")).to_be_visible()
        expect(
            page.locator('(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[1]')).to_have_text(
            '$1.80')
        pages.dashboard.move_money_btn_go_dash.click()
        page.goto(DASHBOARD_CASH_TODAY)
        pages.dashboard.tx_type_first_row.check_text(" Deposit")
        pages.dashboard.company_name_first_row.check_text("540 – Qolo Test")
        pages.dashboard.amount_first_row.check_text('$1.80')

    @allure.title("Move money Credit Issue Wire & check on cash page Connex Pay")
    def test_make_credit_issue_wire_check_on_cash_page_connex_pay(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.move_money_type_operation.click()
        page.locator('//*[contains(text(), "Credit Issue Wire")]').click()
        sleep(2)
        expect(page.locator("[data-test-id='modal-body']").get_by_text("Credit – ConnexPay")).to_be_visible()
        pages.dashboard.move_money_row_to.click()
        page.locator('(//*[@data-test-id="action"])[2]').click()
        pages.dashboard.input_amount.fill('17.00')
        pages.dashboard.move_money_btn_next.click()
        expect(page.get_by_text("Credit Issue Wire • ConnexPay")).to_be_visible()
        expect(page.get_by_text("Review transfer details")).to_be_visible()
        expect(
            page.locator('(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[1]')).to_have_text(
            '$17.00')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[3]')).to_contain_text(
            'Credit – ConnexPay')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[4]')).to_contain_text(
            'ConnexPay')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[5]')).to_contain_text(
            '1 – MTS')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[6]')).to_contain_text(
            'ConnexPay')
        pages.dashboard.move_money_btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.get_by_text("Credit Issue Wire • ConnexPay")).to_be_visible()
        expect(page.locator('(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[1]')).to_have_text(
            '$17.00')
        pages.dashboard.move_money_btn_go_dash.click()
        page.goto(DASHBOARD_CASH_TODAY)
        pages.dashboard.tx_type_first_row.check_text("Deposit fee")
        pages.dashboard.company_name_first_row.check_text("1 – MTS")
        pages.dashboard.amount_first_row.check_text("($0.34)")

    @allure.title("Move money Credit Issue Wire & check on cash page Qolo")
    def test_make_credit_issue_wire_check_on_cash_page_qolo(self, page: Page, pages: Pages, steps: Steps,
                                                                  playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.modal_tab_qolo.click()
        pages.dashboard.move_money_type_operation.click()
        page.locator('//*[contains(text(), "Credit Issue Wire")]').click()
        sleep(2)
        expect(page.locator("[data-test-id='modal-body']").get_by_text("Credit – Qolo")).to_be_visible()
        pages.dashboard.move_money_row_to.click()
        page.locator('//*[@data-test-id="action"]//*[contains(text(), "540 – Qolo Test")]').click()
        pages.dashboard.input_amount.fill('1.70')
        pages.dashboard.move_money_btn_next.click()
        expect(page.get_by_text("Credit Issue Wire • Qolo")).to_be_visible()
        expect(page.get_by_text("Review transfer details")).to_be_visible()
        expect(
            page.locator('(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[1]')).to_have_text(
            '$1.70')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[3]')).to_contain_text(
            'Credit – Qolo')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[4]')).to_contain_text(
            'Qolo')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[5]')).to_contain_text(
            '540 – Qolo Test')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[6]')).to_contain_text(
            'Qolo')
        pages.dashboard.move_money_btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css(
            "color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color",
                                                                                                    "rgb(88, 182, 62)")
        expect(page.get_by_text("Credit Issue Wire • Qolo")).to_be_visible()
        expect(
            page.locator('(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[1]')).to_have_text(
            '$1.70')
        pages.dashboard.move_money_btn_go_dash.click()
        page.goto(DASHBOARD_CASH_TODAY)
        expect(page.locator("(//*[contains(text(), ' Deposit fee')])[1]/ancestor::tr//*[contains(@class, 'styles_tableCompany')]")).to_have_text("540 – Qolo Test")
        expect(page.locator("(//*[contains(text(), 'Deposit (Wire)')])[1]/ancestor::tr//*[contains(@class, 'styles_tableCompany')]")).to_have_text("540 – Qolo Test")
        expect(page.locator("(//*[contains(text(), ' Deposit fee')])[1]/ancestor::tr//*[contains(@class, 'styles_containerBodyMd')]")).to_have_text("($0.03)")
        expect(page.locator("(//*[contains(text(), 'Deposit (Wire)')])[1]/ancestor::tr//*[contains(@class, 'styles_containerBodyMd')]")).to_have_text("$1.70")

    @allure.title("Move money. Credit Clear Connex Pay")
    def test_dashboard_money_clear_connex_pay(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.move_money_type_operation.click()
        page.locator('//div[contains(text(), "Credit Clear")]').scroll_into_view_if_needed()
        page.locator('//div[contains(text(), "Credit Clear")]').click()
        sleep(2)
        page.locator('(//*[contains(@class, "display_flex flex-direction_column")])[2]').click()
        page.locator("//div[contains(text(), 'Main – ConnexPay')]").click()
        expect(page.locator("[data-test-id='modal-body']").get_by_text("Main – ConnexPay")).to_be_visible()
        expect(page.locator("[data-test-id='modal-body']").get_by_text("Credit – ConnexPay")).to_be_visible()
        page.locator('//input[@id="amount"]').fill("1")
        pages.dashboard.btn_next.click()
        pages.dashboard.move_money_modal_from.check_text('Main – ConnexPayConnexPay')
        pages.dashboard.move_money_modal_to.check_text('Credit – ConnexPayConnexPay')
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.00')
        pages.dashboard.btn_transfer.click()
        sleep(2.5)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text('$1.00')
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.get_by_text('Credit Clear • ConnexPay')).to_be_visible()
        pages.dashboard.move_money_modal_from.check_text('Main – ConnexPayConnexPay')
        pages.dashboard.move_money_modal_to.check_text('Credit – ConnexPayConnexPay')

    @allure.title("Move money. Credit Clear Qolo")
    def test_dashboard_money_clear_qolo(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.modal_tab_qolo.click()
        pages.dashboard.move_money_type_operation.click()
        page.locator('//div[contains(text(), "Credit Clear")]').scroll_into_view_if_needed()
        page.locator('//div[contains(text(), "Credit Clear")]').click()
        sleep(2)
        page.locator('(//*[contains(@class, "display_flex flex-direction_column")])[2]').click()
        page.locator('//div[contains(text(), "Main")]').click()
        expect(page.locator("[data-test-id='modal-body']").get_by_text("Main – Qolo")).to_be_visible()
        expect(page.locator("[data-test-id='modal-body']").get_by_text("Credit – Qolo")).to_be_visible()
        page.locator('//input[@id="amount"]').fill("1")
        pages.dashboard.btn_next.click()
        pages.dashboard.move_money_modal_from.check_text('Main – QoloQolo')
        pages.dashboard.move_money_modal_to.check_text('Credit – QoloQolo')
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.00')
        pages.dashboard.btn_transfer.click()
        sleep(2.5)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css(
            "color", "rgb(88, 182, 62)")
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.00')
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color",
                                                                                                    "rgb(88, 182, 62)")
        expect(page.get_by_text('Credit Clear • Qolo')).to_be_visible()
        pages.dashboard.move_money_modal_from.check_text('Main – QoloQolo')
        pages.dashboard.move_money_modal_to.check_text('Credit – QoloQolo')

    @allure.title("Move money Subscription & check on cash page Connex Pay")
    def test_make_subscription_check_on_cash_page_connex_pay(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.move_money_type_operation.click()
        page.locator('//div[contains(text(), "Subscription")]').scroll_into_view_if_needed()
        page.locator('//div[contains(text(), "Subscription")]').click()
        sleep(2)
        expect(page.locator('(//*[@data-test-id="select"])[2]')).to_contain_text(
            'From1 – MTS')
        expect(page.locator('//*[@data-test-id="modal-dialog"]')).to_contain_text('ToRevenue – ConnexPay – ')
        pages.dashboard.input_amount.fill('20.00')
        pages.dashboard.move_money_btn_next.click()
        expect(page.locator("[data-test-id='modal-body']").get_by_text("Subscription • ConnexPay")).to_be_visible()
        expect(page.get_by_text("Review transfer details")).to_be_visible()
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[1]')).to_have_text('$20.00')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[3]')).to_contain_text(
            '1 – MTS')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[4]')).to_contain_text(
            'ConnexPay')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[5]')).to_contain_text(
            'Revenue – ConnexPay')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[6]')).to_contain_text(
            'ConnexPay')
        pages.dashboard.move_money_btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text('$20.00')
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("[data-test-id='modal-body']").get_by_text("Subscription • ConnexPay")).to_be_visible()
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[3]')).to_contain_text(
            '1 – MTS')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[4]')).to_contain_text(
            'ConnexPay')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[5]')).to_contain_text(
            'Revenue – ConnexPay')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[6]')).to_contain_text(
            'ConnexPay')
        pages.dashboard.move_money_btn_go_dash.click()
        page.goto(DASHBOARD_CASH_TODAY)
        pages.dashboard.company_name_first_row.check_text("1 – MTS")
        pages.dashboard.amount_first_row.check_text("($20.00)")

    @allure.title("Move money Fee to Main Connex Pay")
    def test_move_money_fee_to_main_connex_pay(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.move_money_type_operation.click()
        page.locator('//div[contains(text(), "Fee to Main")]').scroll_into_view_if_needed()
        page.locator('//div[contains(text(), "Fee to Main")]').click()
        sleep(2.5)
        expect(page.locator('//*[@data-test-id="modal-dialog"]').get_by_text('Fee – ConnexPay – ')).to_be_visible()
        expect(page.get_by_text('Main – ConnexPay ')).to_be_visible()
        page.locator('//input[@id="amount"]').fill("1")
        pages.dashboard.btn_next.click()
        pages.dashboard.move_money_modal_from.check_text('Fee – ConnexPayConnexPay')
        pages.dashboard.move_money_modal_to.check_text('Main – ConnexPayConnexPay')
        pages.dashboard.btn_transfer.click()
        sleep(2.5)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text('$1.00')
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("[data-test-id='modal-body']").get_by_text("Fee to Main • ConnexPay")).to_be_visible()
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[3]')).to_contain_text(
            'Fee – ConnexPay')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[4]')).to_contain_text(
            'ConnexPay')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[5]')).to_contain_text(
            'Main – ConnexPay')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[6]')).to_contain_text(
            'ConnexPay')

    @allure.title("Move money Fee to Main Qolo")
    def test_move_money_fee_to_main_qolo(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.modal_tab_qolo.click()
        pages.dashboard.move_money_type_operation.click()
        page.locator('//div[contains(text(), "Fee to Main")]').scroll_into_view_if_needed()
        page.locator('//div[contains(text(), "Fee to Main")]').click()
        sleep(2)
        expect(page.locator('//*[@data-test-id="modal-dialog"]').get_by_text('Fee – Qolo – ')).to_be_visible()
        expect(page.get_by_text('Main – Qolo ')).to_be_visible()
        page.locator('//input[@id="amount"]').fill("1")
        pages.dashboard.btn_next.click()
        pages.dashboard.move_money_modal_from.check_text('Fee – QoloQolo')
        pages.dashboard.move_money_modal_to.check_text('Main – QoloQolo')
        pages.dashboard.btn_transfer.click()
        sleep(2.5)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css(
            "color", "rgb(88, 182, 62)")
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.00')
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color",
                                                                                                    "rgb(88, 182, 62)")
        expect(page.locator("[data-test-id='modal-body']").get_by_text("Fee to Main • Qolo")).to_be_visible()
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[3]')).to_contain_text(
            'Fee – Qolo')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[4]')).to_contain_text(
            'Qolo')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[5]')).to_contain_text(
            'Main – Qolo')
        expect(page.locator(
            '(//*[contains(@class, "display_flex flex-direction_column gap_1")]/span)[6]')).to_contain_text(
            'Qolo')

    @allure.title("Move money. Revenue to Main Connex Pay")
    def test_move_money_revenue_to_main_connex_pay(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.move_money_type_operation.click()
        sleep(2)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        sleep(2)
        expect(page.locator("//*[contains(text(), 'Revenue to Main')]")).to_be_visible()
        text_to = pages.dashboard.move_money_to.get_text()
        assert text_to.__contains__('Main – ConnexPay – ')
        page.locator('//input[@id="amount"]').fill("1")
        pages.dashboard.btn_next.click()
        expect(page.locator("//*[contains(text(), 'Revenue to Main')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text('$1.00')
        pages.dashboard.move_money_modal_from.check_text('Revenue – ConnexPayConnexPay')
        pages.dashboard.move_money_modal_to.check_text('Main – ConnexPayConnexPay')
        pages.dashboard.btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("//*[contains(text(), 'Revenue to Main')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.00')
        pages.dashboard.move_money_modal_from.check_text('Revenue – ConnexPayConnexPay')
        pages.dashboard.move_money_modal_to.check_text('Main – ConnexPayConnexPay')

    @allure.title("Move money. Revenue to Main Qolo")
    def test_move_money_revenue_to_main_qolo(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.modal_tab_qolo.click()
        pages.dashboard.move_money_type_operation.click()
        sleep(2)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        sleep(2)
        expect(page.locator("//*[contains(text(), 'Revenue – Qolo – $')]")).to_be_visible()
        text_to = pages.dashboard.move_money_to.get_text()
        assert text_to.__contains__('Main – Qolo – $')
        page.locator('//input[@id="amount"]').fill("1")
        pages.dashboard.btn_next.click()
        expect(page.locator("//*[contains(text(), 'Revenue to Main • Qolo')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.00')
        pages.dashboard.move_money_modal_from.check_text('Revenue – QoloQolo')
        pages.dashboard.move_money_modal_to.check_text('Main – QoloQolo')
        pages.dashboard.btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css(
            "color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color",
                                                                                                    "rgb(88, 182, 62)")
        expect(page.locator("//*[contains(text(), 'Revenue to Main • Qolo')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.00')
        pages.dashboard.move_money_modal_from.check_text('Revenue – QoloQolo')
        pages.dashboard.move_money_modal_to.check_text('Main – QoloQolo')

    @allure.title("Move money. Main to Revenue ConnexPay")
    def test_move_money_main_to_revenue_connex_pay(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.move_money_type_operation.click()
        sleep(2)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        sleep(2)
        page.locator('//input[@id="amount"]').fill("1.23")
        pages.dashboard.btn_next.click()
        expect(page.locator("//span[contains(text(), 'Main to Revenue • ConnexPay')]")).to_be_visible()
        pages.dashboard.move_money_modal_from.check_text('Main – ConnexPayConnexPay')
        pages.dashboard.move_money_modal_to.check_text('Revenue – ConnexPayConnexPay')
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text('$1.23')
        pages.dashboard.btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("//span[contains(text(), 'Main to Revenue • ConnexPay')]")).to_be_visible()
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color", "rgb(88, 182, 62)")
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text('$1.23')
        pages.dashboard.move_money_modal_from.check_text('Main – ConnexPayConnexPay')
        pages.dashboard.move_money_modal_to.check_text('Revenue – ConnexPayConnexPay')

    @allure.title("Move money. Main to Revenue Qolo")
    def test_move_money_main_to_revenue_qolo(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.modal_tab_qolo.click()
        pages.dashboard.move_money_type_operation.click()
        sleep(2)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        sleep(2)
        page.locator('//input[@id="amount"]').fill("1.25")
        pages.dashboard.btn_next.click()
        expect(page.locator("//span[contains(text(), 'Main to Revenue • Qolo')]")).to_be_visible()
        pages.dashboard.move_money_modal_from.check_text('Main – QoloQolo')
        pages.dashboard.move_money_modal_to.check_text('Revenue – QoloQolo')
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.25')
        pages.dashboard.btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("//span[contains(text(), 'Main to Revenue • Qolo')]")).to_be_visible()
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css(
            "color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color",
                                                                                                    "rgb(88, 182, 62)")
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.25')
        pages.dashboard.move_money_modal_from.check_text('Main – QoloQolo')
        pages.dashboard.move_money_modal_to.check_text('Revenue – QoloQolo')

    @allure.step("Move money. Credit Internal ConnexPay")
    def test_move_money_credit_internal_connex_pay(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.move_money_type_operation.click()
        sleep(2)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        sleep(2)
        page.locator('//input[@id="amount"]').fill("1")
        expect(
            page.locator('//*[@data-test-id="modal-body"]').get_by_text('Credit Internal')).to_be_visible()
        expect(
            page.locator('//*[@data-test-id="modal-body"]').get_by_text('Credit – ConnexPay –')).to_be_visible()
        expect(page.locator('//*[@data-test-id="modal-body"]').get_by_text('Main – ConnexPay –')).to_be_visible()
        pages.dashboard.btn_next.click()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.00')
        expect(
            page.locator('//*[@data-test-id="modal-body"]').get_by_text('Credit Internal • ConnexPay')).to_be_visible()
        pages.dashboard.move_money_modal_from.check_text('Credit – ConnexPayConnexPay')
        pages.dashboard.move_money_modal_to.check_text('Main – ConnexPayConnexPay')
        pages.dashboard.btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.00')
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color", "rgb(88, 182, 62)")
        expect(
            page.locator('//*[@data-test-id="modal-body"]').get_by_text('Credit Internal • ConnexPay')).to_be_visible()
        pages.dashboard.move_money_modal_from.check_text('Credit – ConnexPayConnexPay')
        pages.dashboard.move_money_modal_to.check_text('Main – ConnexPayConnexPay')

    @allure.step("Move money. Credit Internal Qolo")
    def test_move_money_credit_internal_qolo(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.modal_tab_qolo.click()
        pages.dashboard.move_money_type_operation.click()
        sleep(2)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        sleep(2)
        page.locator('//input[@id="amount"]').fill("1")
        expect(
            page.locator('//*[@data-test-id="modal-body"]').get_by_text('Credit Internal')).to_be_visible()
        expect(
            page.locator('//*[@data-test-id="modal-body"]').get_by_text('Credit – Qolo –')).to_be_visible()
        expect(page.locator('//*[@data-test-id="modal-body"]').get_by_text('Main – Qolo –')).to_be_visible()
        pages.dashboard.btn_next.click()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.00')
        expect(
            page.locator('//*[@data-test-id="modal-body"]').get_by_text('Credit Internal • Qolo')).to_be_visible()
        pages.dashboard.move_money_modal_from.check_text('Credit – QoloQolo')
        pages.dashboard.move_money_modal_to.check_text('Main – QoloQolo')
        pages.dashboard.btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.00')
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css(
            "color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color",
                                                                                                    "rgb(88, 182, 62)")
        expect(
            page.locator('//*[@data-test-id="modal-body"]').get_by_text('Credit Internal • Qolo')).to_be_visible()
        pages.dashboard.move_money_modal_from.check_text("Credit – QoloQolo")
        pages.dashboard.move_money_modal_to.check_text("Main – QoloQolo")

    @allure.title("Move money. Gift ConnexPay")
    def test_move_money_gift_connex_pay(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.move_money_type_operation.click()
        sleep(2)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        sleep(2)
        expect(
            page.locator('//*[@data-test-id="modal-body"]').get_by_text('Gift')).to_be_visible()
        pages.dashboard.move_money_row_to.click()
        page.locator('//*[@data-index="1"]').click()
        page.locator('//input[@id="amount"]').fill("1")
        pages.dashboard.btn_next.click()
        expect(
            page.locator('//*[@data-test-id="modal-body"]').get_by_text('Gift • ConnexPay')).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text('$1.00')
        pages.dashboard.move_money_modal_from.check_text('Revenue – ConnexPayConnexPay')
        pages.dashboard.move_money_modal_to.check_text('1 – MTSConnexPay')
        pages.dashboard.btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(
            page.locator('//*[@data-test-id="modal-body"]').get_by_text('Gift • ConnexPay')).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.00')
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color", "rgb(88, 182, 62)")
        pages.dashboard.move_money_modal_from.check_text('Revenue – ConnexPayConnexPay')
        pages.dashboard.move_money_modal_to.check_text('1 – MTSConnexPay')
        pages.dashboard.move_money_btn_go_dash.click()
        page.goto(DASHBOARD_CASH_TODAY)
        pages.dashboard.company_name_first_row.check_text("1 – MTS")
        pages.dashboard.amount_first_row.check_text("$1.00")

    @allure.title("Move money. Gift Qolo")
    def test_move_money_gift_qolo(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.modal_tab_qolo.click()
        pages.dashboard.move_money_type_operation.click()
        sleep(2)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        sleep(2)
        expect(page.locator("//*[contains(text(), 'Gift')]")).to_be_visible()
        pages.dashboard.move_money_row_to.click()
        page.locator('//*[@data-index="1"]').click()
        page.locator('//input[@id="amount"]').fill("1")
        pages.dashboard.btn_next.click()
        expect(page.locator("//*[contains(text(), 'Gift • Qolo')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.00')
        pages.dashboard.move_money_modal_from.check_text('Revenue – QoloQolo')
        pages.dashboard.move_money_modal_to.check_text("284 – JncrjoQolo")
        pages.dashboard.btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("//*[contains(text(), 'Gift • Qolo')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.00')
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css(
            "color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color",
                                                                                                    "rgb(88, 182, 62)")
        pages.dashboard.move_money_modal_from.check_text('Revenue – QoloQolo')
        pages.dashboard.move_money_modal_to.check_text("284 – JncrjoQolo")
        pages.dashboard.move_money_btn_go_dash.click()
        page.goto(DASHBOARD_CASH_TODAY)
        pages.dashboard.company_name_first_row.check_text("284 – Jncrjo")
        pages.dashboard.amount_first_row.check_text("$1.00")

    @allure.title("Move money. Inter Account Transfer ConnexPay")
    def test_move_money_inter_account_connex_pay(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.move_money_type_operation.click()
        sleep(2)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        sleep(2)
        page.locator("(//*[contains(@class, 'display_flex flex-direction_column')])[2]").click()
        page.locator('//*[@data-index="1"]').click()
        pages.dashboard.move_money_row_to.click()
        page.locator('//*[@data-index="3"]').click()
        page.locator('//input[@id="amount"]').fill("1")
        expect(page.locator("//*[contains(text(), 'Inter Account Transfer')]")).to_be_visible()
        pages.dashboard.btn_next.click()
        expect(page.locator("//*[contains(text(), 'Inter Account Transfer • ConnexPay')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.00')
        pages.dashboard.move_money_modal_from.check_text('2 – BeelineConnexPay')
        pages.dashboard.move_money_modal_to.check_text('3 – Some New CompanyConnexPay')
        pages.dashboard.btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("//*[contains(text(), 'Inter Account Transfer • ConnexPay')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text('$1.00')
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color", "rgb(88, 182, 62)")
        pages.dashboard.move_money_modal_from.check_text('2 – BeelineConnexPay')
        pages.dashboard.move_money_modal_to.check_text('3 – Some New CompanyConnexPay')
        pages.dashboard.move_money_btn_go_dash.click()
        page.goto(DASHBOARD_CASH_TODAY)
        pages.dashboard.company_name_first_row.check_text("3 – Some New Company")
        pages.dashboard.amount_first_row.check_text("$1.00")

    @allure.title("Move money. Inter Account Transfer Qolo")
    def test_move_money_inter_account_qolo(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.modal_tab_qolo.click()
        pages.dashboard.move_money_type_operation.click()
        sleep(2)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        sleep(2)
        pages.dashboard.move_money_row_to.click()
        page.locator('//*[@data-index="2"]').click()
        page.locator('//input[@id="amount"]').fill("1.05")
        expect(page.locator("//*[contains(text(), 'Inter Account Transfer')]")).to_be_visible()
        pages.dashboard.btn_next.click()
        expect(page.locator("//*[contains(text(), 'Inter Account Transfer • Qolo')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text('$1.05')
        pages.dashboard.move_money_modal_from.check_text('284 – JncrjoQolo')
        pages.dashboard.move_money_modal_to.check_text('540 – Qolo TestQolo')
        pages.dashboard.btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("//*[contains(text(), 'Inter Account Transfer • Qolo')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$1.05')
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css(
            "color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color",
                                                                                                    "rgb(88, 182, 62)")
        pages.dashboard.move_money_modal_from.check_text('284 – JncrjoQolo')
        pages.dashboard.move_money_modal_to.check_text('540 – Qolo TestQolo')
        pages.dashboard.move_money_btn_go_dash.click()
        page.goto(DASHBOARD_CASH_TODAY)
        pages.dashboard.company_name_first_row.check_text("540 – Qolo Test")
        pages.dashboard.amount_first_row.check_text("$1.05")

    @allure.title("Move money. Credit clear netting ConnexPay")
    def test_move_money_credit_clear_netting_connex_pay(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.move_money_type_operation.click()
        sleep(2)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        sleep(2)
        #page.locator("//*[@data-test-id='action']//div[contains(text(), 'Netting – ConnexPay')]").click()
        page.locator('//input[@id="amount"]').fill("2")
        pages.dashboard.btn_next.click()
        expect(page.locator("//*[contains(text(), 'Credit Clear • ConnexPay')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text('$2.00')
        pages.dashboard.move_money_modal_from.check_text('Netting – ConnexPayConnexPay')
        pages.dashboard.move_money_modal_to.check_text('Credit – ConnexPayConnexPay')
        pages.dashboard.btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("//*[contains(text(), 'Credit Clear • ConnexPay')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text('$2.00')
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color", "rgb(88, 182, 62)")
        pages.dashboard.move_money_modal_from.check_text('Netting – ConnexPayConnexPay')
        pages.dashboard.move_money_modal_to.check_text('Credit – ConnexPayConnexPay')

    @allure.title("Move money. Credit clear netting Qolo")
    def test_move_money_credit_clear_netting_qolo(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.modal_tab_qolo.click()
        pages.dashboard.move_money_type_operation.click()
        sleep(2)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        sleep(2)
        page.locator("(//div[contains(@class, 'display_flex flex-direction_column')])[2]").click()
        page.locator("//*[@data-test-id='action']//div[contains(text(), 'Netting – Qolo')]").click()
        page.locator('//input[@id="amount"]').fill("2")
        pages.dashboard.btn_next.click()
        expect(page.locator("//*[contains(text(), 'Credit Clear • Qolo')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$2.00')
        pages.dashboard.move_money_modal_from.check_text('Netting – QoloQolo')
        pages.dashboard.move_money_modal_to.check_text('Credit – QoloQolo')
        pages.dashboard.btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("//*[contains(text(), 'Credit Clear • Qolo')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$2.00')
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color",
                                                                                                    "rgb(88, 182, 62)")
        pages.dashboard.move_money_modal_from.check_text('Netting – QoloQolo')
        pages.dashboard.move_money_modal_to.check_text('Credit – QoloQolo')

    @allure.title("Move money. Netting ConnexPay")
    def test_move_money_netting_connex_pay(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.move_money_type_operation.click()
        sleep(2)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        sleep(2)
        expect(page.locator("(//div[contains(@class, 'display_flex flex-direction_column')])[3]")).to_contain_text('Netting – ConnexPay –')
        expect(page.locator("(//div[contains(@class, 'display_flex flex-direction_column')])[2]")).to_contain_text('MTS')
        page.locator('//input[@id="amount"]').fill("2")
        pages.dashboard.btn_next.click()
        expect(page.locator("//*[contains(text(), 'Netting • ConnexPay')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text('$2.00')
        pages.dashboard.move_money_modal_from.check_text('1 – MTSConnexPay')
        pages.dashboard.move_money_modal_to.check_text('Netting – ConnexPayConnexPay')
        pages.dashboard.btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("//*[contains(text(), 'Netting • ConnexPay')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$2.00')
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color", "rgb(88, 182, 62)")
        pages.dashboard.move_money_modal_from.check_text('1 – MTSConnexPay')
        pages.dashboard.move_money_modal_to.check_text('Netting – ConnexPayConnexPay')

    @allure.title("Move money. Netting Qolo")
    def test_move_money_netting_qolo(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.modal_tab_qolo.click()
        pages.dashboard.move_money_type_operation.click()
        sleep(2)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        sleep(2)
        expect(page.locator("(//div[contains(@class, 'display_flex flex-direction_column')])[3]")).to_contain_text(
            'Netting – Qolo –')
        expect(page.locator("(//div[contains(@class, 'display_flex flex-direction_column')])[2]")).to_contain_text(
            '284 – Jncrjo – ')
        page.locator('//input[@id="amount"]').fill("2")
        pages.dashboard.btn_next.click()
        expect(page.locator("//*[contains(text(), 'Netting • Qolo')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text('$2.00')
        pages.dashboard.move_money_modal_from.check_text('284 – JncrjoQolo')
        pages.dashboard.move_money_modal_to.check_text('Netting – QoloQolo')
        pages.dashboard.btn_transfer.click()
        sleep(2)
        assert pages.dashboard.move_money_title_made_transfer.is_visible()
        expect(page.locator("//*[contains(text(), 'Netting • Qolo')]")).to_be_visible()
        expect(
            page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_text(
            '$2.00')
        expect(page.locator("(//*[contains(@class, 'display_flex flex-direction_column gap_1')]/span)[1]")).to_have_css(
            "color", "rgb(88, 182, 62)")
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-slot="icon"]')).to_have_css("color",
                                                                                                    "rgb(88, 182, 62)")
        pages.dashboard.move_money_modal_from.check_text('284 – JncrjoQolo')
        pages.dashboard.move_money_modal_to.check_text('Netting – QoloQolo')

    @allure.title("Move money. Not enough money")
    def test_check_not_enough_money(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.move_money_type_operation.click()
        sleep(2)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        sleep(2)
        page.locator("(//*[contains(@class, 'styles_endContent')])[3]").click()
        page.locator('(//button[@data-test-id="action"])[5]').click()
        page.locator('//input[@id="amount"]').fill('95.00')
        page.locator('//button[@data-test-id="button"]/span[contains(text(), "Next")]').click()
        expect(page.get_by_text("Review transfer details")).to_be_visible()
        page.locator('//span[contains(text(), "Transfer")]').click()
        pages.cards.toast.check_text('Not enough money.')
        expect(page.locator('//*[@data-test-id="toast"]')).to_have_css("color", "rgb(255, 255, 255)")

    @allure.title("Move money. Amount cannot be zero.")
    def test_check_amount_cannot_be_zero(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.accounts.click()
        page.locator("//h1[contains(text(), 'Accounts')]").wait_for(timeout=2000)
        pages.dashboard.button_move_money.click()
        pages.dashboard.move_money_type_operation.click()
        sleep(2)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        sleep(2)
        page.locator("(//*[contains(@class, 'styles_endContent')])[3]").click()
        page.locator('(//button[@data-test-id="action"])[5]').click()
        page.locator('//input[@id="amount"]').fill('0')
        page.locator('//button[@data-test-id="button"]/span[contains(text(), "Next")]').click()
        expect(page.get_by_text("Review transfer details")).to_be_visible()
        page.locator('//span[contains(text(), "Transfer")]').click()
        pages.cards.toast.check_text("Amount should be greater than 0")
        expect(page.locator('//*[@data-test-id="toast"]')).to_have_css("color", "rgb(255, 255, 255)")
