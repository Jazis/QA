from pages.base_page import BasePage
from widgets.button import Button
from widgets.input import Input


class OnboardingPage(BasePage):
    def __init__(self) -> None:
        super().__init__()

        self.button_continue_en = Button(selector=self._locators.obdord.button_continue_en)
        self.button_continue_ru = Button(selector=self._locators.obdord.button_continue_ru)
        self.button_continue_uk = Button(selector=self._locators.obdord.button_continue_uk)
        self.facebook_check_box = Button(selector=self._locators.obdord.facebook_check_box)
        self.google_check_box = Button(selector=self._locators.obdord.google_check_box)
        self.tik_tok_check_box = Button(selector=self._locators.obdord.tik_tok_check_box)
        self.microsoft_check_box = Button(selector=self._locators.obdord.microsoft_check_box)
        self.taboola_check_box = Button(selector=self._locators.obdord.taboola_check_box)
        self.another_check_box_ru = Button(selector=self._locators.obdord.another_check_box_ru)
        self.title_spend = Button(selector=self._locators.obdord.title_spend)
        self.button_team_en = Button(selector=self._locators.obdord.button_team_en)
        self.button_team_ru = Button(selector=self._locators.obdord.button_team_ru)
        self.money_spend_check_box_en = Button(selector=self._locators.obdord.money_spend_check_box_en)
        self.money_spend_check_box_ru = Button(selector=self._locators.obdord.money_spend_check_box_ru)
        self.money_spend_check_box_uk = Button(selector=self._locators.obdord.money_spend_check_box_uk)
        self.money_spend_check_50_100 = Button(selector=self._locators.obdord.money_spend_check_50_100)
        self.money_spend_30_50_box = Button(selector=self._locators.obdord.money_spend_30_50_box)
        self.money_spend_check_50_100_en = Button(selector=self._locators.obdord.money_spend_check_50_100_en)
        self.money_spend_under_10k_box_en = Button(selector=self._locators.obdord.money_spend_under_10k_box_en)
        self.checkbox_solo_en = Button(selector=self._locators.obdord.checkbox_solo_en)
        self.title_create_company_en = Button(selector=self._locators.obdord.title_create_company_en)
        self.checkbox_team_uk = Button(selector=self._locators.obdord.checkbox_team_uk)
        self.first_name = Input(selector=self._locators.obdord.first_name)
        self.last_name = Input(selector=self._locators.obdord.last_name)
        self.email = Input(selector=self._locators.obdord.email)
        self.email_login = Input(selector=self._locators.obdord.email_login)
        self.telegram = Input(selector=self._locators.obdord.telegram)
        self.password = Input(selector=self._locators.obdord.password)
        self.password_confirm = Input(selector=self._locators.obdord.password_confirm)
        self.button_confirm_create_company_uk = Button(selector=self._locators.obdord.button_confirm_create_company_uk)
        self.button_confirm_create_company_en = Button(selector=self._locators.obdord.button_confirm_create_company_en)
        self.button_confirm_create_company_ru = Button(selector=self._locators.obdord.button_confirm_create_company_ru)
        self.title_lead_ru = Button(selector=self._locators.obdord.title_lead_ru)
        self.button_lead_ru = Button(selector=self._locators.obdord.button_title_lead_ru)
        self.title_check_email_ru = Button(selector=self._locators.obdord.title_check_email_ru)
        self.title_check_email_en = Button(selector=self._locators.obdord.title_check_email_en)
        self.title_check_email_uk = Button(selector=self._locators.obdord.title_check_email_uk)
        self.title_email_address_ru = Button(selector=self._locators.obdord.title_email_address_ru)
        self.title_email_address_en = Button(selector=self._locators.obdord.title_email_address_en)
        self.title_email_address_uk = Button(selector=self._locators.obdord.title_email_address_uk)
        self.input_code = Button(selector=self._locators.obdord.input_code)
        self.btn_code_confirm_ru = Button(selector=self._locators.obdord.btn_code_confirm_ru)
        self.code_confirm_input = Input(selector=self._locators.obdord.code_confirm_input)
        self.btn_code_confirm_en = Button(selector=self._locators.obdord.btn_code_confirm_en)
        self.btn_code_confirm_uk = Button(selector=self._locators.obdord.btn_code_confirm_uk)
        self.row_slider = Button(selector=self._locators.obdord.row_slider)
        self.privacy_policy_ru = Button(selector=self._locators.obdord.privacy_policy_ru)
        self.terms_of_use_ru = Button(selector=self._locators.obdord.terms_of_use_ru)
        self.terms_of_use_en = Button(selector=self._locators.obdord.terms_of_use_en)
        self.privacy_policy_en = Button(selector=self._locators.obdord.privacy_policy_en)
        self.btn_enter_ru = Button(selector=self._locators.obdord.btn_enter_ru)
        self.btn_enter_en = Button(selector=self._locators.obdord.btn_enter_en)
        self.title_lead_uk = Button(selector=self._locators.obdord.title_lead_uk)
        self.button_title_lead_uk = Button(selector=self._locators.obdord.button_title_lead_uk)
        self.button_title_lead_en = Button(selector=self._locators.obdord.button_title_lead_en)
        self.title_lead_en = Button(selector=self._locators.obdord.title_lead_en)
        self.title_cash_after_login = Button(selector=self._locators.obdord.title_cash_after_login)
        self.btn_enter_login_en = Button(selector=self._locators.obdord.btn_enter_login_en)
        self.btn_enter_login_uk = Button(selector=self._locators.obdord.btn_enter_login_uk)
        self.error_invalid_code = Button(selector=self._locators.obdord.error_invalid_code)
        self.btn_solo = Button(selector=self._locators.obdord.btn_solo)
        self.input_company_name = Input(selector=self._locators.obdord.input_company_name)
        self.text_agree_terms = Button(selector=self._locators.obdord.text_agree_terms)
        self.text_wait_list = Button(selector=self._locators.obdord.text_wait_list)




