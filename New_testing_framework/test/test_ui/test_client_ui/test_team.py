from time import sleep

import allure
from playwright.sync_api import Page, expect

from api.function_api import auth_token, api_request_context
from data.input_data.random_data import random_string, random_string_lowercase
from data.input_data.users import USER_RU, USER_DATA_RU, USER_GREY_COMPANY
from pages.pages import Pages
from steps import Steps
from utils.consts import AUTH_URL_ALL_TIME_TEAM


@allure.title("Check title table")
def test_check_title_table(page: Page, pages: Pages,
                           steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Команда")
    pages.team.title_table_user.check_text("Пользователь")
    pages.team.title_table_status.check_text("Статус")
    pages.team.title_table_role.check_text("Роль")
    pages.team.title_table_limit.check_text("Лимит")
    pages.team.title_table_decline_rate.check_text("Decline rate")
    expect(page.locator("(//th[contains(@class, 'styles_tableDeclineRate')])[2]")).to_have_text("4,2 %")
    pages.team.title_table_spend.check_text("Затраты")
    expect(page.locator("//th//div[@data-test-id = 'info-popover-activator']//span/span")).to_have_text("262,55 $")
    pages.team.table_pagination.check_text("6 пользователей")


@allure.title("Check main modal in total spend")
def test_check_main_modal_in_spend(page: Page, pages: Pages,
                                   steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Команда")
    page.locator(
        "//th[contains(@class, 'text-align_end')]//div[@data-test-id = 'floating-activator']").click()
    expect(page.locator("//*[@data-test-id = 'info-popover-content']")).to_have_text('Settled205,00 $Pending101,00 $Reversed18,00 $Refund47,00 $Междунар. комиссия1,46 $Комиссия за деклайн1,00 $Конвертация1,09 $')


@allure.title("Check one row")
def test_check_one_row(page: Page, pages: Pages,
                       steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Команда")
    pages.team.first_row_name_user.wait_for_text('Новый пользователь', timeout=3000)
    pages.team.first_row_name_user.check_text("Новый пользователь")
    pages.team.first_row_status.check_text('Приглашен')
    pages.team.first_row_role.check_text("Админ")
    pages.team.first_row_limit.check_text('Месяц250,00 $')
    pages.team.first_row_declined_rate.check_text('0,0\xa0%')
    pages.team.first_row_spend.check_text('0,00\xa0$')


@allure.title("Check all users")
def test_check_all_users(page: Page, pages: Pages,
                         steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Команда")
    steps.teamSteps.check_all_users(page)


@allure.title("Check modal in spend one row")
def test_check_modal_in_spend(page: Page, pages: Pages,
                              steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Команда")
    page.locator("(//td[contains(@class, 'styles_tableSpend')])[6]").hover()
    page.locator(
        "(//tr//*[@data-test-id = 'info-popover-activator']//div[@data-test-id = 'floating-activator'])[3]").hover()
    page.locator('(//td//*[@data-test-id="floating-activator"])[2]').click()
    steps.teamSteps.check_modal_in_spend(page)


@allure.title("Check modal admin limit")
def test_check_modal_admin_limit(page: Page, pages: Pages,
                                 steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Команда")
    pages.team.first_row_name_user.wait_for_text('Новый пользователь', timeout=3000)
    pages.team.first_row_name_user.click()
    pages.team.modal_name_user.check_text('Новый пользователь')
    pages.team.modal_email_user.check_text('admintest@test.ru')
    pages.team.modal_role_user.check_text('Админ')
    expect(page.locator("//*[@data-test-id = 'limit-info']")).to_have_text('Месяц250,00 $')


@allure.title("Check admin permissions")
def test_check_admin_permissions(page: Page, pages: Pages,
                                 steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Команда")
    pages.cards.spinner.is_on_page(timeout=3000)
    pages.cards.spinner.is_not_on_page(timeout=3000)
    page.locator("(//div[contains(@class, 'display_flex align-items_center gap_3')])[6]").click()
    steps.teamSteps.check_permissions_admin(page)


@allure.title("Check modal employee limit")
def test_modal_employee_limit(page: Page, pages: Pages,
                            steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Команда")
    pages.team.second_row_name_user.click()
    pages.team.modal_name_user.check_text('Новый пользователь')
    pages.team.modal_email_user.check_text('testr@test.com')
    pages.team.modal_role_user.check_text('Сотрудник')
    expect(page.locator("//*[@data-test-id = 'limit-info']")).to_have_text('Лайфтайм200,00 $')


@allure.title("Check employee permissions")
def test_check_employee_permissions(page: Page, pages: Pages,
                                  steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Команда")
    pages.team.second_row_name_user.click()
    steps.teamSteps.check_permissions_employee(page)


@allure.title("Check edit limit to employee")
def test_edit_limit_to_employee(page: Page, pages: Pages,
                              steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_GREY_COMPANY.login, USER_GREY_COMPANY.password, "Team")
    page.locator("//div[contains(text(), 'test empl.')]").click()
    pages.team.pencil_button.click()
    pages.team.title_change_limit.is_on_page(timeout=1000)
    sleep(2)
    page.locator(
        ' (//*[@data-test-id="modal-body"]//div[contains(@class, "display_flex flex-direction_column")])[4]').click()
    pages.team.limit_daily.click()
    pages.team.input_limit_amount.fill(20)
    pages.team.modal_save_limit_en.click()
    sleep(2)
    expect(page.locator("//*[@data-test-id = 'limit-info']//span[contains(text(), 'Daily')]")).to_be_visible()
    expect(page.locator("//*[@data-test-id = 'limit-info']//span[contains(text(), '$20.00')]")).to_be_visible()
    pages.team.menu_button.click()
    pages.team.change_card_limit_en.click()
    page.locator(
        ' (//*[@data-test-id="modal-body"]//div[contains(@class, "display_flex flex-direction_column")])[4]').click()
    pages.team.limit_no_limit.click()
    pages.team.modal_save_limit_en.click()
    sleep(2)
    expect(page.locator("//*[@data-test-id = 'limit-info']//span[contains(text(), 'No limit')]")).to_be_visible()


@allure.title("Check search by user")
def test_search_by_user(page: Page, pages: Pages,
                        steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Команда")
    page.locator("//div[@data-test-id = 'filters-search']//input").fill("fgfh")
    expect(page.locator("//tr[contains(@class, 'hover-visible-container')]")).to_have_count(1)
    expect(page.locator("//tr[contains(@class, 'hover-visible-container')]")).to_have_text(
        ['FFfgfh fghАктивенАдминМесяц300\xa0001,00\xa0$0,0\xa0%0,00\xa0$0,00\xa0$'])
    pages.team.table_pagination.check_text('1 пользователь')


@allure.title("Check filter by active")
def test_filter_by_active(page: Page, pages: Pages,
                          steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Команда")
    pages.team.filter_by_status_ru.click()
    pages.team.status_active.click()
    expect(page.locator("//tr[contains(@class, 'hover-visible-container')]")).to_have_count(2)
    expect(page.locator("//td[contains(@class, 'styles_tableUser')]")).to_have_text(
        ['IEinvated emploee', 'TCtest do not change'])
    expect(page.locator("//td[contains(@class, 'styles_tableStatus')]")).to_have_text(
        ['Активен', 'Активен'])


@allure.title("Check results not found")
def test_results_not_found(page: Page, pages: Pages,
                           steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Команда")
    pages.team.filter_by_status_ru.click()
    pages.team.status_delete.click()
    pages.team.filter_visible.is_on_page(timeout=4000)
    page.get_by_text('Пользователи не найдены').wait_for()
    page.locator("//span[contains(text(),'Попробуйте изменить фильтр или поисковый запрос')]").wait_for()
    assert pages.team.clear_filters_ru.is_visible()


@allure.title("Invite admin")
def test_invite_admin(page: Page, pages: Pages,
                      steps: Steps, playwright, auth_token, api_request_context):
    email = random_string_lowercase(4) + '@gmail.com'
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Команда")
    pages.team.button_invite.click()
    steps.universalSteps.check_second_title(page, "Пригласить пользователя")
    sleep(1)
    pages.team.input_email.click()
    pages.team.input_email.fill(email)
    expect(page.locator('(//*[@data-test-id="radio-button"]//div)[3]')).to_have_text('АдминИмеет полный доступ к управлению деньгами, просмотру баланса, добавления и удаления пользователей, а также управления настройками безопасности')
    expect(page.locator('(//*[@data-test-id="radio-button"]//div)[7]')).to_have_text('СотрудникМожет выпускать карты, видит только свои транзакции')
    assert pages.team.btn_cancel_ru.is_visible()
    pages.team.btn_send_ru.click()
    pages.team.notification_send_letter.is_on_page(timeout=3000)
    sleep(1)
    pages.team.first_row_name_user.click()
    pages.team.modal_name_user.check_text('Новый пользователь')
    pages.team.modal_email_user.check_text(email)
    pages.team.modal_role_user.check_text('Админ')
    pages.team.modal_limit.check_text('Без лимита∞')


@allure.title("Edit role to emploe")
def test_edit_role_to_emploe(page: Page, pages: Pages,
                             steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Команда")
    page.locator("//div[contains(text(), 'test 23434')]").scroll_into_view_if_needed()
    page.locator("//div[contains(text(), 'test 23434')]").click()
    pages.team.menu_button.click()
    pages.team.button_change_role_ru.click()
    pages.team.emploe_role.click()
    pages.team.button_save_ru.click()
    pages.team.modal_role_user.wait_for_text('Сотрудник')
    pages.team.menu_button.click()
    pages.team.button_change_role_ru.click()
    pages.team.admin_role.click()
    pages.team.button_save_ru.click()
    pages.team.modal_role_user.wait_for_text('Админ')


@allure.title("Delete invited admin")
def test_delete_invited_admin(page: Page, pages: Pages,
                              steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Команда")
    pages.team.first_row_name_user.wait_for_text('Новый пользователь', timeout=3000)
    pages.team.first_row_name_user.click()
    pages.team.menu_button.click()
    pages.team.delete_invite.click()
    expect(page.get_by_text("Вы уверены, что хотите удалить это приглашение?")).to_be_visible()
    expect(page.get_by_text(
        "Возможно, пользователь уже получил приглашение, но не сможет создать аккаунт")).to_be_visible()
    pages.team.button_delete.click()
    expect(page.get_by_text("Приглашение удалено")).to_be_visible()


@allure.title("Invite emploe")
def test_invite_emploe(page: Page, pages: Pages,
                       steps: Steps, playwright):
    email = random_string_lowercase(4) + '@gmail.com'
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Команда")
    pages.team.button_invite.click()
    page.get_by_text("Пригласить пользователя").wait_for(timeout=1500)
    sleep(2)
    page.locator('//*[@data-test-id="text-field"]//input[@id="email"]').fill(email)
    pages.team.emploe_role.click()
    pages.team.button_send_invite_ru.click()
    sleep(2)
    pages.team.first_row_name_user.wait_for_text('Новый пользователь')
    pages.team.first_row_name_user.click()
    pages.team.modal_name_user.wait_for_text('Новый пользователь')
    pages.team.modal_email_user.check_text(email)
    pages.team.modal_role_user.check_text('Сотрудник')
    pages.team.modal_limit.check_text('Без лимита∞')


@allure.title("Delete invited emploe")
def test_delete_invited_emploe(page: Page, pages: Pages,
                               steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Команда")
    pages.team.first_row_name_user.wait_for_text('Новый пользователь', timeout=3000)
    pages.team.first_row_name_user.click()
    pages.team.menu_button.click()
    pages.team.delete_invite.click()
    expect(page.get_by_text("Вы уверены, что хотите удалить это приглашение?")).to_be_visible()
    expect(page.get_by_text(
        "Возможно, пользователь уже получил приглашение, но не сможет создать аккаунт")).to_be_visible()
    pages.team.button_delete.click()
    expect(page.get_by_text("Приглашение удалено")).to_be_visible()


@allure.title("Invite admin with wrong email")
def test_invite_admin_with_wrong_email(page: Page, pages: Pages,
                                       steps: Steps, playwright):
    email = random_string(8)
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Команда")
    pages.team.button_invite.click()
    steps.universalSteps.check_second_title(page, "Пригласить пользователя")
    pages.team.input_email.fill(email)
    pages.team.button_send_invite_ru.click()
    expect(page.locator("//span[contains(text(), 'Неверный email адрес')]")).to_be_visible()


@allure.title("Check limit amount error")
def test_check_limit_amount_error(page: Page, pages: Pages,
                                  steps: Steps, playwright):
    email = random_string_lowercase(8) + '@gmail.com'
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Команда")
    pages.team.button_invite.click()
    steps.universalSteps.check_second_title(page, "Пригласить пользователя")
    pages.team.input_email.fill(email)
    pages.team.limit_card.click()
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")
    pages.team.input_limit_amount.click()
    pages.team.input_limit_amount.fill(random_string(6))
    pages.team.button_send_invite_ru.click()
    assert page.get_by_text("Укажите целое значение, без точек и запятых").is_visible()


@allure.title("Check limit amount errors")
def test_check_limit_amount_errors(page: Page, pages: Pages,
                                   steps: Steps, playwright):
    email = random_string_lowercase(8) + '@gmail.com'
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Команда")
    pages.team.button_invite.click()
    steps.universalSteps.check_second_title(page, "Пригласить пользователя")
    pages.team.input_email.fill(email)
    pages.team.limit_card.click()
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")
    pages.team.input_limit_amount.click()
    pages.team.input_limit_amount.fill(-455)
    pages.team.button_send_invite_ru.click()
    assert page.get_by_text("Укажите целое значение, без точек и запятых").is_visible()


@allure.title("Invite admin with limit")
def test_invite_admin_with_limit(page: Page, pages: Pages,
                                 steps: Steps, playwright, auth_token, api_request_context):
    email = random_string_lowercase(8) + '@gmail.com'
    amount = 2
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Команда")
    pages.team.button_invite.click()
    steps.universalSteps.check_second_title(page, "Пригласить пользователя")
    sleep(2)
    pages.team.input_email.fill(email)
    pages.team.limit_card.click()
    pages.team.limit_daily_ru.wait_for_text('День')
    pages.team.limit_daily_ru.click()
    pages.team.input_limit_amount.click()
    pages.team.input_limit_amount.fill(amount)
    pages.team.button_send_invite_ru.click()
    sleep(2)
    pages.team.first_row_name_user.click()
    pages.team.modal_name_user.check_text('Новый пользователь')
    pages.team.modal_email_user.check_text(email)
    pages.team.modal_limit.check_text('День2,00 $')


@allure.title("Invite emploe with limit")
def test_invite_emploe_with_limit(page: Page, pages: Pages,
                                  steps: Steps, playwright, auth_token, api_request_context):
    email = random_string_lowercase(8) + '@gmail.com'
    amount = 50
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_RU.login, USER_RU.password, "Команда")
    pages.team.button_invite.click()
    steps.universalSteps.check_second_title(page, "Пригласить пользователя")
    sleep(1.5)
    pages.team.input_email.fill(email)
    pages.team.emploe_role.click()
    pages.team.limit_card.click()
    pages.team.limit_monthly_ru.click()
    pages.team.input_limit_amount.click()
    pages.team.input_limit_amount.fill(amount)
    pages.team.button_send_invite_ru.click()
    pages.team.button_send_invite_ru.is_not_on_page(timeout=3500)
    pages.team.notification_send_letter.is_not_on_page(timeout=3000)
    sleep(3)
    pages.team.first_row_name_user.click()
    pages.team.modal_name_user.check_text('Новый пользователь')
    pages.team.modal_email_user.check_text(email)
    pages.team.modal_limit.wait_for_text('Месяц0,00\xa0$ / 50,00\xa0$')


@allure.title("Sort by default and new user")
def test_sort_by_default_and_new_user(page: Page, pages: Pages,
                                      steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Команда")
    steps.teamSteps.check_sort_by_new_to_old_user(page)
    pages.team.title_table_user.click()
    pages.team.first_new_sort_ru.is_on_page(timeout=2000)
    sleep(1)
    pages.team.title_table_user.click()
    pages.team.first_old_sort_ru.is_on_page(timeout=2000)
    sleep(1)
    steps.teamSteps.check_sort_by_new_to_old_user(page)


@allure.title("Sort by spend")
def test_sort_by_spend(page: Page, pages: Pages,
                       steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Команда")
    steps.teamSteps.check_sort_by_new_to_old_user(page)
    pages.team.title_table_spend.click()
    pages.team.ascending_sort_ru.is_on_page(timeout=2000)
    steps.teamSteps.check_sort_from_old_to_new_user(page)
    pages.team.title_table_spend.click()
    pages.team.descending_sort_ru.is_on_page(timeout=2000)
    steps.teamSteps.check_sort_by_new_to_old_user(page)


@allure.title("Sort by decline rate")
def test_sort_by_decline_rate(page: Page, pages: Pages,
                              steps: Steps, playwright):
    page.goto(AUTH_URL_ALL_TIME_TEAM)
    steps.auth.authorize_in_test(page, USER_DATA_RU.login, USER_DATA_RU.password, "Команда")
    steps.teamSteps.check_sort_by_new_to_old_user(page)
    pages.team.title_table_decline_rate.click()
    pages.team.ascending_sort_ru.is_on_page(timeout=2000)
    pages.team.title_table_decline_rate.click()
    pages.team.descending_sort_ru.is_on_page(timeout=2000)
    sleep(2)
    steps.teamSteps.check_sort_by_decline_rate(page)
