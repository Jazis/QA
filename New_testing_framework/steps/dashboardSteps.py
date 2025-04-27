
from playwright.sync_api import expect
from steps._base import BaseSteps


class DashboardSteps(BaseSteps):
    def check_total_rows_companies(self, page):
        page.locator("//span[contains(text(), '($529.96)')]").hover()
        page.locator("(//td//div[@data-test-id = 'floating-activator'])[1]").hover()
        expect(page.locator("//*[@data-test-id = 'info-popover-content']")).to_have_text(
            ['Settled$355.00Pending$214.00Reversed$61.00Refund$48.00Cross-border fee$4.52Decline fee$1.50FX fee$2.94'])
        page.locator("//span[contains(text(), '($282.96)')]").hover()
        page.locator("(//td//div[@data-test-id = 'floating-activator'])[2]").hover()
        expect(page.locator("//*[@data-test-id = 'info-popover-content']")).to_have_text(['Settled$278.00Cross-border fee$2.73FX fee$2.23'])

        page.locator("//span[contains(text(), '($224.04)')]").hover()
        page.locator("(//td//div[@data-test-id = 'floating-activator'])[3]").hover()
        expect(page.locator("//*[@data-test-id = 'info-popover-content']")).to_have_text(['Settled$22.00Pending$214.00Refund$16.00Cross-border fee$3.11FX fee$0.93'])

        page.locator("//span[contains(text(), '($194.36)')]").hover()
        page.locator("(//td//div[@data-test-id = 'floating-activator'])[4]").hover()
        expect(page.locator("//*[@data-test-id = 'info-popover-content']")).to_have_text(
            ['Settled$155.00Pending$84.00Reversed$61.00Refund$48.00Cross-border fee$1.72Decline fee$1.50FX fee$0.14'])

        page.locator("//span[contains(text(), '($170.36)')]").hover()
        page.locator("(//td//div[@data-test-id = 'floating-activator'])[5]").hover()
        expect(page.locator("//*[@data-test-id = 'info-popover-content']")).to_have_text(['Pending$168.00Cross-border fee$1.43FX fee$0.93'])

        page.locator("//span[contains(text(), '($152.50)')]").hover()
        page.locator("(//td//div[@data-test-id = 'floating-activator'])[6]").hover()
        expect(page.locator("//*[@data-test-id = 'info-popover-content']")).to_have_text(['Settled$115.00Pending$84.00Reversed$61.00Refund$48.00Decline fee$1.50'])

    def check_each_row_table(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[1]")).to_have_text(
            "168 – red companyActiveBasic013$82.5723.1%$39.0060.0%$0($529.96)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[2]")).to_have_text(
            "171 – ruby roseActivePro02$141.480.0%$0.0050.0%$0($282.96)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[3]")).to_have_text(
            "172 – golden companyActiveBasic04$60.010.0%$0.0075.0%$0($224.04)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[4]")).to_have_text(
            "167 – white companyActiveBasic013$34.6323.1%$39.0060.0%$0($194.36)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[5]")).to_have_text(
            "169 – green companyActiveBasic02$85.180.0%$0.0050.0%$0($170.36)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[6]")).to_have_text(
            "173 – black companyActivePrivate113$28.4323.1%$39.0060.0%$0($152.50)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[7]")).to_have_text(
            "170 – grey companyActiveBasic02$50.980.0%$0.0050.0%$0($101.96)")

    def check_sort_by_issue_first(self, page):
        expect(page.locator("(//tr//*[contains(@class, 'display_flex align-items_center gap_2')])[1]")).to_have_text(
            "173 – black company")
        expect(page.locator("(//td[contains(@class, 'text-align_end')])[1]")).to_have_text('1')


    def check_sort_by_issue_second(self, page):
        expect(page.locator("(//td[contains(@class, 'text-align_end')])[1]")).to_have_text('0')


    def check_total_spend(self, page):
        expect(page.locator("//*[@data-test-id = 'info-popover-content']")).to_have_text(['Settled$980.00Pending$810.00Reversed$183.00Refund$160.00''Cross-border fee$14.47Decline fee$4.50FX fee$7.17'])

    def check_each_row_table_accounts(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[1]")).to_have_text(
            "168 – red company1026728Active$2,434.70$0.00$0.00($529.96)$1,904.74")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[2]")).to_have_text(
            "171 – ruby rose1029366Active$750.94$0.00$0.00($282.96)$467.98")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[3]")).to_have_text(
            "172 – golden company1062075Active$2,250.94$0.00$0.00($224.04)$2,026.90")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[4]")).to_have_text(
            "167 – white company1047836Active$810.32$0.00$0.00($194.36)$615.96")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[5]")).to_have_text(
            "169 – green company1057766Active$1,937.52$0.00$0.00($170.36)$1,767.16")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[6]")).to_have_text(
            "173 – black company1025391Active$2,251.15$0.00$0.00($152.50)$2,098.65")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[7]")).to_have_text(
            "170 – grey company1041407Active$2,560.96$0.00$0.00($101.96)$2,459.00")

    def check_each_row_table_accounts_operational(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[1]")).to_have_text(
            "Revenue2000019Active$2,172.30$0.00$0.00$2,172.30")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[2]")).to_have_text(
            "Revenue2000019Active$2,172.30$0.00$0.00$2,172.30")

    def check_each_row_table_trans(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[1]")).to_have_text(
            "18 May, 07:22FACEBK ADSPending172 – golden companyGBUSD404038••8921 card$46.96")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[4]")).to_have_text(
            "18 May, 07:21FACEBK ADSRefund172 – golden companyUSUSD556150••0007 golden$16.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[5]")).to_have_text(
            "18 May, 07:21FACEBK ADSSettled172 – golden companyGBUSD556150••0007 golden$22.72")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[13]")).to_have_text(
            "18 May, 07:19FACEBK ADSDeclined168 – red companyGBUSD531993••9147 red_card$0.50 + $11.50")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[16]")).to_have_text(
            "18 May, 07:18FACEBK ADSReversed168 – red companyGBUSD531993••9147 red_card$14.64")

    def check_companies_names(self, page):
        expect(page.locator("//td//*[@data-test-id = 'avatar']/following-sibling::span")).to_have_text(['172 – golden company', '172 – golden company', '172 – golden company', '172 – golden company', '172 – golden company', '171 – ruby rose', '171 – ruby rose', '170 – grey company', '170 – grey company', '169 – green company', '169 – green company', '168 – red company', '168 – red company', '168 – red company', '168 – red company', '168 – red company', '168 – red company', '168 – red company', '168 – red company', '168 – red company', '168 – red company', '168 – red company', '168 – red company', '168 – red company', '168 – red company'])

    def check_companies_name_second_page(self, page):
        expect(page.locator(
            "//td//*[@data-test-id = 'avatar']/following-sibling::span")).to_have_text(['168 – red company', '168 – red company', '168 – red company', '167 – white company', '167 – white company', '167 – white company', '167 – white company', '167 – white company', '167 – white company', '167 – white company', '167 – white company', '167 – white company', '167 – white company', '167 – white company', '167 – white company', '167 – white company', '167 – white company', '167 – white company', '167 – white company', '167 – white company', '173 – black company', '173 – black company', '173 – black company', '173 – black company', '173 – black company'])

    def check_companies_name_fird_page(self, page):
        expect(page.locator(
            "//td//*[@data-test-id = 'avatar']/following-sibling::span")).to_have_text(['173 – black company', '173 – black company', '173 – black company', '173 – black company', '173 – black company', '173 – black company', '173 – black company', '173 – black company', '173 – black company', '173 – black company', '173 – black company', '173 – black company'])

    def check_all_cards_first_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCard')]//*[contains(@class, 'truncate')]")).to_have_text(
            ['••8921 card', '••8921 card', '••8921 card', '••0007 golden', '••0007 golden', '••7574 ruby card lifetime', '••3108 rose card limit weekly', '••0914 grey', '••0914 grey', '••4179 card_3', '••4179 card_3', '••9147 red_card', '••9147 red_card', '••9147 red_card', '••9147 red_card', '••9147 red_card', '••9147 red_card', '••9147 red_card', '••9147 red_card', '••9147 red_card', '••9147 red_card', '••9147 red_card', '••9147 red_card', '••9147 red_card', '••9147 red_card'])

    def check_all_cards_second_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCard')]//*[contains(@class, 'truncate')]")).to_have_text(
            ['••9147 red_card', '••9147 red_card', '••9147 red_card', '••9933 employee', '••9933 employee',
             '••9933 employee', '••9933 employee', '••9933 employee', '••9933 employee', '••9933 employee',
             '••9933 employee', '••9933 employee', '••9933 employee', '••9933 employee', '••9933 employee',
             '••9933 employee', '••9933 employee', '••9933 employee', '••9933 employee', '••9933 employee',
             '••6326 white', '••6326 white', '••6326 white', '••6326 white', '••6326 white'])

    def check_companies_cards_fird_page(self, page):
        expect(page.locator(
            "//td[contains(@class, 'styles_tableCard')]//*[contains(@class, 'truncate')]")).to_have_text(
            ['••6326 white', '••6326 white', '••6326 white', '••6326 white', '••6326 white', '••6326 white',
             '••6326 white', '••6326 white', '••6326 white', '••6326 white', '••6326 white', '••6326 white'])

    def check_all_sums_first_page(self, page):
        expect(page.locator(
            "//*[@data-test-id = 'info-popover-activator']//span/span")).to_have_text(
            ['$1,656.14', '$46.96', '$95.36', '$75.00', '$16.00', '$22.72', '$227.96', '$55.00', '$55.00', '$46.96',
             '$95.36', '$75.00', '$15.65', '$11.50', '$14.50', '$14.50', '$14.64', '$36.20', '$12.00', '$10.60',
             '$22.94', '$16.00', '$22.72', '$227.96', '$55.00', '$55.00'])

    def check_all_sums_second_page(self, page):
        expect(page.locator(
            "//*[@data-test-id = 'info-popover-activator']//span/span")).to_have_text(
            ['$1,656.14', '$1,656.14', '$46.96', '$95.36', '$75.00', '$15.65', '$11.50', '$14.50', '$14.50',
             '$14.64', '$36.20', '$12.00', '$10.60', '$22.94', '$16.00', '$22.72', '$23.96', '$55.00', '$55.00',
             '$46.96', '$13.76', '$25.00', '$15.00', '$11.50', '$14.50', '$14.50', '$14.00'])

    def check_all_sums_fird_page(self, page):
        expect(page.locator(
            "//td//*[@data-test-id = 'info-popover-activator']//span/span")).to_have_text(
            ['$35.00', '$12.00', '$10.00', '$22.00', '$16.00', '$22.00', '$23.00', '$15.00', '$55.00', '$46.00',
             '$13.00', '$25.00'])

    def check_cards_each_row_table(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[1]")).to_have_text(
            "••9147 red_cardYyxhInActivered company168 – red companyConnexPay531993Monthly$0.00 / $1,000.00$529.96")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[2]")).to_have_text(
            "••7574 ruby card lifetimeGAwnHCActive5465ft 57567thfg171 – ruby roseConnexPay433451Lifetime$96.76 / $500,000.00$227.96")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[3]")).to_have_text(
            "••8921 cardYBjKDRActivegolden company172 – golden companyConnexPay433451Monthly$0.00 / $1,000.00$217.32")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[5]")).to_have_text(
            "••4179 card_3IpkImTActive46ryty fyhtf169 – green companyConnexPay433451Weekly$0.00 / $600.00$170.36")


    def check_companies_names_on_cards(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[5])[1]")).to_have_text(
            '168 – red company')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[5])[2]")).to_have_text('171 – ruby rose')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[5])[3]")).to_have_text(
            '172 – golden company')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[5])[4]")).to_have_text(
            '167 – white company')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[5])[5]")).to_have_text(
            '169 – green company')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[5])[6]")).to_have_text(
            '173 – black company')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[5])[7]")).to_have_text(
            '170 – grey company')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[5])[8]")).to_have_text('171 – ruby rose')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[5])[9]")).to_have_text(
            '172 – golden company')

    def check_cards_on_cards_page(self, page):
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[1]")).to_have_text('••9147 red_card')
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[2]")).to_have_text('••7574 ruby card lifetime')
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[3]")).to_have_text('••8921 card')
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[4]")).to_have_text('••9933 employee')
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[5]")).to_have_text('••4179 card_3')
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[6]")).to_have_text('••6326 white')
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[7]")).to_have_text('••0914 grey')
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[8]")).to_have_text('••3108 rose card limit weekly')
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[9]")).to_have_text('••0007 golden')

    def check_status_on_cards_page(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[3])[1]")).to_have_text('Active')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[3])[2]")).to_have_text('Active')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[3])[3]")).to_have_text('Active')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[3])[4]")).to_have_text('Active')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[3])[5]")).to_have_text('Active')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[3])[6]")).to_have_text('Active')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[3])[7]")).to_have_text('Active')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[3])[8]")).to_have_text('Active')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[3])[9]")).to_have_text('Active')

    def check_bins_on_cards_page(self, page):
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[3])[1]")).to_have_text(
            '531993')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[3])[2]")).to_have_text(
            '433451')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[3])[3]")).to_have_text(
            '433451')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[3])[4]")).to_have_text(
            '556150')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[3])[5]")).to_have_text(
            '433451')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[3])[6]")).to_have_text(
            '553437')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[3])[7]")).to_have_text(
            '489683000')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[3])[8]")).to_have_text(
            '433451')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[3])[9]")).to_have_text(
            '556150')

    def check_providers_on_cards_page(self, page):
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[2])[1]")).to_have_text(
            'ConnexPay')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[2])[2]")).to_have_text(
            'ConnexPay')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[2])[3]")).to_have_text(
            'ConnexPay')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[2])[4]")).to_have_text(
            'ConnexPay')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[2])[5]")).to_have_text(
            'ConnexPay')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[2])[6]")).to_have_text(
            'ConnexPay')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[2])[7]")).to_have_text(
            'ConnexPay')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')]/following-sibling::td[2])[8]")).to_have_text(
            'ConnexPay')


    def check_limits_on_cards_page(self, page):
        expect(page.locator("(//td[contains(@class, 'styles_tableLimit')])[1]")).to_have_text(
            "Monthly$900.00 / $1,000.00")
        expect(page.locator("(//td[contains(@class, 'styles_tableLimit')])[2]")).to_have_text("No limit∞")
        expect(page.locator("(//td[contains(@class, 'styles_tableLimit')])[3]")).to_have_text(
            "Monthly$0.00 / $1,000.00")
        expect(page.locator("(//td[contains(@class, 'styles_tableLimit')])[4]")).to_have_text("No limit∞")
        expect(page.locator("(//td[contains(@class, 'styles_tableLimit')])[5]")).to_have_text(
            "Weekly$0.00 / $600.00")
        expect(page.locator("(//td[contains(@class, 'styles_tableLimit')])[6]")).to_have_text(
            "Monthly$0.00 / $3,000.00")
        expect(page.locator("(//td[contains(@class, 'styles_tableLimit')])[7]")).to_have_text("No limit∞")
        expect(page.locator("(//td[contains(@class, 'styles_tableLimit')])[8]")).to_have_text(
            "Weekly$0.00 / $5,000.00")
        expect(page.locator("(//td[contains(@class, 'styles_tableLimit')])[9]")).to_have_text("No limit∞")

    def check_spend_on_cards_page(self, page):
        expect(page.locator("//td[contains(@class, 'text-align_end')]")).to_have_text(
            ['$529.96', '$227.96', '$217.32', '$194.36', '$170.36', '$152.50', '$101.96', '$55.00', '$6.72', '$0.00',
             '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00', '$0.00',
             '$0.00', '$0.00', '$0.00'])

    def check_each_row_users(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[1]")).to_have_text(
            "RCred companyAdminredcompany@mail.ru298ActiveNo limit∞168 – red company$529.96$82.5723.1%$39.0060.0%")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[2]")).to_have_text(
            "RRruby roseAdminrubyrose@mail.ru301ActiveNo limit∞171 – ruby rose$282.96$141.480.0%$0.0050.0%")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[3]")).to_have_text(
            "GCgolden companyAdmingoldencompany@mail.ru302ActiveNo limit∞172 – golden company$224.04$60.010.0%$0.0075.0%")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[4]")).to_have_text(
            "TEtest EmployeeEmployeesomeemail@google.com297ActiveNo limit∞167 – white company$194.36$34.6323.1%$39.0060.0%")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[6]")).to_have_text(
            "BCblack companyAdminblackcompany@mail.ru303ActiveNo limit∞173 – black company$152.50$28.4323.1%$39.0060.0%")


    def check_all_names_users(self, page):
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[1]")).to_have_text('RCred company')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[2]")).to_have_text('RRruby rose')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[3]")).to_have_text('GCgolden company')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[4]")).to_have_text('TEtest Employee')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[5]")).to_have_text('GCgreen company')
        expect(page.locator("(//td[contains(@class, 'styles_tableUser')])[6]")).to_have_text('BCblack company')


    def check_all_emails_users(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[3])[1]")).to_have_text(
            'redcompany@mail.ru')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[3])[2]")).to_have_text(
            'rubyrose@mail.ru')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[3])[3]")).to_have_text(
            'goldencompany@mail.ru')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[3])[4]")).to_have_text(
            'someemail@google.com')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[3])[5]")).to_have_text(
            'greencompany@google.com')

    def check_all_roles_users(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[2])[1]")).to_have_text('Admin')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[2])[2]")).to_have_text('Admin')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[2])[3]")).to_have_text('Admin')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[2])[4]")).to_have_text('Employee')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[2])[5]")).to_have_text('Admin')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[2])[6]")).to_have_text('Admin')

    def check_all_statuses_users(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[5])[1]")).to_have_text('Active')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[5])[2]")).to_have_text('Active')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[5])[3]")).to_have_text('Active')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[5])[4]")).to_have_text('Active')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[5])[5]")).to_have_text('Active')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[5])[5]")).to_have_text('Active')

    def check_all_limits_users(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[6])[1]")).to_have_text('No limit∞')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[6])[2]")).to_have_text('No limit∞')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[6])[3]")).to_have_text('No limit∞')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[6])[4]")).to_have_text('No limit∞')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[6])[6]")).to_have_text('No limit∞')

    def check_all_companies_users(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[7])[1]")).to_have_text(
            '168 – red company')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[7])[2]")).to_have_text('171 – ruby rose')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[7])[3]")).to_have_text(
            '172 – golden company')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[7])[4]")).to_have_text(
            '167 – white company')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[7])[5]")).to_have_text(
            '169 – green company')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[7])[6]")).to_have_text(
            '173 – black company')

    def check_all_spend_users(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[8])[1]")).to_have_text('$529.96')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[8])[2]")).to_have_text('$282.96')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[8])[3]")).to_have_text('$224.04')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[8])[4]")).to_have_text('$194.36')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[8])[5]")).to_have_text('$170.36')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[8])[6]")).to_have_text('$152.50')

    def check_all_avg_amount_users(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[9])[1]")).to_have_text('$82.57')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[9])[2]")).to_have_text('$141.48')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[9])[3]")).to_have_text('$60.01')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[9])[4]")).to_have_text('$34.63')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[9])[5]")).to_have_text('$85.18')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[9])[6]")).to_have_text('$28.43')

    def check_all_decline_rate_users(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[10])[1]")).to_have_text('23.1%')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[10])[2]")).to_have_text('0.0%')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[10])[3]")).to_have_text('0.0%')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[10])[4]")).to_have_text('23.1%')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[10])[5]")).to_have_text('0.0%')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[10])[6]")).to_have_text('23.1%')

    def check_all_decline_international_users(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[12])[1]")).to_have_text('60.0%')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[12])[2]")).to_have_text('50.0%')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[12])[3]")).to_have_text('75.0%')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[12])[4]")).to_have_text('60.0%')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[12])[5]")).to_have_text('50.0%')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')]//td[12])[6]")).to_have_text('60.0%')

    def check_ech_bill(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[1]")).to_have_text(
            '10 Jun199 – subscr. testProCanceled10 Jun – 11 Jul$371.00Canceledon 12 Jun, 16:56')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[2]")).to_have_text(
            '10 Jun199 – subscr. testBasicCanceled10 Jun – 11 Jul$0.00Canceledon 12 Jun, 03:10')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[3]")).to_have_text(
            '10 Jun199 – subscr. testPrivateCanceled10 Jun – 11 Jul$600.00Canceledon 25 Nov, 09:11')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[4]")).to_have_text(
            '10 Jun203 – tesat rfgt5443ProUnpaid10 Jun – 10 Jun 2025$4,718.00ChargeCancel')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[5]")).to_have_text(
            '10 Jun202 – nmfdADSF retrytyPrivateUnpaid10 Jun – 10 Jul$600.00ChargeCancel')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[6]")).to_have_text(
            '10 Jun203 – tesat rfgt5443BasicUnpaid10 Jun – 11 Jun 2025$1,000.00ChargeCancel')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[7]")).to_have_text(
            '10 Jun202 – nmfdADSF retrytyPrivateUnpaid10 Jun – 11 Jul$600.00ChargeCancel')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[8]")).to_have_text(
            '10 Jun202 – nmfdADSF retrytyBasicCanceled10 Jun – 11 Jun 2025$1,000.00Canceledon 15 Aug, 12:41')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[9]")).to_have_text(
            '10 Jun202 – nmfdADSF retrytyBasicUnpaid10 Jun – 11 Jun 2025$1,000.00ChargeCancel')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[10]")).to_have_text(
            '10 Jun200 – 1398h 3476nBasicUnpaid10 Jun – 10 Jul$100.00ChargeCancel')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[11]")).to_have_text(
            '10 Jun202 – nmfdADSF retrytyProCanceled10 Jun – 11 Jul$471.00Canceledon 10 Jun, 11:01')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[12]")).to_have_text(
            '10 Jun201 – ki877 gfhghgProPaid10 Jun – 11 Jul$471.00Paidon 10 Jun, 08:21')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[13]")).to_have_text(
            '10 Jun200 – 1398h 3476nBasicPaid10 Jun – 11 Jul$100.00Paidon 10 Jun, 07:32')

    def check_sort_bu_default(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableAmount')]")).to_have_text(['$371.00', '$0.00', '$600.00', '$4,718.00', '$600.00', '$1,000.00', '$600.00', '$1,000.00', '$1,000.00', '$100.00', '$471.00', '$471.00', '$100.00'])

    def check_sort_highest_to_lowest(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableAmount')]")).to_have_text(['$4,718.00', '$1,000.00', '$1,000.00', '$1,000.00', '$600.00', '$600.00', '$600.00', '$471.00', '$471.00', '$371.00', '$100.00', '$100.00', '$0.00'])
    def check_sort_lowest_to_highest(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableAmount')]")).to_have_text(['$0.00', '$100.00', '$100.00', '$371.00', '$471.00', '$471.00', '$600.00', '$600.00', '$600.00', '$1,000.00', '$1,000.00', '$1,000.00', '$4,718.00'])

    def check_sort_by_date_to_newest(self, page):
        expect(page.locator("//td[1]")).to_have_text(['10 Jun', '10 Jun', '10 Jun', '10 Jun', '10 Jun', '10 Jun', '10 Jun', '10 Jun', '10 Jun', '10 Jun', '10 Jun', '10 Jun', '10 Jun'])

    def check_each_row_cash_page_1(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[1]")).to_have_text("18 Jun, 16:25 Deposit fee6 – ConnCompany($20.00)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[2]")).to_have_text("18 Jun, 16:25 Deposit6 – ConnCompany$1,000.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[3]")).to_have_text("18 Jun, 16:25 Deposit fee6 – ConnCompany($25.00)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[4]")).to_have_text("18 Jun, 16:25 Deposit6 – ConnCompany$700.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[5]")).to_have_text("18 Jun, 14:56 Deposit fee222 – dsef dsfdsg($0.58)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[6]")).to_have_text("18 Jun, 14:56 Deposit222 – dsef dsfdsg$29.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[7]")).to_have_text("18 Jun, 14:55 Deposit fee222 – dsef dsfdsg($0.20)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[8]")).to_have_text("18 Jun, 14:55 Deposit222 – dsef dsfdsg$10.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[9]")).to_have_text("18 Jun, 14:54 Deposit$29.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[10]")).to_have_text("18 Jun, 14:54 Deposit$29.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[11]")).to_have_text("18 Jun, 14:10 Deposit222 – dsef dsfdsg$25.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[12]")).to_have_text("18 Jun, 13:56 Deposit fee222 – dsef dsfdsg($0.40)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[13]")).to_have_text("18 Jun, 13:56 Deposit222 – dsef dsfdsg$20.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[14]")).to_have_text("18 Jun, 13:56 Deposit fee222 – dsef dsfdsg($0.60)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[15]")).to_have_text("18 Jun, 13:56 Deposit222 – dsef dsfdsg$30.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[16]")).to_have_text("18 Jun, 13:55 Deposit fee1 – MTS($0.40)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[17]")).to_have_text("18 Jun, 13:55 Deposit1 – MTS$20.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[18]")).to_have_text("18 Jun, 13:52 Deposit58 – onb1 onb1$20.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[19]")).to_have_text("18 Jun, 13:50 Deposit61 – ghgjghj hgjghjhgfj$20.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[20]")).to_have_text("18 Jun, 13:47 Deposit fee1 – MTS($20.10)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[20]")).to_have_text("18 Jun, 13:47 Deposit fee1 – MTS($20.10)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[21]")).to_have_text("18 Jun, 13:47 Deposit1 – MTS$1,005.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[22]")).to_have_text("18 Jun, 13:34 Deposit1 – MTS$1,005.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[23]")).to_have_text("18 Jun, 13:34 Deposit1 – MTS$1.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[24]")).to_have_text("18 Jun, 13:32 Deposit222 – dsef dsfdsg$105.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[25]")).to_have_text("18 Jun, 13:31 Deposit222 – dsef dsfdsg$10.00")

    def check_each_row_cash_page_2(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[1]")).to_have_text("18 Jun, 10:25 Referral202 – nmfdADSF retryty$250.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[2]")).to_have_text("18 Jun, 10:25 Referral1 – MTS$250.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[3]")).to_have_text("18 Jun, 10:19 Referral222 – dsef dsfdsg$250.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[4]")).to_have_text("18 Jun, 10:19 Referral1 – MTS$250.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[5]")).to_have_text("18 Jun, 10:06 Deposit222 – dsef dsfdsg$7,000.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[6]")).to_have_text("18 Jun, 09:54 Deposit222 – dsef dsfdsg$5,000.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[7]")).to_have_text("17 Jun, 09:58Pro Subscription1 – MTS($12.00)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[8]")).to_have_text("17 Jun, 09:52 Deposit fee1 – MTS($0.28)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[9]")).to_have_text("17 Jun, 09:52 Deposit1 – MTS$14.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[10]")).to_have_text("17 Jun, 09:42 Deposit1 – MTS$10.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[11]")).to_have_text("17 Jun, 09:38 Withdrawal2 – Beeline($50.00)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[12]")).to_have_text("17 Jun, 09:34 Deposit216 – UmhcrFgSMW ATxU$10.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[13]")).to_have_text("13 Jun, 15:10Basic Subscription210 – trytud fhfghgfjgfj($100.00)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[14]")).to_have_text("13 Jun, 15:10Basic Subscription210 – trytud fhfghgfjgfj($100.00)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[15]")).to_have_text("13 Jun, 15:10 Deposit210 – trytud fhfghgfjgfj$600.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[16]")).to_have_text("12 Jun, 17:58 Deposit206 – hmhjgkhgk hkghkhkghk$700.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[17]")).to_have_text("12 Jun, 03:10Basic Subscription6 – ConnCompany($100.00)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[18]")).to_have_text("10 Jun, 14:29 Deposit203 – tesat rfgt5443$300.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[19]")).to_have_text("10 Jun, 10:04 Deposit202 – nmfdADSF retryty$200.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[20]")).to_have_text("10 Jun, 08:21Pro Subscription201 – ki877 gfhghg($471.00)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[21]")).to_have_text("10 Jun, 08:21 Deposit201 – ki877 gfhghg$30.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[22]")).to_have_text("10 Jun, 07:55 Deposit201 – ki877 gfhghg$470.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[23]")).to_have_text("10 Jun, 07:32Basic Subscription200 – 1398h 3476n($100.00)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[24]")).to_have_text("10 Jun, 07:15 Deposit200 – 1398h 3476n$100.00")

    def check_each_row_deposits(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[1]")).to_have_text("18 Jun, 16:25 Deposit6 – ConnCompany$1,000.00")
        expect(page.locator("(//td[contains(@class, 'styles')]/span[contains(@class, 'styles')])[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[2]")).to_have_text("18 Jun, 16:25 Deposit6 – ConnCompany$700.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[3]")).to_have_text("18 Jun, 14:56 Deposit222 – dsef dsfdsg$29.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[4]")).to_have_text("18 Jun, 14:55 Deposit222 – dsef dsfdsg$10.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[5]")).to_have_text("18 Jun, 14:54 Deposit$29.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[6]")).to_have_text("18 Jun, 14:54 Deposit$29.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[7]")).to_have_text("18 Jun, 14:10 Deposit222 – dsef dsfdsg$25.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[8]")).to_have_text("18 Jun, 13:56 Deposit222 – dsef dsfdsg$20.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[9]")).to_have_text("18 Jun, 13:56 Deposit222 – dsef dsfdsg$30.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[10]")).to_have_text("18 Jun, 13:55 Deposit1 – MTS$20.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[11]")).to_have_text("18 Jun, 13:52 Deposit58 – onb1 onb1$20.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[12]")).to_have_text("18 Jun, 13:50 Deposit61 – ghgjghj hgjghjhgfj$20.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[13]")).to_have_text("18 Jun, 13:47 Deposit1 – MTS$1,005.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[14]")).to_have_text("18 Jun, 13:34 Deposit1 – MTS$1,005.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[15]")).to_have_text("18 Jun, 13:34 Deposit1 – MTS$1.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[16]")).to_have_text("18 Jun, 13:32 Deposit222 – dsef dsfdsg$105.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[17]")).to_have_text("18 Jun, 13:31 Deposit222 – dsef dsfdsg$10.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[18]")).to_have_text("18 Jun, 10:06 Deposit222 – dsef dsfdsg$7,000.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[19]")).to_have_text("18 Jun, 09:54 Deposit222 – dsef dsfdsg$5,000.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[20]")).to_have_text("17 Jun, 09:52 Deposit1 – MTS$14.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[21]")).to_have_text("17 Jun, 09:42 Deposit1 – MTS$10.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[22]")).to_have_text("17 Jun, 09:34 Deposit216 – UmhcrFgSMW ATxU$10.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[23]")).to_have_text("13 Jun, 15:10 Deposit210 – trytud fhfghgfjgfj$600.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[24]")).to_have_text("12 Jun, 17:58 Deposit206 – hmhjgkhgk hkghkhkghk$700.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[25]")).to_have_text("10 Jun, 14:29 Deposit203 – tesat rfgt5443$300.00")

    def check_each_row_deposits_2(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[1]")).to_have_text("10 Jun, 10:04 Deposit202 – nmfdADSF retryty$200.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[2]")).to_have_text("10 Jun, 08:21 Deposit201 – ki877 gfhghg$30.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[3]")).to_have_text("10 Jun, 07:55 Deposit201 – ki877 gfhghg$470.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[4]")).to_have_text("10 Jun, 07:15 Deposit200 – 1398h 3476n$100.00")

    def check_each_row_withdrawals(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[1]")).to_have_text("17 Jun, 09:38 Withdrawal2 – Beeline($50.00)")
        expect(page.locator("(//td[contains(@class, 'styles')]/span[contains(@class, 'styles')])[1]")).to_have_css("color", "rgb(20, 21, 26)")


    def check_each_row_subscriptions(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[1]")).to_have_text("17 Jun, 09:58Pro Subscription1 – MTS($12.00)")
        expect(page.locator("(//td[contains(@class, 'styles')]/span[contains(@class, 'styles')])[1]")).to_have_css("color", "rgb(20, 21, 26)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[2]")).to_have_text("13 Jun, 15:10Basic Subscription210 – trytud fhfghgfjgfj($100.00)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[3]")).to_have_text("13 Jun, 15:10Basic Subscription210 – trytud fhfghgfjgfj($100.00)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[4]")).to_have_text("12 Jun, 03:10Basic Subscription6 – ConnCompany($100.00)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[5]")).to_have_text("10 Jun, 08:21Pro Subscription201 – ki877 gfhghg($471.00)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[6]")).to_have_text("10 Jun, 07:32Basic Subscription200 – 1398h 3476n($100.00)")

    def check_each_row_referral(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[1]")).to_have_text("18 Jun, 10:25 Referral202 – nmfdADSF retryty$250.00")
        expect(page.locator("(//td[contains(@class, 'styles')]/span[contains(@class, 'styles')])[1]")).to_have_css("color", "rgb(88, 182, 62)")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[2]")).to_have_text("18 Jun, 10:25 Referral1 – MTS$250.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[3]")).to_have_text("18 Jun, 10:19 Referral222 – dsef dsfdsg$250.00")
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[4]")).to_have_text("18 Jun, 10:19 Referral1 – MTS$250.00")

    def check_companies_after_search_mts(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCompany')]")).to_have_count(12)
        expect(page.locator("//td[contains(@class, 'styles_tableCompany')]")).to_have_text(['1 – MTS', '1 – MTS', '1 – MTS', '1 – MTS', '1 – MTS', '1 – MTS', '1 – MTS', '1 – MTS', '1 – MTS', '1 – MTS', '1 – MTS', '1 – MTS'])

    def check_companies_after_search_222(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCompany')]")).to_have_count(14)
        expect(page.locator("//td[contains(@class, 'styles_tableCompany')]")).to_have_text(['222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg'])

    def check_companies_filter_deposit(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCompany')]")).to_have_count(25)
        expect(page.locator("//td[contains(@class, 'styles_tableCompany')]")).to_have_text(['6 – ConnCompany', '6 – ConnCompany', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '', '', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '1 – MTS', '58 – onb1 onb1', '61 – ghgjghj hgjghjhgfj', '1 – MTS', '1 – MTS', '1 – MTS', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '1 – MTS', '1 – MTS', '216 – UmhcrFgSMW ATxU', '210 – trytud fhfghgfjgfj', '206 – hmhjgkhgk hkghkhkghk', '203 – tesat rfgt5443'])

    def check_sort_by_amount_to_higest(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCompany')]")).to_have_text(['222 – dsef dsfdsg', '222 – dsef dsfdsg', '1 – MTS', '1 – MTS', '6 – ConnCompany', '206 – hmhjgkhgk hkghkhkghk', '6 – ConnCompany', '210 – trytud fhfghgfjgfj', '201 – ki877 gfhghg', '201 – ki877 gfhghg', '203 – tesat rfgt5443', '1 – MTS', '202 – nmfdADSF retryty', '1 – MTS', '222 – dsef dsfdsg', '202 – nmfdADSF retryty', '222 – dsef dsfdsg', '200 – 1398h 3476n', '200 – 1398h 3476n', '6 – ConnCompany', '210 – trytud fhfghgfjgfj', '210 – trytud fhfghgfjgfj', '2 – Beeline', '222 – dsef dsfdsg', '201 – ki877 gfhghg'])
    def check_sort_by_amount_to_lowest(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCompany')]")).to_have_text(['222 – dsef dsfdsg', '1 – MTS', '222 – dsef dsfdsg', '1 – MTS', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '1 – MTS', '222 – dsef dsfdsg', '1 – MTS', '216 – UmhcrFgSMW ATxU', '222 – dsef dsfdsg', '1 – MTS', '1 – MTS', '61 – ghgjghj hgjghjhgfj', '58 – onb1 onb1', '6 – ConnCompany', '1 – MTS', '222 – dsef dsfdsg', '1 – MTS', '222 – dsef dsfdsg', '6 – ConnCompany', '', '', '222 – dsef dsfdsg', '222 – dsef dsfdsg'])

    def check_sort_by_datetime_to_oldest(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCompany')]")).to_have_text(['6 – ConnCompany', '6 – ConnCompany', '6 – ConnCompany', '6 – ConnCompany', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '', '', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '1 – MTS', '1 – MTS', '58 – onb1 onb1', '61 – ghgjghj hgjghjhgfj', '1 – MTS', '1 – MTS', '1 – MTS', '1 – MTS', '222 – dsef dsfdsg', '222 – dsef dsfdsg'])

    def check_sort_by_datetime_to_newest(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCompany')]")).to_have_text(['200 – 1398h 3476n', '200 – 1398h 3476n', '201 – ki877 gfhghg', '201 – ki877 gfhghg', '201 – ki877 gfhghg', '202 – nmfdADSF retryty', '203 – tesat rfgt5443', '6 – ConnCompany', '206 – hmhjgkhgk hkghkhkghk', '210 – trytud fhfghgfjgfj', '210 – trytud fhfghgfjgfj', '210 – trytud fhfghgfjgfj', '216 – UmhcrFgSMW ATxU', '2 – Beeline', '1 – MTS', '1 – MTS', '1 – MTS', '1 – MTS', '222 – dsef dsfdsg', '222 – dsef dsfdsg', '1 – MTS', '222 – dsef dsfdsg', '1 – MTS', '202 – nmfdADSF retryty', '222 – dsef dsfdsg'])
    def check_status_active_companies(self, page):
        expect(page.locator("//*[@data-test-id='badge']")).to_have_text(['Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active'])

    def check_text_at_row_companies(self, page, n, text):
        expect(page.locator("(//td[contains(@class, 'text-align_end')])" + f'[{n}]')).to_have_text(text)

    def check_text_in_row_top_ups(self, page, n, m, text):
        expect(page.locator(f"(//td[contains(text(), '{n}')]/ancestor::tr//following-sibling::td)" + f'[{m}]')).to_have_text(text)
    def check_text_widgets_top_ups(self, page, n, m, text):
        expect(page.locator("(//*[@data-test-id='widget'])" + f'[{n}]' + "//span" + f'[{m}]')).to_have_text(text)
    def check_filters_top_ups(self, page, text):
        expect(page.locator(f"//*[@data-test-id='popper-content']//span[contains(text()," + f"'{text}')]")).to_be_visible()

    def check_filters_referrals(self, page, text):
        expect(page.locator("//*[@data-test-id='checkbox']//span[contains(text()," + f"'{text}')]")).to_be_visible()

    def check_companies_referrals(self, page, m, text):
        expect(page.locator(f"(//div[contains(@class, 'display_flex align-items_center gap_2')])" + f"[{m}]")).to_have_text(text)

    def check_status_in_row(self, page, m, text):
        expect(page.locator("(//*[@data-test-id='badge'])" + f"[{m}]")).to_have_text(text)

    def check_widget_batches(self, page, text, sum):
        expect(page.locator("//*[@data-test-id='widget']//span[contains(text()," + f"'{text}')]")).to_be_visible()
        expect(page.locator(
            "//*[@data-test-id='widget']//*[contains(text()," + f"'{text}')]/following-sibling::span")).to_have_text(sum)

    def check_tabs_batches(self, page, text):
        expect(page.locator("//*[@data-test-id='tab']//div[contains(text()," + f"'{text}')]")).to_be_visible()

    def check_filters_batches(self, page, text):
        expect(page.locator("//*[@data-test-id='button-group']//span[contains(text()," + f"'{text}')]")).to_be_visible()