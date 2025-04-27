class Dashboard:
    filter_status = "(//button//span[contains(text(), 'Status')])[1]"
    filter_by_owner = "//button//span[contains(text(), 'Owner type')]"
    title_table_company = "//th[contains(text(), 'Company')]"
    title_table_status = "//th[contains(text(), 'Status')]"
    title_table_issue = "//span[contains(text(), 'Issued cards')]"
    title_table_trans = "(//span[contains(text(), 'Transactions')])[2]"
    title_table_avg = "//span[contains(text(), 'Avg. transaction')]"
    title_table_decline = "//span[contains(text(), 'Decline rate')]"
    title_table_international = "//span[contains(text(), 'International')]"
    title_table_money_in = "//span[contains(text(), 'Deposits')]"
    title_table_spend = "//span[contains(text(), 'Spend')]"
    total_row_table = "//tr[contains(@class, 'styles_summary')]"
    title_invite_company = "//h2[contains(text(), 'Invite a company')]"
    input_name_company = "//input[@id='name']"
    input_emai_company = "//input[@id='email']"
    button_invite_company = "//button//span[contains(text(),'Send invite')]"
    input_company_type = "(//div[@data-test-id= 'select']//div)[7]"
    first_name_company_at_table = "(//div[contains(@class, 'display_flex align-items_center gap_3')])[1]"


    ##### Accounts
    button_move_money = "//button//span[contains(text(), 'Move money')]"
    client_balance = "//span[contains(text(), 'Client balance')]"
    credit_balance = "//span[contains(text(), 'Credit balance')]"
    master_balance = "//span[contains(text(), 'Master balance')]"
    clients = "//div[contains(text(), 'Clients')]"
    operational = "//div[contains(text(), 'Operational')]"
    user_name = "//span[contains(text(), 'Joe Dow')]"
    filter_company = "(//button//span[contains(text(), 'Company')])[1]"
    move_money_from = "(//*[@data-test-id='modal-body']//*[contains(@class, 'truncate')])[1]"
    move_money_to = '(//*[@id="to_account"]//following-sibling::div)[1]'
    btn_next = "//*[@data-test-id='button']//span[contains(text(), 'Next')]"
    btn_transfer = '//*[@data-test-id="button"]//span[contains(text(), "Transfer")]'


