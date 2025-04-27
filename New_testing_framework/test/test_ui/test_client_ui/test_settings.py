import re
from time import sleep

import allure
import pytest
from playwright.sync_api import Page, expect

from data.input_data.random_data import random_string
from data.input_data.users import USER_RU, USER_DATA_RU, USER_GREY_COMPANY, USER_WHITE_COMPANY_EMPLOYEE
from pages.pages import Pages
from steps import Steps
from utils.consts import AUTH_URL_ALL_TIME, AUTH_URL


class TestSettings:
    @allure.title("Change language")
    def test_modal_change_language(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(AUTH_URL)
        page.locator("//input[@id='username']").fill(USER_GREY_COMPANY.login)
        page.locator("//input[@id='password']").fill(USER_GREY_COMPANY.password)
        pages.auth.login_button.click()
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.settings_user.main_avatar_empty.wait_for()
        pages.settings_user.language_edit.click()
        sleep(1)
        pages.settings_user.select_timezone.click()
        pages.settings_user.english_in_modal.check_text('En')
        pages.settings_user.english_in_row.check_text('English')
        pages.settings_user.russian_in_modal.check_text('Ру')
        pages.settings_user.russian_in_row.check_text('Русский')
        pages.settings_user.ukr_in_modal.check_text('Ук')
        pages.settings_user.ukr_in_row.check_text('Українська')
        pages.settings_user.english_in_row.click()
        pages.settings_user.button_save.click()

    @allure.title("Check settings page en")
    def test_check_settings_page_en(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_GREY_COMPANY.login, USER_GREY_COMPANY.password, "Cash")
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.settings_user.main_avatar_empty.wait_for()
        assert page.locator("//div[contains(text(), 'Email')]").is_visible()
        assert page.locator("//span[contains(text(), 'greycompany@mail.ru')]").is_visible()
        assert page.locator("(//span[contains(text(), 'Edit')])[1]").is_visible()
        assert page.locator("//div[contains(text(), 'Name')]").is_visible()
        assert page.locator("(//span[contains(text(), 'Edit')])[2]").is_visible()
        assert page.locator("//div[contains(text(), 'Profile picture')]").is_visible()
        assert pages.settings_user.profile_avatar_empty.is_visible()
        assert page.locator("(//div[@data-test-id = 'avatar'])[2]").is_visible()
        assert page.locator("//*[contains(text(), 'Add')]").is_visible()
        assert page.locator("//div[contains(text(), 'Language')]").is_visible()
        assert page.locator("//span[contains(text(), 'English')]").is_visible()
        assert page.locator("(//span[contains(text(), 'Edit')])[3]").is_visible()
        assert page.locator("//div[contains(text(), 'Timezone')]").is_visible()
        assert page.locator("//span[contains(text(), 'GMT+03:00 – Europe/Moscow')]").is_visible()
        assert page.locator("(//span[contains(text(), 'Edit')])[4]").is_visible()

    @allure.title("Check edit email")
    def test_check_edit_email(self, page: Page, pages: Pages,
                                 steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_GREY_COMPANY.login, USER_GREY_COMPANY.password, "Cash")
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.settings_user.main_avatar_empty.is_on_page(timeout=3000)
        page.locator("(//*[contains(text(), 'Edit')])[1]").click()
        sleep(1)
        expect(page.locator("//*[@data-test-id = 'modal-dialog']")).to_be_visible()
        pages.settings_user.button_show_password.click()
        expect(page.locator("//*[@data-test-id = 'modal-dialog']//h2")).to_have_text('Change email')
        expect(page.locator("//label[@for='password']")).to_have_text('Current password')
        expect(page.locator("//label[@for='email']")).to_have_text('New email')
        expect(page.locator("//*[@data-test-id='button']//span[contains(text(), 'Cancel')]")).to_be_visible()
        page.locator('//input[@id="email"]').fill(USER_GREY_COMPANY.login)
        page.locator('//input[@id="password"]').fill(USER_GREY_COMPANY.password)
        page.locator('//*[@data-test-id="button"]//span[contains(text(), "Update")]').click()
        expect(page.locator('//span[contains(text(), "User with this email already exists")]')).to_be_visible()

    @allure.title("Check edit name")
    def test_check_edit_name(self, page: Page, pages: Pages,
                             steps: Steps, playwright):
        name = random_string(7)
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_GREY_COMPANY.login, USER_GREY_COMPANY.password, "Cash")
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.settings_user.main_avatar_empty.wait_for()
        page.locator("(//*[@data-test-id = 'button-link']//span[contains(text(), 'Edit')])[2]").click()
        pages.settings_user.input_name.clear()
        pages.settings_user.input_name.fill(name)
        pages.settings_user.input_last_name.fill(name)
        pages.settings_user.button_update.click()
        pages.settings_user.toast_saved_changes.check_text("Your name has been changed")
        pages.settings_user.toast_saved_changes.is_not_on_page(timeout=2500)
        new_name = pages.settings_user.span_name.get_text()
        assert new_name == name + " " + name
        title = pages.settings_user.title.get_text()
        assert title == name + " " + name

    @allure.title("Add avatar")
    def test_add_avatar(self, page: Page, pages: Pages,
                        steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_GREY_COMPANY.login, USER_GREY_COMPANY.password, "Cash")
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.settings_user.main_avatar_empty.wait_for()
        page.locator("//span[contains(text(), 'Add')]").click()
        expect(page.locator("//h2/div[contains(text(), 'Add profile picture')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), 'Accepts .jpg and .png files')]")).to_be_visible()
        pages.settings_user.add_file.click()
        pages.settings_user.button_update.click()
        pages.settings_user.toast_saved_changes.check_text('Profile picture has been updated')

    @allure.title("Check timezone")
    def test_check_timezone(self, page: Page, pages: Pages,
                            steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_GREY_COMPANY.login, USER_GREY_COMPANY.password, "Cash")
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.settings_user.main_avatar_empty.wait_for()
        page.locator("(//*[contains(text(), 'Edit')])[4]").click()
        sleep(1)
        pages.settings_user.select_timezone.click()
        pages.settings_user.title_change.check_text('Change timezone')
        sleep(1)
        page.locator('//button[@data-index="286"]').click()
        expect(page.locator('//*[@data-test-id="form"]//*[@data-test-id="select"]')).to_have_text('GMT+03:00 – Europe/Moscow')

    @allure.title("Check profile company")
    def test_check_profile_company(self, page: Page, pages: Pages,
                                   steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.profile_company_ru.click()
        pages.settings_user.title.check_text('test do not change')
        expect(page.locator("//div[contains(text(), 'Название компании')]")).to_be_visible()
        expect(page.locator(
            "//span[contains(text(), 'Свяжитесь с нами, чтобы изменить название компании')]")).to_be_visible()
        expect(page.locator("//div[contains(text(), 'Логотип компании')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), 'test do not change')]")).to_be_visible()
        assert pages.settings_user.profile_avatar_empty.is_visible()

    @allure.title("Change avatar company")
    def test_check_avatar_change_company(self, page: Page, pages: Pages,
                                         steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.profile_company_ru.click()
        pages.settings_user.title.check_text('test do not change')
        pages.settings_user.button_add_file_ru.click()
        sleep(1)
        pages.settings_user.title_change.check_text('Добавить логотипЛоготип должен быть не меньше 256x256 px и будет виден только участникам вашей команды')
        pages.settings_user.size_files.check_text('Допускаются файлы .jpg и .png')
        assert pages.settings_user.add_file.is_visible()
        pages.settings_user.button_update.click()
        pages.settings_user.toast_saved_changes.check_text('Логотип компании был обновлен')

    @allure.title("Check billing page")
    def test_check_billing_page(self, page: Page, pages: Pages,
                                steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.billing_page_ru.click()
        expect(page.locator("h1")).to_have_text("Биллинг")
        pages.settings_user.tariff_name.check_text('Pro')
        pages.settings_user.status_active.check_text('Активный')
        pages.settings_user.description_tariff.check_text('2% Crypto• 2% Wire• 10 Бинов• Бесплатные карты')
        assert pages.settings_user.limits_of_users_ru.is_visible()
        expect(page.locator("//*[@data-test-id = 'tag']//div[contains(text(), 'Передача карт')]")).to_be_visible()
        expect(page.locator("//*[@data-test-id = 'tag']//div[contains(text(), 'Международные Бины')]")).to_be_visible()
        assert page.locator("//span[contains(text(), 'Ежемесячная подписка')]").is_visible()
        pages.settings_user.sum_tariff.check_text('471,00 $')

    @allure.title("Check current tariff plan")
    def test_check_current_tariff_plan(self, page: Page, pages: Pages,
                                       steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.tariff_plans_ru.click()
        pages.settings_user.title_tariff_plans_ru.is_on_page(timeout=3000)
        expect(page.locator(
            "(//*[@data-test-id = 'badge'])[2]//span/ancestor::div[contains(@class, 'gap_4 padding-block-end_2')]/span[contains(text(), 'Pro')]")).to_be_visible()

    @allure.title("Check available tariff basic")
    def test_check_available_tariff_basic(self, page: Page, pages: Pages,
                                          steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.tariff_plans_ru.click()
        pages.settings_user.title_tariff_plans_ru.is_on_page(timeout=3000)
        assert pages.settings_user.basic_tariff.wait_for()
        assert pages.settings_user.basic_tariff.is_visible()
        expect(page.locator("//p[contains(text(), 'Для соло и небольших команд')]")).to_be_visible()
        pages.settings_user.sum_first_tariff.check_text('100\xa0$')
        pages.settings_user.sum_first_tariff_time.check_text(' / месяц')
        pages.settings_user.description_first_tariff.check_text('Private возможности:2% Crypto2% Wire10 БиновБесплатные картыПередача картЛимиты пользователейМеждународные Бины')

    @allure.title("Compare description basic")
    def test_compare_description_basic(self, page: Page, pages: Pages,
                                       steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.tariff_plans_ru.click()
        pages.settings_user.title_tariff_plans_ru.is_on_page(timeout=3000)
        sleep(2)
        expect(page.locator("(//main//div[contains(@class, 'styles_container')])[2]/div[1]")).to_have_text('Basic')
        expect(page.locator("(//main//div[contains(@class, 'styles_container')])[1]")).to_have_text('Тарифные планы')
        expect(page.locator("(//main//div[contains(@class, 'styles_container')])[2]/p")).to_have_text(
            'Для соло и небольших команд')
        expect(page.locator("(//main//div[contains(@class, 'styles_container')])[2]/div[2]")).to_have_text(
            "100 $ / месяц")
        expect(page.locator("(//main//div[contains(@class, 'styles_container')])[2]/div[4]/span")).to_have_text(
            "Basic возможности:")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[2]//div[contains(@class, 'display_flex gap_2')][1]")).to_have_text(
            "3% Crypto")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[2]//div[contains(@class, 'display_flex gap_2')][2]")).to_have_text(
            "3% Wire")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[2]//div[contains(@class, 'display_flex gap_2')][3]")).to_have_text(
            "2 Бина")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[2]//div[contains(@class, 'display_flex gap_2')][4]")).to_have_text(
            "Бесплатные карты")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[2]//div[contains(@class, 'display_flex gap_2')][5]")).to_have_text(
            "Передача карт")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[2]//div[contains(@class, 'display_flex gap_2')][6]")).to_have_text(
            "Лимиты пользователей")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[2]//div[contains(@class, 'display_flex gap_2')][7]")).to_have_text(
            "Международные Бины")

    @allure.title("Compare description pro")
    def test_compare_description_pro(self, page: Page, pages: Pages,
                                     steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.tariff_plans_ru.click()
        pages.settings_user.title_tariff_plans_ru.is_on_page(timeout=3000)
        expect(page.locator("(//main//div[contains(@class, 'styles_container')])[3]/div[1]")).to_have_text(
            'ProТекущий тариф')
        expect(page.locator("(//main//div[contains(@class, 'styles_container')])[3]/p")).to_have_text(
            'Для профессионалов')
        expect(page.locator("(//main//div[contains(@class, 'styles_container')])[3]/div[2]")).to_have_text(
            "471 $ / месяц")
        expect(page.locator("(//main//div[contains(@class, 'styles_container')])[3]/div[4]/span")).to_have_text(
            "Pro возможности:")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[3]//div[contains(@class, 'display_flex gap_2')][1]")).to_have_text(
            "2% Crypto")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[3]//div[contains(@class, 'display_flex gap_2')][2]")).to_have_text(
            "2% Wire")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[3]//div[contains(@class, 'display_flex gap_2')][3]")).to_have_text(
            "10 Бинов")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[3]//div[contains(@class, 'display_flex gap_2')][4]")).to_have_text(
            "Бесплатные карты")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[3]//div[contains(@class, 'display_flex gap_2')][5]")).to_have_text(
            "Передача карт")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[3]//div[contains(@class, 'display_flex gap_2')][6]")).to_have_text(
            "Лимиты пользователей")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[3]//div[contains(@class, 'display_flex gap_2')][7]")).to_have_text(
            "Международные Бины")

    @allure.title("Compare description private")
    def test_compare_description_private(self, page: Page, pages: Pages,
                                         steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.tariff_plans_ru.click()
        pages.settings_user.title_tariff_plans_ru.is_on_page(timeout=3000)
        expect(page.locator("(//main//div[contains(@class, 'styles_container')])[5]/div[1]")).to_have_text(
            'Private')
        expect(page.locator("(//main//div[contains(@class, 'styles_container')])[5]/p")).to_have_text(
            'Для крупных команд')
        expect(page.locator("(//main//div[contains(@class, 'styles_container')])[5]/div[2]")).to_have_text(
            "600 $ / месяц")
        expect(page.locator("(//main//div[contains(@class, 'styles_container')])[5]/div[4]/span")).to_have_text(
            "Private возможности:")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[5]//div[contains(@class, 'display_flex gap_2')][1]")).to_have_text(
            "2% Crypto")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[5]//div[contains(@class, 'display_flex gap_2')][2]")).to_have_text(
            "2% Wire")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[5]//div[contains(@class, 'display_flex gap_2')][3]")).to_have_text(
            "10 Бинов")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[5]//div[contains(@class, 'display_flex gap_2')][4]")).to_have_text(
            "Бесплатные карты")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[5]//div[contains(@class, 'display_flex gap_2')][5]")).to_have_text(
            "Передача карт")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[5]//div[contains(@class, 'display_flex gap_2')][6]")).to_have_text(
            "Лимиты пользователей")
        expect(page.locator(
            "(//main//div[contains(@class, 'styles_container')])[5]//div[contains(@class, 'display_flex gap_2')][7]")).to_have_text(
            "Международные Бины")

    @allure.title("Compare table")
    def test_compare_table(self, page: Page, pages: Pages,
                           steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.tariff_plans_ru.click()
        pages.settings_user.title_tariff_plans_ru.is_on_page(timeout=3000)
        expect(page.locator("//table[contains(@class, 'styles_table')]/thead")).to_have_text("СравнениеBasicProPrivate")
        expect(page.locator("//table[contains(@class, 'styles_table')]/tbody//tr[1]")).to_have_text("Crypto3%2%2%")
        expect(page.locator("//table[contains(@class, 'styles_table')]/tbody//tr[2]")).to_have_text("Wire3%2%2%")
        expect(page.locator("//table[contains(@class, 'styles_table')]/tbody//tr[3]")).to_have_text("Бины21010 ")
        expect(page.locator("//table[contains(@class, 'styles_table')]/tbody//tr[4]")).to_have_text("Бесплатные карты")
        steps.teamSteps.check_features_in_plans(page, '4', '1')
        steps.teamSteps.check_features_in_plans(page, '4', '2')
        steps.teamSteps.check_features_in_plans(page, '4', '3')
        expect(page.locator("//table[contains(@class, 'styles_table')]/tbody//tr[5]")).to_have_text("Передача карт")
        steps.teamSteps.check_features_in_plans(page, '5', '1')
        steps.teamSteps.check_features_in_plans(page, '5', '2')
        steps.teamSteps.check_features_in_plans(page, '5', '3')
        expect(page.locator("//table[contains(@class, 'styles_table')]/tbody//tr[6]")).to_have_text(
            "Лимиты пользователей")
        steps.teamSteps.check_features_in_plans(page, '6', '1')
        steps.teamSteps.check_features_in_plans(page, '6', '2')
        steps.teamSteps.check_features_in_plans(page, '6', '3')
        expect(page.locator("//table[contains(@class, 'styles_table')]/tbody//tr[7]")).to_have_text(
            "Международные Бины")
        steps.teamSteps.check_features_in_plans(page, '7', '1')
        steps.teamSteps.check_features_in_plans(page, '7', '2')
        steps.teamSteps.check_features_in_plans(page, '7', '3')

    @allure.title("Check bins")
    def test_check_bins(self, page: Page, pages: Pages,
                        steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.button_bin_ru.click()
        pages.settings_user.title_tariff_plans.wait_for_text('Доступные Бины')
        pages.settings_user.title_tariff_plans.check_text('Доступные Бины')
        expect(page.locator("//div[contains(@class, 'styles_containerHoverable')]")).to_have_count(7)
        expect(page.locator(
            "//span[contains(text(), '404038')]/ancestor::div[contains(@class, 'styles_containerHoverable')]")).to_have_text(
            'PrivatePrepaid404038USD • US • 3DS')
        expect(page.locator(
            "//span[contains(text(), '559292')]/ancestor::div[contains(@class, 'styles_containerHoverable')]")).to_have_text(
            'BasicCredit559292USD • US')
        expect(page.locator(
            "//span[contains(text(), '556371')]/ancestor::div[contains(@class, 'styles_containerHoverable')]")).to_have_text(
            'Credit556371USD • US')
        expect(page.locator(
            "//span[contains(text(), '489683')]/ancestor::div[contains(@class, 'styles_containerHoverable')]")).to_have_text(
            'PrivatePrepaid489683USD • US')
        expect(page.locator(
            "//span[contains(text(), '531993')]/ancestor::div[contains(@class, 'styles_containerHoverable')]")).to_have_text(
            'Credit531993USD • US')
        expect(page.locator(
            "//span[contains(text(), '519075')]/ancestor::div[contains(@class, 'styles_containerHoverable')]")).to_have_text(
            'Credit519075USD • US')
        expect(page.locator(
            "//span[contains(text(), '553437')]/ancestor::div[contains(@class, 'styles_containerHoverable')]")).to_have_text(
            'Credit553437International')

    @allure.title("Check bin visa")
    def test_check_bin_visa(self, page: Page, pages: Pages,
                            steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.button_bin_ru.click()
        pages.settings_user.title_tariff_plans.wait_for_text('Доступные Бины')
        pages.settings_user.title_tariff_plans.check_text('Доступные Бины')
        expect(page.locator(
            "//span[contains(text(), '404038')]/ancestor::div[contains(@class, 'styles_containerHoverable')]/div[1]")).to_have_text(
            'PrivatePrepaid')
        expect(page.locator(
            "//span[contains(text(), '404038')]/ancestor::div[contains(@class, 'styles_containerHoverable')]/div[2]")).to_have_text(
            '404038USD • US • 3DS')
        expect(page.locator(
            "//span[contains(text(), '404038')]/ancestor::div[contains(@class, 'styles_containerHoverable')]/div[2]/img")).to_be_visible()

    @allure.title("Check bin mc")
    def test_check_bin_mc(self, page: Page, pages: Pages,
                          steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.button_bin_ru.click()
        pages.settings_user.title_tariff_plans.wait_for_text('Доступные Бины')
        pages.settings_user.title_tariff_plans.check_text('Доступные Бины')
        expect(page.locator(
            "//span[contains(text(), '559292')]/ancestor::div[contains(@class, 'styles_containerHoverable')]/div[1]")).to_have_text(
            'BasicCredit')
        expect(page.locator(
            "//span[contains(text(), '559292')]/ancestor::div[contains(@class, 'styles_containerHoverable')]/div[2]")).to_have_text(
            '559292USD • US')
        expect(page.locator(
            "//span[contains(text(), '559292')]/ancestor::div[contains(@class, 'styles_containerHoverable')]/div[2]/img")).to_be_visible()

    @allure.title("Check modal bin mc")
    def test_check_modal_bin_mc(self, page: Page, pages: Pages,
                                steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.button_bin_ru.click()
        pages.settings_user.title_tariff_plans.wait_for_text('Доступные Бины')
        pages.settings_user.title_tariff_plans.check_text('Доступные Бины')
        page.locator("//span[contains(text(), '559292')]").click()
        pages.settings_user.title_modal_bin.check_text('MasterCard Credit')
        pages.settings_user.type_modal_bin.check_text('Basic')
        expect(page.locator("(//*[@data-test-id = 'modal-dialog']//*[contains(text(), 'Credit')])[2]")).to_be_visible()
        pages.settings_user.number_bin_in_modal.check_text('559292USD • US')
        assert pages.settings_user.img_network_modal_bin.is_visible()
        expect(page.locator("//*[@data-test-id = 'modal-dialog']//span[contains(text(), 'Категория')]")).to_be_visible()
        expect(page.get_by_text('Commercial')).to_be_visible()
        expect(page.get_by_text('Тип')).to_be_visible()
        expect(page.locator("//*[@data-test-id]//span[contains(text(), 'Credit')]")).to_be_visible()
        expect(page.locator("//*[@data-test-id]//span[contains(text(), 'Страна')]")).to_be_visible()
        expect(page.locator("(//*[@data-test-id]//div[contains(text(), 'US')])[1]")).to_be_visible()
        expect(page.locator("//*[@data-test-id]//span[contains(text(), 'Валюта')]")).to_be_visible()
        expect(page.locator("//*[@data-test-id]//div[contains(text(), 'USD')]")).to_be_visible()
        steps.teamSteps.check_text_bin_modal(page, '5', 'Комиссия за обмен валюты1 % + 0,01 $')
        steps.teamSteps.check_text_bin_modal(page, '6', 'Комиссия за международный платеж1 % + 0,50 $')

    @allure.title("Check modal bin visa")
    def test_check_modal_bin_visa(self, page: Page, pages: Pages,
                                  steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.button_bin_ru.click()
        pages.settings_user.title_tariff_plans.wait_for_text('Доступные Бины')
        pages.settings_user.title_tariff_plans.check_text('Доступные Бины')
        page.locator("//span[contains(text(), '404038')]").click()
        pages.settings_user.title_modal_bin.check_text('Visa Prepaid')
        pages.settings_user.type_modal_bin.check_text('Private')
        expect(page.locator("(//*[@data-test-id = 'modal-dialog']//*[contains(text(), 'Prepaid')])[2]")).to_be_visible()
        pages.settings_user.number_bin_in_modal.check_text('404038USD • US • 3DS')
        pages.settings_user.img_network_modal_bin.is_visible()
        expect(page.locator("//*[@data-test-id = 'modal-dialog']//span[contains(text(), 'Категория')]")).to_be_visible()
        expect(page.get_by_text('Consumer')).to_be_visible()
        expect(page.get_by_text('Тип')).to_be_visible()
        expect(page.locator("//*[@data-test-id]//span[contains(text(), 'Prepaid')]")).to_be_visible()
        expect(page.locator("//*[@data-test-id]//span[contains(text(), 'Страна')]")).to_be_visible()
        expect(page.locator("(//*[@data-test-id]//div[contains(text(), 'US')])[1]")).to_be_visible()
        expect(page.locator("//*[@data-test-id]//span[contains(text(), 'Валюта')]")).to_be_visible()
        expect(page.locator("//*[@data-test-id]//div[contains(text(), 'USD')]")).to_be_visible()
        steps.teamSteps.check_text_bin_modal(page, '5', 'Комиссия за обмен валюты1 % + 0,01 $')
        steps.teamSteps.check_text_bin_modal(page, '6', 'Комиссия за международный платеж1 % + 0,50 $')

    @allure.title("Check modal basic prepaid")
    def test_check_modal_basic_prepaid(self, page: Page, pages: Pages,
                                       steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.button_bin_ru.click()
        pages.settings_user.title_tariff_plans.wait_for_text('Доступные Бины')
        pages.settings_user.title_tariff_plans.check_text('Доступные Бины')
        page.locator("//span[contains(text(), '404038')]").click()
        pages.settings_user.info_in_modal.check_text('КатегорияConsumerТипPrepaidСтранаUSВалютаUSDКомиссия за обмен валюты1 % + 0,01 $Комиссия за международный платеж1 % + 0,50 $')
        pages.settings_user.title.check_text('Visa Prepaid')
        pages.settings_user.basic_in_modal_card.wait_for()
        assert pages.settings_user.prepaid_in_modal_card.is_visible()
        assert pages.settings_user.number_card_basic_prepaid.is_visible()

    @allure.title("Check modal premium credit")
    def test_check_modal_premium_credit(self, page: Page, pages: Pages,
                                        steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.button_bin_ru.click()
        pages.settings_user.title_tariff_plans.wait_for_text('Доступные Бины')
        pages.settings_user.title_tariff_plans.check_text('Доступные Бины')
        page.locator("//span[contains(text(), '556371')]").click()
        pages.settings_user.info_in_modal.check_text("КатегорияCommercialТипCreditСтранаUSВалютаUSDКомиссия за обмен валюты1 % + 0,01 $Комиссия за международный платеж1 % + 0,50 $")
        pages.settings_user.title.check_text('MasterCard Credit')
        assert pages.settings_user.credit_in_modal_card.is_visible()

    @allure.title("Check modal private prepaid")
    def test_check_modal_private_prepaid(self, page: Page, pages: Pages,
                                         steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.button_bin_ru.click()
        pages.settings_user.title_tariff_plans.wait_for_text('Доступные Бины')
        pages.settings_user.title_tariff_plans.check_text('Доступные Бины')
        page.locator("(//div[contains(@class, 'styles_containerHoverable')])[3]").click()
        pages.settings_user.info_in_modal.check_text("КатегорияConsumerТипPrepaidСтранаUSВалютаUSDКомиссия за обмен валюты1 % + 0,01 $Комиссия за международный платеж1 % + 0,50 $")
        pages.settings_user.title.check_text('Visa Prepaid')
        assert pages.settings_user.prepaid_in_modal_card.is_visible()
        assert pages.settings_user.private_in_modal_card.is_visible()


    @allure.title("Check modal credit international")
    def test_check_modal_credit_international(self, page: Page, pages: Pages,
                                              steps: Steps, playwright):
        page.goto(AUTH_URL_ALL_TIME)
        steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.button_bin_ru.click()
        pages.settings_user.title_tariff_plans.wait_for_text('Доступные Бины')
        pages.settings_user.title_tariff_plans.check_text('Доступные Бины')
        page.locator("//span[contains(text(), '553437')]").click()
        pages.settings_user.info_in_modal.check_text('КатегорияCommercialТипCreditСтранаUSВалютаМультивалютнаяКомиссия за обмен валюты0\xa0%Комиссия за международный платеж0\xa0%')
        pages.settings_user.title.check_text('MasterCard Credit')
        assert pages.settings_user.credit_in_modal_card.is_visible()
        assert pages.settings_user.international_in_modal_card.is_visible()
        assert pages.settings_user.number_card_international.is_visible()

    @allure.title("Security check password")
    def test_security_check_pass(self, page: Page, pages: Pages,
                                 steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.button_security_ru.click()
        assert pages.settings_user.title_security_page_ru.is_on_page(timeout=2000)
        pages.settings_user.change_password_ru.click()
        assert pages.settings_user.title_modal_change_ru.is_visible()
        pages.settings_user.input_old_password.fill(USER_RU.password)
        pages.settings_user.input_new_password.fill(USER_RU.password)
        pages.settings_user.input_confirm_password.fill(USER_RU.password)
        pages.settings_user.button_save.click()
        pages.settings_user.toast_saved_changes.check_text('Ваш пароль изменен')

    @allure.title("Check page security")
    def test_check_page_security(self, page: Page, pages: Pages,
                                 steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.navigation.button_security_ru.click()
        assert pages.settings_user.title_security_page_ru.is_on_page(timeout=2000)
        assert pages.settings_user.title_password_ru.is_visible()
        assert pages.settings_user.title_session_ru.is_visible()
        pages.settings_user.title_active_session.check_text('Все активные сессии с russianlanguige@mail.ru')
        assert pages.settings_user.this_session_ru.is_on_page(timeout=1500)
        assert pages.settings_user.language_session_ru.is_visible()

    @allure.title("Reset all sessions")
    def test_reset_all_sessions(self, page: Page, pages: Pages,
                                steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        page.locator("//*[contains(text(), 'Мой профиль')]").click()
        pages.navigation.button_security_ru.click()
        pages.settings_user.user_session.wait_for(timeout=1500)
        assert pages.settings_user.user_session.is_visible()
        pages.settings_user.button_reset_all_sessions_ru.click()
        assert pages.settings_user.user_session.is_not_on_page(timeout=1500)

    @allure.title("Reset current session")
    def test_reset_current_session(self, page: Page, pages: Pages,
                                   steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        page.locator("//*[contains(text(), 'Мой профиль')]").click()
        pages.navigation.button_security_ru.click()
        pages.settings_user.user_session.wait_for(timeout=1500)
        pages.settings_user.current_session.hover()
        pages.settings_user.button_reset_current_session_ru.click()
        assert pages.auth.login_input.wait_for(timeout=1500)
        assert pages.auth.password_input.is_visible()
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, 'Счет')

    @allure.title("Go to profile company")
    def test_go_to_profile_company(self, page: Page, pages: Pages,
                                   steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, 'Счет')
        pages.navigation.name_company.click()
        pages.navigation.profile_company_ru.click()
        pages.settings_user.main_avatar_empty.is_on_page(timeout=3000)
        assert page.locator("//h2[contains(text(), 'MTS')]").is_visible()

    @pytest.mark.skip("")
    @allure.title("Check your referrals")
    def test_check_your_referrals(self, page: Page, pages: Pages,
                                  steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, 'Счет')
        pages.navigation.name_company.click()
        pages.navigation.referral_company_ru.click()
        assert pages.settings_user.title_referral_ru.wait_for()
        steps.universalSteps.check_titles_at_table(page, '1', 'Компания')
        steps.universalSteps.check_titles_at_table(page, '2', 'Статус')
        steps.universalSteps.check_any_text_at_row_table(page, '1', 'NMnmfdADSF retryty')
        steps.universalSteps.check_any_text_at_row_table(page, '2', 'Выплачено')
        steps.universalSteps.check_any_text_at_row_table(page, '5', 'KAKate Test')
        steps.universalSteps.check_any_text_at_row_table(page, '6', 'В листе ожидания')
        steps.universalSteps.check_any_text_at_row_table(page, '7', 'SOSolo With code')
        steps.universalSteps.check_any_text_at_row_table(page, '8', 'Онбординг пройден')
        steps.universalSteps.check_any_text_at_row_table(page, '15', 'SOSolo Mts')
        steps.universalSteps.check_any_text_at_row_table(page, '16', 'Отказано')
        expect(page.locator('(//div[@data-test-id="item-with-pip"])[1]')).to_be_visible()
#TODO: переписать тесты на провеку сода и ссылки, оформления страницы

    @allure.title("Check page 2FA")
    def test_check_2_fa(self, page: Page, pages: Pages,
                        steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_GREY_COMPANY.login, USER_GREY_COMPANY.password, 'Cash ')
        expect(page.locator('(//*[@data-test-id="alert"]/div/span)[1]')).to_have_text('Secure your account')
        expect(page.locator('(//*[@data-test-id="alert"]/div/span)[2]/p')).to_have_text(
            '2FA is now available to all users. Add an extra layer of security to your account now ')
        pages.navigation.btn_set_up_2fa.click()
        expect(page.locator('//*[@data-test-id="modal-body"]//p')).to_have_text("Can't scan the QR? Enter this key")
        expect(
            page.locator('(//*[@data-test-id="modal-body"]//*[@data-test-id="text-field"])[1]//input')).to_have_value(
            re.compile(r"^.{16}$"), timeout=2000)
        assert page.get_by_text('Code from the app').is_visible()
        assert page.get_by_placeholder("123 456").is_visible()
        pages.navigation.btn_chancel_2fa_en.click()
        expect(page.locator('//*[@data-test-id="modal-body"]')).not_to_be_visible()

    @allure.title("Input wrong long code")
    def test_input_wrong_long_code_2fa(self, page: Page, pages: Pages,
                                       steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_GREY_COMPANY.login, USER_GREY_COMPANY.password, 'Cash ')
        pages.navigation.btn_set_up_2fa.click()
        pages.settings_user.input_code_2fa.fill('4356433546')
        pages.navigation.btn_verify_en.click()
        expect(page.locator("//span[contains(text(), 'Ensure this field has no more than 6 characters.')]")).to_be_visible(timeout=1000)

    @allure.title("Input wrong short code")
    def test_input_wrong_short_code_2fa(self, page: Page, pages: Pages,
                                        steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_GREY_COMPANY.login, USER_GREY_COMPANY.password, 'Cash ')
        pages.navigation.btn_set_up_2fa.click()
        pages.settings_user.input_code_2fa.fill('43563')
        pages.navigation.btn_verify_en.click()
        expect(page.locator("//span[contains(text(), 'Ensure this field has at least 6 characters.')]")).to_be_visible(timeout=1000)

    @allure.title("Input wrong code")
    def test_input_wrong_code_2fa(self, page: Page, pages: Pages,
                                  steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_GREY_COMPANY.login, USER_GREY_COMPANY.password, 'Cash ')
        pages.navigation.btn_set_up_2fa.click()
        pages.settings_user.input_code_2fa.fill('435634')
        pages.navigation.btn_verify_en.click()
        expect(page.locator("//span[contains(text(), 'Invalid TOTP code')]")).to_be_visible(timeout=1000)

    @allure.title("Input code with letters and special symbols")
    def test_input_code_with_letters_and_special_symbols_2fa(self, page: Page, pages: Pages,
                                                             steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_GREY_COMPANY.login, USER_GREY_COMPANY.password, 'Cash ')
        pages.navigation.btn_set_up_2fa.click()
        pages.settings_user.input_code_2fa.fill('hf&^%#')
        pages.navigation.btn_verify_en.click()
        expect(page.locator("//span[contains(text(), 'Invalid TOTP code')]")).to_be_visible(timeout=1000)

    @allure.title("Copy code")
    def test_copy_code_2fa(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_GREY_COMPANY.login, USER_GREY_COMPANY.password, 'Cash ')
        pages.navigation.btn_set_up_2fa.click()
        pages.navigation.btn_copy_code.click()
        expect(page.locator('//*[@data-test-id="toast"]//span[contains(text(), "2FA key copied")]')).to_be_visible()

    @allure.title("Check 2FA at secure settings")
    def test_check_2fa_secure_settings(self, page: Page, pages: Pages,
                                       steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_GREY_COMPANY.login, USER_GREY_COMPANY.password, 'Cash ')
        pages.navigation.settings_user.click()
        page.locator("//div[contains(text(), 'My profile')]").click()
        page.locator("//div//*[contains(text(), 'Security')]").click()
        page.locator("//span[contains(text(), 'Two-factor authentication')]").wait_for(timeout=2500)
        expect(page.locator("//span[contains(text(), 'Auth app')]")).to_be_visible()
        expect(page.locator("//span[contains(text(), 'Add extra protection')]")).to_be_visible()
        page.locator("//span[contains(text(), 'Set up')]").click()
        expect(page.locator("//*[contains(text(), 'Set up 2FA')]")).to_be_visible()
        expect(page.locator('//*[@data-test-id="modal-body"]//p')).to_have_text("Can't scan the QR? Enter this key")
        expect(
            page.locator('(//*[@data-test-id="modal-body"]//*[@data-test-id="text-field"])[1]//input')).to_have_value(
            re.compile(r"^.{16}$"), timeout=2000)
        assert page.get_by_text('Code from the app').is_visible()
        assert page.get_by_placeholder("123 456").is_visible()
        page.locator("//*[contains(text(), 'Cancel')]").click()
        expect(page.locator("//*[contains(text(), 'Set up 2FA')]")).not_to_be_visible()

    @allure.title("Change theme")
    def test_change_theme(self, page: Page, pages: Pages,
                          steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, 'Счет')
        pages.navigation.settings_user.click()
        page.locator("//div[contains(text(), 'Мой профиль')]").click()
        expect(page.locator("//div[contains(text(), 'Тема')]")).to_be_visible()
        pages.settings_user.theme.click()
        pages.settings_user.ukr_in_row.click()
        expect(page.locator('//*[@data-theme="midnight"]')).to_be_visible()
        sleep(1)
        pages.settings_user.theme.click()
        pages.settings_user.russian_in_row.click()
        expect(page.locator('//*[@data-theme="light"]')).to_be_visible()

    @allure.title("Change language")
    def test_change_language(self, page: Page, pages: Pages,
                             steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_GREY_COMPANY.login, USER_GREY_COMPANY.password, "Cash")
        pages.navigation.settings_user.click()
        pages.navigation.my_profile.click()
        pages.settings_user.main_avatar_empty.wait_for()
        assert page.locator("//span[contains(text(), 'English')]").is_visible()
        page.locator("(//span[contains(text(), 'Edit')])[3]").click()
        page.locator("(//div[contains(@class, 'styles_endContent')])[2]").click()
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        pages.settings_user.button_update.click()
        pages.settings_user.toast_saved_changes.check_text('The language has been changed')
        page.locator("//div[contains(text(), 'Аватар профілю')]").wait_for()
        assert page.locator("//span[contains(text(), 'Українська')]").is_visible()
        page.locator("(//span[contains(text(), 'Редагувати')])[3]").click()
        sleep(1)
        expect(page.locator("//*[@data-test-id='modal-dialog']//div[contains(@class, 'styles_content')]")).to_have_text(
            'Українська')
        page.locator('//*[@data-test-id="modal-dialog"]//div[contains(@class, "styles_endContent")]').click()
        page.keyboard.press("ArrowUp")
        page.keyboard.press("ArrowUp")
        page.keyboard.press("Enter")
        pages.settings_user.button_update.click()
        pages.settings_user.toast_saved_changes.check_text('The language has been changed')

    @allure.title("Check your limit in the navigation bar")
    def test_check_your_limit_in_navigation_bar(self, page: Page, pages: Pages,
                             steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, 'Счет')
        assert pages.navigation.row_name.is_visible()
        expect(page.locator('(//*[@data-test-id="floating-activator"])[2]//div[@data-test-id="avatar"]')).to_be_visible()
        expect(page.locator('(//*[@data-test-id="floating-activator"])[2]//span[contains(text(), "test test")]')).to_be_visible()
        expect(page.locator('(//*[@data-test-id="limit-info"]//span)[1]')).to_have_text("Лайфтайм")
        expect(page.locator('(//*[@data-test-id="limit-info"]//span)[4]')).to_contain_text('290 000,00 $')

    @allure.title("Check help center in the navigation bar")
    def test_check_help_center_in_navigation_bar(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_WHITE_COMPANY_EMPLOYEE.login, USER_WHITE_COMPANY_EMPLOYEE.password, 'Картки')
        page.locator('(//*[@data-test-id="menu-button-activator"])').click()
        expect(page.locator('//*[@data-test-id="action"]//div[contains(text(), "База знань")]')).to_be_visible()

    @allure.title("Check offer to tune 2fa")
    def test_check_offer_to_tune_2fa(self, page: Page, pages: Pages, steps: Steps, playwright):
        page.goto(AUTH_URL)
        steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, 'Счет')
        expect(page.locator('(//*[@data-test-id="alert"]//span)[1]')).to_have_text('Защитите свой аккаунт')
        expect(page.locator('(//*[@data-test-id="alert"]//span)[2]/p')).to_have_text('2FA теперь доступна всем пользователям. Добавьте дополнительный уровень безопасности к вашему аккаунту прямо сейчас')
        expect(page.locator('(//*[@data-test-id="alert"]//span)[2]//button')).to_have_text('Настроить 2FA')




