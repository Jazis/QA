class CashBalance:
    accessible_balance_ru = "(//span[contains(text(), 'Доступный баланс')])[1]"
    accessible_balance_sum = "(//*[@data-test-id = 'widget'])[1]/span[2]"
    accessible_balance_account_ru = "//span[contains(text(), 'Доступно')]/following-sibling::span"
    balance_hold_ru = "//span[contains(text(), 'В холде')]"
    table_balance = '//*[@data-test-id="table-body"]//td[contains(@class, "styles_tableBalance")]'
    total_balance_ru = '//span[contains(text(),"Общий баланс")]/following-sibling::span'
    balance_hold_sum = "(//*[@data-test-id = 'widget']//span[contains(@class, 'styles_containerSubdued')])[3]"
    balance_hold_account = "//span[contains(text(), 'В холде')]/following-sibling::span"
    alert_title = "(//*[@data-test-id='alert'])[2]//span[1]"
    alert_text = "(//*[@data-test-id='alert'])[2]//span[2]"
    alert_title_with_trial = "(//*[@data-test-id='alert'])[3]//span[1]"
    alert_text_with_trial = "(//*[@data-test-id='alert'])[3]//span[2]"
    calendar_for_schedule = "//*[@tabindex='0']//div[contains(@class, 'styles_content')]"
    button_back_to_cash = '//h1/ancestor::button/*[@data-slot="icon"]'
    icon_go_to_account = '(//tr)[2]'
    total_popover = '(//*[@data-test-id="info-popover-activator"]//*[@data-test-id="floating-activator"])[1]/following-sibling::span/span'
    total_popover_icon_modal = "(//th[contains(@class, 'text-align_end')]//*[@data-test-id='floating-activator'])[2]"
    total_popover_icon = '//th[contains(@class, "text-align_end")]//*[@data-test-id="floating-activator"]'
    row_slider = "//div[@data-test-id = 'progress']"
    balance_in_total_popover_ru = '//*[contains(text(), "Итоговый баланс")]/following-sibling::span'
    row_pending_transactions = '(//*[@data-test-id="button-link"])[2]//span'
    total_sum_at_pending_trans_modal = '(//*[@data-test-id="modal-body"]//*[@data-test-id="info-popover-activator"]//span/span)[1]'
    date_first_pending_at_modal = '(//*[@data-test-id="date-popover"])[1]'
    sum_first_pending_at_modal = '(//*[@data-test-id="modal-body"]//*[contains(@class, "display_flex align-items_center justify-content_flex-end gap_2")]//span/span)[2]'
    button_close_modal_pending = '//*[@data-test-id="modal-header"]//button[@type="button"]'
    beg_balance_popover_ru = '//span[contains(text(), "Стартовый баланс")]/following-sibling::span'
    money_in_popover_ru = "//span[contains(text(), 'Поступления')]/following-sibling::span"
    money_out_popover_ru = "//span[contains(text(), 'Расходы')]/following-sibling::span"
    crypto_deposit_ru = "//span[contains(text(), 'Крипто депозит')]/following-sibling::span"
    crypto_fee_ru = "//span[contains(text(), 'Комиссия за депозит')]/following-sibling::span"
    card_spend_ru = "//span[contains(text(), 'Оплата по картам')]/following-sibling::span"
    card_spend_en = "//span[contains(text(), 'Settled')]/following-sibling::span"
    settled_fee_ru = "//span[contains(text(), 'Конвертация')]/following-sibling::span"
    cross_border_fee_settled_ru = "//span[contains(text(), 'Междунар. комиссия')]/following-sibling::span"
    decline_fee_ru = "//span[contains(text(), 'Комиссия за деклайн')]/following-sibling::span"
    refund_ru = "//span[contains(text(), 'Возврат по картам')]/following-sibling::span"
    refund_fee_ru = "//span[contains(text(), 'Возврат междунар. комиссии')]/following-sibling::span"
    end_balance_ru = "//span[contains(text(), 'Итоговый баланс')]/following-sibling::span"
    filter_deposit_ru = "//span[contains(text(), 'Крипто депозит')]"
    filter_deposit_fee_ru = "//span[contains(text(), 'Комиссия за депозит')]"
    filter_card_settled_ru = "//span[contains(text(), 'Оплата по картам')]"
    filter_card_declined_ru = "//span[contains(text(), 'Комиссия за деклайн')]"
    filter_card_refund_ru = "//span[contains(text(), 'Возврат по картам')]"
    filter_type_ru = '//*[@data-test-id="button"]//span[contains(text(), "Тип")]'
    user_at_modal = "(//td[contains(@class, 'styles_tableUser')]//*[@class='truncate'])[1]"  #first row
    card_at_modal = "(//td[contains(@class, 'styles_tableCard')]//*[@class='truncate'])[1]"  #first row
    amount_at_modal = "(//*[@role='dialog']//td[contains(@class, 'styles_tableAmount')])[1]" #first row
    status_at_modal = "(//td[contains(@class, 'styles_tableStatus')]//*[@data-test-id='badge'])[1]"
    popover_at_modal = '(//*[@role="dialog"]//*[@data-test-id="info-popover-activator"]/div/div)[1]'