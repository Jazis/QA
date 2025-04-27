from time import sleep

import allure
from playwright.sync_api import Page, expect

from api.function_api import api_request_context, \
    api_post, api_request
from data.input_data.banners import DISABLE_COMPANY_RU, ACCOUNT_OFF, ACCOUNT_OFF_EN, RESTRICT_COMPANY_EN, HIGH_DECLINE_RATE_EN, \
    HIGH_DECLINE_RATE_TEXT_EN, HIGH_DECLINE_RATE_UK, HIGH_DECLINE_RATE_TEXT_UK
from data.input_data.data_card import DECLINED, COUNTRY_US, CURRENCY_USD, COUNTRY_GB, CURRENCY_EUR, REVERSAL, REFUND, \
    DECLINED_PENDING, SETTLED, PENDING
from data.input_data.decline_reasons import APPROVED_SUCCES
from data.input_data.random_data import generate_random_float

from data.input_data.users import USER_RU, USER_DATA_RU, USER_WHITE_COMPANY, USER_DISABLED_COMPANY, USER_RESTRICTED_COMPANY, \
    USER_RESTRICTED_EMPLOYEE, USER_DISABLED_EMPLOYEE, USER_WHITE_COMPANY_EMPLOYEE, USER_RUBY_ROSE
from pages.pages import Pages
from steps import Steps
from test.test_api.conftest import MC
from test.test_transactions.conftest import CARD_LIFETIME
from utils.consts import AUTH_URL_ALL_TIME, AUTH_URL


