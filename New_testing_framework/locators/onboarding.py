class OnboardingLocator:
    button_continue_en = "//span[contains(text(), 'Next')]"
    button_continue_ru = "//span[contains(text(), 'Продолжить')]"
    button_continue_uk = "//span[contains(text(), 'Далі')]"
    facebook_check_box = "//span[contains(text(), 'Facebook Ads')]/ancestor::button//label[@data-test-id = 'checkbox']"
    google_check_box = "//span[contains(text(), 'Google Ads')]/ancestor::button//label[@data-test-id = 'checkbox']"
    tik_tok_check_box = "//span[contains(text(), 'TikTok Ads')]/ancestor::button//label[@data-test-id = 'checkbox']"
    microsoft_check_box = "//span[contains(text(), 'Microsoft Ads')]/ancestor::button//label[@data-test-id = 'checkbox']"
    taboola_check_box = "//span[contains(text(), 'Taboola')]/ancestor::button//label[@data-test-id = 'checkbox']"
    another_check_box_ru = "//span[contains(text(), 'Другое')]/ancestor::button//label[@data-test-id = 'checkbox']"
    title_spend = "//h1"
    button_team_en = "//*[@data-test-id = 'pseudo-button']//span[contains(text(), 'Team')]"
    button_team_ru = "//*[@data-test-id = 'pseudo-button']//span[contains(text(), 'Команда')]"
    error_invalid_code = "//span[contains(text(), 'Invalid code')]"
    money_spend_check_box_ru = "//*[@data-test-id='pseudo-button']//span[contains(text(), 'Более 100 000$')]"
    money_spend_check_box_en = "//*[@data-test-id = 'pseudo-button']//span[contains(text(), 'Over $100,000')]"
    money_spend_30_50_box = "//*[@data-test-id = 'pseudo-button']//span[contains(text(), '$30,000 – $50,000')]"
    money_spend_under_10k_box_en = "//*[@data-test-id = 'pseudo-button']//span[contains(text(), 'Under $10,000')]"
    money_spend_check_box_uk = "//span[contains(text(), 'Понад $100,000')]"
    money_spend_check_50_100 = "//span[contains(text(), '50 000$ – 100 000$')]"
    money_spend_check_50_100_en = "//*[@data-test-id = 'pseudo-button']//span[contains(text(), '$50,000 – $100,000')]"
    btn_solo = "(//*[@data-test-id =  'pseudo-button'])[2]"
    checkbox_team_uk = "//*[@data-test-id = 'pseudo-button']//span[contains(text(), 'Команда')]"
    checkbox_solo_en = "//span[contains(text(), 'solo)]"
    title_create_company_en = '//h1[contains(text(), "Create your account")]'
    first_name = '//input[@id="first_name"]'
    last_name = '//input[@id="last_name"]'
    email = '//input[@id="email"]'
    email_login = '//input[@id="username"]'
    telegram = '//input[@id="telegram"]'
    password = '//input[@id="password"]'
    password_confirm = '//input[@id="confirmPassword"]'
    button_confirm_create_company_uk = "//button//span[contains(text(), 'Створити обліковий запис')]"
    button_confirm_create_company_ru = "//button//span[contains(text(), 'Создать аккаунт')]"
    button_confirm_create_company_en = "//span[contains(text(), 'Create account')]"
    title_lead_ru = "//h1[contains(text(), 'Оставить заявку')]"
    title_lead_uk = "//h1[contains(text(), 'Залишити заявку')]"
    title_lead_en = "//h1[contains(text(), 'Join waitlist')]"
    button_title_lead_ru = "//span[contains(text(), 'Оставить заявку')]"
    button_title_lead_uk = "//span[contains(text(), 'Залишити заявку')]"
    button_title_lead_en = '//button[@data-test-id="button"]'
    title_check_email_ru = "//h1[contains(text(), 'Проверьте свой email')]"
    title_check_email_en = "//h1[contains(text(), 'Check your inbox')]"
    title_check_email_uk = "//h1[contains(text(), 'Перевірте свою поштову скриньку')]"
    title_email_address_ru = "//span[contains(text(), 'Мы отправили временную ссылку для входа на ')]"
    title_email_address_en = "//span[contains(text(), 'We sent a temporary login link to ')]"
    title_email_address_uk = "//span[contains(text(), 'Ми надіслали тимчасове посилання для входу на ')]"
    input_code = '//*[@data-test-id="text-field"]//input'
    btn_code_confirm_ru = "//span[contains(text(), 'Ввести код подтверждения')]"
    code_confirm_input = "//input[@id='code']"
    btn_code_confirm_en = "//span[contains(text(), 'Enter confirmation code')]"
    btn_code_confirm_uk = "//span[contains(text(), 'Введіть код для входу')]"
    row_slider = "//div[@data-test-id = 'progress']"
    privacy_policy_ru = '//*[contains(text(), "Политика конфиденциальности")]'
    privacy_policy_en = '//*[contains(text(), "Privacy policy")]'
    terms_of_use_ru = '//*[contains(text(), "Условия использования")]'
    terms_of_use_en = '//*[contains(text(), "Terms of Service")]'
    btn_enter_ru = '//*[contains(text(), "Войти")]'
    btn_enter_en = '//*[contains(text(), "Login")]'
    btn_enter_login_en = '//button//span[contains(text(), "Log In")]'
    btn_enter_login_uk = '//span[contains(text(), "Увійти")]'
    title_cash_after_login = '//h1'
    input_company_name = '//input[@id="company_name"]'
    text_agree_terms = '(//p)[2]'
    text_wait_list = '//h1/following-sibling::span'

