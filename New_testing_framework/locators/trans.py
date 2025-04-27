class Transactions:
    btn_export = "//button[@data-test-id = 'modal-activator']"
    filter_trans = "//div[@data-test-id = 'text-field']//input"
    btn_status_ru = "(//div[@data-test-id = 'filters-filters']//*[@data-test-id='button'])[1]"
    btn_user_ru = "(//div[@data-test-id = 'filters-filters']//*[@data-test-id='button'])[2]"
    btn_card_ru = "(//div[@data-test-id = 'filters-filters']//*[@data-test-id='button'])[3]"
    btn_date_and_time_ru = "//span[contains(text(), 'Дата и время')]"
    all_spend_sum = "(//div[@data-test-id = 'info-popover-activator'])[1]//span//span"
    btn_next_page = "(//*[@data-test-id = 'table-pagination']//button[@data-test-id = 'button'])[2]"
    first_row = "(//tr[contains(@class, 'hover-visible-container')])[1]"
    five_row = "(//tr[contains(@class, 'hover-visible-container')])[5]"
    eight_row = "(//tr[contains(@class, 'hover-visible-container')])[8]"
    twelve_row = "(//tr[contains(@class, 'hover-visible-container')])[12]"
    seventeen_row = "(//tr[contains(@class, 'hover-visible-container')])[17]"
    sixteen_row = "(//tr[contains(@class, 'hover-visible-container')])[16]"
    twenty_one_row = "(//tr[contains(@class, 'hover-visible-container')])[21]"
    twenty_two_row = "(//tr[contains(@class, 'hover-visible-container')])[22]"
    settled_card_transaction = "//*[@data-test-id = 'modal-header']//span[contains(text(),'Settled')]"
    refund_card_transaction = "//div[@data-test-id = 'modal-dialog']//div[@data-test-id = 'badge']//span[contains(text(),'Refund')]"
    reversed_card_transaction = "//h2//*[@data-test-id = 'badge']//span[contains(text(),'Reversed')]"
    declined_card_transaction = "//div[@data-test-id = 'modal-dialog']//div[@data-test-id = 'badge']//span[contains(text(),'Declined')]"
    pending_card_transaction = "//div[@data-test-id = 'modal-dialog']//div[@data-test-id = 'badge']//span[contains(text(),'Pending')]"
    sum_trans_on_card_pending = "//div[@data-test-id = 'modal-body']//p"
    sum_trans_on_card_settled = "//*[@data-test-id = 'modal-body']//p"
    number_card_on_card = "(//div[@data-test-id = 'modal-body']//div[contains(@class, 'display_flex flex-direction_column gap_1')])[1]"
    ads_trans_on_card = "(//div[@data-test-id = 'modal-body']//div[contains(@class, 'display_flex flex-direction_column gap_1')])[3]"
    btn_close_card = "//div[contains(@class, 'styles_titleEndContent')]"
    filter_settled = "//*[@data-test-id = 'checkbox']//span[contains(text(), 'Settled')]"
    filter_refund = "//*[@data-test-id = 'checkbox']//span[contains(text(), 'Refund')]"
    filter_pending = "//*[@data-test-id = 'checkbox']//span[contains(text(), 'Pending')]"
    filter_reversed = "//*[@data-test-id = 'checkbox']//span[contains(text(), 'Reversed')]"
    filter_declined = "//*[@data-test-id = 'checkbox']//span[contains(text(), 'Declined')]"
    selected_filters = "//*[@data-test-id = 'tag']"
    filter_by_card_ru = "//button[@data-test-id = 'button']//span[contains(text(), 'Карта')]"
    id_trans = "(//div[contains(@class, 'display_flex flex-direction_column gap_3')])[5]"
    popper_activator = "//th[contains(@class, 'text-align_end')]//*[@data-test-id = 'floating-activator']"
    description_modal_trans = "(//div[@data-test-id = 'modal-body']//div[contains(@class, 'display_flex flex-direction_column gap_3')])[1]"
    country_modal_trans = "(//div[@data-test-id = 'modal-body']//div[contains(@class, 'display_flex flex-direction_column gap_3')])[2]"
    currency_modal_trans = "(//div[@data-test-id = 'modal-body']//div[contains(@class, 'display_flex flex-direction_column gap_3')])[3]"
    mcc_modal_trans = "(//div[@data-test-id = 'modal-body']//div[contains(@class, 'display_flex flex-direction_column gap_3')])[4]"
    transaction_id_modal_trans = "(//div[@data-test-id = 'modal-body']//div[contains(@class, 'display_flex flex-direction_column gap_3')])[5]"
    input_at_filter = "(//div[@data-test-id = 'text-field']//input)[2]"
    checkbox_filter_first = "(//*[@data-test-id='checkbox'])[1]"
    checkbox_filter_second = "(//*[@data-test-id='checkbox'])[2]"
    sum_trans_first_row = '(//td//*[@data-test-id="floating-activator"])[2]/following-sibling::span'
    sum_decline_first_row = '(//tr)[3]//*[@data-test-id="info-popover-activator"]//span/span'
    sum_with_fee_decline_first_row = '((//tr)[3]//*[@data-test-id="info-popover-activator"]//span)[1]'
    sum_trans_first_row_spend_trans = '(//td//*[@data-test-id="floating-activator"])[2]/following-sibling::span'
    first_refund_in_table = '(//*[@data-test-id="badge"]/span[contains(text(), "Refund")])[1]'
    first_settled_in_table = '(//*[@data-test-id="badge"]/span[contains(text(), "Settled")])[1]'

    widget_sum_trans = '(//div[contains(@class, "display_flex justify-content_space-between gap_4")]//span)[1]'
    widget_sum_trans_graph = '(//*[@fill="transparent"])[1]'
    widget_sum_spend = '(//div[contains(@class, "display_flex justify-content_space-between gap_4")]//span)[2]'
    widget_sum_spend_graph = '(//*[@fill="transparent"])[2]'
    widget_count_trans_declined = '(//div[contains(@class, "display_flex justify-content_space-between gap_4")]//span)[3]'
    widget_count_trans_declined_graph = '(//*[@fill="transparent"])[3]'
    widget_sum_trans_declined = '(//div[contains(@class, "display_flex justify-content_space-between gap_4")]//span)[4]'
    widget_sum_trans_declined_graph = '(//*[@fill="transparent"])[4]'
    widget_trans_decline_rate = '(//div[contains(@class, "display_flex justify-content_space-between gap_4")]//span)[5]'
    widget_trans_decline_rate_graph = '(//*[@fill="transparent"])[5]'
    widget_title_decline_rate = "//div[contains(text(), 'Decline rate')]"




