import allure
from playwright.sync_api import expect

from steps._base import BaseSteps


class TeamSteps(BaseSteps):
    @allure.step('Check sort rows on team page')
    def check_sort_by_new_to_old_user(self, page):
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[1]")).to_have_text(
            "Новый пользователь")
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[2]")).to_have_text(
            "Новый пользователь")
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[3]")).to_have_text(
            "Новый пользователь")
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[4]")).to_have_text(
            "Новый пользователь")
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[5]")).to_have_text(
            "IEinvated emploee")
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[6]")).to_have_text(
            "TCtest do not change")

    @allure.step('Check sort rows on team page')
    def check_sort_from_old_to_new_user(self, page):
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[1]")).to_have_text(
            "TCtest do not change")
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[2]")).to_have_text(
            "IEinvated emploee")
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[3]")).to_have_text(
            "Новый пользователь")
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[4]")).to_have_text(
            "Новый пользователь")
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[5]")).to_have_text(
            "Новый пользователь")
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[6]")).to_have_text(
            "Новый пользователь")

    @allure.step('Check sort rows on team page')
    def check_sort_by_decline_rate(self, page):
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[1]")).to_have_text(
            "Новый пользователь")
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[2]")).to_have_text(
            "IEinvated emploee")
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[3]")).to_have_text(
            "Новый пользователь")
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[4]")).to_have_text(
            "Новый пользователь")
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[5]")).to_have_text(
            "Новый пользователь")
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[6]")).to_have_text(
            "TCtest do not change")

    @allure.step('Check permissions employee')
    def check_permissions_employee(self, page):
        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[1]")).to_have_text(
            'Редактировать все карты команды')
        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[1]/*[1]")).to_have_css("color", "rgb(230, 72, 61)")

        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[2]")).to_have_text('Просмотр страницы Карты, просмотр и редактирование своих карт')
        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[2]/*[1]")).to_have_css("color", "rgb(88, 182, 62)")

        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[3]")).to_have_text('Просмотр всех карт команды')
        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[3]/*[1]")).to_have_css("color", "rgb(230, 72, 61)")

        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[4]")).to_have_text('Просмотр баланса')
        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[4]/*[1]")).to_have_css("color", "rgb(230, 72, 61)")

        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[5]")).to_have_text('Просмотр страницы Счет')
        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[5]/*[1]")).to_have_css("color", "rgb(230, 72, 61)")

        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[6]")).to_have_text('Удаление пользователей')
        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[6]/*[1]")).to_have_css("color", "rgb(230, 72, 61)")

        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[7]")).to_have_text('Редактирование пользователей')
        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[7]/*[1]")).to_have_css("color", "rgb(230, 72, 61)")

        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[8]")).to_have_text('Приглашение пользователей')
        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[8]/*[1]")).to_have_css("color", "rgb(230, 72, 61)")

        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[9]")).to_have_text('Просмотр страницы Команда')
        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[9]/*[1]")).to_have_css("color", "rgb(230, 72, 61)")

        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[10]")).to_have_text('Экспорт транзакций')
        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[10]/*[1]")).to_have_css("color", "rgb(88, 182, 62)")

        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[11]")).to_have_text('Просмотр только своих транзакций')
        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[11]/*[1]")).to_have_css("color", "rgb(88, 182, 62)")

        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[12]")).to_have_text('Просмотр всех транзакций команды')
        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[12]/*[1]")).to_have_css("color", "rgb(230, 72, 61)")

        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[13]")).to_have_text('Доступ к реферальной программе')
        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[13]/*[1]")).to_have_css("color", "rgb(230, 72, 61)")

        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[14]")).to_have_text('Company settings pages view')
        expect(page.locator("(//div[contains(@class, 'display_flex gap_3')])[14]/*[1]")).to_have_css("color", "rgb(230, 72, 61)")

    @allure.step('Check permissions admin')
    def check_permissions_admin(self, page):
        expect(page.locator(
            "(//*[contains(@class, 'display_flex gap')]//*[contains(@class, 'flex-shrink')])[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex gap_3')])[1]")).to_have_text(
            'Редактировать все карты команды')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex gap')]//*[contains(@class, 'flex-shrink')])[2]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex gap_3')])[2]")).to_have_text(
            'Просмотр страницы Карты, просмотр и редактирование своих карт')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex gap')]//*[contains(@class, 'flex-shrink')])[3]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex gap_3')])[3]")).to_have_text(
            'Просмотр всех карт команды')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex gap')]//*[contains(@class, 'flex-shrink')])[4]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex gap_3')])[4]")).to_have_text(
            'Просмотр баланса')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex gap')]//*[contains(@class, 'flex-shrink')])[5]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex gap_3')])[5]")).to_have_text(
            'Просмотр страницы Счет')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex gap')]//*[contains(@class, 'flex-shrink')])[6]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex gap_3')])[6]")).to_have_text(
            'Удаление пользователей')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex gap')]//*[contains(@class, 'flex-shrink')])[7]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex gap_3')])[7]")).to_have_text(
            'Редактирование пользователей')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex gap')]//*[contains(@class, 'flex-shrink')])[8]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex gap_3')])[8]")).to_have_text(
            'Приглашение пользователей')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex gap')]//*[contains(@class, 'flex-shrink')])[9]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex gap_3')])[9]")).to_have_text(
            'Просмотр страницы Команда')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex gap')]//*[contains(@class, 'flex-shrink')])[10]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex gap_3')])[10]")).to_have_text(
            'Экспорт транзакций')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex gap')]//*[contains(@class, 'flex-shrink')])[11]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex gap_3')])[11]")).to_have_text(
            'Просмотр только своих транзакций')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex gap')]//*[contains(@class, 'flex-shrink')])[12]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex gap_3')])[12]")).to_have_text(
            'Просмотр всех транзакций команды')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex gap')]//*[contains(@class, 'flex-shrink')])[13]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex gap_3')])[13]")).to_have_text(
            'Доступ к реферальной программе')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex gap')]//*[contains(@class, 'flex-shrink')])[14]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//*[contains(@class, 'display_flex gap_3')])[14]")).to_have_text(
            'Company settings pages view')


    def check_all_users(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableUser')]")).to_have_text(
            ['Новый пользователь', 'Новый пользователь', 'Новый пользователь', 'Новый пользователь',
             'IEinvated emploee',
             'TCtest do not change'])
        expect(page.locator("//td[contains(@class, 'styles_tableStatus')]")).to_have_text(
            ['Приглашен', 'Приглашен', 'Приглашен',
             'Приглашен', 'Активен', 'Активен'])
        expect(page.locator("//td[contains(@class, 'styles_tableRole')]")).to_have_text(
            ['Админ', 'Сотрудник', 'Сотрудник', 'Админ', 'Сотрудник', 'Админ'])
        expect(page.locator("//td[contains(@class, 'styles_tableLimit')]")).to_have_text(
            ['Месяц250,00\xa0$', 'Лайфтайм200,00\xa0$', 'Неделя100,00\xa0$', 'Без лимита∞', 'Без лимита∞', 'Без лимита∞'])
        expect(page.locator("//td[contains(@class, 'styles_tableDeclineRate')]")).to_have_text(
            ['0,0\xa0%', '0,0\xa0%', '0,0\xa0%', '0,0\xa0%', '0,0\xa0%', '5,6\xa0%'])
        expect(page.locator("//td[contains(@class, 'styles_tableSpend')]")).to_have_text(
            ['0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '13,00\xa0$', '249,55\xa0$'])

    def check_modal_in_spend(self, page):
        expect(page.locator("//*[@data-test-id = 'info-popover-content']")).to_have_text(
            [ 'Settled203,00\xa0$Pending90,00\xa0$Reversed18,00\xa0$Refund47,00\xa0$Междунар. комиссия1,46\xa0$Комиссия за деклайн1,00\xa0$Конвертация1,09\xa0$'])

    def check_text_bin_modal(self, page, m, text):
        expect(page.locator(f"(//*[@data-test-id]//div[contains(@class, 'display_flex flex-direction_column gap_3')])" + f"[{m}]")).to_have_text(text)

    def check_features_in_plans(self, page, m, n):
        expect(page.locator(
            "(//table[contains(@class, 'styles_table')]/tbody//tr" + f"[{m}]//*[@data-slot='icon'])" + f"[{n}]")).to_be_visible()