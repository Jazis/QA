from time import sleep

import allure
from playwright.sync_api import Page, expect
from data.input_data.users import USER_01
from pages.pages import Pages
from steps import Steps
from utils.consts import DASHBOARD_SUBSCRIPTIONS_RANGE, DASHBOARD_SUBS_RANGE, DASHBOARD_URL, DASHBOARD_SUBS_ALL_TIME


class TestDashboardSubscriptions:
    @allure.title("Check page subscriptions")
    def test_check_page_subscriptions(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_SUBSCRIPTIONS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Subscriptions')
        expect(page.locator('//*[@placeholder="Company name or ID"]')).to_be_visible()
        assert pages.dashboard.filter_plan.is_visible()
        assert pages.dashboard.filter_by_status.is_visible()
        assert pages.dashboard.filter_by_company.is_visible()
        expect(page.locator('//*[@data-test-id="date-picker-with-presets-activator"]//span[contains(text(), "6 Sept – 10 Sept")]')).to_be_visible()
        expect(page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Date")]')).to_be_visible()
        expect(page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Amount")]')).to_be_visible()
        steps.universalSteps.check_titles_at_table(page, '2', 'Company')
        steps.universalSteps.check_titles_at_table(page, '3', 'Plan')
        steps.universalSteps.check_titles_at_table(page, '4', 'Status')
        steps.universalSteps.check_titles_at_table(page, '5', 'Period')
        expect(page.locator("//th[@colspan='5']")).to_have_text('$700.00')
        steps.universalSteps.check_any_text_at_row_table(page, '1', '10 Sept')
        steps.universalSteps.check_any_text_at_row_table(page, '2', '565 – brnGYcmI')
        steps.universalSteps.check_any_text_at_row_table(page, '3', 'Pro')
        steps.universalSteps.check_any_text_at_row_table(page, '4', 'Unpaid')
        steps.universalSteps.check_any_text_at_row_table(page, '5', '10 Sept – 11 Oct')
        steps.universalSteps.check_any_text_at_row_table(page, '6', '$371.00')
        expect(page.locator("(//td)[7]//button[1]")).to_have_text('Charge')
        expect(page.locator("(//td)[7]//button[2]")).to_have_text('Cancel')

        steps.universalSteps.check_any_text_at_row_table(page, '50', '7 Sept')
        steps.universalSteps.check_any_text_at_row_table(page, '51', '200 – 1398h 3476n')
        steps.universalSteps.check_any_text_at_row_table(page, '52', 'Pro')
        steps.universalSteps.check_any_text_at_row_table(page, '53', 'Canceled')
        steps.universalSteps.check_any_text_at_row_table(page, '54', '8 Sept – 8 Oct')
        steps.universalSteps.check_any_text_at_row_table(page, '55', '$471.00')
        expect(page.locator("(//td)[56]//span[1]")).to_have_text('Canceled')
        expect(page.locator("(//td)[56]//span[2]")).to_have_text('on 10 Sept, 12:42')

        steps.universalSteps.check_any_text_at_row_table(page, '57', '7 Sept')
        expect(page.locator("(//td)[58]//*[@data-test-id='item-with-pip']")).to_be_visible()
        steps.universalSteps.check_any_text_at_row_table(page, '58', '202 – nmfdADSF retryty')
        steps.universalSteps.check_any_text_at_row_table(page, '59', 'Private')
        steps.universalSteps.check_any_text_at_row_table(page, '60', 'Paid')
        steps.universalSteps.check_any_text_at_row_table(page, '61', '8 Sept – 8 Oct')
        steps.universalSteps.check_any_text_at_row_table(page, '62', '$600.00')
        expect(page.locator("(//td)[63]//span[1]")).to_have_text('Paid')
        expect(page.locator("(//td)[63]//span[2]")).to_have_text('on 10 Sept, 12:42')

    @allure.title("Search by name company")
    def test_search_by_company(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_SUBSCRIPTIONS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Subscriptions')
        page.locator('//input[@placeholder="Company name or ID"]').fill(' Iip')
        pages.dashboard.table_pagination.check_text('1 subscription')
        steps.universalSteps.check_any_text_at_row_table(page, '1', '10 Sept')
        steps.universalSteps.check_any_text_at_row_table(page, '2', '331 – Iipeu')
        steps.universalSteps.check_any_text_at_row_table(page, '3', 'Basic')
        steps.universalSteps.check_any_text_at_row_table(page, '4', 'Unpaid')
        steps.universalSteps.check_any_text_at_row_table(page, '5', '10 Sept – 11 Oct')
        steps.universalSteps.check_any_text_at_row_table(page, '6', '$100.00')
        expect(page.locator('(//td)[7]//button[1]')).to_have_text('Charge')
        expect(page.locator('(//td)[7]//button[2]')).to_have_text('Cancel')

    @allure.title("Filter by plan")
    def test_filter_by_plan(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_SUBSCRIPTIONS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Subscriptions')
        pages.dashboard.filter_plan.click()
        expect(page.locator('(//*[@data-test-id="checkbox"])[1]')).to_have_text('Basic')
        expect(page.locator('(//*[@data-test-id="checkbox"])[2]')).to_have_text('Pro')
        assert pages.dashboard.checkbox_private.is_visible()
        pages.dashboard.checkbox_private.click()
        pages.dashboard.table_pagination.check_text('2 subscriptions')
        pages.dashboard.tag.check_text('Private')
        steps.universalSteps.check_any_text_at_row_table(page, '2', '202 – nmfdADSF retryty')
        steps.universalSteps.check_any_text_at_row_table(page, '3', 'Private')
        steps.universalSteps.check_any_text_at_row_table(page, '9', '196 – testvvvvfg fdggr')
        steps.universalSteps.check_any_text_at_row_table(page, '10', 'Private')

    @allure.title("Filter by status")
    def test_filter_by_status(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_SUBSCRIPTIONS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Subscriptions')
        pages.dashboard.filter_by_status.click()
        expect(page.locator('//*[@data-test-id="checkbox"]//span[contains(text(), "Unpaid")]')).to_be_visible()
        expect(page.locator('//*[@data-test-id="checkbox"]//span[contains(text(), "Paid")]')).to_be_visible()
        page.locator('//*[@data-test-id="checkbox"]//span[contains(text(), "Paid")]').click()
        expect(page.locator('//*[@data-test-id="checkbox"]//span[contains(text(), "Failed")]')).to_be_visible()
        expect(page.locator('//*[@data-test-id="checkbox"]//span[contains(text(), "Canceled")]')).to_be_visible()
        page.locator('//*[@data-test-id="checkbox"]//span[contains(text(), "Canceled")]').click()
        pages.dashboard.tag.check_text('Paid, Canceled')
        pages.dashboard.table_pagination.check_text('3 subscriptions')
        steps.universalSteps.check_any_text_at_row_table(page, '2', '281 – EQlMct')
        steps.universalSteps.check_any_text_at_row_table(page, '4', 'Paid')
        steps.universalSteps.check_any_text_at_row_table(page, '9', '200 – 1398h 3476n')
        steps.universalSteps.check_any_text_at_row_table(page, '10', 'Pro')

    @allure.title("Filter by company")
    def test_filter_by_company(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_SUBSCRIPTIONS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Subscriptions')
        pages.dashboard.filter_company.click()
        page.locator("(//*[@data-test-id='text-field'])[2]//input").fill('EQlMct')
        page.locator("//span[contains(text(), '281 – EQlMct')]").click()
        pages.dashboard.tag.check_text("281 – EQlMct")
        steps.universalSteps.check_any_text_at_row_table(page, '2', '281 – EQlMct')
        steps.universalSteps.check_any_text_at_row_table(page, '4', 'Paid')
        pages.dashboard.table_pagination.check_text('1 subscription')

    @allure.title("Sort by date")
    def test_sort_by_date(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_SUBSCRIPTIONS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Subscriptions')
        steps.universalSteps.check_any_text_at_row_table(page, '1', '10 Sept')
        page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Date")]').hover()
        expect(page.locator("//span[contains(text(), 'Newest first')]")).to_be_visible()
        page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Date")]').click()
        expect(page.locator("//span[contains(text(), 'Oldest first')]")).to_be_visible()
        steps.universalSteps.check_any_text_at_row_table(page, '1', '6 Sept')
        pages.dashboard.table_pagination.check_text('13 subscriptions')

    @allure.title("Sort by amount")
    def test_sort_by_amount(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_SUBSCRIPTIONS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Subscriptions')
        steps.universalSteps.check_any_text_at_row_table(page, '6', '$371.00')
        page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Amount")]').hover()
        expect(page.locator("//span[contains(text(), 'Highest to lowest')]")).to_be_visible()
        page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Amount")]').click()
        page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Amount")]').click()
        expect(page.locator("//span[contains(text(), 'Lowest to highest')]")).to_be_visible()
        steps.universalSteps.check_any_text_at_row_table(page, '6', '$100.00')
        pages.dashboard.table_pagination.check_text('13 subscriptions')

    @allure.title("Check button Charge")
    def test_check_button_charge(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_SUBSCRIPTIONS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Subscriptions')
        page.locator("(//td)[7]//button[1]").click()
        steps.universalSteps.check_second_title(page, 'Subscription charge')
        expect(page.locator('//*[@data-test-id="modal-body"]//span[contains(text(), "$371.00")]')).to_be_visible()
        expect(page.locator('//*[@data-test-id="modal-body"]//span[contains(text(), "From")]')).to_be_visible()
        expect(page.locator('//*[@data-test-id="modal-body"]//span[contains(text(), "565 – brnGYcmI")]')).to_be_visible()
        expect(page.locator('(//*[@data-test-id="modal-body"]//span[contains(text(), ".00")])[2]')).to_be_visible()
        expect(page.locator('(//*[@data-test-id="modal-footer"]//button)[1]')).to_be_visible()
        expect(page.locator('(//*[@data-test-id="modal-footer"]//button)[2]')).to_be_visible()

    @allure.title("Check button Cancel")
    def test_check_button_cancel(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_SUBSCRIPTIONS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Subscriptions')
        page.locator("(//td)[7]//button[2]").click()
        steps.universalSteps.check_second_title(page, "Are you sure you want to cancel the company's subscription?")
        expect(page.locator('//*[@data-test-id="modal-body"]//span[contains(text(), "565 – brnGYcmI")]')).to_be_visible()
        expect(page.locator('//button//span[contains(text(), "Yes, cancel")]')).to_be_visible()
        page.locator('//button//span[contains(text(), "Back")]').click()
        expect(page.locator('//button//span[contains(text(), "Yes, cancel")]')).not_to_be_visible()

    @allure.title("Check colors on page")
    def test_check_colors_on_page(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(DASHBOARD_SUBSCRIPTIONS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Subscriptions')
        expect(page.locator('(//*[@data-test-id="button"])[4]')).to_have_css("color", "rgb(255, 255, 255)")
        expect(page.locator('(//*[@data-test-id="button"])[5]')).to_have_css("color", "rgb(20, 21, 26)")
        expect(page.locator('(//*[contains(@class, "display_flex gap_1")]//span)[5]')).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator('(//*[contains(@class, "display_flex gap_1")]//span)[6]')).to_have_css("color", "rgba(20, 21, 26, 0.6)")
        expect(page.locator('(//*[contains(@class, "display_flex gap_1")]//span)[15]')).to_have_css("color", "rgb(230, 72, 61)")
        expect(page.locator('(//*[contains(@class, "display_flex gap_1")]//span)[16]')).to_have_css("color", "rgba(20, 21, 26, 0.6)")
        expect(page.locator('(//*[@data-test-id="pip"])[1]')).to_have_css("color", "rgb(253, 176, 34)")
        expect(page.locator('(//*[@data-test-id="pip"])[3]')).to_have_css("color", "rgb(111, 198, 87)")
        expect(page.locator('(//*[@data-test-id="pip"])[8]')).to_have_css("color", "rgba(20, 21, 26, 0.4)")
        page.locator('(//*[@data-test-id="button"])[4]').click()
        page.locator('//*[@data-test-id="modal-dialog"]//span[text()="Charge"]').click()
        expect(page.locator("//*[@data-test-id='toast']")).to_have_css("color", "rgb(255, 255, 255)")

    @allure.title("Check each row bill")
    def test_check_each_row_bill(self, page: Page, pages: Pages,
                                 steps: Steps, playwright):
        page.goto(DASHBOARD_SUBS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Subscriptions')
        steps.dashboardSteps.check_ech_bill(page)
        pages.dashboard.table_pagination.check_text("13 subscriptions")

    @allure.title("Check charge button")
    def test_check_charge_button(self, page: Page, pages: Pages,
                                 steps: Steps, playwright):
        page.goto(DASHBOARD_SUBS_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Subscriptions')
        pages.dashboard.button_charge_first.click()
        steps.universalSteps.check_second_title(page, "Subscription charge")
        page.locator(
            "//*[@data-test-id='modal-footer']//*[@data-test-id='button']/span[contains(text(), 'Charge')]").click()
        pages.cards.toast.check_text("Payment failed: Not enough money.")

    @allure.title("Check chancel button")
    def test_check_chancel_button(self, page: Page, pages: Pages,
                                  steps: Steps, playwright):
        #time_now = datetime.now().strftime("%d %b, %H")  #:%M
        page.goto(DASHBOARD_URL)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Companies')
        pages.navigation_dashboard.dash_subscriptions.click()
        pages.dashboard.button_chancel_first.click()
        expect(page.locator('//h2')).to_have_text("Are you sure you want to cancel the company's subscription?")
        expect(page.locator('//*[@data-test-id="modal-body"]//*[@data-test-id="avatar"]')).to_be_visible()
        expect(page.locator("//*[@data-test-id='modal-footer']//*[contains(text(), 'Back')]")).to_be_visible()
        expect(page.locator('//*[@data-test-id="modal-footer"]//*[contains(text(), "Yes, cancel")]')).to_be_visible()
        page.locator('//*[@data-test-id="modal-footer"]//*[contains(text(), "Yes, cancel")]').click()
        pages.cards.toast.check_text("Subscription has been canceled")
        steps.dashboardSteps.check_status_in_row(page, '1', 'Canceled')
        expect(page.locator(
            "//*[contains(@class, 'display_flex gap_1')]/span[contains(text(), 'Canceled')]").last).to_have_text(
            'Canceled')
        sleep(1)
        #expect(page.locator(f"//*[contains(text(), 'on {time_now}')]")).to_be_visible()

    @allure.title("Check sort by amount")
    def test_check_sort_by_amount(self, page: Page, pages: Pages,
                                  steps: Steps, playwright):
        page.goto(DASHBOARD_SUBS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Subscriptions')
        steps.dashboardSteps.check_sort_bu_default(page)
        page.locator('(//*[@data-test-id="sortable-heading"])[2]').click()
        sleep(1.5)
        steps.dashboardSteps.check_sort_highest_to_lowest(page)
        page.locator('(//*[@data-test-id="sortable-heading"])[2]').click()
        page.locator("(//td[contains(@class, 'styles_tableAmount')]//span[contains(text(), '$0.00')])[1]").wait_for()
        steps.dashboardSteps.check_sort_lowest_to_highest(page)

    @allure.title("Check sort by date")
    def test_check_sort_by_date(self, page: Page, pages: Pages,
                                steps: Steps, playwright):
        page.goto(DASHBOARD_SUBS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Subscriptions')
        steps.dashboardSteps.check_sort_bu_default(page)
        page.locator('(//*[@data-test-id="sortable-heading"])[1]').click()
        sleep(1.5)
        steps.dashboardSteps.check_sort_by_date_to_newest(page)

    @allure.title("Check filter by status and company")
    def test_check_filter_by_status_and_company(self, page: Page, pages: Pages,
                                                steps: Steps, playwright):
        page.goto(DASHBOARD_SUBS_RANGE)
        steps.auth.authorize_in_test(page, USER_01.login, USER_01.password, 'Subscriptions')
        pages.dashboard.filter_status.click()
        pages.dashboard.checkbox_paid.click()
        pages.dashboard.filter_company.click()
        page.locator('//*[@data-test-id="menu-content"]//input[@autocomplete="off"]').fill('200')
        page.locator("//span[contains(text(), '200 – 1398h 3476n')]").click()
        sleep(2)
        pages.dashboard.tag.check_text('Paid')
        pages.dashboard.tag_2.check_text('200 – 1398h 3476n')
        expect(page.locator('//*[@title]')).to_have_text('200 – 1398h 3476n')
        steps.universalSteps.check_any_text_at_row_table(page, '4', 'Paid')
        steps.universalSteps.check_any_text_at_row_table(page, '7', 'Paidon 10 Jun, 07:32')






