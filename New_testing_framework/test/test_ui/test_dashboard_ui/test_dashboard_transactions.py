from time import sleep

import allure
from playwright.sync_api import Page, expect

from api.function_api import api_request_context, api_post
from data.input_data.data_card import CARD_UK, PENDING, COUNTRY_US, CURRENCY_USD, SETTLED, COUNTRY_GB, CURRENCY_EUR, REFUND, \
    REVERSAL, DECLINED, DECLINED_PENDING
from data.input_data.users import USER_01
from pages.pages import Pages
from steps import Steps
from test.test_api.conftest import VISA, MC, VISA_TRANS
from utils.consts import DASHBOARD_URL, DASHBOARD_URL_TRANS_RANGE


class TestDashboardTransactions:
    @allure.title("Check page transactions")
    def test_check_page_transactions(self, page: Page, pages: Pages,
                                       steps: Steps, playwright):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        assert pages.dashboard.title_trans.is_visible()
        assert pages.dashboard.spend.is_visible()
        assert pages.dashboard.pre_auth.is_visible()
        assert pages.dashboard.filter_company.is_visible()
        assert pages.dashboard.filter_by_user.is_visible()
        assert pages.dashboard.filter_status.is_visible()
        assert pages.dashboard.filter_by_card.is_visible()

    @allure.title("Check total row table")
    def test_check_total_row_table(self, page: Page, pages: Pages,
                                   steps: Steps, playwright):
        page.goto(DASHBOARD_URL_TRANS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Transactions')
        assert pages.dashboard.title_trans.is_visible()
        pages.dashboard.total_row_table.check_text("18 May – 19 May$1,656.14")

    @allure.title("Check all total spend")
    def test_check_all_total_spend(self, page: Page, pages: Pages,
                                   steps: Steps, playwright):
        page.goto(DASHBOARD_URL_TRANS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Transactions')
        assert pages.dashboard.title_trans.is_visible()
        page.locator("(//*[@data-test-id = 'info-popover-activator']//div)[2]").click()
        steps.dashboardSteps.check_total_spend(page)

    @allure.title("Check pending fee")
    def test_check_pending_fee(self, page: Page, pages: Pages,
                               steps: Steps, playwright):
        page.goto(DASHBOARD_URL_TRANS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Transactions')
        page.locator("(//span[contains(text(), '$95.36')])[1]").hover()
        page.locator("(//*[@data-test-id = 'info-popover-activator']/div/div)[3]").hover()
        pages.dashboard.popper_info.check_text('Payment$93.00Cross-border fee$1.43FX fee$0.93')

    @allure.title("Check settled fee")
    def test_check_settled_fee(self, page: Page, pages: Pages,
                               steps: Steps, playwright):
        page.goto(DASHBOARD_URL_TRANS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Transactions')
        page.locator("(//span[contains(text(), '$227.96')])[1]").hover()
        page.locator("(//*[@data-test-id = 'info-popover-activator']/div/div)[7]").hover()
        pages.dashboard.popper_info.check_text('Payment$223.00Cross-border fee$2.73FX fee$2.23')

    @allure.title("Check reversed fee")
    def test_check_reversed_fee(self, page: Page, pages: Pages,
                                steps: Steps, playwright):
        page.goto(DASHBOARD_URL_TRANS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Transactions')
        page.locator("(//span[contains(text(), '$36.20')])[1]").hover()
        page.locator("(//*[@data-test-id = 'info-popover-activator']/div/div)[19]").hover()
        pages.dashboard.popper_info.check_text('Payment$35.00Cross-border fee$0.85FX fee$0.35')

    @allure.title("Check refund fee")
    def test_check_refund_fee(self, page: Page, pages: Pages,
                              steps: Steps, playwright):
        page.goto(DASHBOARD_URL_TRANS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Transactions')
        page.locator("(//span[contains(text(), '$22.94')])[1]").hover()
        page.locator("(//*[@data-test-id = 'info-popover-activator']/div/div)[22]").hover()
        pages.dashboard.popper_info.check_text('Payment$22.00Cross-border fee$0.72FX fee$0.22')

    @allure.title("Check decline fee")
    def test_check_decline_fee(self, page: Page, pages: Pages,
                               steps: Steps, playwright):
        page.goto(DASHBOARD_URL_TRANS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Transactions')
        page.locator("(//span[contains(text(), '$0.50')])[1]").hover()
        page.locator("(//*[@data-test-id = 'info-popover-activator']/div/div)[15]").hover()
        pages.dashboard.popper_info.check_text('Payment$14.00Decline fee$0.50')
        expect(page.locator('(//*[@data-test-id="pip"])[13]')).to_have_css("color", "rgb(230, 72, 61)")

    @allure.title("Check each row table")
    def test_check_each_row_table(self, page: Page, pages: Pages,
                                  steps: Steps, playwright):
        page.goto(DASHBOARD_URL_TRANS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Transactions')
        steps.dashboardSteps.check_each_row_table_trans(page)

    @allure.title("Check all companies")
    def test_check_all_companies(self, page: Page, pages: Pages,
                                 steps: Steps, playwright):
        page.goto(DASHBOARD_URL_TRANS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Transactions')
        steps.dashboardSteps.check_companies_names(page)
        pages.dashboard.button_next.click()
        steps.dashboardSteps.check_companies_name_second_page(page)
        pages.dashboard.button_next.click()
        steps.dashboardSteps.check_companies_name_fird_page(page)

    @allure.title("Check all cards")
    def test_check_all_cards(self, page: Page, pages: Pages,
                             steps: Steps, playwright):
        page.goto(DASHBOARD_URL_TRANS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Transactions')
        steps.dashboardSteps.check_all_cards_first_page(page)
        pages.dashboard.button_next.click()
        steps.dashboardSteps.check_all_cards_second_page(page)
        pages.dashboard.button_next.click()
        steps.dashboardSteps.check_companies_cards_fird_page(page)

    @allure.title("Check all sums")
    def test_check_all_sums(self, page: Page, pages: Pages,
                            steps: Steps, playwright):
        page.goto(DASHBOARD_URL_TRANS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Transactions')
        steps.dashboardSteps.check_all_sums_first_page(page)
        pages.dashboard.button_next.click()
        steps.dashboardSteps.check_all_sums_second_page(page)
        pages.dashboard.button_next.click()
        steps.dashboardSteps.check_all_sums_fird_page(page)

    @allure.title("Check modal pending transactions")
    def test_check_pending_modal(self, page: Page, pages: Pages,
                                 steps: Steps, playwright):
        page.goto(DASHBOARD_URL_TRANS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Transactions')
        page.locator("(//tr[contains(@class, 'hover-visible-container')])[10]").click()
        assert pages.dashboard.pending_modal.is_visible()
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-test-id="pip"]')).to_have_css("color", "rgba(20, 21, 26, 0.6)")
        expect(page.locator('//*[@data-test-id="modal-body"]//p')).to_have_css("color", "rgba(20, 21, 26, 0.6)")
        expect(page.locator("//*[contains(text(), '$93.00')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), '••4179 card_3')]")).to_be_visible()
        expect(page.locator("(//span[contains(text(), 'green company')])[3]")).to_be_visible()
        expect(page.locator("//span[contains(text(), '18 May, 07:20')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), 'Converted to 2.00 EUR')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), '1.00 USD = 0.02 EUR')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), 'Exchange fee $0.93')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), 'International fee $1.43')]")).to_be_visible()
        assert pages.dashboard.pending_in_modal.is_visible()
        assert pages.dashboard.facebook_modal.is_visible()
        assert pages.dashboard.gb_country_modal.is_visible()
        assert pages.dashboard.mcc_modal.is_visible()
        expect(page.locator("//div[contains(text(), '5273')]")).to_be_visible()

    @allure.title("Check modal settled transactions")
    def test_check_settled_modal(self, page: Page, pages: Pages,
                                 steps: Steps, playwright):
        page.goto(DASHBOARD_URL_TRANS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Transactions')
        page.locator("(//tr[contains(@class, 'hover-visible-container')])[23]").click()
        assert pages.dashboard.settled_modal.is_visible()
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-test-id="pip"]')).to_have_css("color", "rgb(111, 198, 87)")
        expect(page.locator('//*[@data-test-id="modal-body"]//p')).to_have_css("color", "rgb(20, 21, 26)")
        expect(page.locator("//*[contains(text(), '$223.00')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), '••9147 red_card')]")).to_be_visible()
        expect(page.locator("//*[@data-test-id = 'modal-body']//span[contains(text(), 'red company')]")).to_be_visible()
        expect(page.locator("(//span[contains(text(), '18 May, 07:17')])[1]")).to_be_visible()
        expect(page.locator("//span[contains(text(), 'Converted to 2.00 EUR')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), '1.00 USD = 0.01 EUR')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), 'Exchange fee $2.23')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), 'International fee $2.73')]")).to_be_visible()
        assert pages.dashboard.settled_in_modal.is_visible()
        assert pages.dashboard.facebook_modal.is_visible()
        assert pages.dashboard.gb_country_modal.is_visible()
        assert pages.dashboard.mcc_modal.is_visible()
        expect(page.locator("//div[contains(text(), '5250')]")).to_be_visible()

    @allure.title("Check modal refund transactions")
    def test_check_refund_modal(self, page: Page, pages: Pages,
                                steps: Steps, playwright):
        page.goto(DASHBOARD_URL_TRANS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Transactions')
        page.locator("(//tr[contains(@class, 'hover-visible-container')])[20]").click()
        assert pages.dashboard.refund_modal.is_visible()
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-test-id="pip"]')).to_have_css("color", "rgb(69, 143, 255)")
        expect(page.locator('//*[@data-test-id="modal-body"]//p')).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("//p[contains(text(), '$22.00')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), '••9147 red_card')]")).to_be_visible()
        expect(page.locator(
            "//*[@data-test-id = 'modal-body']//span[contains(text(), 'red company')]")).to_be_visible()
        expect(page.locator("(//span[contains(text(), '18 May, 07:17')])[1]")).to_be_visible()
        assert pages.dashboard.refund_in_modal.is_visible()
        assert pages.dashboard.facebook_modal.is_visible()
        assert pages.dashboard.gb_country_modal.is_visible()
        assert pages.dashboard.mcc_modal.is_visible()
        expect(page.locator("//div[contains(text(), '5255')]")).to_be_visible()

    @allure.title("Check modal reversed transactions")
    def test_check_reversed_modal(self, page: Page, pages: Pages,
                                  steps: Steps, playwright):
        page.goto(DASHBOARD_URL_TRANS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Transactions')
        page.locator("(//tr[contains(@class, 'hover-visible-container')])[17]").click()
        assert pages.dashboard.reversed_modal.is_visible()
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-test-id="pip"]')).to_have_css("color", "rgb(253, 176, 34)")
        expect(page.locator('//*[@data-test-id="modal-body"]//p')).to_have_css("color", "rgb(20, 21, 26)")
        pages.dashboard.reversed_sum.check_text('$35.00')
        expect(page.locator("//span[contains(text(), '••9147 red_card')]")).to_be_visible()
        expect(page.locator("//*[@data-test-id = 'modal-body']//span[contains(text(), 'red company')]")).to_be_visible()
        expect(page.locator("(//span[contains(text(), '18 May, 07:18')])[1]")).to_be_visible()
        expect(page.locator("(//span[contains(text(), '18 May, 07:18')])[2]")).to_be_visible()
        assert pages.dashboard.reversed_in_modal.is_visible()
        assert pages.dashboard.facebook_modal.is_visible()
        assert pages.dashboard.gb_country_modal.is_visible()
        assert pages.dashboard.mcc_modal.is_visible()
        expect(page.locator("//div[contains(text(), '5260')]")).to_be_visible()

    @allure.title("Check modal declined transactions")
    def test_check_declined_modal(self, page: Page, pages: Pages,
                                  steps: Steps, playwright):
        page.goto(DASHBOARD_URL_TRANS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Transactions')
        pages.dashboard.button_next.click()
        pages.cards.spinner.is_not_on_page(timeout=3000)
        page.locator("(//tr[contains(@class, 'hover-visible-container')])[5]").click()
        assert pages.dashboard.declined_modal.is_visible()
        expect(page.locator('//*[@data-test-id="modal-header"]//*[@data-test-id="pip"]')).to_have_css("color", "rgb(230, 72, 61)")
        expect(page.locator('//*[@data-test-id="modal-body"]//p')).to_have_css("color", "rgb(230, 72, 61)")
        pages.dashboard.reversed_sum.check_text('$11.00')
        expect(page.locator("//span[contains(text(), '••9933 employee')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), 'test Employee')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), '18 May, 07:15')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), 'Transaction declined')]")).to_be_visible()
        expect(page.locator(
            "//span[contains(text(), 'The transaction was declined for an unknown reason.')]")).to_be_visible()
        expect(page.locator("//div[contains(text(), 'Decline fee $0.50')]")).to_be_visible()
        assert pages.dashboard.facebook_modal.is_visible()
        assert pages.dashboard.gb_country_modal.is_visible()
        assert pages.dashboard.mcc_modal.is_visible()
        expect(page.locator("//div[contains(text(), '5239')]")).to_be_visible()

    @allure.title("Send new transaction pending")
    def test_check_new_trans_pending(self, page: Page, pages: Pages,
                                     steps: Steps, playwright, api_request_context):
        num = 88
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        sleep(1)
        pages.dashboard.total_spend_icon.click()
        text = pages.dashboard.total_pending_sum.get_text()
        total = pages.dashboard.total_spend_sum_trans.get_text()
        cross_fee = pages.dashboard.total_cross_border_fee.get_text()
        fee = pages.dashboard.total_fx_fee.get_text()
        api_post(api_request_context, num, CARD_UK, PENDING, COUNTRY_US, CURRENCY_USD)
        page.reload()
        pages.dashboard.total_spend_icon.click()
        text_after = pages.dashboard.total_pending_sum.get_text()
        cross_fee_after = pages.dashboard.total_cross_border_fee.get_text()
        fee_after = pages.dashboard.total_fx_fee.get_text()
        total_after = pages.dashboard.total_spend_sum_trans.get_text()
        assert total < total_after
        assert text < text_after
        assert cross_fee == cross_fee_after
        assert fee == fee_after
        pages.dashboard.status_trans_first_row.check_text("Pending")

    @allure.title("Send new transaction pending fee")
    def test_check_new_trans_pending_fee(self, page: Page, pages: Pages,
                                         steps: Steps, playwright, api_request_context):
        num = 18
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        pages.dashboard.total_spend_icon.click()
        total = pages.dashboard.total_spend_sum_trans.get_text()
        text = pages.dashboard.total_cross_border_fee.get_text()
        fee = pages.dashboard.total_fx_fee.get_text()
        api_post(api_request_context, num, CARD_UK, PENDING, COUNTRY_GB, CURRENCY_USD)
        page.reload()
        pages.dashboard.total_spend_icon.click()
        text_after = pages.dashboard.total_cross_border_fee.get_text()
        fee_after = pages.dashboard.total_fx_fee.get_text()
        total_after = pages.dashboard.total_spend_sum_trans.get_text()
        assert total < total_after
        assert text < text_after
        assert fee == fee_after
        pages.dashboard.status_trans_first_row.check_text("Pending")

    @allure.title("Send new pending fx fee transaction")
    def test_check_new_trans_pending_fx_fee(self, page: Page, pages: Pages,
                                            steps: Steps, playwright, api_request_context):
        num = 30
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        pages.dashboard.total_spend_icon.click()
        text = pages.dashboard.total_fx_fee.get_text()
        fee = pages.dashboard.total_cross_border_fee.get_text()
        total = pages.dashboard.total_spend_sum_trans.get_text()
        api_post(api_request_context, num, CARD_UK, PENDING, COUNTRY_GB, CURRENCY_EUR)
        page.reload()
        pages.dashboard.total_spend_icon.click()
        text_after = pages.dashboard.total_fx_fee.get_text()
        fee_after = pages.dashboard.total_cross_border_fee.get_text()
        total_after = pages.dashboard.total_spend_sum_trans.get_text()
        assert total < total_after
        assert text < text_after
        assert fee < fee_after
        pages.dashboard.status_trans_first_row.check_text("Pending")

    @allure.title("Send new settled transaction")
    def test_check_new_trans_settled(self, page: Page, pages: Pages,
                                     steps: Steps, playwright, api_request_context):
        num = 50
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        pages.dashboard.total_spend_icon.click()
        text = pages.dashboard.total_settled_sum.get_text()
        cross_fee = pages.dashboard.total_cross_border_fee.get_text()
        fee = pages.dashboard.total_fx_fee.get_text()
        total = pages.dashboard.total_spend_sum_trans.get_text()
        api_post(api_request_context, num, CARD_UK, SETTLED, COUNTRY_US, CURRENCY_USD)
        page.reload()
        pages.dashboard.total_spend_icon.click()
        text_after = pages.dashboard.total_settled_sum.get_text()
        cross_fee_after = pages.dashboard.total_cross_border_fee.get_text()
        fee_after = pages.dashboard.total_fx_fee.get_text()
        total_after = pages.dashboard.total_spend_sum_trans.get_text()
        assert total < total_after
        assert text < text_after
        assert fee == fee_after
        assert cross_fee == cross_fee_after
        pages.dashboard.status_trans_first_row.check_text("Settled")

    @allure.title("Send new settled fee transaction")
    def test_check_new_trans_settled_fee(self, page: Page, pages: Pages,
                                         steps: Steps, playwright, api_request_context):
        num = 35
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        pages.dashboard.total_spend_icon.click()
        text = pages.dashboard.total_settled_sum.get_text()
        total = pages.dashboard.total_spend_sum_trans.get_text()
        cross_fee = pages.dashboard.total_cross_border_fee.get_text()
        fee = pages.dashboard.total_fx_fee.get_text()
        api_post(api_request_context, num, CARD_UK, SETTLED, COUNTRY_GB, CURRENCY_USD)
        page.reload()
        pages.dashboard.total_spend_icon.click()
        text_after = pages.dashboard.total_settled_sum.get_text()
        total_after = pages.dashboard.total_spend_sum_trans.get_text()
        cross_fee_after = pages.dashboard.total_cross_border_fee.get_text()
        fee_after = pages.dashboard.total_fx_fee.get_text()
        assert total < total_after
        assert text < text_after
        assert fee == fee_after
        assert cross_fee < cross_fee_after
        pages.dashboard.status_trans_first_row.check_text("Settled")

    @allure.title("Send new settled fx fee transaction")
    def test_check_new_trans_settled_fx_fee(self, page: Page, pages: Pages,
                                            steps: Steps, playwright, api_request_context):
        num = 65
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        pages.dashboard.total_spend_icon.click()
        total = pages.dashboard.total_spend_sum_trans.get_text()
        text = pages.dashboard.total_refund_sum.get_text()
        cross_fee = pages.dashboard.total_cross_border_fee.get_text()
        fee = pages.dashboard.total_fx_fee.get_text()
        api_post(api_request_context, num, CARD_UK, SETTLED, COUNTRY_GB, CURRENCY_EUR)
        page.reload()
        pages.dashboard.total_spend_icon.click()
        total_after = pages.dashboard.total_spend_sum_trans.get_text()
        text_after = pages.dashboard.total_refund_sum.get_text()
        cross_fee_after = pages.dashboard.total_cross_border_fee.get_text()
        fee_after = pages.dashboard.total_fx_fee.get_text()
        assert total < total_after
        assert text == text_after
        assert fee < fee_after
        assert cross_fee < cross_fee_after
        pages.dashboard.status_trans_first_row.check_text("Settled")

    @allure.title("Send new refund transaction")
    def test_check_new_trans_refund(self, page: Page, pages: Pages,
                                    steps: Steps, playwright, api_request_context):
        num = 39
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        pages.dashboard.total_spend_icon.click()
        text = pages.dashboard.total_refund_sum.get_text()
        cross_fee = pages.dashboard.total_cross_border_fee.get_text()
        total = pages.dashboard.total_spend_sum_trans.get_text()
        fee = pages.dashboard.total_fx_fee.get_text()
        api_post(api_request_context, num, CARD_UK, REFUND, COUNTRY_US, CURRENCY_USD)
        page.reload()
        pages.dashboard.total_spend_icon.click()
        text_after = pages.dashboard.total_refund_sum.get_text()
        cross_fee_after = pages.dashboard.total_cross_border_fee.get_text()
        fee_after = pages.dashboard.total_fx_fee.get_text()
        total_after = pages.dashboard.total_spend_sum_trans.get_text()
        assert total > total_after
        assert text < text_after
        assert fee == fee_after
        assert cross_fee == cross_fee_after
        pages.dashboard.status_trans_first_row.check_text("Refund")

    @allure.title("Send new refund fee transaction")
    def test_check_new_trans_refund_fee(self, page: Page, pages: Pages,
                                        steps: Steps, playwright, api_request_context):
        num = 29
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        pages.dashboard.total_spend_icon.click()
        total = pages.dashboard.total_spend_sum_trans.get_text()
        text = pages.dashboard.total_refund_sum.get_text()
        cross_fee = pages.dashboard.total_cross_border_fee.get_text()
        fee = pages.dashboard.total_fx_fee.get_text()
        api_post(api_request_context, num, CARD_UK, REFUND, COUNTRY_GB, CURRENCY_USD)
        page.reload()
        pages.dashboard.total_spend_icon.click()
        text_after = pages.dashboard.total_refund_sum.get_text()
        cross_fee_after = pages.dashboard.total_cross_border_fee.get_text()
        fee_after = pages.dashboard.total_fx_fee.get_text()
        total_after = pages.dashboard.total_spend_sum_trans.get_text()
        assert total > total_after
        assert text < text_after
        assert fee == fee_after
        assert cross_fee > cross_fee_after
        pages.dashboard.status_trans_first_row.check_text("Refund")

    @allure.title("Send new refund fx fee transaction")
    def test_check_new_trans_refund_fx_fee(self, page: Page, pages: Pages,
                                           steps: Steps, playwright, api_request_context):
        num = 16
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        pages.dashboard.total_spend_icon.click()
        total = pages.dashboard.total_spend_sum_trans.get_text()
        text = pages.dashboard.total_refund_sum.get_text()
        cross_fee = pages.dashboard.total_cross_border_fee.get_text()
        fee = pages.dashboard.total_fx_fee.get_text()
        api_post(api_request_context, num, CARD_UK, REFUND, COUNTRY_GB, CURRENCY_EUR)
        page.reload()
        pages.dashboard.total_spend_icon.click()
        total_after = pages.dashboard.total_spend_sum_trans.get_text()
        text_after = pages.dashboard.total_refund_sum.get_text()
        cross_fee_after = pages.dashboard.total_cross_border_fee.get_text()
        fee_after = pages.dashboard.total_fx_fee.get_text()
        assert total > total_after
        assert text < text_after
        assert fee > fee_after
        assert cross_fee > cross_fee_after
        pages.dashboard.status_trans_first_row.check_text("Refund")

    @allure.title("Send new reversed transaction")
    def test_check_new_trans_reversed(self, page: Page, pages: Pages,
                                      steps: Steps, playwright, api_request_context):
        num = 46
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        pages.dashboard.total_spend_icon.click()
        text = pages.dashboard.total_reversed_sum.get_text()
        cross_fee = pages.dashboard.total_cross_border_fee.get_text()
        fee = pages.dashboard.total_fx_fee.get_text()
        total = pages.dashboard.total_spend_sum_trans.get_text()
        api_post(api_request_context, num, CARD_UK, REVERSAL, COUNTRY_US, CURRENCY_USD)
        page.reload()
        pages.dashboard.total_spend_icon.click()
        text_after = pages.dashboard.total_reversed_sum.get_text()
        cross_fee_after = pages.dashboard.total_cross_border_fee.get_text()
        fee_after = pages.dashboard.total_fx_fee.get_text()
        total_after = pages.dashboard.total_spend_sum_trans.get_text()
        assert total == total_after
        assert text < text_after
        assert fee == fee_after
        assert cross_fee == cross_fee_after
        pages.dashboard.status_trans_first_row.check_text("Reversed")

    @allure.title("Send new reversed fee transaction")
    def test_check_new_trans_reversed_fee(self, page: Page, pages: Pages,
                                          steps: Steps, playwright, api_request_context):
        num = 17
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        pages.dashboard.total_spend_icon.click()
        text = pages.dashboard.total_reversed_sum.get_text()
        total = pages.dashboard.total_spend_sum_trans.get_text()
        cross_fee = pages.dashboard.total_cross_border_fee.get_text()
        fee = pages.dashboard.total_fx_fee.get_text()
        api_post(api_request_context, num, CARD_UK, REVERSAL, COUNTRY_GB, CURRENCY_USD)
        page.reload()
        pages.dashboard.total_spend_icon.click()
        text_after = pages.dashboard.total_reversed_sum.get_text()
        cross_fee_after = pages.dashboard.total_cross_border_fee.get_text()
        fee_after = pages.dashboard.total_fx_fee.get_text()
        total_after = pages.dashboard.total_spend_sum_trans.get_text()
        assert total == total_after
        assert text < text_after
        assert fee == fee_after
        assert cross_fee == cross_fee_after
        pages.dashboard.status_trans_first_row.check_text("Reversed")

    @allure.title("Send new reversed fx fee transaction")
    def test_check_new_trans_reversed_fx_fee(self, page: Page, pages: Pages,
                                             steps: Steps, playwright, api_request_context):
        num = 21
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        pages.dashboard.total_spend_icon.click()
        text = pages.dashboard.total_reversed_sum.get_text()
        cross_fee = pages.dashboard.total_cross_border_fee.get_text()
        fee = pages.dashboard.total_fx_fee.get_text()
        total = pages.dashboard.total_spend_sum_trans.get_text()
        api_post(api_request_context, num, CARD_UK, REVERSAL, COUNTRY_GB, CURRENCY_USD)
        page.reload()
        pages.dashboard.total_spend_icon.click()
        text_after = pages.dashboard.total_reversed_sum.get_text()
        cross_fee_after = pages.dashboard.total_cross_border_fee.get_text()
        total_after = pages.dashboard.total_spend_sum_trans.get_text()
        fee_after = pages.dashboard.total_fx_fee.get_text()
        assert text < text_after
        assert fee == fee_after
        assert cross_fee == cross_fee_after
        assert total == total_after
        pages.dashboard.status_trans_first_row.check_text("Reversed")

    @allure.title("Send new decline transaction")
    def test_check_new_trans_decline(self, page: Page, pages: Pages,
                                     steps: Steps, playwright, api_request_context):
        num = 10
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        pages.dashboard.total_spend_icon.click()
        text = pages.dashboard.total_decline_fee.get_text()
        cross_fee = pages.dashboard.total_cross_border_fee.get_text()
        fee = pages.dashboard.total_fx_fee.get_text()
        total = pages.dashboard.total_spend_sum_trans.get_text()
        api_post(api_request_context, num, VISA, DECLINED, COUNTRY_US, CURRENCY_USD)
        page.reload()
        pages.dashboard.total_spend_icon.click()
        text_after = pages.dashboard.total_decline_fee.get_text()
        cross_fee_after = pages.dashboard.total_cross_border_fee.get_text()
        fee_after = pages.dashboard.total_fx_fee.get_text()
        total_after = pages.dashboard.total_spend_sum_trans.get_text()
        assert total < total_after
        assert text < text_after
        assert fee == fee_after
        assert cross_fee == cross_fee_after
        pages.dashboard.status_trans_first_row.check_text("Declined")

    @allure.title("Send new decline fee transaction")
    def test_check_new_trans_decline_fee(self, page: Page, pages: Pages,
                                         steps: Steps, playwright, api_request_context):
        num = 15
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        pages.dashboard.total_spend_icon.click()
        text = pages.dashboard.total_decline_fee.get_text()
        cross_fee = pages.dashboard.total_cross_border_fee.get_text()
        fee = pages.dashboard.total_fx_fee.get_text()
        total = pages.dashboard.total_spend_sum_trans.get_text()
        api_post(api_request_context, num, VISA, DECLINED, COUNTRY_GB, CURRENCY_USD)
        page.reload()
        pages.dashboard.total_spend_icon.click()
        text_after = pages.dashboard.total_decline_fee.get_text()
        cross_fee_after = pages.dashboard.total_cross_border_fee.get_text()
        fee_after = pages.dashboard.total_fx_fee.get_text()
        total_after = pages.dashboard.total_spend_sum_trans.get_text()
        assert total < total_after
        assert text < text_after
        assert fee == fee_after
        assert cross_fee == cross_fee_after
        pages.dashboard.status_trans_first_row.check_text("Declined")

    @allure.title("Send new decline fx fee transaction")
    def test_check_new_trans_decline_fx_fee(self, page: Page, pages: Pages,
                                            steps: Steps, playwright, api_request_context):
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        pages.dashboard.total_spend_icon.click()
        text = pages.dashboard.total_decline_fee.get_text()
        cross_fee = pages.dashboard.total_cross_border_fee.get_text()
        fee = pages.dashboard.total_fx_fee.get_text()
        total = pages.dashboard.total_spend_sum_trans.get_text()
        api_post(api_request_context, 18, VISA, DECLINED, COUNTRY_GB, CURRENCY_EUR)
        page.reload()
        pages.dashboard.total_spend_icon.click()
        text_after = pages.dashboard.total_decline_fee.get_text()
        cross_fee_after = pages.dashboard.total_cross_border_fee.get_text()
        fee_after = pages.dashboard.total_fx_fee.get_text()
        total_after = pages.dashboard.total_spend_sum_trans.get_text()
        assert total < total_after
        assert text < text_after
        assert fee == fee_after
        assert cross_fee == cross_fee_after
        pages.dashboard.status_trans_first_row.check_text("Declined")

    @allure.title("Send new declined pending transaction")
    def test_check_new_trans_declined_pending(self, page: Page, pages: Pages,
                                              steps: Steps, playwright, api_request_context):
        num = 23
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        pages.dashboard.total_spend_icon.click()
        settled = pages.dashboard.total_settled_sum.get_text()
        decline = pages.dashboard.total_decline_fee.get_text()
        cross_fee = pages.dashboard.total_cross_border_fee.get_text()
        fee = pages.dashboard.total_fx_fee.get_text()
        total = pages.dashboard.total_spend_sum_trans.get_text()
        reversed = pages.dashboard.total_reversed_sum.get_text()
        pending = pages.dashboard.total_pending_sum.get_text()
        refund = pages.dashboard.total_refund_sum.get_text()
        api_post(api_request_context, num, CARD_UK, DECLINED_PENDING, COUNTRY_GB, CURRENCY_EUR)
        page.reload()
        pages.dashboard.total_spend_icon.click()
        refund_after = pages.dashboard.total_refund_sum.get_text()
        decline_after = pages.dashboard.total_decline_fee.get_text()
        cross_fee_after = pages.dashboard.total_cross_border_fee.get_text()
        fee_after = pages.dashboard.total_fx_fee.get_text()
        total_after = pages.dashboard.total_spend_sum_trans.get_text()
        pending_after = pages.dashboard.total_pending_sum.get_text()
        settled_after = pages.dashboard.total_settled_sum.get_text()
        reversed_after = pages.dashboard.total_reversed_sum.get_text()
        assert reversed == reversed_after
        assert settled == settled_after
        assert pending == pending_after
        assert total == total_after
        assert decline == decline_after
        assert fee == fee_after
        assert refund == refund_after
        assert cross_fee == cross_fee_after
        pages.dashboard.status_trans_first_row.check_text("Pending")

    @allure.title("Send new pending transaction for pre-auth with fee")
    def test_check_new_trans_pending_pre_auth_with_fee(self, page: Page, pages: Pages,
                                              steps: Steps, playwright, api_request_context):
        num = 0
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        api_post(api_request_context, num, CARD_UK, DECLINED_PENDING, COUNTRY_GB, CURRENCY_EUR)
        page.locator("//*[@data-test-id='tab']//div[contains(text(), 'Pre-auth')]").click()
        steps.dashboardSteps.check_status_in_row(page, '1', 'Pending')
        expect(page.locator('(//td//*[contains(@class, "truncate")])[1]')).to_have_text('1 – MTS')
        steps.universalSteps.check_any_text_at_row_table(page, '5', 'GB')
        steps.universalSteps.check_any_text_at_row_table(page, '6', 'EUR')
        steps.universalSteps.check_any_text_at_row_table(page, '7', '556150')

    @allure.title("Send new pending transaction for pre-auth without fee")
    def test_check_new_trans_pending_pre_auth_without_fee(self, page: Page, pages: Pages,
                                                        steps: Steps, playwright, api_request_context):
        num = 0
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        api_post(api_request_context, num, VISA, DECLINED_PENDING, COUNTRY_US, CURRENCY_USD)
        page.locator("//*[@data-test-id='tab']//div[contains(text(), 'Pre-auth')]").click()
        steps.dashboardSteps.check_status_in_row(page, '1', 'Pending')
        expect(page.locator('(//td//*[contains(@class, "truncate")])[1]')).to_have_text('1 – MTS')
        steps.universalSteps.check_any_text_at_row_table(page, '5', 'US')
        steps.universalSteps.check_any_text_at_row_table(page, '6', 'USD')
        steps.universalSteps.check_any_text_at_row_table(page, '7', '531993')

    @allure.title("Send new declined transaction for pre-auth without fee")
    def test_check_new_trans_declined_pre_auth_without_fee(self, page: Page, pages: Pages,
                                                          steps: Steps, playwright, api_request_context):
        num = 0
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        api_post(api_request_context, num, MC, DECLINED, COUNTRY_US, CURRENCY_USD)
        page.locator("//*[@data-test-id='tab']//div[contains(text(), 'Pre-auth')]").click()
        steps.dashboardSteps.check_status_in_row(page, '1', 'Declined')
        expect(page.locator('(//td//*[contains(@class, "truncate")])[1]')).to_have_text('1 – MTS')
        steps.universalSteps.check_any_text_at_row_table(page, '5', 'US')
        steps.universalSteps.check_any_text_at_row_table(page, '6', 'USD')
        steps.universalSteps.check_any_text_at_row_table(page, '7', '531993')

    @allure.title("Send new declined transaction for pre-auth with fee")
    def test_check_new_trans_declined_pre_auth_with_fee(self, page: Page, pages: Pages,
                                                           steps: Steps, playwright, api_request_context):
        num = 0
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.transactions.click()
        pages.dashboard.title_trans.is_on_page(timeout=3000)
        api_post(api_request_context, num, VISA_TRANS, DECLINED, COUNTRY_GB, CURRENCY_EUR)
        page.locator("//*[@data-test-id='tab']//div[contains(text(), 'Pre-auth')]").click()
        steps.dashboardSteps.check_status_in_row(page, '1', 'Declined')
        expect(page.locator('(//td//*[contains(@class, "truncate")])[1]')).to_have_text('1 – MTS')
        steps.universalSteps.check_any_text_at_row_table(page, '5', 'GB')
        steps.universalSteps.check_any_text_at_row_table(page, '6', 'EUR')
        steps.universalSteps.check_any_text_at_row_table(page, '7', '441112')

