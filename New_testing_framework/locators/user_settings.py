class UserSettings:
    main_avatar_empty = "(//div[contains(@class, 'avatar styles_container')])[1]"
    profile_avatar_empty = "(//div[@data-test-id = 'avatar'])[1]"
    button_show_password = "//*[@data-test-id = 'modal-dialog']//button[@data-test-id = 'button-link']"
    input_name = '//input[@id="first_name"]'
    input_last_name = '//input[@id="last_name"]'
    button_update = '(//button[@data-test-id="button"])[2]'
    toast_saved_changes = '(//*[@data-test-id="toast"])'
    span_name = "(//*[contains(@class, 'padding-block-end')]//span[contains(@class, 'styles_containerMedium')])[2]"
    title = "//h2"
    add_file = "//*[@data-test-id = 'modal-dialog']//div[contains(@class, 'styles_inner')]"
    button_save = "//*[@data-test-id = 'modal-footer']//*[@data-test-id = 'button'][2]"
    select_timezone = "//*[@data-test-id = 'form']"
    title_change = "//*[@data-test-id = 'modal-dialog']//h2"
    button_add_file_ru = "//span[contains(text(), 'Добавить')]"
    size_files = "(//span[contains(@class, 'styles_containerBodySm')])[3]"
    tariff_name = "//div[contains(@class, 'display_flex justify-content_space-between gap_4')]/span"
    sum_tariff = "(//span[contains(@class, 'styles_containerHeadingXl')])[2]"
    status_active = "(//*[@data-test-id = 'badge'])[2]/span"
    description_tariff = "//div[contains(@class, 'display_flex gap_1')]"
    limits_of_users_ru = "//*[@data-test-id = 'tag']//div[contains(text(), 'Лимиты пользователей')]"
    title_tariff_plans_ru = "//h1[contains(text(), 'Тарифные планы')]"
    title_tariff_plans = "//h1"
    basic_tariff = "//div[contains(@class, 'gap_4 padding-block-end_2')]/span[contains(text(), 'Basic')]"
    sum_first_tariff = "//p[contains(text(), 'Для соло и небольших команд')]/following-sibling::div//span[contains(@class, 'styles_containerHeading3xl')]"
    sum_first_tariff_time = "(//p[contains(text(), 'Для соло и небольших команд')]/following-sibling::div//span[contains(@class, 'styles_containerSubdued')])[1]"
    description_first_tariff = "(//div[contains(@class, 'display_flex flex-direction_column gap_3')])[3]"
    info_in_modal = "(//div[contains(@class, 'padding-inline-end_5')])[2]"
    basic_in_modal_card = "//div[@data-test-id = 'modal-body']//span[contains(text(), 'Basic')]"
    private_in_modal_card = "//div[@data-test-id = 'modal-body']//span[contains(text(), 'Private')]"
    credit_in_modal_card = "//div[@data-test-id = 'modal-body']//span[contains(text(), 'Credit')]"
    prepaid_in_modal_card = "//div[@data-test-id = 'modal-body']//span[contains(text(), 'Prepaid')]"
    number_card_basic_prepaid = "//div[@data-test-id = 'modal-body']//span[contains(text(), '404038')]"
    international_in_modal_card = "//div[@data-test-id = 'modal-body']//span[contains(text(), 'International')]"
    number_card_international = "//div[@data-test-id = 'modal-body']//span[contains(text(), '553437')]"
    title_security_page_ru = "//h2[contains(text(), 'Безопасность')]"
    change_password_ru = "//span[contains(@class, 'styles_text')][contains(text(), 'Сменить пароль')]"
    title_modal_change_ru = "//h2[contains(text(), 'Сменить пароль')]"
    input_old_password = "//input[@id = 'old_password']"
    input_new_password = "//input[@id = 'new_password']"
    input_confirm_password = "//input[@id = 'confirmPassword']"
    title_password_ru = "//span[contains(text(), 'Пароль')]"
    title_session_ru = "//span[contains(text(), 'Сессии')]"
    title_active_session = "//span[contains(@class, ' styles_template')]"
    this_session_ru = "//span[contains(text(), 'Текущая сессия')]"
    language_session_ru = "//span[contains(text(), 'Текущая сессия')]"
    title_referral_ru = "//h1[contains(text(), 'Порекомендовать команду')]"
    button_reset_all_sessions_ru = '//*[@data-test-id="button"]//span[contains(text(), "Сбросить все")]'
    button_reset_current_session_ru = "//span[contains(@class, 'styles_text')][contains(text(), 'Выйти')]"
    user_session = "(//div[contains(@class, 'hover-visible-container')])[2]"
    current_session = "(//div[contains(@class, 'hover-visible-container')])[1]"
    theme = '//*[@data-test-id="select"]'
    theme_light = '//*[@data-index="1"]'
    english_in_modal = '//*[@data-index="0"]/div[contains(@class, "styles_localeCode")]'
    russian_in_modal = '//*[@data-index="1"]/div[contains(@class, "styles_localeCode")]'
    ukr_in_modal = '//*[@data-index="2"]/div[contains(@class, "styles_localeCode")]'
    english_in_row = '//*[@data-index="0"]//div[contains(@class, "styles_container")]'
    russian_in_row = '//*[@data-index="1"]//div[contains(@class, "styles_container")]'
    ukr_in_row = '//*[@data-index="2"]//div[contains(@class, "styles_container")]'
    language_edit = "(//*[@data-test-id='button-link'])[5]"
    title_modal_bin = "//*[@data-test-id = 'modal-dialog']//*[@data-test-id='modal-header']"
    type_modal_bin = "//*[@data-test-id = 'modal-dialog']//*[contains(@class,'display_flex align-items_center gap_2')]"
    number_bin_in_modal = "//*[@data-test-id = 'modal-dialog']//*[contains(@class, 'position_relative display_flex')]"
    img_network_modal_bin = "//*[@data-test-id = 'modal-dialog']//*[contains(@class, 'position_relative display_flex')]//img"
    input_code_2fa = '//*[@data-test-id="modal-body"]//*[@name="totp_code"]'