###########Companies
    menu_modal_company = '//*[@data-test-id="modal-header"]//button[@data-test-id="button"][1]'
    first_row_name_company = "(//tr//*[contains(@class, 'display_flex align-items_center gap_2')])[1]"
    status_modal_company = '//*[@data-test-id="modal-dialog"]//*[@data-test-id="badge"]//span'
    decline_fe_modal_company = '//*[@data-test-id="modal-dialog"]//*[contains(@class, "styles_tile")]//span[contains(text(), "Decline fee")]'
    icon_cards_count_edit = '(//*[@data-test-id="modal-dialog"]//*[@data-slot="icon"])[3]'
    icon_critical_limit_edit = '(//*[@data-test-id="modal-dialog"]//*[@data-slot="icon"])[4]'
    sum_critical_limit = "(//span[contains(@class, 'styles_containerHeadingLg')])[2]"
    count_limit_cards = "(//span[contains(@class, 'styles_containerHeadingLg')])[1]"
    btn_choose_plan = '//*[@data-test-id="select"]'
    btn_change_plan = "//button//span[contains(text(), 'Change plan')]"
    btn_next_at_modal = "//button//span[contains(text(), 'Next')]"
    btn_save_modal = '//button//span[contains(text(), "Save")]'
    input_critical_balance = '//input[@id="critical_balance"]'
    input_cards_quantity_limit = '//input[@id="cards_quantity_limit"]'
    toast_natural_number = "//span[contains(text(), 'Must be a natural number')]"

    ###Transactions
    spend = "//div[contains(text(), 'Spend')]"
    title_trans = "//h1[contains(text(), 'Transactions')]"
    pre_auth = "//div[contains(text(), 'Pre-auth')]"
    filter_by_user = "//*[@data-test-id = 'button-group']//span[contains(text(), 'User')]"
    filter_by_card = "(//span[contains(text(), 'Card')])[2]"
    button_next = "//*[@data-test-id = 'table-pagination']//button[2]"
    pending_modal = "//*[@data-test-id = 'modal-header']//span[contains(text(), 'Pending')]"
    settled_modal = "//*[@data-test-id = 'modal-header']//span[contains(text(), 'Settled')]"
    reversed_modal = "//*[@data-test-id = 'modal-header']//span[contains(text(), 'Reversed')]"
    reversed_in_modal = "//*[@data-test-id = 'modal-body']//span[contains(text(), 'Reversed')]"
    refund_modal = "//*[@data-test-id = 'modal-header']//span[contains(text(), 'Refund')]"
    pending_in_modal = "//*[@data-test-id = 'modal-body']//span[contains(text(), 'Pending')]"
    settled_in_modal = "//*[@data-test-id = 'modal-body']//span[contains(text(), 'Settled')]"
    refund_in_modal = "//*[@data-test-id = 'modal-body']//span[contains(text(), 'Refund')]"
    facebook_modal = "//*[@data-test-id = 'modal-body']//div[contains(text(), 'FACEBK ADS')]"
    gb_country_modal = "//*[@data-test-id = 'modal-body']//div[contains(text(), 'GB')]"
    mcc_modal = "//*[@data-test-id = 'modal-body']//div[contains(text(), '7311')]"
    reversed_sum = "//p[contains(@class, 'text-decoration_line-through')]"
    declined_modal = "//*[@data-test-id = 'modal-header']//span[contains(text(), 'Declined')]"
    total_pending_sum = "//*[@data-test-id = 'info-popover-content']//span[contains(text(), 'Pending')]/following-sibling::span"
    total_settled_sum = "//*[@data-test-id = 'info-popover-content']//span[contains(text(), 'Settled')]/following-sibling::span"
    total_refund_sum = "//*[@data-test-id = 'info-popover-content']//span[contains(text(), 'Refund')]/following-sibling::span"
    total_reversed_sum = "//*[@data-test-id = 'info-popover-content']//span[contains(text(), 'Reversed')]/following-sibling::span"
    total_decline_fee = "//*[@data-test-id = 'info-popover-content']//span[contains(text(), 'Decline fee')]/following-sibling::span"
    total_spend_icon = "//th//*[@data-test-id = 'info-popover-activator']/div/div"
    total_spend_sum_trans = "(//*[@data-test-id = 'info-popover-activator']//span/span)[1]"
    total_cross_border_fee = "//*[@data-test-id = 'info-popover-content']//*[contains(text(), 'Cross-border fee')]/following-sibling::span"
    total_fx_fee = "//*[@data-test-id = 'info-popover-content']//*[contains(text(), 'FX fee')]/following-sibling::span"
    popper_info = "//*[@data-test-id = 'info-popover-content']"
    status_trans_first_row = "(//*[@data-test-id = 'badge'])[1]"

    ####Cards
    title_cards = "//h1[contains(text(), 'Cards')]"
    filter_account = "//*[@data-test-id = 'button-group']//span[contains(text(), 'Account')]"
    filter_network = "//*[@data-test-id = 'button-group']//span[contains(text(), 'Network')]"
    filter_limit = "//*[@data-test-id = 'button-group']//span[contains(text(), 'Limit')]"
    filter_provider = "//*[@data-test-id = 'button-group']//span[contains(text(), 'Provider')]"
    total_spend_sum = "//span[contains(text(), '$1,656.14')]"
    modal_info_in_row = "//*[@data-test-id = 'info-popover-content']"

    ##########Users
    title_users = "//h1[contains(text(), 'Users')]"
    filter_by_role = "//button//span[contains(text(), 'Role')]"

    #####Subscriptions
    filter_plan = "//*[@data-test-id = 'filters-filters']//*[contains(text(), 'Plan')]"
    filter_by_status = "//*[@data-test-id = 'filters-filters']//*[contains(text(), 'Status')]"
    filter_by_company = "//*[@data-test-id = 'filters-filters']//*[contains(text(), 'Company')]"
    button_charge_first = "(//*[@data-test-id='button']/span[contains(text(), 'Charge')])[1]"
    button_chancel_first = "(//*[@data-test-id='button']/span[contains(text(), 'Cancel')])[1]"
    checkbox_private = '//*[@data-test-id="checkbox"]//span[contains(text(), "Private")]'
    checkbox_paid = '//*[@data-test-id="checkbox"]//span[contains(text(), "Paid")]'
    table_pagination = '//*[@data-test-id="table-pagination"]'




    ################Cash
    tab_all_transactions = '//*[@data-test-id="tab"]//div[contains(text(), "All transactions")]'
    tab_deposits = '//*[@data-test-id="tab"]//div[contains(text(), "Deposits")]'
    tab_withdrawals = '//*[@data-test-id="tab"]//div[contains(text(), "Withdrawals")]'
    tab_subscriptions = '//*[@data-test-id="tab"]//div[contains(text(), "Subscriptions")]'
    tab_referrals = '//*[@data-test-id="tab"]//div[contains(text(), "Referrals")]'
    input_search = '(//*[@data-test-id="text-field"]//input)[1]'
    filter_button_company = "//*[@data-test-id='button']/span[contains(text(), 'Company')]"
    filter_button_tx_type = "//*[@data-test-id='button']/span[contains(text(), 'Tx Type')]"
    title_datetime = '//*[@data-test-id="sortable-heading"]//span[contains(text(), "Datetime")]'
    title_amount = '//*[@data-test-id="sortable-heading"]//span[contains(text(), "Amount")]'
    title_tx_type = "//th[contains(text(), 'Tx Type')]"
    title_company = "//th[contains(text(), 'Company')]"
    filter_tag_deposit = "//*[@data-test-id='tag']//div[contains(text(), 'Deposit')]"
    filter_tag_withdrawal = "//*[@data-test-id='tag']//div[contains(text(), 'Withdrawal')]"
    filter_tag_subscription = "//*[@data-test-id='tag']//div[contains(text(), 'Subscription')]"
    filter_tag_referral = "//*[@data-test-id='tag']//div[contains(text(), 'Referral')]"
    move_money_row_to = "(//*[contains(@class, 'display_flex flex-direction_column')])[3]"
    input_amount = '//input[@id="amount"]'
    move_money_btn_next = '//button[@data-test-id="button"]/span[contains(text(), "Next")]'
    move_money_btn_transfer = '//span[contains(text(), "Transfer")]'
    move_money_btn_go_dash = '//span[contains(text(), "Go to Dashboard")]'
    move_money_type_operation = '(//*[contains(@class, "display_flex flex-direction_column")])[1]'
    move_money_subscription_title = '(//*[@data-test-id="modal-body"])//span[contains(text(), "Subscription")]'
    move_money_modal_from = "(//div[contains(@class, 'display_flex flex-direction_column gap_1 flex_1')])[1]"
    move_money_modal_to = "(//div[contains(@class, 'display_flex flex-direction_column gap_1 flex_1')])[2]"
    move_money_title_made_transfer = "//*[contains(text(), 'You’ve made a transfer')]"
    tx_type_first_row = "(//*[contains(@class, 'display_flex align-items_center gap_3')])[1]"
    company_name_first_row = "(//*[contains(@class, 'display_flex align-items_center gap_3')])[2]"
    amount_first_row = '(//*[contains(@class, "styles_tableAmount")])[1]'
    date_at_table = "//tr[contains(@class, 'styles_summary')]/th[1]"
    total_sum_at_table = "//tr[contains(@class, 'styles_summary')]/th[3]"
    modal_tab_qolo = "//*[@data-test-id='modal-body']//*[@data-test-id='tab']//*[contains(text(), 'Qolo')]"
    modal_tab_connexpay = "//*[@data-test-id='modal-body']//*[@data-test-id='tab']//*[contains(text(), 'ConnexPay')]"




