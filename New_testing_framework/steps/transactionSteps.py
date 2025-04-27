from time import sleep

import allure
from playwright.sync_api import expect

from steps._base import BaseSteps


class TransactionSteps(BaseSteps):
    @allure.step('Check all dates')
    def check_all_dates(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableDate')]")).to_have_text(
            ['22 апр. 2024 г., 17:13', '22 апр. 2024 г., 17:13', '22 апр. 2024 г., 17:12', '22 апр. 2024 г., 17:10',
             '22 апр. 2024 г., 17:10', '22 апр. 2024 г., 17:10', '22 апр. 2024 г., 17:10', '22 апр. 2024 г., 17:09',
             '22 апр. 2024 г., 17:09', '22 апр. 2024 г., 17:09', '22 апр. 2024 г., 17:09', '22 апр. 2024 г., 16:52',
             '18 апр. 2024 г., 10:25', '18 апр. 2024 г., 10:24', '18 апр. 2024 г., 10:23', '18 апр. 2024 г., 10:22',
             '18 апр. 2024 г., 10:20', '18 апр. 2024 г., 10:20', '18 апр. 2024 г., 10:20', '18 апр. 2024 г., 10:20',
             '18 апр. 2024 г., 10:19', '18 апр. 2024 г., 10:19', '18 апр. 2024 г., 10:19', '18 апр. 2024 г., 10:19',
             '18 апр. 2024 г., 10:19'])


    @allure.step('Check all dates second page')
    def check_all_dates_second_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableDate')]")).to_have_text(
            ['18 апр. 2024 г., 10:19', '18 апр. 2024 г., 10:18', '18 апр. 2024 г., 10:18', '18 апр. 2024 г., 10:18',
             '18 апр. 2024 г., 10:18', '18 апр. 2024 г., 10:18', '18 апр. 2024 г., 10:17', '18 апр. 2024 г., 10:17',
             '18 апр. 2024 г., 10:14', '18 апр. 2024 г., 10:14', '18 апр. 2024 г., 10:13', '18 апр. 2024 г., 10:08',
             '18 апр. 2024 г., 10:07', '18 апр. 2024 г., 10:07', '18 апр. 2024 г., 10:07', '18 апр. 2024 г., 10:07',
             '18 апр. 2024 г., 10:06', '18 апр. 2024 г., 10:04', '18 апр. 2024 г., 10:04', '18 апр. 2024 г., 10:04',
             '18 апр. 2024 г., 10:03', '18 апр. 2024 г., 10:01', '18 апр. 2024 г., 10:00', '18 апр. 2024 г., 10:00',
             '18 апр. 2024 г., 09:57'])

    @allure.step('Check all dates third page')
    def check_all_dates_third_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableDate')]")).to_have_text(
            ['18 апр. 2024 г., 09:57', '18 апр. 2024 г., 09:56', '18 апр. 2024 г., 09:55', '18 апр. 2024 г., 09:53',
             '18 апр. 2024 г., 09:51', '18 апр. 2024 г., 09:49'])

    @allure.title("Check all transactions")
    def check_all_transactions(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableTransaction')]")).to_have_text(
            ['FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS',
             'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS',
             'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS',
             'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS'])

    @allure.title("Check all transactions second page")
    def check_all_transactions_second_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableTransaction')]")).to_have_text(
            ['FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS',
             'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS',
             'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS',
             'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS'])

    @allure.title("Check all transactions third page")
    def check_all_transactions_third_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableTransaction')]")).to_have_text(
            ['FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS', 'FACEBK ADS'])

    @allure.title("Check all statuses")
    def check_all_statuses(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableStatus')]")).to_have_text(
            ['Pending', 'Pending', 'Pending', 'Pending', 'Pending', 'Pending', 'Pending', 'Pending', 'Pending',
             'Pending', 'Pending', 'Settled', 'Settled', 'Settled', 'Settled', 'Refund', 'Pending', 'Pending',
             'Pending', 'Pending', 'Refund', 'Refund', 'Refund', 'Settled', 'Settled'])

    @allure.title("Check all statuses second page")
    def check_all_statuses_second_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableStatus')]")).to_have_text(
            ['Settled', 'Settled', 'Settled', 'Settled', 'Refund', 'Refund', 'Refund', 'Pending', 'Pending', 'Pending', 'Pending', 'Pending', 'Pending', 'Pending', 'Pending', 'Pending', 'Reversed', 'Settled', 'Settled', 'Settled', 'Settled', 'Declined', 'Settled', 'Refund', 'Settled'])

    @allure.title("Check all statuses third page")
    def check_all_statuses_third_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableStatus')]")).to_have_text(
            ['Declined', 'Reversed', 'Pending', 'Pending', 'Settled', 'Reversed'])

    @allure.title("Check all users")
    def check_all_users(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableUser')]")).to_have_text(
            ['invated emploee', 'invated emploee', 'invated emploee', 'invated emploee', 'invated emploee',
             'invated emploee', 'invated emploee', 'invated emploee', 'invated emploee', 'invated emploee',
             'invated emploee', 'invated emploee', 'test do not change', 'test do not change', 'test do not change',
             'test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change', 'test do not change'])

    @allure.title("Check all users second page")
    def check_all_users_second_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableUser')]")).to_have_text(
            ['test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change'])

    @allure.title("Check all users third page")
    def check_all_users_third_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableUser')]")).to_have_text(
            ['test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change', 'test do not change'])

    @allure.title("Check all cards")
    def check_all_cards(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCard')]")).to_have_text(
            ['••6070 65767', '••6070 65767', '••6070 65767', '••8002 6 apple', '••8002 6 apple', '••8002 6 apple',
             '••8002 6 apple', '••8002 6 apple', '••8002 6 apple', '••8002 6 apple', '••8002 6 apple', '••8002 6 apple',
             '••4039 dfd vcvcvcbcv', '••6978 fdgfgfd erwe', '••3663 WEDSCXS', '••3663 WEDSCXS', '••3663 WEDSCXS',
             '••3663 WEDSCXS', '••3663 WEDSCXS', '••3663 WEDSCXS', '••3663 WEDSCXS', '••3663 WEDSCXS', '••3663 WEDSCXS',
             '••3663 WEDSCXS', '••3663 WEDSCXS'])

    @allure.title("Check all cards second page")
    def check_all_cards_second_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCard')]")).to_have_text(
            ['••3663 WEDSCXS', '••9053 ASDCX', '••9053 ASDCX', '••9053 ASDCX', '••9053 ASDCX', '••9053 ASDCX',
             '••9053 ASDCX', '••9053 ASDCX', '••9053 ASDCX', '••9053 ASDCX', '••9053 ASDCX', '••4518 HRTYU',
             '••4518 HRTYU', '••4518 HRTYU', '••4518 HRTYU', '••4518 HRTYU', '••4518 HRTYU', '••1839 ASQWEDC',
             '••1839 ASQWEDC', '••1839 ASQWEDC', '••1839 ASQWEDC', '••1839 ASQWEDC', '••1839 ASQWEDC', '••1839 ASQWEDC',
             '••6980 test'])

    @allure.title("Check all cards third page")
    def check_all_cards_third_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCard')]")).to_have_text(
            ['••6980 test', '••6980 test', '••6980 test', '••6980 test', '••6980 test', '••6980 test'])

    @allure.title("Check all spend money")
    def check_all_money(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableAmount')]")).to_have_text(
            ['1,00\xa0$', '1,00\xa0$', '1,00\xa0$', '1,00\xa0$', '1,00\xa0$', '1,00\xa0$', '1,00\xa0$', '1,00\xa0$',
             '1,00\xa0$', '1,00\xa0$', '1,00\xa0$', '2,00\xa0$', '19,19\xa0$', '15,15\xa0$', '15,15\xa0$', '14,64\xa0$',
             '21,00\xa0$', '21,00\xa0$', '1,00\xa0$', '1,00\xa0$', '14,00\xa0$', '14,00\xa0$', '1,00\xa0$',
             '15,00\xa0$', '15,00\xa0$'])

    @allure.title("Check all spend money second page")
    def check_all_money_second_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableAmount')]")).to_have_text(
            ['15,00\xa0$', '15,00\xa0$', '15,00\xa0$', '1,00\xa0$', '1,00\xa0$', '1,00\xa0$', '1,00\xa0$', '11,00\xa0$', '11,00\xa0$', '10,00\xa0$', '1,00\xa0$', '1,00\xa0$', '1,00\xa0$', '1,00\xa0$', '1,00\xa0$', '1,00\xa0$', '1,00\xa0$', '20,90\xa0$', '20,90\xa0$', '20,90\xa0$', '0,50\xa0$ + 13,00\xa0$', '0,50\xa0$ + 1,00\xa0$', '1,00\xa0$', '1,00\xa0$', '2,00\xa0$'])

    @allure.title("Check all spend money third page")
    def check_all_money_third_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableAmount')]")).to_have_text(
            ['0,50\xa0$ + 21,00\xa0$', '16,00\xa0$', '4,00\xa0$', '4,00\xa0$', '2,00\xa0$', '1,00\xa0$'])

    @allure.title("Check filter statuses")
    def check_filter_statuses(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableStatus')]")).to_have_text(
            ['Settled', 'Settled', 'Settled', 'Settled', 'Refund', 'Refund', 'Refund', 'Refund', 'Settled', 'Settled',
             'Settled', 'Settled', 'Settled', 'Settled', 'Refund', 'Refund', 'Refund', 'Settled', 'Settled', 'Settled',
             'Settled', 'Settled', 'Refund', 'Settled', 'Settled'])

    @allure.title("Check filter by users")
    def check_filter_by_users(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableUser')]")).to_have_text(
            ['invated emploee', 'invated emploee', 'invated emploee', 'invated emploee', 'invated emploee',
             'invated emploee', 'invated emploee', 'invated emploee', 'invated emploee', 'invated emploee',
             'invated emploee', 'invated emploee'])

    @allure.title("Check filter by card")
    def check_filter_by_card(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCard')]")).to_have_text(
            ['••8002 6 apple', '••8002 6 apple', '••8002 6 apple', '••8002 6 apple', '••8002 6 apple', '••8002 6 apple',
             '••8002 6 apple', '••8002 6 apple', '••8002 6 apple'])

    @allure.title("Check results after search")
    def check_results_after_search(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableStatus')]")).to_have_text(
            ['Declined', 'Reversed', 'Pending', 'Pending', 'Reversed'])
        expect(page.locator("//td[contains(@class, 'styles_tableCard')]")).to_have_text(
            ['••6980 test', '••6980 test', '••6980 test', '••6980 test', '••6980 test'])
        expect(page.locator("//td[contains(@class, 'styles_tableUser')]")).to_have_text(
            ['test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change'])

    @allure.title("Check text at info-popover")
    def check_text_at_info_popover(self, page):
        expect(page.locator("//div[@data-test-id = 'info-popover-content']")).to_have_text(['Pending8,00\xa0$Reversed17,00\xa0$Комиссия за деклайн0,50\xa0$'])
        expect(page.locator("//th[contains(@class, 'text-align_end')]//*[@data-test-id = 'floating-activator']/following-sibling::span")).to_have_text(
            "8,50 $")

    @allure.title("Check dates sort by time")
    def check_dates_sort_by_time(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableDate')]")).to_have_text(
            ['22 апр. 2024 г., 17:13', '22 апр. 2024 г., 17:13', '22 апр. 2024 г., 17:12', '22 апр. 2024 г., 17:10', '22 апр. 2024 г., 17:10', '22 апр. 2024 г., 17:10', '22 апр. 2024 г., 17:10', '22 апр. 2024 г., 17:09', '22 апр. 2024 г., 17:09', '22 апр. 2024 г., 17:09', '22 апр. 2024 г., 17:09', '22 апр. 2024 г., 16:52'])

    @allure.title("Check text info-popover content")
    def check_text_info_popover_content(self, page, text):
        page.locator("(//td[contains(@class, 'styles_tableAmount')])[1]").hover()
        expect(page.locator("//*[@data-test-id = 'info-popover-content']")).to_have_text(text)

    @allure.title("Check text info-popover content decline")
    def check_text_info_popover_content_decline(self, page, text):
        page.locator("(//td[contains(@class, 'styles_tableAmount')])[1]").hover()
        page.locator('(//td//*[@data-test-id="floating-activator"])[3]').click()
        expect(page.locator("//*[@data-test-id = 'info-popover-content']")).to_have_text(text)

    @allure.title("Check all row transactions employee")
    def check_all_row_transactions_employee(self, page):
        expect(page.locator("//tr[contains(@class, 'hover-visible-container')]")).to_have_text(
            ['22 апр. 2024 г., 17:13FACEBK ADSPendinginvated emploee••6070 657671,00\xa0$', '22 апр. 2024 г., 17:13FACEBK ADSPendinginvated emploee••6070 657671,00\xa0$', '22 апр. 2024 г., 17:12FACEBK ADSPendinginvated emploee••6070 657671,00\xa0$', '22 апр. 2024 г., 17:10FACEBK ADSPendinginvated emploee••8002 6 apple1,00\xa0$', '22 апр. 2024 г., 17:10FACEBK ADSPendinginvated emploee••8002 6 apple1,00\xa0$', '22 апр. 2024 г., 17:10FACEBK ADSPendinginvated emploee••8002 6 apple1,00\xa0$', '22 апр. 2024 г., 17:10FACEBK ADSPendinginvated emploee••8002 6 apple1,00\xa0$', '22 апр. 2024 г., 17:09FACEBK ADSPendinginvated emploee••8002 6 apple1,00\xa0$', '22 апр. 2024 г., 17:09FACEBK ADSPendinginvated emploee••8002 6 apple1,00\xa0$', '22 апр. 2024 г., 17:09FACEBK ADSPendinginvated emploee••8002 6 apple1,00\xa0$', '22 апр. 2024 г., 17:09FACEBK ADSPendinginvated emploee••8002 6 apple1,00\xa0$', '22 апр. 2024 г., 16:52FACEBK ADSSettledinvated emploee••8002 6 apple2,00\xa0$'])

    @allure.title("Check some rows transactions")
    def check_some_rows_transactions(self, pages):
        pages.trans.first_row.check_text('18 апр. 2024 г., 10:19FACEBK ADSSettledtest do not change••3663 WEDSCXS15,00 $')
        pages.trans.five_row.check_text('18 апр. 2024 г., 10:18FACEBK ADSRefundtest do not change••9053 ASDCX1,00 $')
        pages.trans.eight_row.check_text('18 апр. 2024 г., 10:17FACEBK ADSPendingtest do not change••9053 ASDCX11,00\xa0$')
        pages.trans.seventeen_row.check_text('18 апр. 2024 г., 10:06FACEBK ADSReversedtest do not change••4518 HRTYU1,00\xa0$')
        pages.trans.twenty_two_row.check_text('18 апр. 2024 г., 10:01FACEBK ADSDeclinedtest do not change••1839 ASQWEDC0,50 $ + 1,00 $')
        pages.trans.twenty_one_row.check_text('18 апр. 2024 г., 10:03FACEBK ADSSettledtest do not change••1839 ASQWEDC0,50 $ + 13,00 $')
