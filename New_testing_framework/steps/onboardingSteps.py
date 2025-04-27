import allure
from playwright.sync_api import expect

from steps._base import BaseSteps


class OnboardingSteps(BaseSteps):
    @allure.step('Click btn next')
    def click_next(self):
        self.pages.onboard.button_continue_en.click()

    @allure.step('Click button next ru')
    def click_btn_next_ru(self):
        self.pages.onboard.button_continue_ru.click()

    @allure.step('Click button next uk')
    def click_btn_next_uk(self):
        self.pages.onboard.button_continue_uk.click()

    @allure.step('Check btn disabled')
    def check_btn_disabled(self, page):
        expect(page.locator("//span[contains(text(), 'Next')]")).to_be_disabled()

    @allure.step('Check btn disabled ru')
    def check_btn_disabled_ru(self, page):
        expect(page.locator("//span[contains(text(), 'Продолжить')]")).to_be_disabled()

    @allure.step('Check btn disabled uk')
    def check_btn_disabled_uk(self, page):
        expect(page.locator("//span[contains(text(), 'Далі')]")).to_be_disabled()

    @allure.step('Click checkbox Facebook')
    def click_facebook(self):
        self.pages.onboard.facebook_check_box.click()

    @allure.step('Click checkbox Google')
    def click_google(self):
        self.pages.onboard.google_check_box.click()

    @allure.step('Click checkbox Tik Tok')
    def click_tik_tok(self):
        self.pages.onboard.tik_tok_check_box.click()

    @allure.step('Click checkbox Microsoft')
    def click_microsoft(self):
        self.pages.onboard.microsoft_check_box.click()

    @allure.step('Click checkbox another')
    def click_another(self):
        self.pages.onboard.another_check_box_ru.click()

    @allure.step('Click checkbox Taboola')
    def click_taboola(self):
        self.pages.onboard.taboola_check_box.click()

    @allure.step('Check title en monthly spend')
    def check_title_en(self):
        assert self.pages.onboard.title_spend.get_text(), "What's the monthly spend?"

    @allure.step('Check title monthly spend ru')
    def check_title_ru(self):
        assert self.pages.onboard.title_spend.get_text(), "Какой ваш ежемесячный спенд?"

    @allure.step('Title first page ru')
    def check_first_page_ru(self):
        assert self.pages.onboard.title_spend.get_text(), "Какие рекламные сети вы оплачиваете?"

    @allure.step('Title first page uk')
    def check_first_page_uk(self):
        assert self.pages.onboard.title_spend.get_text(), "За які рекламні мережі ви платите?"

    @allure.step('Title first page en')
    def check_first_page_en(self):
        assert self.pages.onboard.title_spend.get_text(), "Which advertising networks do you pay for?"

    @allure.step('Title first page uk')
    def check_title_uk(self):
        assert self.pages.onboard.title_spend.get_text(), "Які щомісячні витрати?"

    @allure.step('Title solo or team ru')
    def check_title_solo_or_team_ru(self):
        assert self.pages.onboard.title_spend.get_text(), "Вы работаете в команде или соло?"

    @allure.step('Title solo or team uk')
    def check_title_solo_or_team_uk(self):
        assert self.pages.onboard.title_spend.get_text(), "Ви команда чи соло?"

    @allure.step('Title solo or team en')
    def check_title_solo_or_team_en(self):
        assert self.pages.onboard.title_spend.get_text(), ("Are you a team or solo?")

    @allure.step('Click button team en')
    def click_button_team_en(self):
        self.pages.onboard.button_team_en.click()

    @allure.step('Title leave lead')
    def check_title_leave_lead_uk(self):
        assert self.pages.onboard.title_spend.get_text(), "Залишити заявку"

    @allure.step('Title create company uk')
    def check_title_create_company_uk(self):
        assert self.pages.onboard.title_spend.get_text(), "Створіть свій обліковий запис"

    @allure.step('Click btn over 100000 en')
    def click_btn_over_100000(self):
        self.pages.onboard.money_spend_check_box_en.click()

    @allure.step('Click btn 50-100 000')
    def click_btn_50_100(self):
        self.pages.onboard.money_spend_check_50_100.click()

    @allure.step('Click btn more 100 000 ru')
    def click_btn_more_100_ru(self):
        self.pages.onboard.money_spend_check_box_ru.click()

    @allure.step('Click btn 50-100 000')
    def click_btn_50_100_en(self):
        self.pages.onboard.money_spend_check_50_100_en.click()

    @allure.step('Click btn create company ')
    def click_btn_confirm_create_uk(self):
        self.pages.onboard.button_confirm_create_company_uk.click()

    @allure.step('Check title create company')
    def check_title_create_company(self):
        self.pages.onboard.title_create_company_en.is_visible()

    @allure.step('Fill first name')
    def fill_first_name(self, text=None):
        self.pages.onboard.first_name.fill(text)

    @allure.step('Fill last name')
    def fill_last_name(self, text=None):
        self.pages.onboard.last_name.fill(text)

    @allure.step('Fill email')
    def fill_email(self, text=None):
        self.pages.onboard.email.fill(text)

    @allure.step('Fill email login')
    def fill_email_login(self, text=None):
        self.pages.onboard.email_login.fill(text)

    @allure.step('Fill telegram')
    def fill_telegram(self, text=None):
        self.pages.onboard.telegram.fill(text)

    @allure.step('Fill company name')
    def fill_company_name(self, text=None):
        self.pages.onboard.input_company_name.fill(text)

    @allure.step('Fill password')
    def fill_password(self, text=None):
        self.pages.onboard.password.fill(text)

    @allure.step('Fill password confirm')
    def fill_password_confirm(self, text=None):
        self.pages.onboard.password_confirm.fill(text)

    @allure.step('Click btn confirm create company en')
    def click_company_create(self):
        self.pages.onboard.button_confirm_create_company_en.click()

    @allure.step('Title check email en')
    def title_check_email_en(self):
        self.pages.onboard.title_check_email_en.is_visible()

    @allure.step('Title check email ru')
    def title_check_email_ru(self):
        self.pages.onboard.title_check_email_ru.is_visible()

    @allure.step('Title check email uk')
    def title_check_email_uk(self):
        self.pages.onboard.title_check_email_uk.is_visible()

    @allure.step('Title check email address en')
    def title_check_email_address_en(self):
        self.pages.onboard.title_email_address_en.is_visible()

    @allure.step('Title check email address ru')
    def title_check_email_address_ru(self):
        self.pages.onboard.title_email_address_ru.is_visible()

    @allure.step('Title check email address uk')
    def title_check_email_address_uk(self):
        self.pages.onboard.title_email_address_uk.is_visible()

    @allure.step('Button code visible en')
    def button_code_en(self):
        self.pages.onboard.input_code.is_visible()

    @allure.step('Button check name ru')
    def button_create_company_ru(self):
        self.pages.onboard.button_confirm_create_company_ru.is_visible()

    @allure.step('Button click ru')
    def click_button_create_company_ru(self):
        self.pages.onboard.button_confirm_create_company_ru.click()

    @allure.step('Check btn code confirm ru')
    def btn_code_confirm_ru(self):
        self.pages.onboard.btn_code_confirm_ru.is_visible()

    @allure.step('Check btn code confirm')
    def send_code_confirm(self, text):
        self.pages.onboard.code_confirm_input.fill(text)

    @allure.step('Check btn code confirm uk')
    def btn_code_confirm_uk(self):
        self.pages.onboard.btn_code_confirm_uk.is_visible()

    @allure.step('Check btn code confirm en')
    def btn_code_confirm_en(self):
        self.pages.onboard.btn_code_confirm_en.is_visible()

    @allure.step('Title lead ru')
    def title_lead_ru(self):
        self.pages.onboard.title_lead_ru.is_visible()

    @allure.step('Title lead uk')
    def title_lead_uk(self):
        self.pages.onboard.title_lead_uk.is_visible()

    @allure.step('Title lead en')
    def title_lead_en(self):
        self.pages.onboard.title_lead_en.is_visible()

    @allure.step('Click create lead ru')
    def click_create_lead_ru(self):
        self.pages.onboard.button_lead_ru.click()

    @allure.step('Click create lead uk')
    def click_create_lead_uk(self):
        self.pages.onboard.button_title_lead_uk.click()

    @allure.step('Click create lead en')
    def click_create_lead_en(self):
        self.pages.onboard.button_title_lead_en.click()

    @allure.step('Slider visible')
    def slider_visible(self):
        self.pages.onboard.row_slider.is_on_page(timeout=3000)
        self.pages.onboard.row_slider.is_visible()

    @allure.step('Check policy')
    def policy_visible_ru(self):
        self.pages.onboard.privacy_policy_ru.is_visible()

    @allure.step('Check policy')
    def policy_visible_en(self):
        self.pages.onboard.privacy_policy_en.is_visible()

    @allure.step('Check terms of use')
    def terms_of_use_visible_ru(self):
        self.pages.onboard.terms_of_use_ru.is_visible()

    @allure.step('Check terms of use')
    def terms_of_use_visible_en(self):
        self.pages.onboard.terms_of_use_en.is_visible()

    @allure.step('Check button login')
    def check_btn_login_ru(self):
        self.pages.onboard.btn_enter_ru.is_visible()

    @allure.step('Check button login')
    def check_btn_login_en(self):
        self.pages.onboard.btn_enter_en.is_visible()

    @allure.step('Click button login')
    def click_btn_login_ru(self):
        self.pages.onboard.btn_enter_ru.click()

    @allure.step('Click button login')
    def click_btn_enter_login_en(self):
        self.pages.onboard.btn_enter_login_en.click()

    @allure.step('Click button login')
    def click_btn_enter_login_uk(self):
        self.pages.onboard.btn_enter_login_uk.click()

    @allure.step('Check error')
    def check_error_invalid_code(self):
        assert self.pages.onboard.error_invalid_code.get_text(), 'Invalid code'

    @allure.step('Check text agree en')
    def check_text_agree_en(self):
        assert self.pages.onboard.text_agree_terms.get_text(), 'Pressing the button "Create account", you agree with the Terms of Service and that you have read and understood our Privacy Policy'

    @allure.step('Check text agree uk')
    def check_text_agree_uk(self):
        assert self.pages.onboard.text_agree_terms.get_text(), 'Натискаючи кнопку "Створити обліковий запис", ви погоджуєтеся з Умовами надання послуг, а також з тим, що ви прочитали і зрозуміли нашу Політику конфіденційності'

    @allure.step('Check text wait list en')
    def check_text_in_wait_list_en(self):
        assert self.pages.onboard.text_wait_list.get_text(), "We are currently working with a limited number of partners — this allows us to create the best service together with experienced teams. As soon as we're ready to expand our circle of partners, we'll let you know immediately! If you have any questions, please contact the manager on Telegram."

    @allure.step('Check text wait list ru')
    def check_text_in_wait_list_ru(self):
        assert self.pages.onboard.text_wait_list.get_text(), 'В настоящее время мы сотрудничаем с ограниченным числом партнеров — это позволяет нам создавать лучший сервис совместно с опытными командами. Как только мы будем готовы расширить круг партнеров, мы незамедлительно сообщим вам об этом! Если у вас возникли вопросы, пожалуйста, свяжитесь с менеджером в Telegram.'

    @allure.step('Check text wait list uk')
    def check_text_in_wait_list_uk(self):
        assert self.pages.onboard.text_wait_list.get_text(), "Наразі ми співпрацюємо з обмеженою кількістю партнерів — це дозволяє нам створювати найкращий сервіс спільно з досвідченими командами. Як тільки ми будемо готові розширити коло партнерів, ми негайно повідомимо вам про це! Якщо у вас виникли запитання, будь ласка, зв'яжіться з менеджером у Telegram."