class TestCash:

    @allure.title('Check calendar and cash page')
    def test_check_calendar_and_cash_page(self, page: Page, pages: Pages,
                                steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.cash_balance.calendar_for_schedule.check_text('Последние 30 дней')
        pages.cash_balance.calendar_for_schedule.click()
        expect(page.locator('//*[@data-index="1"]')).to_have_text('Последние 7 дней')
        expect(page.locator('//*[@data-index="2"]')).to_have_text('Текущая неделя')
        expect(page.locator('//*[@data-index="3"]')).to_have_text('Текущий месяц')
        expect(page.locator('//*[@data-index="4"]')).to_have_text('Текущий квартал')
        expect(page.locator('//*[@data-index="5"]')).to_have_text('Текущий год')
        expect(page.locator('//*[@data-index="6"]')).to_have_text('Все время')
        page.locator('//*[@data-index="6"]').click()
        expect(page.locator('//*[contains(@class, "styles_tableStub")]//*[@data-slot="icon"]')).to_be_visible()
        pages.cash_balance.calendar_for_schedule.check_text('Все время')
        expect(page.locator('h2')).to_have_text('Аккаунты')
        expect(page.locator('(//tr/th)[1]')).to_have_text('Аккаунт')
        expect(page.locator('(//tr/th)[2]')).to_have_text('Доступный баланс')

    @allure.title('Check page account')
    def test_check_page_account(self, page: Page, pages: Pages,
                                   steps: Steps, playwright, api_request_context):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        sleep(2)
        pages.cash_balance.table_balance.click()
        expect(page.locator('h1')).to_have_text('Основной •••8850')
        assert pages.cash_balance.button_back_to_cash.is_visible()
        expect(page.locator('(//*[@data-test-id="state-card"]/span)[1]')).to_have_text('Транзакции не найдены')
        expect(page.locator('(//*[@data-test-id="state-card"]/span)[2]')).to_have_text('Попробуйте изменить фильтр или поисковый запрос')
        expect(page.locator('(//span[contains(text(), "26 транзакции в обработке")]/ancestor::button/*[@data-slot="icon"])[1]')).to_be_visible()
        expect(page.locator('(//span[contains(text(), "26 транзакции в обработке")]/ancestor::button/*[@data-slot="icon"])[2]')).to_be_visible()
        expect(page.locator('(//*[contains(@class, "styles_tileContainer")])[2]//span[contains(text(), "Номер счета")]')).to_be_visible()
        expect(page.locator('(//*[contains(@class, "styles_tileContainer")])[2]//span[contains(text(), "•••8850")]')).to_be_visible()
        expect(page.locator('(//*[contains(@class, "styles_tileContainer")])[2]//span[contains(text(), "Текущая выписка")]')).to_be_visible()
        expect(page.locator('(//*[contains(@class, "styles_tileContainer")])[2]//span[contains(text(), "Скоро")]')).to_be_visible()
        expect(page.locator('(//*[contains(@class, "styles_tileContainer")])[2]//span[contains(text(), "Просмотреть все выписки")]')).to_be_visible()
        expect(page.locator('h2')).to_have_text('Обработанные транзакции')
        expect(page.locator('//*[@data-test-id="button"]//span[contains(text(), "Тип")]')).to_be_visible()
        expect(page.locator("//th//div[contains(@class, 'display_flex align-items_center gap_1')]")).to_have_text('Дата и время')
        expect(page.locator("//th[contains(@class, 'styles_tableTransaction')]")).to_have_text('Транзакция')
        expect(page.locator("//th[contains(@class, 'styles_tableAmount')]")).to_have_text('Сумма')
        pages.cash_balance.filter_type_ru.click()
        expect(page.locator("//span[contains(text(), 'Крипто депозит')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), 'Комиссия за депозит')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), 'Комиссия за депозит')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), 'Оплата по картам')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), 'Комиссия за деклайн')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), 'Возврат по картам')]")).to_be_visible()

    @allure.title('Check all balances')
    def test_check_all_balances(self, page: Page, pages: Pages,
                                steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password, "Счет")
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        sleep(2)
        assert pages.cash_balance.accessible_balance_ru.is_visible()
        assert pages.cash_balance.balance_hold_ru.is_visible()
        balance_hold = pages.cash_balance.balance_hold_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        expect(page.locator('(//td//div[@data-test-id="avatar"])[1]')).to_be_visible()
        expect(page.locator('(//*[contains(@class, "display_flex align-items_center gap_3")])[1]')).to_have_text(
            'Основной •••9366')
        assert pages.cash_balance.icon_go_to_account.is_visible()
        pages.cash_balance.table_balance.click()
        expect(page.locator('h1')).to_have_text('Основной •••9366')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        balance_total_popover = pages.cash_balance.total_popover.get_text()
        assert balance_navigation == accessible_balance
        assert accessible_balance == table_balance
        assert balance_hold == balance_hold_account
        assert total_balance == balance_total_popover
        assert accessible_balance_account == balance_navigation
        assert pages.cash_balance.row_slider.is_on_page()
        pages.cash_balance.total_popover_icon.click()
        balance_at_total_popover = pages.cash_balance.balance_in_total_popover_ru.get_text()
        assert balance_at_total_popover == total_balance

    @allure.title('Check pending transactions in modal')
    def test_check_pending_transactions_in_modal(self, page: Page, pages: Pages,
                                steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        sleep(2)
        page.locator('//*[@data-test-id="table-body"]').click()
        expect(page.locator('//h1')).to_have_text('Основной •••8850')
        expect(page.locator("//*[contains(text(), '26 транзакции в обработке')]")).to_be_visible()
        page.locator("//*[contains(text(), '26 транзакции в обработке')]").click()
        expect(page.locator('//*[@data-test-id="modal-dialog"]//h2')).to_have_text('Транзакции в холде')
        expect(page.locator('(//*[@data-test-id="modal-body"]//th)[1]')).to_have_text('Дата и время')
        expect(page.locator('(//*[@data-test-id="modal-body"]//th)[2]')).to_have_text('Транзакция')
        expect(page.locator('(//*[@data-test-id="modal-body"]//th)[3]')).to_have_text('Статус')
        expect(page.locator('(//*[@data-test-id="modal-body"]//th)[4]')).to_have_text('Пользователь')
        expect(page.locator('(//*[@data-test-id="modal-body"]//th)[5]')).to_have_text('Карта')
        expect(page.locator('(//*[@data-test-id="modal-body"]//th)[6]')).to_have_text('Затраты')
        expect(page.locator('(//*[@data-test-id="modal-body"]//th)[7]')).to_have_text('18 апр. 2024 г. – 22 апр. 2024 г.')
        expect(page.locator('(//*[@data-test-id="modal-body"]//th)[9]')).to_have_text('101,00 $')
        page.locator('(//*[@data-test-id="modal-body"]//*[@data-test-id="info-popover-activator"]//*[@data-test-id="floating-activator"])[1]').hover()
        expect(page.locator('(//*[@data-test-id="info-popover-content"])[1]')).to_have_text('Pending101,00 $')
        page.locator("(//*[@data-test-id='modal-body']//tr[contains(@class, 'hover-visible-container')])[1]").hover()
        page.locator("(//*[@data-test-id='modal-body']//*[@data-test-id='date-popover']//*[@data-test-id='floating-activator'])[1]").hover()
        expect(page.locator('//*[@data-test-id="tooltip-content"]')).to_have_text("22 апр. 2024 г., 14:13 (UTC+00:00)")
        page.locator("(//*[@data-test-id='modal-body']//tr[contains(@class, 'hover-visible-container')])[1]").hover()
        page.locator('(//*[@data-test-id="modal-body"]//div[@data-test-id="floating-activator"])[5]').click()
        expect(page.locator('//*[@data-test-id="modal-body"]//div[@data-test-id="info-popover-content"]')).to_have_text('Оплата1,00 $')
        expect(page.locator('//*[@data-test-id="modal-body"]//div[@data-test-id="table-pagination"]')).to_have_text('1-10 из 26 транзакций')
        expect(page.locator('(//*[@data-test-id="modal-body"]//tr)[3]')).to_have_text('22 апр. 2024 г., 17:13FACEBK ADSPendinginvated emploee••6070 65767Оплата1,00 $1,00 $')
        page.locator('(//*[@data-test-id="modal-body"]//button[@data-test-id="button"])[2]').click()
        expect(page.locator('(//*[@data-test-id="modal-body"]//tr)[3]')).to_have_text('22 апр. 2024 г., 17:09FACEBK ADSPendinginvated emploee••8002 6 apple1,00 $')
        pages.cash_balance.button_close_modal_pending.click()
        assert pages.cash_balance.button_close_modal_pending.is_not_on_page()

    @allure.title('Check new pending transaction in modal')
    def test_check_new_pending_transaction_in_modal(self, page: Page, pages: Pages,
                                   steps: Steps, playwright, api_request_context):
        s = generate_random_float()
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RUBY_ROSE.login, USER_RUBY_ROSE.password, "Счет")
        sleep(2)
        page.locator('//*[@data-test-id="table-body"]').click()
        expect(page.locator('//h1')).to_have_text('Основной •••9366')
        row_pending = pages.cash_balance.row_pending_transactions.get_text()
        pages.cash_balance.row_pending_transactions.click()
        total_sum = pages.cash_balance.total_sum_at_pending_trans_modal.get_text()
        date_transaction = pages.cash_balance.date_first_pending_at_modal.get_text()
        sum_pending = pages.cash_balance.sum_first_pending_at_modal.get_text()
        pages.cash_balance.button_close_modal_pending.click()
        api_post(api_request_context, s, CARD_LIFETIME, PENDING, COUNTRY_US, CURRENCY_USD)
        page.reload()
        sleep(2)
        pages.cash_balance.row_pending_transactions.click()
        row_pending_after = pages.cash_balance.row_pending_transactions.get_text()
        sleep(1)
        total_sum_after = pages.cash_balance.total_sum_at_pending_trans_modal.get_text()
        date_transaction_after = pages.cash_balance.date_first_pending_at_modal.get_text()
        sum_pending_after = pages.cash_balance.sum_first_pending_at_modal.get_text()
        assert row_pending < row_pending_after
        assert total_sum < total_sum_after
        assert date_transaction < date_transaction_after
        assert sum_pending != sum_pending_after

    @allure.title('Check total popover all time')
    def test_check_total_popover_all_time(self, page: Page, pages: Pages, steps: Steps, playwright, api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        sleep(2)
        pages.cash_balance.table_balance.click()
        expect(page.locator('h1')).to_have_text('Основной •••8850')
        pages.cash_balance.total_popover_icon.click()
        pages.cash_balance.beg_balance_popover_ru.check_text('0,00 $')
        pages.cash_balance.crypto_deposit_ru.check_text('1 270,00 $')
        pages.cash_balance.money_in_popover_ru.check_text('1 317,64 $')
        pages.cash_balance.money_out_popover_ru.check_text('-211,49 $')
        pages.cash_balance.crypto_fee_ru.check_text('-2,30 $')
        pages.cash_balance.card_spend_ru.check_text('-205,00 $')
        pages.cash_balance.settled_fee_ru.check_text('-1,09 $')
        pages.cash_balance.cross_border_fee_settled_ru.check_text('-2,10 $')
        pages.cash_balance.decline_fee_ru.check_text('-1,00 $')
        pages.cash_balance.refund_ru.check_text('47,00 $')
        pages.cash_balance.refund_fee_ru.check_text('0,64 $')
        pages.cash_balance.end_balance_ru.check_text('1 106,15 $')
        pages.cash_balance.total_popover.check_text('1 106,15 $')

    @allure.title('Check total popover two days')
    def test_check_total_popover_two_days(self, page: Page, pages: Pages, steps: Steps, playwright, api_request_context):
        page.goto("https://dev.app.devhost.io/cash/account?dateRange=2024-04-29_2024-04-30&id=138&page=1")
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Основной •••8850')
        pages.cash_balance.total_popover_icon.click()
        pages.cash_balance.beg_balance_popover_ru.check_text('0,00 $')
        pages.cash_balance.crypto_deposit_ru.check_text('270,00 $')
        pages.cash_balance.crypto_fee_ru.check_text('-2,30 $')
        pages.cash_balance.end_balance_ru.check_text('267,70 $')
        pages.cash_balance.money_out_popover_ru.check_text('-2,30 $')
        pages.cash_balance.money_in_popover_ru.check_text('270,00 $')
        pages.cash_balance.total_popover.check_text('267,70 $')

    @allure.title('Check total popover with filter crypto')
    def test_check_total_popover_with_filter_crypto(self, page: Page, pages: Pages, steps: Steps, playwright, api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        sleep(2)
        pages.cash_balance.table_balance.click()
        expect(page.locator('h1')).to_have_text('Основной •••8850')
        pages.cash_balance.total_popover_icon.click()
        pages.cash_balance.filter_type_ru.click()
        pages.cash_balance.filter_deposit_ru.click()
        pages.cash_balance.filter_type_ru.click()
        pages.trans.selected_filters.check_text('Крипто депозит')
        pages.cash_balance.total_popover_icon.click()
        assert pages.cash_balance.beg_balance_popover_ru.is_not_on_page()
        assert pages.cash_balance.end_balance_ru.is_not_on_page()
        pages.cash_balance.crypto_deposit_ru.check_text('1 270,00 $')
        pages.cash_balance.money_in_popover_ru.check_text('1 270,00 $')
        pages.cash_balance.total_popover.check_text('1 270,00 $')

    @allure.title('Check total popover with filters card spend')
    def test_check_total_popover_with_filters_card_spend(self, page: Page, pages: Pages, steps: Steps, playwright,
                                                    api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        sleep(2)
        pages.cash_balance.table_balance.click()
        expect(page.locator('h1')).to_have_text('Основной •••8850')
        pages.cash_balance.filter_type_ru.click()
        pages.cash_balance.filter_card_settled_ru.click()
        pages.cash_balance.filter_card_declined_ru.click()
        pages.cash_balance.filter_card_refund_ru.click()
        pages.cash_balance.filter_type_ru.click()
        pages.trans.selected_filters.check_text('Оплата по картам, Комиссия за деклайн, Возврат по картам')
        pages.cash_balance.total_popover_icon.click()
        assert pages.cash_balance.beg_balance_popover_ru.is_not_on_page()
        assert pages.cash_balance.end_balance_ru.is_not_on_page()
        pages.cash_balance.card_spend_ru.check_text('-205,00 $')
        pages.cash_balance.settled_fee_ru.check_text('-1,09 $')
        pages.cash_balance.cross_border_fee_settled_ru.check_text('-2,10 $')
        pages.cash_balance.decline_fee_ru.check_text('-1,00 $')
        pages.cash_balance.refund_ru.check_text('47,00 $')
        pages.cash_balance.refund_fee_ru.check_text('0,64 $')
        pages.cash_balance.total_popover.check_text('-161,55 $')
        pages.cash_balance.money_in_popover_ru.check_text('47,64 $')
        pages.cash_balance.money_out_popover_ru.check_text('-209,19 $')

    @allure.title('Check table with filters card spend')
    def test_check_table_with_filters_card_spend(self, page: Page, pages: Pages, steps: Steps, playwright, api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        sleep(2)
        pages.cash_balance.table_balance.click()
        expect(page.locator('h1')).to_have_text('Основной •••8850')
        pages.cash_balance.filter_type_ru.click()
        pages.cash_balance.filter_card_settled_ru.click()
        pages.cash_balance.filter_card_declined_ru.click()
        pages.cash_balance.filter_card_refund_ru.click()
        pages.cash_balance.filter_type_ru.click()
        pages.trans.selected_filters.check_text('Оплата по картам, Комиссия за деклайн, Возврат по картам')
        pages.team.table_pagination.check_text('4 транзакции')
        expect(page.locator("(//td[contains(@class, 'styles_tableDate')])[1]")).to_have_text('22 апр. 2024 г.')
        expect(page.locator("(//td[contains(@class, 'styles_tableDate')])[2]")).to_have_text('18 апр. 2024 г.')
        expect(page.locator("(//td[contains(@class, 'styles_tableDate')])[3]")).to_have_text('18 апр. 2024 г.')
        expect(page.locator("(//td[contains(@class, 'styles_tableDate')])[4]")).to_have_text('18 апр. 2024 г.')

        expect(page.locator("(//*[contains(@class, 'gap_2 min-width_0')])[1]")).to_have_text('Оплата по картам1')
        expect(page.locator("(//*[contains(@class, 'gap_2 min-width_0')])[2]")).to_have_text('Оплата по картам16')
        expect(page.locator("(//*[contains(@class, 'gap_2 min-width_0')])[3]")).to_have_text('Возврат по картам8')
        expect(page.locator("(//*[contains(@class, 'gap_2 min-width_0')])[4]")).to_have_text('Комиссия за деклайн2')

        expect(page.locator("(//td[contains(@class, 'styles_tableAmount')])[1]")).to_have_text('-2,00 $')
        expect(page.locator("(//td[contains(@class, 'styles_tableAmount')])[2]")).to_have_text('-206,19 $')
        expect(page.locator("(//td[contains(@class, 'styles_tableAmount')])[3]")).to_have_text('47,64 $')
        expect(page.locator("(//td[contains(@class, 'styles_tableAmount')])[4]")).to_have_text('-1,00 $')

    @allure.title('Check modal card spend')
    def test_check_modal_card_spend(self, page: Page, pages: Pages, steps: Steps, playwright, api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        sleep(2)
        pages.cash_balance.table_balance.click()
        expect(page.locator('h1')).to_have_text('Основной •••8850')
        page.locator("(//*[contains(text(), 'Оплата по картам')])[2]").click()
        expect(page.locator('(//h2)[2]')).to_have_text('Завершенные транзакции')
        expect(page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Дата и время")]')).to_be_visible()
        expect(page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Затраты")]')).to_be_visible()
        steps.universalSteps.check_titles_at_table(page, 10, 'Транзакция')
        steps.universalSteps.check_titles_at_table(page, 11, 'Статус')
        steps.universalSteps.check_titles_at_table(page, 12, 'Обработано')
        steps.universalSteps.check_titles_at_table(page, 13, 'Пользователь')
        steps.universalSteps.check_titles_at_table(page, 14, 'Карта')
        expect(page.locator('(//*[@role="dialog"]//*[@data-test-id="info-popover-activator"]//span/span)[1]')).to_have_text('206,19 $')
        expect(page.get_by_text('1-10 из 16 транзакций')).to_be_visible()
        sleep(1)
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//div[contains(text(), '18 апр. 2024 г., 10:04')])[1]")).to_be_visible()
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//div[contains(text(), '18 апр. 2024 г., 10:04')])[2]")).to_be_visible()
        expect(page.locator("(//*[contains(@class, 'display_flex align-items_center gap_md_3')]//*[@title='FACEBK ADS'])[1]")).to_be_visible()
        pages.cash_balance.status_at_modal.check_text('Settled')
        pages.cash_balance.user_at_modal.check_text('test do not change')
        pages.cash_balance.card_at_modal.check_text("••4039 dfd vcvcvcbcv")
        expect(page.locator('(//*[@role="dialog"]//*[@data-test-id="info-popover-activator"]//span/span)[2]')).to_have_text('19,19 $')
        expect(page.locator('(//*[@role="dialog"]//*[@data-test-id="info-popover-activator"]//span/span)[1]')).to_have_text('206,19 $')
        pages.cash_balance.total_popover_icon_modal.click()
        pages.cash_balance.settled_fee_ru.check_text('1,09 $')
        pages.cash_balance.cross_border_fee_settled_ru.check_text('2,10 $')
        pages.cash_balance.card_spend_en.check_text('203,00 $')
        page.locator('(//button[@data-test-id="button"])[5]').click()
        expect(page.get_by_text('11-16 из 16 транзакций')).to_be_visible()

    @allure.title('Check popovers card spend')
    def test_check_popovers_card_spend(self, page: Page, pages: Pages, steps: Steps, playwright, api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        sleep(2)
        pages.cash_balance.table_balance.click()
        expect(page.locator('h1')).to_have_text('Основной •••8850')
        expect(page.locator("(//td[contains(@class, 'styles_tableAmount')])[12]")).to_have_text('-206,19 $')
        page.locator("(//td[contains(@class, 'styles_tableAmount')])[12]").hover()
        page.locator('(//*[@data-test-id="info-popover-activator"])[3]/div/div').click()
        steps.cashSteps.check_row_at_popover(page, 1, 'Оплата')
        steps.cashSteps.check_row_at_popover(page, 2, '-203,00 $')
        steps.cashSteps.check_row_at_popover(page, 3, 'Междунар. комиссия')
        steps.cashSteps.check_row_at_popover(page, 4, '-2,10 $')
        steps.cashSteps.check_row_at_popover(page, 5, 'Конвертация')
        steps.cashSteps.check_row_at_popover(page, 6, '-1,09 $')
        page.locator("(//*[contains(text(), 'Оплата по картам')])[2]").click()
        expect(page.locator('(//*[@role="dialog"]//*[@data-test-id="info-popover-activator"]//span)[1]')).to_have_text('206,19 $')
        pages.cash_balance.popover_at_modal.click()
        steps.cashSteps.check_row_at_popover(page, 1, 'Settled')
        steps.cashSteps.check_row_at_popover(page, 2, '203,00 $')
        steps.cashSteps.check_row_at_popover(page, 3, 'Междунар. комиссия')
        steps.cashSteps.check_row_at_popover(page, 4, '2,10 $')
        steps.cashSteps.check_row_at_popover(page, 5, 'Конвертация')
        steps.cashSteps.check_row_at_popover(page, 6, '1,09 $')
        page.locator("(//*[@role='dialog']//td[contains(@class, 'styles_tableAmount')])[3]").hover()
        page.locator('(//*[@role="dialog"]//*[@data-test-id="info-popover-activator"]/div/div)[4]').click()
        steps.cashSteps.check_row_at_popover(page, 1, 'Оплата')
        steps.cashSteps.check_row_at_popover(page, 2, '15,00 $')
        steps.cashSteps.check_row_at_popover(page, 3, 'Конвертация')
        steps.cashSteps.check_row_at_popover(page, 4, '0,15 $')

    @allure.title('Check modal card refund')
    def test_check_modal_card_refund(self, page: Page, pages: Pages, steps: Steps, playwright, api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        sleep(2)
        pages.cash_balance.table_balance.click()
        expect(page.locator('h1')).to_have_text('Основной •••8850')
        page.locator("//*[contains(text(), 'Возврат по картам')]").click()
        expect(page.locator('(//h2)[2]')).to_have_text('Возвраты')
        expect(page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Дата и время")]')).to_be_visible()
        expect(page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Затраты")]')).to_be_visible()
        steps.universalSteps.check_titles_at_table(page, 10, 'Транзакция')
        steps.universalSteps.check_titles_at_table(page, 11, 'Статус')
        steps.universalSteps.check_titles_at_table(page, 12, 'Обработано')
        steps.universalSteps.check_titles_at_table(page, 13, 'Пользователь')
        steps.universalSteps.check_titles_at_table(page, 14, 'Карта')
        expect(page.locator('(//*[@role="dialog"]//*[@data-test-id="info-popover-activator"]//span/span)[1]')).to_have_text('47,64 $')
        expect(page.get_by_text('8 транзакций')).to_be_visible()
        expect(page.locator(
            "(//tr[contains(@class, 'hover-visible-container')]//div[contains(text(), '18 апр. 2024 г., 10:22')])[1]")).to_be_visible()
        expect(page.locator(
            "(//tr[contains(@class, 'hover-visible-container')]//div[contains(text(), '18 апр. 2024 г., 10:22')])[2]")).to_be_visible()
        expect(page.locator(
            "(//*[contains(@class, 'display_flex align-items_center gap_md_3')]//*[@title='FACEBK ADS'])[1]")).to_be_visible()
        pages.cash_balance.status_at_modal.check_text('Refund')
        pages.cash_balance.user_at_modal.check_text('test do not change')
        pages.cash_balance.card_at_modal.check_text("••3663 WEDSCXS")
        expect(page.locator(
            '(//*[@role="dialog"]//*[@data-test-id="info-popover-activator"]//span/span)[2]')).to_have_text('14,64 $')

    @allure.title('Check popovers card refund')
    def test_check_popovers_card_refund(self, page: Page, pages: Pages, steps: Steps, playwright, api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        sleep(2)
        pages.cash_balance.table_balance.click()
        expect(page.locator('h1')).to_have_text('Основной •••8850')
        expect(page.locator("(//td[contains(@class, 'styles_tableAmount')])[13]")).to_have_text('47,64 $')
        page.locator("(//td[contains(@class, 'styles_tableAmount')])[14]").hover()
        page.locator('(//*[@data-test-id="info-popover-activator"])[4]/div/div').click()
        steps.cashSteps.check_row_at_popover(page, 1, 'Оплата')
        steps.cashSteps.check_row_at_popover(page, 2, '47,00 $')
        steps.cashSteps.check_row_at_popover(page, 3, 'Междунар. комиссия')
        steps.cashSteps.check_row_at_popover(page, 4, '0,64 $')
        page.locator("//*[contains(text(), 'Возврат по картам')]").click()
        expect(page.locator('(//*[@role="dialog"]//*[@data-test-id="info-popover-activator"]//span)[1]')).to_have_text(
            '47,64 $')
        pages.cash_balance.popover_at_modal.click()
        steps.cashSteps.check_row_at_popover(page, 1, 'Refund')
        steps.cashSteps.check_row_at_popover(page, 2, '47,00 $')
        steps.cashSteps.check_row_at_popover(page, 3, 'Междунар. комиссия')
        steps.cashSteps.check_row_at_popover(page, 4, '0,64 $')
        pages.cash_balance.popover_at_modal.click()
        pages.cash_balance.amount_at_modal.check_text('14,64 $')
        pages.cash_balance.amount_at_modal.hover()
        page.locator('(//*[@role="dialog"]//*[@data-test-id="info-popover-activator"]/div/div)[2]').click()
        steps.cashSteps.check_row_at_popover(page, 1, 'Оплата')
        steps.cashSteps.check_row_at_popover(page, 2, '14,00 $')
        steps.cashSteps.check_row_at_popover(page, 3, 'Междунар. комиссия')
        steps.cashSteps.check_row_at_popover(page, 4, '0,64 $')

    @allure.title('Check modal card decline')
    def test_check_modal_card_decline(self, page: Page, pages: Pages, steps: Steps, playwright, api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        sleep(2)
        pages.cash_balance.table_balance.click()
        expect(page.locator('h1')).to_have_text('Основной •••8850')
        page.locator("//*[contains(text(), 'Комиссия за деклайн')]").click()
        expect(page.locator('(//h2)[2]')).to_have_text('Отклоненные транзакции')
        expect(page.locator(
            '//*[@data-test-id="sortable-heading"]//span[contains(text(), "Дата и время")]')).to_be_visible()
        expect(page.locator('//*[@data-test-id="sortable-heading"]//span[contains(text(), "Затраты")]')).to_be_visible()
        steps.universalSteps.check_titles_at_table(page, 10, 'Транзакция')
        steps.universalSteps.check_titles_at_table(page, 11, 'Статус')
        steps.universalSteps.check_titles_at_table(page, 12, 'Пользователь')
        steps.universalSteps.check_titles_at_table(page, 13, 'Карта')
        expect(page.locator(
            "(//tr[contains(@class, 'hover-visible-container')]//div[contains(text(), '18 апр. 2024 г., 10:01')])[1]")).to_be_visible()
        expect(page.locator(
            "(//*[contains(@class, 'display_flex align-items_center gap_md_3')]//*[@title='FACEBK ADS'])[1]")).to_be_visible()
        pages.cash_balance.status_at_modal.check_text('Declined')
        pages.cash_balance.status_at_modal.hover()
        expect(page.locator('//*[@data-test-id="tooltip-content"]')).to_have_text('The transaction was declined for an unknown reason.')
        pages.cash_balance.user_at_modal.check_text('test do not change')
        pages.cash_balance.card_at_modal.check_text("••1839 ASQWEDC")
        expect(page.locator(
            '(//*[@role="dialog"]//*[@data-test-id="info-popover-activator"]//span/span)[2]/ancestor::span')).to_have_text('0,50 $ + 1,00 $')
        expect(page.get_by_text('2 транзакции')).to_be_visible()

    @allure.title('Check popovers card decline')
    def test_check_popovers_card_decline(self, page: Page, pages: Pages, steps: Steps, playwright, api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        sleep(2)
        pages.cash_balance.table_balance.click()
        expect(page.locator('h1')).to_have_text('Основной •••8850')
        expect(page.locator("(//td[contains(@class, 'styles_tableAmount')])[14]")).to_have_text('-1,00 $')
        page.locator("(//td[contains(@class, 'styles_tableAmount')])[15]").hover()
        page.locator('(//*[@data-test-id="info-popover-activator"])[5]/div/div').click()
        steps.cashSteps.check_row_at_popover(page, 1, 'Оплата')
        steps.cashSteps.check_row_at_popover(page, 2, '-1,00 $')
        page.locator("//*[contains(text(), 'Комиссия за деклайн')]").click()
        expect(page.locator('(//*[@role="dialog"]//*[@data-test-id="info-popover-activator"]//span)[1]')).to_have_text(
            '1,00 $')
        pages.cash_balance.popover_at_modal.click()
        steps.cashSteps.check_row_at_popover(page, 1, 'Комиссия за деклайн')
        steps.cashSteps.check_row_at_popover(page, 2, '1,00 $')
        pages.cash_balance.popover_at_modal.click()
        pages.cash_balance.amount_at_modal.check_text('0,50 $ + 1,00 $')
        pages.cash_balance.amount_at_modal.hover()
        page.locator('(//*[@role="dialog"]//*[@data-test-id="info-popover-activator"]/div/div)[2]').click()
        steps.cashSteps.check_row_at_popover(page, 1, 'Оплата')
        steps.cashSteps.check_row_at_popover(page, 2, '1,00 $')
        steps.cashSteps.check_row_at_popover(page, 3, 'Комиссия за деклайн')
        steps.cashSteps.check_row_at_popover(page, 4, '0,50 $')

    @allure.title('Check table with filters crypto')
    def test_check_table_with_filters_crypto(self, page: Page, pages: Pages, steps: Steps, playwright, api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        sleep(2)
        pages.cash_balance.table_balance.click()
        expect(page.locator('h1')).to_have_text('Основной •••8850')
        pages.cash_balance.filter_type_ru.click()
        pages.cash_balance.filter_deposit_ru.click()
        pages.cash_balance.filter_deposit_fee_ru.click()
        pages.team.table_pagination.check_text('11 транзакций')
        expect(page.locator("(//td[contains(@class, 'styles_tableDate')])[1]")).to_have_text('30 апр. 2024 г., 07:10')
        expect(page.locator("(//td[contains(@class, 'styles_tableDate')])[2]")).to_have_text('30 апр. 2024 г., 07:10')
        expect(page.locator("(//td[contains(@class, 'styles_tableDate')])[3]")).to_have_text('30 апр. 2024 г., 07:09')
        expect(page.locator("(//td[contains(@class, 'styles_tableDate')])[4]")).to_have_text('30 апр. 2024 г., 07:06')

        expect(page.locator("(//*[contains(@class, 'gap_2 min-width_0')])[1]")).to_have_text('Комиссия за депозит')
        expect(page.locator("(//*[contains(@class, 'gap_2 min-width_0')])[2]")).to_have_text('Крипто депозит')

        expect(page.locator("(//td[contains(@class, 'styles_tableAmount')])[2]")).to_have_text('40,00 $')
        expect(page.locator("(//td[contains(@class, 'styles_tableAmount')])[1]")).to_have_text('-0,80 $')

    @allure.title('Check balance after pending transaction')
    def test_check_balance_pending(self, page: Page, pages: Pages, steps: Steps, playwright, api_request_context):
        ser = 50
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        sleep(1)
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_post(api_request_context, ser, MC, PENDING, COUNTRY_US, CURRENCY_USD)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation > balance_navigation_after
        assert accessible_balance > accessible_balance_after
        assert hold < hold_after
        assert table_balance > table_balance_after

        assert total_balance == total_balance_after
        assert accessible_balance_account > accessible_balance_account_after
        assert balance_hold_account < balance_hold_account_after

    @allure.title('Check balance after pending transaction with Fx + Cross-border fee')
    def test_check_balance_pending_fees(self, page: Page, pages: Pages,
                                   steps: Steps, playwright, api_request_context):
        ser = 5
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        sleep(1)
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_post(api_request_context, ser, MC, PENDING, COUNTRY_GB, CURRENCY_EUR)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation > balance_navigation_after
        assert accessible_balance > accessible_balance_after
        assert hold < hold_after
        assert table_balance > table_balance_after

        assert total_balance == total_balance_after
        assert accessible_balance_account > accessible_balance_account_after
        assert balance_hold_account < balance_hold_account_after

    @allure.title('Check balance after pending transaction with Cross-border fee')
    def test_check_balance_pending_fee_cross(self, page: Page, pages: Pages,
                                    steps: Steps, playwright, api_request_context):
        ser = 9
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")

        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_post(api_request_context, ser, MC, PENDING, COUNTRY_GB, CURRENCY_USD)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation > balance_navigation_after
        assert accessible_balance > accessible_balance_after
        assert hold < hold_after
        assert table_balance > table_balance_after

        assert total_balance == total_balance_after
        assert accessible_balance_account > accessible_balance_account_after
        assert balance_hold_account < balance_hold_account_after

    @allure.title('Check balance after pending transaction with Fx fee')
    def test_check_balance_pending_fx_fee(self, page: Page, pages: Pages,
                                    steps: Steps, playwright, api_request_context):
        ser = 11
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")

        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_post(api_request_context, ser, MC, PENDING, COUNTRY_US, CURRENCY_EUR)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation > balance_navigation_after
        assert accessible_balance > accessible_balance_after
        assert hold < hold_after
        assert table_balance > table_balance_after

        assert total_balance == total_balance_after
        assert accessible_balance_account > accessible_balance_account_after
        assert balance_hold_account < balance_hold_account_after

    @allure.title('Check balance after settled transaction')
    def test_check_balance_settled(self, page: Page, pages: Pages,
                               steps: Steps, playwright, api_request_context):
        ser = 30
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        sleep(1)
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_post(api_request_context, ser, MC, SETTLED, COUNTRY_US, CURRENCY_USD)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation > balance_navigation_after
        assert accessible_balance > accessible_balance_after
        assert hold == hold_after
        assert table_balance > table_balance_after

        assert total_balance > total_balance_after
        assert accessible_balance_account > accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after

    @allure.title('Check balance after settled transaction with Cross-border fee + Fx')
    def test_check_balance_settled_fees(self, page: Page, pages: Pages,
                                   steps: Steps, playwright, api_request_context):
        ser = 33
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")

        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.icon_go_to_account.click()
        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_post(api_request_context, ser, MC, SETTLED, COUNTRY_GB, CURRENCY_EUR)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation > balance_navigation_after
        assert accessible_balance > accessible_balance_after
        assert hold == hold_after
        assert table_balance > table_balance_after

        assert total_balance > total_balance_after
        assert accessible_balance_account > accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after

    @allure.title('Check balance after settled transaction with Cross-border fee')
    def test_check_balance_settled_cross_fee(self, page: Page, pages: Pages,
                                    steps: Steps, playwright, api_request_context):
        ser = 21
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")

        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_post(api_request_context, ser, MC, SETTLED, COUNTRY_GB, CURRENCY_USD)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation > balance_navigation_after
        assert accessible_balance > accessible_balance_after
        assert hold == hold_after
        assert table_balance > table_balance_after

        assert total_balance > total_balance_after
        assert accessible_balance_account > accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after

    @allure.title('Check balance after settled transaction with Fx fee')
    def test_check_balance_settled_fx_fee(self, page: Page, pages: Pages,
                                             steps: Steps, playwright, api_request_context):
        ser = 21
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")

        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_post(api_request_context, ser, MC, SETTLED, COUNTRY_US, CURRENCY_EUR)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation > balance_navigation_after
        assert accessible_balance > accessible_balance_after
        assert hold == hold_after
        assert table_balance > table_balance_after

        assert total_balance > total_balance_after
        assert accessible_balance_account > accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after

    @allure.title('Check balance after reversed transaction')
    def test_check_balance_reversed(self, page: Page, pages: Pages,
                                steps: Steps, playwright, api_request_context):
        ser = 1
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        sleep(1.5)
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_request(api_request_context, ser, MC, APPROVED_SUCCES, REVERSAL, COUNTRY_US, CURRENCY_USD)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation == balance_navigation_after
        assert accessible_balance == accessible_balance_after
        assert hold == hold_after
        assert table_balance == table_balance_after

        assert total_balance == total_balance_after
        assert accessible_balance_account == accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after

    @allure.title('Check balance after reversed transaction with Cross-border fee + Fx')
    def test_check_balance_reversed_fees(self, page: Page, pages: Pages,
                                    steps: Steps, playwright, api_request_context):
        ser = 11
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        sleep(1.5)
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_request(api_request_context, ser, MC, APPROVED_SUCCES, REVERSAL, COUNTRY_GB, CURRENCY_EUR)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation == balance_navigation_after
        assert accessible_balance == accessible_balance_after
        assert hold == hold_after
        assert table_balance == table_balance_after

        assert total_balance == total_balance_after
        assert accessible_balance_account == accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after

    @allure.title('Check balance after reversed transaction with Fx fee')
    def test_check_balance_reversed_fee_fx(self, page: Page, pages: Pages,
                                     steps: Steps, playwright, api_request_context):
        ser = 14
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        sleep(1.5)
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_request(api_request_context, ser, MC, APPROVED_SUCCES, REVERSAL, COUNTRY_US, CURRENCY_EUR)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation == balance_navigation_after
        assert accessible_balance == accessible_balance_after
        assert hold == hold_after
        assert table_balance == table_balance_after

        assert total_balance == total_balance_after
        assert accessible_balance_account == accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after

    @allure.title('Check balance after reversed transaction with Cross-border fee')
    def test_check_balance_reversed_cross_fee(self, page: Page, pages: Pages,
                                           steps: Steps, playwright, api_request_context):
        ser = 14
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        sleep(1.5)
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_request(api_request_context, ser, MC, APPROVED_SUCCES, REVERSAL, COUNTRY_GB, CURRENCY_USD)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation == balance_navigation_after
        assert accessible_balance == accessible_balance_after
        assert hold == hold_after
        assert table_balance == table_balance_after

        assert total_balance == total_balance_after
        assert accessible_balance_account == accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after

    @allure.title('Check balance after refund transaction')
    def test_check_balance_refund(self, page: Page, pages: Pages,
                              steps: Steps, playwright, api_request_context):
        ser = 15
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        sleep(1.5)
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_request(api_request_context, ser, MC, APPROVED_SUCCES, REFUND, COUNTRY_US, CURRENCY_USD)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation < balance_navigation_after
        assert accessible_balance < accessible_balance_after
        assert hold == hold_after
        assert table_balance < table_balance_after

        assert total_balance < total_balance_after
        assert accessible_balance_account < accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after

    @allure.title('Check balance after refund transaction with Cross-border fee + Fx')
    def test_check_balance_refund_fees(self, page: Page, pages: Pages,
                                  steps: Steps, playwright, api_request_context):
        ser = 29
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        sleep(1.5)
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_request(api_request_context, ser, MC, APPROVED_SUCCES, REFUND, COUNTRY_GB, CURRENCY_EUR)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation < balance_navigation_after
        assert accessible_balance < accessible_balance_after
        assert hold == hold_after
        assert table_balance < table_balance_after

        assert total_balance < total_balance_after
        assert accessible_balance_account < accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after

    @allure.title('Check balance after refund transaction with Fx fee')
    def test_check_balance_refund_fx_fee(self, page: Page, pages: Pages,
                                   steps: Steps, playwright, api_request_context):
        ser = 28
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        sleep(1.5)
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_post(api_request_context, ser, MC, REFUND, COUNTRY_US, CURRENCY_EUR)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation < balance_navigation_after
        assert accessible_balance < accessible_balance_after
        assert hold == hold_after
        assert table_balance < table_balance_after

        assert total_balance < total_balance_after
        assert accessible_balance_account < accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after

    @allure.title('Check balance after refund transaction with Cross-border fee')
    def test_check_balance_refund_cross_fee(self, page: Page, pages: Pages,
                                         steps: Steps, playwright, api_request_context):
        ser = 28
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        sleep(1.5)
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_post(api_request_context, ser, MC, REFUND, COUNTRY_GB, CURRENCY_USD)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation < balance_navigation_after
        assert accessible_balance < accessible_balance_after
        assert hold == hold_after
        assert table_balance < table_balance_after

        assert total_balance < total_balance_after
        assert accessible_balance_account < accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after

    @allure.title('Check balance after declined transaction')
    def test_check_balance_declined(self, page: Page, pages: Pages,
                                steps: Steps, playwright, api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        sleep(1.5)
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_post(api_request_context, 30, MC, DECLINED, COUNTRY_US, CURRENCY_USD)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation > balance_navigation_after
        assert accessible_balance > accessible_balance_after
        assert hold == hold_after
        assert table_balance > table_balance_after

        assert total_balance > total_balance_after
        assert accessible_balance_account > accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after

    @allure.title('Check balance after declined transaction with Cross-border fee + Fx')
    def test_check_balance_declined_fees(self, page: Page, pages: Pages,
                                    steps: Steps, playwright, api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        sleep(1.5)
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_post(api_request_context, 35, MC, DECLINED, COUNTRY_GB, CURRENCY_EUR)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation > balance_navigation_after
        assert accessible_balance > accessible_balance_after
        assert hold == hold_after
        assert table_balance > table_balance_after

        assert total_balance > total_balance_after
        assert accessible_balance_account > accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after

    @allure.title('Check balance after declined transaction with Cross-border fee')
    def test_check_balance_declined_cross_fee(self, page: Page, pages: Pages,
                                     steps: Steps, playwright, api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        sleep(1.5)
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_post(api_request_context, 10, MC, DECLINED, COUNTRY_GB, CURRENCY_USD)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation > balance_navigation_after
        assert accessible_balance > accessible_balance_after
        assert hold == hold_after
        assert table_balance > table_balance_after

        assert total_balance > total_balance_after
        assert accessible_balance_account > accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after

    @allure.title('Check balance after declined transaction with Fx fee')
    def test_check_balance_declined_fx_fee(self, page: Page, pages: Pages,
                                              steps: Steps, playwright, api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        sleep(1.5)
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_post(api_request_context, 30, MC, DECLINED, COUNTRY_US, CURRENCY_EUR)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation > balance_navigation_after
        assert accessible_balance > accessible_balance_after
        assert hold == hold_after
        assert table_balance > table_balance_after

        assert total_balance > total_balance_after
        assert accessible_balance_account > accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after

    @allure.title('Check balance after declined pending transaction')
    def test_check_balance_declined_pending(self, page: Page, pages: Pages,
                                        steps: Steps, playwright, api_request_context):
        ser = 6
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        sleep(1.5)
        balance_navigation = pages.navigation.cash_text_sum.get_text()
        accessible_balance = pages.cash_balance.accessible_balance_sum.get_text()
        hold = pages.cash_balance.balance_hold_sum.get_text()
        table_balance = pages.cash_balance.table_balance.get_text()
        pages.cash_balance.table_balance.click()

        expect(page.locator('h1')).to_have_text('Основной •••1481')
        total_balance = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account = pages.cash_balance.balance_hold_account.get_text()
        api_request(api_request_context, ser, MC, APPROVED_SUCCES, DECLINED_PENDING, COUNTRY_GB, CURRENCY_USD)
        page.reload()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        total_balance_after = pages.cash_balance.total_balance_ru.get_text()
        accessible_balance_account_after = pages.cash_balance.accessible_balance_account_ru.get_text()
        balance_hold_account_after = pages.cash_balance.balance_hold_account.get_text()

        pages.cash_balance.button_back_to_cash.click()
        sleep(2)
        table_balance_after = pages.cash_balance.table_balance.get_text()
        balance_navigation_after = pages.navigation.cash_text_sum.get_text()
        accessible_balance_after = pages.cash_balance.accessible_balance_sum.get_text()
        hold_after = pages.cash_balance.balance_hold_sum.get_text()

        assert balance_navigation == balance_navigation_after
        assert accessible_balance == accessible_balance_after
        assert hold == hold_after
        assert table_balance == table_balance_after

        assert total_balance == total_balance_after
        assert accessible_balance_account == accessible_balance_account_after
        assert balance_hold_account == balance_hold_account_after


@allure.title("Check banner for disabled company admin + employee")
def test_check_banner_disabled_company(page: Page, pages: Pages,
                                       steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME)
    steps.auth.authorize_in_test(page, USER_DISABLED_COMPANY.login, USER_DISABLED_COMPANY.password, "Счет")
    pages.cash_balance.alert_title.check_text(ACCOUNT_OFF)
    pages.cash_balance.alert_text.check_text(DISABLE_COMPANY_RU)
    pages.navigation.row_name.click()
    pages.navigation.log_out_ru.click()
    steps.auth.authorize_in_test(page, USER_DISABLED_EMPLOYEE.login, USER_DISABLED_EMPLOYEE.password, "Карты")
    pages.cash_balance.alert_title.check_text(ACCOUNT_OFF)
    pages.cash_balance.alert_text.check_text(DISABLE_COMPANY_RU)


@allure.title("Check banner for restricted company admin + employee")
def test_check_banner_restricted_company(page: Page, pages: Pages,
                                       steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME)
    steps.auth.authorize_in_test(page, USER_RESTRICTED_COMPANY.login, USER_RESTRICTED_COMPANY.password, "Cash")
    pages.cash_balance.alert_title.check_text("Your trial is over")
    pages.cash_balance.alert_text.check_text('Contact your manager to choose plan and continue')
    pages.cash_balance.alert_title_with_trial.check_text(ACCOUNT_OFF_EN)
    pages.cash_balance.alert_text_with_trial.check_text(RESTRICT_COMPANY_EN)
    pages.navigation.row_name.click()
    pages.navigation.log_out_en.click()
    steps.auth.authorize_in_test(page, USER_RESTRICTED_EMPLOYEE.login, USER_RESTRICTED_EMPLOYEE.password, "Cards")
    expect(page.locator("//span[contains(text(), 'Cards will be available after the first top-up')]")).to_be_visible()
    expect(page.get_by_text("You'll be able to create cards and see a list of them after the first deposit")).to_be_visible()
    pages.cash_balance.alert_title_with_trial.check_text(ACCOUNT_OFF_EN)
    pages.cash_balance.alert_text_with_trial.check_text(RESTRICT_COMPANY_EN)


@allure.title("Check banner decline rate company admin + employee")
def test_check_banner_decline_rate_company(page: Page, pages: Pages,
                                       steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME)
    steps.auth.authorize_in_test(page, USER_WHITE_COMPANY.login, USER_WHITE_COMPANY.password, "Счет")
    pages.cash_balance.alert_title.check_text(HIGH_DECLINE_RATE_EN)
    pages.cash_balance.alert_text.check_text(HIGH_DECLINE_RATE_TEXT_EN)
    pages.navigation.row_name.click()
    pages.navigation.log_out_ru.click()
    steps.auth.authorize_in_test(page, USER_WHITE_COMPANY_EMPLOYEE.login, USER_WHITE_COMPANY_EMPLOYEE.password, "Картки")
    pages.cash_balance.alert_title.check_text(HIGH_DECLINE_RATE_UK)
    pages.cash_balance.alert_text.check_text(HIGH_DECLINE_RATE_TEXT_UK)



