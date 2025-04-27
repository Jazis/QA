from pages.base_page import BasePage
from widgets.button import Button


class NavigationPage(BasePage):
    def __init__(self) -> None:
        super().__init__()

        self.navigation_cards_ru = Button(selector=self._locators.navigation.navigation_cards_ru)
        self.navigation_trans_ru = Button(selector=self._locators.navigation.navigation_trans_ru)
        self.navigation_trans_uk = Button(selector=self._locators.navigation.navigation_trans_uk)
        self.navigation_balance_ru = Button(selector=self._locators.navigation.navigation_balance_ru)
        self.cash_text_sum = Button(selector=self._locators.navigation.cash_text_sum)
        self.navigation_team_ru = Button(selector=self._locators.navigation.navigation_team_ru)
        self.navigation_team_en = Button(selector=self._locators.navigation.navigation_team_en)
        self.settings_user = Button(selector=self._locators.navigation.settings_user)
        self.my_profile = Button(selector=self._locators.navigation.my_profile)
        self.profile_company_ru = Button(selector=self._locators.navigation.profile_company_ru)
        self.referral_company_ru = Button(selector=self._locators.navigation.referral_company_ru)
        self.billing_page_ru = Button(selector=self._locators.navigation.billing_page_ru)
        self.tariff_plans_ru = Button(selector=self._locators.navigation.tariff_plans_ru)
        self.button_bin_ru = Button(selector=self._locators.navigation.button_bin_ru)
        self.button_security_ru = Button(selector=self._locators.navigation.button_security_ru)
        self.name_company = Button(selector=self._locators.navigation.name_company)
        self.name_company_for_employee = Button(selector=self._locators.navigation.name_company_for_employee)
        self.btn_set_up_2fa = Button(selector=self._locators.navigation.btn_set_up_2fa)
        self.btn_chancel_2fa_en = Button(selector=self._locators.navigation.btn_chancel_2fa_en)
        self.btn_verify_en = Button(selector=self._locators.navigation.btn_verify_en)
        self.btn_copy_code = Button(selector=self._locators.navigation.btn_copy_code)
        self.row_name = Button(selector=self._locators.navigation.row_name)
        self.log_out_ru = Button(selector=self._locators.navigation.log_out_ru)
        self.log_out_en = Button(selector=self._locators.navigation.log_out_en)
