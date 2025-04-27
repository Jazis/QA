class AuthLocators:
    login = "(//div[contains(@class, 'styles_wrapper')])[1]/input"
    pass_word = "//input[@id='password']"
    login_button = "//button[contains(@class, 'button styles_container')]"
    title = "//h1[contains(text(), 'Добро пожаловать в dev host')]"

    header_logo = "//*[contains(@class, 'styles_headerLogo')]"
    footer_text = "//*[contains(@class, 'styles_footer')]/p[contains(text(), '© 2025 dev host')]"

    base_elements = {
        "en-GB": {
            "no_account": "Don't have an account?",
            "request_invite": "Request invite",
            "forgot_password": "Forgot your password?",
            "header_text": "Cash",
            "privacy_policy": "Privacy policy",
            "terms_of_use": "Terms of Service",
        },
        "uk-UA": {
            "no_account": "Ви не маєте облікового запису?",
            "request_invite": "Отримати запрошення",
            "forgot_password": "Забули пароль?",
            "header_text": "Картки",
            "privacy_policy": "Політика конфіденційності",
            "terms_of_use": "Умови використання",
        },
        "ru-RU": {
            "no_account": "У вас нет аккаунта?",
            "request_invite": "Получить инвайт",
            "forgot_password": "Забыли пароль?",
            "header_text": "Счет",
            "privacy_policy": "Политика конфиденциальности",
            "terms_of_use": "Условия использования",
        }
    }
