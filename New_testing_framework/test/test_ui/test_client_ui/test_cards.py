from time import sleep

import allure
import pytest

from playwright.sync_api import Page, expect
from api.function_api import api_request_context, api_request_with_available_balance
from api.function_api import api_set_limit
from data.input_data.data_card import BILLING_ADDRESS, SETTLED, COUNTRY_US, CURRENCY_USD
from data.input_data.decline_reasons import APPROVED_SUCCES
from data.input_data.random_data import random_string, random_numbers
from data.input_data.users import USER_RU, USER_DATA_RU, USER_DATA_RU_EMPLOYEE, USER_UK, USER_WHITE_COMPANY
from pages.pages import Pages
from steps import Steps
from utils.consts import AUTH_URL_ALL_TIME, AUTH_URL, AUTH_URL_ALL_TIME_EMPLOYEE


class TestCards:
    @allure.title("Check page of cards")
    def test_check_page_of_cards(self, page: Page, pages: Pages,
                                 steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        assert pages.cards.filter_name_card.is_visible()
        pages.cards.status_card_ru.is_on_page(timeout=3000)
        assert pages.cards.status_card_ru.is_visible()
        assert pages.cards.bin_card_filter.is_visible()
        assert pages.cards.user_card_filter.is_visible()
        pages.cards.calendar_button.is_on_page()
        assert pages.cards.create_card_ru.is_visible()
        assert pages.cards.title_table_card_ru.is_visible()
        assert pages.cards.title_table_limit_ru.is_visible()
        assert pages.cards.title_table_status_ru.is_visible()
        assert pages.cards.title_table_bin_ru.is_visible()
        assert pages.cards.title_table_user_ru.is_visible()
        assert pages.cards.title_table_money_ru.is_visible()
        pages.cards.popover_activator.check_text('262,55 $')
        pages.cards.popover_activator_icon.click()
        steps.cardsSteps.check_total_sum_spend(page)
        steps.cardsSteps.check_color_status_at_table(page)

    @allure.title("Check card's info popover")
    def test_check_cards_info_popover(self, page: Page, pages: Pages,
                                 steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        steps.cardsSteps.check_total_sum_of_one_card(page)

    @pytest.mark.skip("")
    @allure.title("Create card no limit")
    def test_create_card_no_limit(self, page: Page, pages: Pages,
                              steps: Steps, playwright):
        name_card = random_string(6)
        page.goto(AUTH_URL_ALL_TIME)
        pages.auth.login_input.is_on_page(timeout=2500)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.button_create_card_ru.click()
        pages.cards.name_create_card_ru.is_on_page(timeout=3000)
        pages.cards.name_create_card_ru.click()
        pages.cards.name_create_card_ru.fill(name_card)
        pages.cards.bin_default_create_card_ru.is_visible()
        steps.cardsSteps.check_default_limit_create_card_ru(page)
        pages.cards.card_limit_disabled.is_on_page()
        pages.cards.button_create_ru.click()
        sleep(3)
        assert pages.cards.modal_created_card_active_ru.is_on_page(timeout=3000)
        assert pages.cards.modal_card_no_limit_ru.is_on_page(timeout=2000)
        pages.cards.modal_created_card_real_name_ru.check_text(name_card)

    @pytest.mark.skip("")
    @allure.title("Create card another bin")
    def test_change_bin_create_card(self, page: Page, pages: Pages,
                                steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.button_create_card_ru.click()
        pages.cards.name_create_card_ru.is_on_page(timeout=3000)
        pages.cards.card_bin.click()
        pages.cards.card_bin_second.is_on_page(timeout=3000)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        pages.cards.button_create_ru.click()
        assert pages.cards.modal_created_card_name_ru.is_on_page(timeout=3000)
        assert pages.cards.modal_created_card_active_ru.is_visible()
        value = page.get_attribute("//img[contains(@class, 'styles_paymentSystemLogo')]", "src")
        assert value == '/images/payment-system/visa.svg'

    @pytest.mark.skip("")
    @allure.title("Create card with monthly limit")
    def test_create_card_monthly_limit(self, page: Page, pages: Pages,
                                   steps: Steps, playwright):
        n = random_numbers()
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.button_create_card_ru.click()
        pages.cards.name_create_card_ru.is_on_page()
        pages.cards.limit_card.is_on_page(timeout=3_000)
        pages.cards.limit_card.click()
        pages.cards.no_limit_card_limit.is_on_page(timeout=3_000)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        steps.cardsSteps.fill_limit_amount(n)
        pages.cards.button_create_ru.click()
        assert pages.cards.modal_created_card_name_ru.is_on_page()
        assert pages.cards.modal_created_card_active_ru.is_on_page()
        assert pages.cards.modal_card_month_limit_ru.is_on_page()
        steps.cardsSteps.check_limit_amount_on_card(n)

    @pytest.mark.skip("")
    @allure.title("Create card with lifetime limit")
    def test_cards_lifetime_limit(self, page: Page, pages: Pages,
                              steps: Steps, playwright):
        m = random_numbers()
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.button_create_card_ru.click()
        pages.cards.name_create_card_ru.is_on_page()
        pages.cards.limit_card.is_on_page(timeout=3_000)
        pages.cards.limit_card.click()
        pages.cards.no_limit_card_limit.is_on_page(timeout=3_000)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        steps.cardsSteps.fill_limit_amount(m)
        pages.cards.button_create_ru.click()
        assert pages.cards.modal_created_card_name_ru.is_on_page()
        assert pages.cards.modal_created_card_active_ru.is_on_page()
        assert pages.cards.modal_card_lifetime_limit_ru.is_on_page()
        steps.cardsSteps.check_limit_amount_on_card(m)

    @pytest.mark.skip("")
    @allure.title("Create card with day limit")
    def test_cards_day_limit(self, page: Page, pages: Pages,
                         steps: Steps, playwright):
        n = random_numbers()
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.button_create_card_ru.click()
        pages.cards.name_create_card_ru.is_on_page()
        pages.cards.limit_card.is_on_page(timeout=3_000)
        pages.cards.limit_card.click()
        sleep(2)
        pages.cards.no_limit_card_limit.is_on_page(timeout=3_000)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        steps.cardsSteps.fill_limit_amount(n)
        pages.cards.button_create_ru.click()
        sleep(2)
        assert pages.cards.modal_created_card_name_ru.is_on_page()
        assert pages.cards.modal_created_card_active_ru.is_on_page()
        assert pages.cards.modal_card_day_limit_ru.is_on_page()
        steps.cardsSteps.check_limit_amount_on_card(n)

    @pytest.mark.skip("")
    @allure.title("Create card with week limit")
    def test_create_card_week_limit(self, page: Page, pages: Pages,
                                steps: Steps, playwright):
        m = random_numbers()
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.button_create_card_ru.click()
        pages.cards.name_create_card_ru.is_on_page()
        pages.cards.limit_card.is_on_page(timeout=3_000)
        pages.cards.limit_card.click()
        pages.cards.no_limit_card_limit.is_on_page(timeout=3_000)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        steps.cardsSteps.fill_limit_amount(m)
        pages.cards.button_create_ru.click()
        sleep(2)
        assert pages.cards.modal_created_card_name_ru.is_on_page()
        assert pages.cards.modal_created_card_active_ru.is_on_page()
        assert pages.cards.modal_card_week_limit_ru.is_on_page()
        steps.cardsSteps.check_limit_amount_on_card(m)
        pages.cards.billing_address_title.check_text("Биллинг адрес")
        pages.cards.billing_address.check_text(BILLING_ADDRESS)

    @allure.title("Check copy card number")
    def test_check_card_number_copy(self, page: Page, pages: Pages,
                                steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU_EMPLOYEE.login, USER_DATA_RU_EMPLOYEE.password, "Карты")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        page.locator("//*[contains(text(),'••7485')]").click()
        value = page.get_attribute("//img[contains(@class, 'styles_paymentSystem')]", "src")
        assert value == '/images/payment-system/mastercard.svg'
        pages.cards.hidden_card_data.click()
        sleep(1)
        pages.cards.modal_card_number.click()
        pages.cards.toast_copy_number.check_text('Поле "Номер" скопировано')
        sleep(1)
        pages.cards.toast_close_button.click()
        pages.cards.modal_card_exp.click()
        expect(page.get_by_text('Поле "Годен до" скопировано')).to_be_visible()
        pages.cards.modal_card_cvc.click()
        expect(page.get_by_text('Поле "CVC" скопировано')).to_be_visible()

    @allure.title("Change name card")
    def test_change_name_card(self, page: Page, pages: Pages,
                          steps: Steps, playwright):
        new_name = random_string(7)
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.first_active_status_at_table.click()
        name_before = pages.cards.modal_created_card_real_name_ru.get_text()
        pages.cards.button_more_ru.click()
        pages.cards.button_change_name_ru.click()
        pages.cards.name_create_card_ru.fill(new_name)
        pages.cards.button_save_ru.click()
        pages.cards.close_modal_card.click()
        pages.cards.title_cash_after_login.is_not_on_page(timeout=3000)
        pages.cards.first_active_status_at_table.click()
        name_after = pages.cards.modal_created_card_real_name_ru.get_text()
        assert name_before != name_after
        assert name_after == new_name

    @allure.title("Change limit card with button more")
    def test_change_card_limit_with_button(self, page: Page, pages: Pages,
                                       steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.first_active_status_at_table.click()
        pages.cards.button_more_ru.click()
        pages.cards.change_card_limit_ru.click()
        pages.cards.modal_choose_limit.click()
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        pages.cards.input_limit_amount.fill(200)
        pages.cards.modal_save_limit_ru.click()
        pages.cards.close_modal_card.click()
        pages.cards.title_cash_after_login.is_not_on_page(timeout=3000)
        pages.cards.first_active_status_at_table.click()
        sleep(2.5)
        assert pages.cards.modal_card_lifetime_limit_ru.is_visible()
        pages.cards.modal_card_limit_amount_ru.check_text('200,00\xa0$')

    @allure.title("Change limit card with pencil")
    def test_change_limit_card_with_pencil(self, page: Page, pages: Pages,
                                       steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.first_active_status_at_table.click()
        pages.cards.modal_pencil_button.click()
        pages.cards.modal_choose_limit.click()
        page.keyboard.press("ArrowUp")
        page.keyboard.press("Enter")
        pages.cards.input_limit_amount.fill(100)
        pages.cards.modal_save_limit_ru.click()
        pages.cards.close_modal_card.click()
        pages.cards.title_cash_after_login.is_not_on_page(timeout=3000)
        pages.cards.first_active_status_at_table.click()
        pages.cards.modal_card_month_limit_ru.is_on_page(timeout=2000)
        expect(page.locator(
            "(//div[@data-test-id = 'modal-body']//span[contains(@class, 'styles_containerBodyMd')])[3]")).to_have_text(
                '100,00\xa0$')

    @pytest.mark.skip("")
    @allure.title("Close card")
    def test_close_card_button(self, page: Page, pages: Pages,
                           steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.spinner.is_on_page(timeout=3000)
        page.locator("(//td[contains(@class, 'styles_tableCard')])[1]").click()
        pages.cards.button_more_ru.wait_for()
        pages.cards.button_more_ru.click()
        pages.cards.close_card_button_ru.click()
        assert pages.cards.title_close_card_ru.is_on_page()
        assert pages.cards.logo_card_modal_close_card.is_on_page()
        pages.cards.modal_button_close_card_ru.click()
        pages.cards.close_modal_card.click()
        pages.cards.title_cash_after_login.is_not_on_page(timeout=3000)
        page.locator("(//td[contains(@class, 'styles_tableCard')])[1]").click()
        pages.cards.title_of_closed_card.check_text('Closed')

    @allure.title("Freeze card")
    def test_freeze_card(self, page: Page, pages: Pages,
                     steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        sleep(3)
        page.locator("(//td[contains(@class, 'styles_tableCard')])[3]").click()
        pages.cards.button_freeze_card.click()
        pages.cards.close_modal_card.click()
        expect(page.locator('(//*[@data-test-id="badge"])[3]')).to_have_text('Frozen')
        page.locator("(//td[contains(@class, 'styles_tableCard')])[3]").click()
        sleep(3)
        pages.cards.button_unfreeze_card.click()
        assert pages.cards.modal_created_card_active_ru.is_on_page()
        pages.cards.close_modal_card.click()
        expect(page.locator('(//*[@data-test-id="badge"])[3]')).to_have_text('Active')

    @allure.title("Go to transactions")
    def test_go_to_transactions(self, page: Page, pages: Pages,
                            steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.spinner.is_on_page(timeout=3000)
        page.locator("//td[contains(@class, 'styles_tableCard')]").nth(5).click()
        pages.cards.button_go_to_transactions.click()
        page.locator("//h1[contains(text(), 'Транзакции')]").wait_for(timeout=3000)
        pages.onboard.title_cash_after_login.check_text('Транзакции')

    @allure.title("Check quantity cards")
    def test_check_quantity_cards(self, page: Page, pages: Pages,
                              steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.title_my_cards_ru.click()
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        expect(page.locator("//td[contains(@class, 'styles_tableCard')]")).to_have_count(25)
        pages.cards.arrow_next_page_button.click()
        expect(page.locator("//td[contains(@class, 'styles_tableCard')]")).to_have_count(3)

    @allure.title("Check all names cards from My cards")
    def test_check_all_name_cards(self, page: Page, pages: Pages,
                              steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.title_my_cards_ru.click()
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        steps.cardsSteps.check_all_name_cards(page)
        pages.cards.arrow_next_page_button.click()
        steps.cardsSteps.check_all_name_cards_next_page(page)

    @allure.title("Check all statuses cards from My cards")
    def test_check_all_status_cards(self, page: Page, pages: Pages,
                                steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.title_my_cards_ru.click()
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        steps.cardsSteps.check_all_status_cards(page)
        pages.cards.arrow_next_page_button.click()
        steps.cardsSteps.check_all_status_cards_next_page(page)

    @allure.title("Check bin all cards from My cards")
    def test_check_bin_all_cards(self, page: Page, pages: Pages,
                             steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.title_my_cards_ru.click()
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        steps.cardsSteps.check_bin_all_cards(page)
        pages.cards.arrow_next_page_button.click()
        steps.cardsSteps.check_bin_all_cards_next_page(page)

    @allure.title("Check limit all my cards from My cards")
    def test_check_limit_all_my_cards(self, page: Page, pages: Pages,
                                  steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.title_my_cards_ru.click()
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        steps.cardsSteps.check_limit_all_cards(page)
        pages.cards.arrow_next_page_button.click()
        steps.cardsSteps.check_limit_all_cards_next_page(page)

    @allure.title("Check user name all cards")
    def test_check_user_name_all_cards(self, page: Page, pages: Pages,
                                   steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        steps.cardsSteps.check_check_user_name_all_cards(page)
        pages.cards.arrow_next_page_button.click()
        steps.cardsSteps.check_check_user_name_all_cards_next_page(page)

    @allure.title("Check spend all cards")
    def test_check_spend_all_cards(self, page: Page, pages: Pages,
                               steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.title_my_cards_ru.click()
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        steps.cardsSteps.check_check_spend_all_cards(page)
        pages.cards.arrow_next_page_button.click()
        steps.cardsSteps.check_check_spend_all_cards_next_page(page)

    @allure.title("Check row active card from My cards")
    def test_check_row_active_card(self, page: Page, pages: Pages,
                               steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.title_my_cards_ru.click()
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        expect(page.locator(
            "//*[contains(@class, 'hover-visible-container')]").filter(has_text='••6980 test')).to_have_text(
            "••6980 testActive553437Без лимита∞12,50 $")

    @allure.title("Check number card mc")
    def test_check_number_card_mc(self, page: Page, pages: Pages,
                              steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.title_my_cards_ru.click()
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        page.locator("//td[contains(@class, 'styles_tableCard')]").nth(1).click()
        pages.cards.hidden_card_data.click()
        pages.cards.number_of_card.check_text("5561  5042  6142  1839")
        page.locator("//span[contains(text(), '04 / 25')]").wait_for()
        assert page.get_by_text("04 / 25").is_visible()
        assert page.get_by_text("671").is_visible()

    @allure.title("Check number card visa")
    def test_check_number_card_visa(self, page: Page, pages: Pages,
                                steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.title_my_cards_ru.click()
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        page.locator("(//td[contains(@class, 'styles_tableCard')])[8]").click()
        pages.cards.hidden_card_data.click()
        pages.cards.number_of_card.check_text("4334 5152 8275 6978")
        page.locator("//span[contains(text(), '04 / 25')]").wait_for()
        assert page.get_by_text("04 / 25").is_visible()
        assert page.get_by_text("499").is_visible()

    @allure.title("Check number freeze card")
    def test_check_number_freeze_card(self, page: Page, pages: Pages,
                                  steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.title_my_cards_ru.click()
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        pages.cards.card_freeze_user_data.click()
        assert pages.cards.modal_closed_number_card.is_visible()
        pages.cards.modal_closed_number_card.check_text('••••  ••••  ••••  9542')
        page.get_by_label("23test do not change").get_by_text("Frozen").is_visible()

    @allure.title("Check number closed card")
    def test_check_number_closed_card(self, page: Page, pages: Pages,
                                  steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.title_my_cards_ru.click()
        pages.cards.card_closed_user_data.is_not_on_page(timeout=3500)
        pages.cards.card_closed_user_data.click()
        assert pages.cards.modal_card_number.is_visible()
        pages.cards.modal_closed_number_card.check_text("••••  ••••  ••••  7669")
        page.get_by_label("23test do not change").get_by_text("Closed").is_visible()

    @allure.title("Check spend money")
    def test_check_spend_money(self, page: Page, pages: Pages,
                           steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.title_my_cards_ru.click()
        sleep(2)
        page.locator("(//td[contains(@class, 'styles_tableCard')])[5]").click()
        sleep(2)
        pages.cards.amount_spend.check_text('60,51 $ /')
        pages.cards.modal_card_limit_amount_ru.check_text('100,00\xa0$')

    @allure.title("Check all spend money")
    def test_check_all_spend_money(self, page: Page, pages: Pages,
                               steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.title_my_cards_ru.click()
        pages.cards.card_closed_user_data.is_not_on_page(timeout=3500)
        steps.cardsSteps.check_popper_activator_info(page)
        assert pages.cards.date_filter_in_title_table.is_visible()
        pages.cards.sum_in_title_table.check_text('249,55\xa0$')

    @allure.title("Check from All cards cards quantity cards")
    def test_all_cards_check_quantity_cards(self, page: Page, pages: Pages,
                                        steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        expect(page.locator("//td[contains(@class, 'styles_tableCard')]")).to_have_count(25)
        pages.cards.arrow_next_page_button.click()
        expect(page.locator("//td[contains(@class, 'styles_tableCard')]")).to_have_count(7)

    @allure.title("Check from All cards all names cards")
    def test_all_cards_check_all_name_cards(self, page: Page, pages: Pages,
                                        steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        steps.cardsSteps.all_cards_check_all_name_cards(page)
        pages.cards.arrow_next_page_button.click()
        steps.cardsSteps.all_cards_check_all_name_cards_next_page(page)

    @allure.title("Check from All cards all statuses cards")
    def test_all_cards_check_all_status_cards(self, page: Page, pages: Pages,
                                          steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        steps.cardsSteps.check_all_cards_check_all_status_cards(page)
        pages.cards.arrow_next_page_button.click()
        steps.cardsSteps.check_all_cards_check_all_status_cards_next_page(page)

    @allure.title("Check from All cards all bins")
    def test_all_cards_check_bin_all_cards(self, page: Page, pages: Pages,
                                       steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        steps.cardsSteps.check_all_cards_check_bin_all_cards(page)
        pages.cards.arrow_next_page_button.click()
        steps.cardsSteps.check_all_cards_check_bin_all_cards_next_page(page)

    @allure.title("Check from All cards limits all cards")
    def test_all_cards_check_limit_all_cards(self, page: Page, pages: Pages,
                                         steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        steps.cardsSteps.all_cards_check_limit_all_cards(page)
        pages.cards.arrow_next_page_button.click()
        steps.cardsSteps.all_cards_check_limit_all_cards_next_page(page)

    @allure.title("Check from All cards all user names")
    def test_all_cards_check_user_name_all_cards(self, page: Page, pages: Pages,
                                             steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        steps.cardsSteps.check_all_cards_check_user_name_all_cards(page)
        pages.cards.arrow_next_page_button.click()
        steps.cardsSteps.check_all_cards_check_user_name_all_cards_next_page(page)

    @allure.title("Check from All cards all spend")
    def test_all_cards_check_spend_all_cards(self, page: Page, pages: Pages,
                                         steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        steps.cardsSteps.check_all_cards_check_spend_all_cards(page)
        pages.cards.arrow_next_page_button.click()
        steps.cardsSteps.check_all_cards_check_spend_all_cards_next_page(page)

    @allure.title("Check from All cards one row active card")
    def test_all_cards_check_row_active_card(self, page: Page, pages: Pages,
                                         steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        expect(page.locator(
            "//*[contains(@class, 'hover-visible-container')]").filter(has_text='••8002 6 apple')).to_have_text(
            "••8002 6 appleActive433451Лайфтайм10,00 $ / 100,00 $invated emploee10,00 $")

    @allure.title("Check from All cards data of mc card")
    def test_all_cards_check_number_card_mc(self, page: Page, pages: Pages,
                                        steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        page.locator("(//td[contains(@class, 'styles_tableCard')])[5]").click()
        pages.cards.hidden_card_data.click()
        pages.cards.number_of_card.check_text("5534  3765  1978  6980")
        page.locator("//span[contains(text(), '04 / 25')]").wait_for()
        assert page.get_by_text("04 / 25").is_visible()
        assert page.get_by_text("443").is_visible()

    @allure.title("Check from All cards data of visa card")
    def test_all_cards_check_number_card_visa(self, page: Page, pages: Pages,
                                          steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        page.locator("(//td[contains(@class, 'styles_tableCard')])[12]").click()
        pages.cards.hidden_card_data.click()
        pages.cards.number_of_card.check_text("4334 5152 8275 6978")
        page.locator("//span[contains(text(), '04 / 25')]").wait_for()
        assert page.get_by_text("04 / 25").is_visible()
        assert page.locator("//span[contains(text(), '499')]").is_visible()
        pages.cards.modal_title_card.check_text('fdgfgfd erwe')
        expect(page.locator('//*[@data-test-id="modal-body"]//*[@data-test-id="pip"]')).to_have_css("color", "rgb(111, 198, 87)")
        assert pages.cards.button_freeze_card.is_visible()
        assert pages.cards.button_go_to_transactions.is_visible()
        assert pages.cards.button_more_ru.is_visible()
        assert pages.cards.modal_title_billing_address_ru.is_visible()
        pages.cards.modal_billing_address.check_text(BILLING_ADDRESS)
        pages.cards.modal_billing_address.click()
        pages.cards.toast.check_text('Поле "Биллинг адрес" скопировано')

    @allure.title("Check from All cards data of freeze card")
    def test_all_cards_check__number_freeze_card(self, page: Page, pages: Pages,
                                             steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.card_freeze_user_data.is_on_page(timeout=3500)
        pages.cards.card_freeze_user_data.click()
        sleep(1.5)
        pages.cards.modal_card_number.click()
        pages.cards.modal_card_number.check_text('4896 8303 6231 9542')
        page.get_by_label("23test do not change").get_by_text("Frozen").is_visible()
        assert pages.cards.button_go_to_transactions.is_visible()
        assert pages.cards.button_unfreeze_card.is_visible()
        assert pages.cards.button_more_ru.is_not_on_page()
        assert pages.cards.modal_close_card.is_visible()
        assert pages.cards.modal_title_billing_address_ru.is_visible()
        pages.cards.modal_billing_address.check_text(BILLING_ADDRESS)
        pages.cards.modal_billing_address.click()
        pages.cards.toast.check_text('Поле "Биллинг адрес" скопировано')

    @allure.title("Check from All cards data of closed card")
    def test_all_cards_check_number_closed_card(self, page: Page, pages: Pages,
                                            steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=2000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.card_closed_user_data.is_on_page(timeout=3500)
        pages.cards.card_closed_user_data.click()
        pages.cards.hidden_card_data.click()
        sleep(1.5)
        pages.cards.modal_card_number.check_text("5561  5007  4548  7669")
        page.get_by_label("23test do not change").get_by_text("Closed").is_visible()
        assert pages.cards.button_go_to_transactions.is_visible()
        assert pages.cards.button_freeze_card.is_not_on_page()
        assert pages.cards.button_more_ru.is_not_on_page()
        assert pages.cards.modal_title_billing_address_ru.is_visible()
        pages.cards.modal_billing_address.check_text(BILLING_ADDRESS)
        pages.cards.modal_billing_address.click()
        pages.cards.toast.check_text('Поле "Биллинг адрес" скопировано')

    @allure.title("Check from All cards spend money")
    def test_all_cards_check_spend_money(self, page: Page, pages: Pages,
                                     steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.card_closed_user_data.is_not_on_page(timeout=3500)
        page.locator("(//td[contains(@class, 'styles_tableCard')])[9]").click()
        pages.cards.amount_spend.is_on_page(timeout=4000)
        pages.cards.amount_spend.check_text('60,51 $ /')
        pages.cards.modal_card_limit_amount_ru.check_text('100,00\xa0$')

    @allure.title("Check from All cards total spend")
    def test_all_cards_check_all_spend_money(self, page: Page, pages: Pages,
                                         steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.card_closed_user_data.is_not_on_page(timeout=3500)
        steps.cardsSteps.check_from_all_cards_total_spend(page)
        assert pages.cards.date_filter_in_title_table.is_visible()
        pages.cards.sum_in_title_table.check_text('262,55\xa0$')

    @allure.title("Check from All cards filter by name")
    def test_all_cards_filter_by_name_card(self, page: Page, pages: Pages,
                                       steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.filter_name_card.is_on_page(timeout=3000)
        page.locator("//div[@data-test-id = 'filters-search']//input").fill("test")
        pages.cards.filter_name_card.keyboard.press("Enter")
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        pages.cards.first_card_after_search.check_text('••6980 testActive553437Без лимита∞test do not change12,50 $')
        pages.cards.first_card_after_search.click()
        assert pages.cards.modal_created_card_active_ru.is_on_page()
        pages.cards.modal_created_card_real_name_ru.check_text("test")

    @allure.title("Check from All cards not found")
    def test_all_cards_no_results(self, page: Page, pages: Pages,
                              steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.filter_name_card.is_on_page(timeout=3000)
        page.locator("//div[@data-test-id = 'filters-search']//input").fill("tesss")
        pages.cards.cards_not_found.check_text("Карты не найденыПопробуйте изменить фильтр или поисковый запросОчистить фильтры")
        page.get_by_text("Очистить фильтры").click()
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        pages.cards.filter_name_card.check_text("")
        assert page.locator("(//td[contains(@class,'styles_tableCard')])[1]").is_visible()

    @allure.title("Check from All cards filter by last numbers active card")
    def test_all_cards_filter_by_last_numbers_active(self, page: Page, pages: Pages,
                                                 steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.status_card_ru.click()
        page.locator("(//*[@data-test-id = 'checkbox'])[3]").click()
        pages.cards.status_card_ru.click()
        assert page.locator("//*[@data-test-id = 'tag']").get_by_text(
            "Active").is_visible()
        page.locator("//div[@data-test-id = 'filters-search']//input").fill("9880")
        pages.cards.spinner.is_on_page(timeout=3000)
        pages.cards.spinner.is_not_on_page(timeout=3000)
        pages.cards.first_card_after_search.check_text('••9880 56 yuhjiko9Active553437Месяц44,00 $test do not change0,00 $')

    @allure.title("Check from All cards filter by bin user")
    def test_all_cards_filter_by_bin_user(self, page: Page, pages: Pages,
                                      steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.bin_card_filter.click()
        page.locator(
            "(//*[@data-test-id = 'text-field'])[2]//input").fill('553437')
        page.locator("//div[contains(@class, 'styles_wrapper')]//span[contains(text(), '553437')]").click()
        page.locator("(//button[@data-test-id = 'button-link'])[1]").click()
        page.locator("//div[contains(@class, 'padding-block-end_3')]//input").fill('559666')
        page.locator("//div[contains(@class, 'styles_wrapper')]//span[contains(text(), '559666')]").click()
        assert page.locator(
            "//*[@data-test-id = 'tag']//div[contains(text(), '553437, 559666')]").is_visible()
        pages.cards.user_card_filter.click()
        page.locator(
            "//div[contains(@class, 'styles_wrapper')]//span[contains(text(), 'test do not change')]").click()
        assert page.locator(
            "(//*[@data-test-id = 'tag'])[2]//div[contains(text(), 'test do not change')]").is_visible()
        steps.cardsSteps.check_cards_filter_by_bin_user(page)
        pages.cards.title_my_cards_ru.click()
        steps.cardsSteps.check_cards_filter_by_bin_user_next_page(page)

    @allure.title("Check from All cards filter by calendar")
    def test_all_cards_filter_by_calendar(self, page: Page, pages: Pages,
                                      steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.calendar_button.click()
        pages.cards.calendar_all_time.click()
        sleep(1.5)
        page.locator("(//button[@data-test-id = 'button'])[6]").click()
        sleep(3)
        steps.cardsSteps.check_all_cards_filter_by_calendar_rows(page)
        pages.cards.title_my_cards_ru.click()
        steps.cardsSteps.check_all_cards_filter_by_calendar_rows_next_page(page)

    @allure.title("Check page employee")
    def test_card_check_page_employee(self, page: Page, pages: Pages,
                                    steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU_EMPLOYEE.login, USER_DATA_RU_EMPLOYEE.password, "Карты")
        pages.cards.create_card_ru.is_visible()
        assert pages.cards.title_my_cards_ru.is_not_on_page()
        assert pages.cards.title_all_cards_ru.is_not_on_page()
        steps.universalSteps.check_titles_at_table(page, '1', "Карта")
        steps.universalSteps.check_titles_at_table(page, '2', "Статус")
        steps.universalSteps.check_titles_at_table(page, '3', "BIN")
        steps.universalSteps.check_titles_at_table(page, '4', "Лимит")
        steps.universalSteps.check_titles_at_table(page, '5', "Затраты")
        expect(page.locator("//div[contains(@class, 'styles_container')][contains(text(), '4 карты')]")).to_be_visible()

    @allure.title("Check navigation page employee")
    def test_check_navigation_page_employee(self, page: Page, pages: Pages,
                                        steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU_EMPLOYEE.login, USER_DATA_RU_EMPLOYEE.password, "Карты")
        assert pages.navigation.navigation_team_ru.is_not_on_page()
        assert pages.navigation.cash_text_sum.is_not_on_page()
        assert pages.navigation.navigation_balance_ru.is_not_on_page(timeout=3000)
        pages.navigation.name_company_for_employee.check_text("test do not change")
        pages.navigation.name_company_for_employee.click()
        assert pages.navigation.profile_company_ru.is_not_on_page(timeout=1500)

    @allure.title("Check all rows employee")
    def test_check_rows_employee(self, page: Page, pages: Pages,
                             steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU_EMPLOYEE.login, USER_DATA_RU_EMPLOYEE.password, "Карты")
        pages.trans.first_row.check_text('••7485 stringActive553437Без лимита∞0,00\xa0$')
        steps.cardsSteps.check_rows_employee_cards(page)

    @allure.title("Check change limit employee")
    def test_change_limit_employee(self, page: Page, pages: Pages,
                               steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_UK.login, USER_UK.password, 'Картки')
        page.locator("//div[contains(text(), '••5022 test')]").click()
        pages.cards.modal_pencil_button.click()
        pages.cards.modal_choose_limit.is_on_page(timeout=2000)
        pages.cards.modal_choose_limit.click()
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        pages.cards.input_limit_amount.fill(100)
        pages.cards.modal_save_limit_uk.click()
        pages.cards.close_modal_card.click()
        page.reload()
        pages.cards.spinner.is_not_on_page(timeout=3000)
        page.locator("//div[contains(text(), '••5022 test')]").click()
        pages.cards.modal_card_day_limit_ru.is_on_page(timeout=2000)
        expect(page.locator(
            "(//div[@data-test-id = 'modal-body']//span[contains(@class, 'styles_containerBodyMd')])[3]")).to_have_text(
                '100,00\xa0$')

    @pytest.mark.skip("")
    @allure.title("Check create card employee")
    def test_create_card_employee(self, page: Page, pages: Pages,
                              steps: Steps, playwright):
        name_card = random_string(8)
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_UK.login, USER_UK.password, 'Картки')
        pages.cards.btn_create_card_uk.click()
        pages.cards.name_create_card_ru.is_on_page(timeout=3000)
        pages.cards.name_create_card_ru.click()
        page.locator("(//div[contains(@class, 'styles_wrapper')]//input)[2]").fill(name_card)
        pages.cards.bin_default_create_card_ru.is_visible()
        pages.cards.card_limit_disabled.is_on_page()
        pages.cards.button_create_uk.click()
        assert pages.cards.modal_created_card_active_uk.is_on_page(timeout=3000)
        assert pages.cards.modal_card_no_limit_uk.is_visible()
        pages.cards.modal_created_card_real_name_ru.check_text(name_card)

    @pytest.mark.skip("")
    @allure.title("Check close card employee")
    def test_close_card_employee(self, page: Page, pages: Pages,
                             steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_UK.login, USER_UK.password, 'Картки')
        page.locator("(//tr[contains(@class, 'hover-visible-container')])[2]").click()
        pages.cards.button_more_uk.click()
        pages.cards.modal_button_close_card_uk.click()
        pages.cards.modal_confirm_close_card_uk.click()
        pages.cards.title_of_closed_card_uk.is_on_page(timeout=2000)

    @allure.title("Check all spend employee")
    def test_check_all_spend_employee(self, page: Page, pages: Pages,
                                  steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME_EMPLOYEE)
        steps.auth.authorize_in_test(page, USER_DATA_RU_EMPLOYEE.login, USER_DATA_RU_EMPLOYEE.password, "Карты")
        page.locator(
            "//th[contains(@class, 'text-align_end')]//div[@data-test-id = 'floating-activator']").click()
        expect(page.locator("//div[@data-test-id = 'info-popover-content']")).to_have_text(['Settled2,00\xa0$Pending11,00\xa0$'])

    @allure.title("Check change card data employee")
    def test_change_card_data_employee(self, page: Page, pages: Pages,
                                   steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU_EMPLOYEE.login, USER_DATA_RU_EMPLOYEE.password, "Карты")
        pages.cards.first_card_after_search.click()
        pages.cards.button_more_ru.click()
        pages.cards.modal_change_card.check_text('Изменить названиеИзменить лимитПередать картуЗакрыть карту')

    @allure.title("Check freeze card employee")
    def test_freeze_card_employee(self, page: Page, pages: Pages,
                              steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU_EMPLOYEE.login, USER_DATA_RU_EMPLOYEE.password, "Карты")
        pages.cards.first_card_after_search.click()
        pages.cards.button_freeze_card.click()
        pages.cards.close_modal_card.click()
        pages.cards.title_cash_after_login.is_not_on_page(timeout=3000)
        pages.cards.first_card_after_search.click()
        pages.cards.button_unfreeze_card.is_on_page(timeout=2000)
        pages.cards.button_unfreeze_card.click()
        assert pages.cards.modal_created_card_active_ru.is_on_page()

    @allure.title("Check card data employee")
    def test_check_card_data_employee(self, page: Page, pages: Pages,
                                  steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU_EMPLOYEE.login, USER_DATA_RU_EMPLOYEE.password, "Карты")
        pages.cards.first_card_after_search.is_on_page(timeout=3500)
        pages.cards.second_card_employee.click()
        page.locator("//span[contains(text(), '6 apple')]").wait_for(timeout=3000)
        assert page.locator("(//span[contains(text(), 'invated emploee')])[2]").is_visible()
        assert pages.cards.modal_created_card_active_ru.is_on_page()
        assert page.locator("(//span[contains(text(), 'Лайфтайм')])[2]").is_visible()
        assert page.locator("//span[contains(text(), 'Биллинг адрес')]").is_visible()

    @allure.title("Check sort by newest to oldest  employee")
    def test_sort_by_newest_oldest(self, page: Page, pages: Pages,
                               steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        steps.cardsSteps.check_sort_card_by_default(page)
        pages.cards.title_table_card_ru.click()
        pages.team.first_old_sort_ru.is_on_page(timeout=2000)
        steps.cardsSteps.check_sort_card_by_old_cards(page)
        pages.cards.title_table_card_ru.click()
        pages.team.first_new_sort_ru.is_on_page(timeout=2000)
        steps.cardsSteps.check_sort_card_by_default(page)

    @allure.title("Check sort by spend employee")
    def test_sort_by_spend(self, page: Page, pages: Pages,
                       steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        steps.cardsSteps.check_sort_card_by_default(page)
        pages.cards.title_table_spend_ru.click()
        pages.team.ascending_sort_ru.is_on_page(timeout=2000)
        steps.cardsSteps.check_sort_by_descending(page)
        pages.cards.title_table_spend_ru.click()
        steps.cardsSteps.check_sort_card_by_ascending(page)
        pages.cards.title_table_spend_ru.click()
        pages.team.descending_sort_ru.is_on_page(timeout=2000)
        steps.cardsSteps.check_sort_card_by_ascending(page)

    @allure.title("Check button 'Clear filters'")
    def test_clear_filters(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.status_card_ru.click()
        pages.cards.filter_closed_card_ru.click()
        pages.cards.bin_card_filter.click()
        pages.cards.filter_bin_553437.click()
        pages.cards.bin_card_filter.click()
        pages.cards.tag_bin_553437.is_visible()
        pages.cards.tag_closed_ru.is_visible()
        page.get_by_text("Карты не найдены").wait_for(timeout=2000)
        pages.cards.tag_closed_ru.is_visible()
        page.get_by_text('Попробуйте изменить фильтр или поисковый запрос').is_visible()
        pages.cards.button_clear_filters_ru.click()
        expect(page.locator('//*[@data-test-id="tag"]//div[contains(text(), "553437")]')).not_to_be_visible()
        expect(page.locator('//*[@data-test-id="tag"]//div[contains(text(), "Закрыта")]')).not_to_be_visible()

    @allure.title("Check status 'Expired'")
    def test_check_status_expired(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.navigation.navigation_cards_ru.is_not_on_page(timeout=3000)
        pages.cards.title_cash_after_login.check_text("Карты")
        pages.cards.status_card_ru.click()
        assert pages.cards.status_closed.is_visible()
        assert pages.cards.status_active.is_visible()
        assert pages.cards.status_frozen.is_visible()
        assert pages.cards.status_expired.is_visible()
        pages.cards.status_expired.click()
        expect(page.locator('//*[@data-test-id="badge"]')).to_have_text(['Expired'])
        page.locator("//div[contains(text(), '••7032 Аpple juce')]").click()
        assert pages.cards.modal_closed_number_card.is_visible()
        pages.cards.modal_title_card.check_text('Аpple juce')
        pages.cards.modal_title_owner.check_text('Joe Dow')
        expect(page.locator('//*[@data-test-id="modal-body"]//*[@data-test-id="pip"]')).to_have_css("color", "rgb(230, 72, 61)")
        expect(page.locator('//*[@data-test-id="modal-body"]//*[@data-test-id="pip"]/following-sibling::span')).to_have_text('Expired')
        assert pages.cards.button_freeze_card.is_not_on_page()
        assert pages.cards.button_more_ru.is_not_on_page()
        expect(page.locator("//*[@data-test-id='button']//span[text()='Транзакции']")).to_be_visible()
        expect(page.locator("//*[@data-test-id='button']//span[text()='Закрыть']")).to_be_visible()

    @allure.title("Check card's spend correct balance & limit day")
    def test_check_card_spend_limit_day(self, page: Page, pages: Pages, steps: Steps, playwright, api_request_context):
        card = "fe1ed4f7-4d5e-42ce-b6b8-7b398e973b09"
        api_set_limit(api_request_context, USER_WHITE_COMPANY.login, USER_WHITE_COMPANY.password, 241, None, 1)
        page.goto(AUTH_URL_ALL_TIME)
        api_set_limit(api_request_context, USER_WHITE_COMPANY.login, USER_WHITE_COMPANY.password, 241, 100, 2)
        api_request_with_available_balance(api_request_context, 90, card, APPROVED_SUCCES, SETTLED, COUNTRY_US, CURRENCY_USD, 10)
        steps.auth.authorize_in_test(page, USER_WHITE_COMPANY.login, USER_WHITE_COMPANY.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        expect(page.locator('//*[contains(text(), "test_card")]/ancestor::tr//div[@data-test-id="table-cell-limit"]')).to_have_text("День90,00 $ / 100,00 $")
        expect(page.locator('//*[contains(text(), "test_card")]/ancestor::tr//div[@style="width: 90%;"]')).to_be_visible()

    @allure.title("Open data card and copy all active card")
    def test_open_data_card_and_copy_all(self, page: Page, pages: Pages, steps: Steps, playwright,
                                                               api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.cards.first_card_after_search.click()
        sleep(1)
        pages.cards.right_arrow_first_card.hover()
        expect(page.locator('//*[@data-test-id="tooltip-content"]')).to_have_text('Следующая→')
        pages.cards.right_arrow_first_card.click()
        pages.cards.right_arrow_card.click()
        pages.cards.right_arrow_card.click()
        pages.cards.right_arrow_card.click()
        pages.cards.right_arrow_card.click()
        pages.cards.hidden_card_data.click()
        sleep(3)
        pages.cards.copy_all.click()
        expect(page.locator('//*[@data-test-id="tooltip-content"]')).to_have_text('Копировать все')
        pages.cards.toast.check_text('Детали карты скопированы')

    @allure.title("Open data card and copy all frozen card")
    def test_open_data_card_and_copy_all_frozen_card(self, page: Page, pages: Pages, steps: Steps, playwright,
                                         api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.cards.card_freeze_user_data.click()
        assert pages.cards.hidden_card_data.is_on_page()
        pages.cards.copy_all.is_not_on_page()
        page.keyboard.press("R")
        sleep(3)
        pages.cards.not_hidden_card_data.check_text("4896  8303  6231  9542EXP04 / 25CVC704")
        pages.cards.copy_all.click()
        expect(page.locator('//*[@data-test-id="tooltip-content"]')).to_have_text('Копировать все')
        pages.cards.toast.check_text('Детали карты скопированы')

    @allure.title("Open data card and copy all closed card")
    def test_open_data_card_and_copy_all_closed_card(self, page: Page, pages: Pages, steps: Steps, playwright,
                                         api_request_context):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Счет")
        pages.navigation.navigation_cards_ru.click()
        pages.cards.card_closed_user_data.click()
        pages.cards.hidden_card_data.hover()
        expect(page.locator("//*[contains(@class, 'display_flex align-items_center gap_1_5')]")).to_have_text('ПоказатьR')
        pages.cards.hidden_card_data.click()
        sleep(3)
        pages.cards.not_hidden_card_data.check_text("5561  5007  4548  7669EXP04 / 25CVC932")
        pages.cards.copy_all.click()
        expect(page.locator('//*[@data-test-id="tooltip-content"]')).to_have_text('Копировать все')
        pages.cards.toast.check_text('Детали карты скопированы')
        pages.cards.left_arrow_card.hover()
        expect(page.locator('//*[@data-test-id="tooltip-content"]')).to_have_text('Предыдущая←')
        pages.cards.left_arrow_card.click()
        assert pages.cards.hidden_card_data.is_visible()