############Wallets
    tab_clients = '//*[@data-test-id="tab"]//div[contains(text(), "Clients")]'
    tab_operational = '//*[@data-test-id="tab"]//div[contains(text(), "Operational")]'
    input_company = '//*[@placeholder="Address, company or ID"]'
    filter_blockchain = "//button//span[contains(text(), 'Blockchain')]"
    filter_token = "//button//span[contains(text(), 'Token')]"
    tag = '(//*[@data-test-id="tag"])[1]'
    tag_2 = '(//*[@data-test-id="tag"])[2]'
    tag_3 = '(//*[@data-test-id="tag"])[3]'
    tag_close = '//*[@data-test-id="tag"]/button'
    info_popover = "//div[@data-test-id = 'info-popover-content']"


###########Top-up
    checkbox_choose = '//*[@data-test-id="table-header"]//*[@data-test-id="checkbox"]'
    new_batch_modal = '(//*[@data-test-id="button"]//span[contains(text(), "Batch")])[2]'
    tab_connex_pay = "//*[@data-test-id='tab']//div[contains(text(), 'ConnexPay')]"
    tab_processed = "//*[@data-test-id='tab']//div[contains(text(), 'Processed')]"
    tab_all = "//*[@data-test-id='tab']//div[contains(text(), 'All')]"
    tab_usdc_erc = "//*[@data-test-id='tab']//div[contains(text(), 'USDC ERC')]"
    tab_usdt_erc = "//*[@data-test-id='tab']//div[contains(text(), 'USDT ERC')]"
    tab_qolo = "//*[@data-test-id='tab']//div[contains(text(), 'Qolo')]"
    no_results = '//span[contains(text(), "No results found")]'
    btn_clear_filters = '//span[contains(text(), "Clear filters")]'
    text_change_filter = '//span[contains(text(), "Try changing the filters or search term")]'



