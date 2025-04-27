class Cards:
    title_all_cards_ru = '//div[contains(text(), "Все карты")]'
    title_my_cards_ru = '//div[contains(text(), "Мои карты")]'
    filter_name_card = "//div[contains(@class, 'styles_container')]//input"
    status_card_ru = "(//div[@data-test-id = 'filters-filters']//*[@data-test-id='button'])[1]"
    bin_card_filter = "//div[contains(@class, 'styles_container')]//span[contains(text(), 'BIN')]"
    user_card_filter = "//div[contains(@class, 'styles_container')]//span[contains(text(), 'Пользователь')]"
    calendar_button = '//*[@data-test-id="date-picker-with-presets-activator"]'
    calendar_all_time = '(//*[@data-test-id="action"])[8]'
    calendar_button_apply_ru = "//button[contains(@class, 'button' )]//span[contains(text(), 'Применить')]"
    create_card_ru = '//*[contains(text(), "Выпустить карту")]'
    title_table_card_ru = "//span[contains(text(), 'Карта')]"
    title_table_status_ru = '//th[contains(text(), "Статус")]'
    title_table_limit_ru = '//th[contains(text(), "Лимит")]'
    title_table_bin_ru = '//th[contains(text(), "BIN")]'
    title_table_user_ru = '//th[contains(text(), "Пользователь")]'
    title_table_money_ru = '//span[contains(text(), "Затраты")]'
    btn_create_card_uk = '//span[contains(text(), "Випустити картку")]'
    name_create_card_ru = "//div[contains(@class, 'styles_wrapper')]//input[@id= 'name']"
    bin_default_create_card_ru = '//div[contains(text(), "Visa 441112")]'
    no_limit_card_limit = '//*[@id="limit"]'
    limit_card = "(//div[contains(@class, 'display_flex flex-direction_column')])[3]"
    card_limit_disabled = '//div[contains(@class, "styles_wrapperDisabled")]'
    button_create_ru = '//span[text()= "Выпустить"]'
    button_create_uk = '//span[text()= "Випустити"]'
    modal_created_card_name_ru = '//span[contains(text(), "Карта пользователя")]'
    modal_created_card_real_name_ru = '//h2//span[1]'
    modal_created_card_active_ru = "//div[@data-test-id = 'modal-body']//span[contains(text(), 'Active')]"
    modal_created_card_active_uk = "//div[@data-test-id = 'modal-body']//span[contains(text(), 'Active')]"
    card_bin_second = "//*[@name='card_bin']//option[2]"
    card_bin = "(//div[contains(@class, 'styles_endContent')])[1]"
    modal_card_no_limit_ru = "//div[@data-test-id = 'modal-body']//span[contains(text(), 'Без лимита')]"
    modal_card_no_limit_uk = "//div[@data-test-id = 'modal-body']//span[contains(text(), 'Без ліміту')]"
    modal_card_month_limit_ru = "//div[@data-test-id = 'modal-body']//span[contains(text(), 'Месяц')]"
    modal_card_lifetime_limit_ru = "//div[@data-test-id = 'modal-body']//span[contains(text(), 'Лайфтайм')]"
    modal_card_day_limit_ru = "//div[@data-test-id = 'modal-body']//span[contains(text(), 'День')]"
    modal_card_week_limit_ru = "//div[@data-test-id = 'modal-body']//span[contains(text(), 'Неделя')]"
    modal_card_limit_amount_ru = "//span[contains(@class, 'styles_containerBodyMd')][2]"
    input_limit_amount = "//input[@id = 'limit_amount']"
    billing_address_title = "//div[contains(@class, 'display_flex flex-direction_column gap_3')]/span"
    billing_address = "//*[@data-test-id = 'button-link']"
    arrow_next_page_button = "(//*[@data-test-id = 'table-pagination']//*[@data-test-id = 'button'])[2]"
    hidden_card_data = "//*[@data-test-id='button-link']//*[contains(@class, 'styles_wrapper')]"
    not_hidden_card_data = "//*[contains(@class, 'styles_sectionRevealed')]"
    toast_copy_number = "//*[@data-test-id='toast']"
    toast_close_button = "//button[contains(@class, 'styles_dismiss')]"
    button_more_ru = "//button//span[contains(text(), 'Еще')]"
    button_more_uk = "//span[contains(text(), 'Ще')]"
    button_change_name_ru = "//div[contains(text(), 'Изменить название')]"
    button_save_ru = "//span[contains(text(), 'Сохранить')]"
    change_card_limit_ru = "//div[contains(text(), 'Изменить лимит')]"
    change_card_limit_en = "//div[contains(text(), 'Edit limits')]"
    modal_choose_limit = '//*[@data-test-id="select"]/div'
    modal_save_limit_ru = "//span[contains(text(), 'Сохранить лимит')]"
    modal_save_limit_en = "//button[@data-test-id = 'button']//span[contains(text(), 'Save limit')]"
    modal_save_limit_uk = '//*[@data-test-id="button"]//span[contains(text(), "Зберегти ліміт")]'
    close_card_button_ru = "//div[contains(text(), 'Закрыть карту')]"
    title_close_card_ru = "//h2[contains(text(), 'Вы уверены, что хотите закрыть эту карту? Это действие не может быть отменено')]"
    logo_card_modal_close_card = "(//div[@data-test-id = 'modal-body']//img)[1]"
    modal_button_close_card_ru = "//span[contains(text(), 'Да, закрыть')]"
    title_of_closed_card = "//div[@data-test-id = 'modal-body']//div[contains(@class, 'justify-content_space-between gap')]"
    button_freeze_card = "//span[contains(text(), 'Заморозить')]"
    button_unfreeze_card = "//span[contains(text(), 'Разморозить')]"
    button_go_to_transactions = "(//span[contains(text(), 'Транзакции')])[2]"
    number_of_card = "(//*[@data-test-id='button-link'])[1]"
    amount_spend = "(//*[@data-test-id='limit-info']//span[contains(@class, 'styles_container')])[2]"
    card_freeze_user_data = "(//span[contains(text(), 'Frozen')])[1]"
    card_closed_user_data = "(//span[contains(text(), 'Closed')])[1]"
    date_filter_in_title_table = "//tr[contains(@class, 'styles_summary')]//th[1]"
    sum_in_title_table = "//th[contains(@class, 'text-align_end')]"
    first_card_after_search = "(//tr[contains(@class, 'hover-visible-container')])[1]"
    spinner = "//*[@data-test-id = 'spinner']"
    cards_not_found = "//*[@data-test-id = 'state-card']"
    modal_change_card = "//*[@data-test-id = 'action-list']"
    second_card_employee = "(//td[contains(@class, 'styles_tableCard')])[2]"
    modal_button_close_card_uk = "//div[contains(text(), 'Закрити картку')]"
    modal_confirm_close_card_uk = "//span[contains(text(), 'Так, закрити')]"
    title_of_closed_card_uk = "//div[@data-test-id = 'modal-body']//span[contains(text(), 'Closed')]"
    title_table_spend_ru = "//span[contains(text(), 'Затраты')]"
    filter_closed_card_ru = '//*[@data-test-id="checkbox"]//span[contains(text(), "Closed")]'
    filter_bin_553437 = '//*[@data-test-id="checkbox"]//span[contains(text(), "553437")]'
    tag_closed_ru = '//*[@data-test-id="tag"]//div[contains(text(), "Закрыта")]'
    tag_bin_553437 = '//*[@data-test-id="tag"]//div[contains(text(), "553437")]'
    button_clear_filters_ru = '//*[@data-test-id="button"]//span[contains(text(), "Очистить фильтры")]'
    modal_closed_number_card = "//div[@data-test-id = 'modal-body']//*[contains(@class, 'styles_containerHeadingMd')]"
    status_closed = '//*[@data-test-id="checkbox"]//span[contains(text(), "Closed")]'
    status_active = "//*[@data-test-id='checkbox']//span[contains(text(), 'Active')]"
    status_frozen = "//*[@data-test-id='checkbox']//span[contains(text(), 'Frozen')]"
    status_expired = "//*[@data-test-id='checkbox']//span[contains(text(), 'Expired')]"
    modal_title_card = '//*[@data-test-id="card-modal-title-header"]'
    modal_title_owner = '//*[@data-test-id="card-modal-title-subheader"]'
    popover_activator = '//th//*[@data-test-id="info-popover-activator"]'
    popover_activator_icon = '(//th//*[@data-test-id="floating-activator"])[3]'
    modal_title_billing_address_ru = "//span[contains(text(), 'Биллинг адрес')]"
    modal_billing_address = '(//*[@data-test-id="button-link"])[4]'
    toast = '//*[@data-test-id="toast"]'
    modal_close_card = '//span[contains(text(), "Закрыть")]'
    close_modal_card = "//*[contains(@class, 'styles_titleEndContent')]/button"
    first_active_status_at_table = "(//span[contains(text(), 'Active')])[1]"
    right_arrow_first_card = "(//*[@data-test-id='modal']//*[contains(@class, 'display_flex gap_05')]/div)[1]"
    right_arrow_card = "(//*[@data-test-id='modal']//*[contains(@class, 'display_flex gap_05')]/div)[2]"
    left_arrow_card = "(//*[@data-test-id='modal']//*[contains(@class, 'display_flex gap_05')]/div)[1]"
    copy_all = '(//*[@data-test-id="modal"]//*[@data-test-id="button"])[4]'
    modal_pencil_button = '//*[@data-test-id="limit-info"]//*[@data-test-id="button"]'
    modal_card_number = '(//*[@data-test-id="floating-activator"]//*[@data-test-id="button-link"]/span)[1]'
    modal_card_exp = '(//*[@data-test-id="floating-activator"]//*[@data-test-id="button-link"]/span)[2]'
    modal_card_cvc = '(//*[@data-test-id="floating-activator"]//*[@data-test-id="button-link"]/span)[3]'






