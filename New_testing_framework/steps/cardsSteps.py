import allure
from playwright.sync_api import expect
from steps._base import BaseSteps


class CardsSteps(BaseSteps):

    @allure.step("Check default limit create card")
    def check_default_limit_create_card_ru(self, page):
        expect(page.locator("(//div[contains(@class, 'display_flex flex-direction_column')])[3]")).to_have_text('Без лимита')

    @allure.step("Fill limit")
    def fill_limit_amount(self, n):
        self.pages.cards.input_limit_amount.fill(n)

    @allure.step("Check limit amount on card")
    def check_limit_amount_on_card(self, n):
        assert self.pages.cards.modal_card_limit_amount_ru.get_text(), n

    @allure.step("Check sort card by default")
    def check_sort_card_by_default(self, page):
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[1]")).to_have_text(
            "••7485 string")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[2]")).to_have_text(
            "••8002 6 apple")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[3]")).to_have_text(
            "••6070 65767")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[4]")).to_have_text(
            "••7752 123456")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[5]")).to_have_text(
            "••6980 test")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[6]")).to_have_text(
            "••1839 ASQWEDC")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[7]")).to_have_text(
            "••4518 HRTYU")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[8]")).to_have_text(
            "••9053 ASDCX")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[9]")).to_have_text(
            "••3663 WEDSCXS")

    @allure.step("Check sort card by default")
    def check_sort_card_by_old_cards(self, page):
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[1]")).to_have_text(
            "••3495 Facebook")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[2]")).to_have_text(
            "••3860 tik tok")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[3]")).to_have_text(
            "••6513 taboola")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[4]")).to_have_text(
            "••1089 ADC")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[5]")).to_have_text(
            "••9759 Visa")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[6]")).to_have_text(
            "••0414 qwerty")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[7]")).to_have_text(
            "••8741 tyuiop")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[8]")).to_have_text(
            "••3920 ghjkll")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[9]")).to_have_text(
            "••4694 xeawsdret")

    @allure.step("Check sort card ascending one month")
    def check_sort_card_by_ascending(self, page):
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[1]")).to_have_text(
            "••1839 ASQWEDC")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[2]")).to_have_text(
            "••9053 ASDCX ")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[3]")).to_have_text(
            "••3663 WEDSCXS")


    @allure.step("Check sort card descending one month")
    def check_sort_by_descending(self, page):
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[1]")).to_have_text(
            "••1839 ASQWEDC")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[2]")).to_have_text(
            "••9053 ASDCX")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[3]")).to_have_text(
            "••3663 WEDSCXS")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[4]")).to_have_text(
            "••4039 dfd vcvcvcbcv")
        expect(page.locator("(//td[contains(@class, 'styles_tableCard')])[5]")).to_have_text(
            "••6978 fdgfgfd erwe")


    def check_all_cards_filter_by_calendar_rows(self, page):
        expect(page.locator("//tr[contains(@class, 'hover-visible-container')]")).to_have_text(
            ['••7485 stringActive553437Без лимита∞invated emploee0,00\xa0$', '••8002 6 appleActive433451Лайфтайм10,00\xa0$ / 100,00\xa0$invated emploee10,00\xa0$', '••6070 65767Active489683Неделя67,00\xa0$invated emploee3,00\xa0$', '••7752 123456Active559666Без лимита∞invated emploee0,00\xa0$', '••6980 testActive553437Без лимита∞test do not change12,50\xa0$', '••1839 ASQWEDCActive556150Месяц567,00\xa0$test do not change76,20\xa0$', '••4518 HRTYUActive531993Неделя99,00\xa0$test do not change5,00\xa0$', '••9053 ASDCXActive556150Месяц44,00\xa0$test do not change61,00\xa0$', '••3663 WEDSCXSActive559292Лайфтайм60,51\xa0$ / 100,00\xa0$test do not change60,51\xa0$', '••8662 ASXCvfg bfdfgActive556150День89,00\xa0$test do not change0,00\xa0$', '••9880 56 yuhjiko9Active553437Месяц44,00\xa0$test do not change0,00\xa0$', '••6978 fdgfgfd erweActive404038Неделя33,00\xa0$test do not change15,15\xa0$', '••9542 23Frozen489683Без лимита∞test do not change0,00\xa0$', '••7669 fdfer gfhgfhgfh 34343432Closed556150Без лимита∞test do not change0,00\xa0$', '••4039 dfd vcvcvcbcvActive559292Без лимита∞test do not change19,19\xa0$', '••6044 34 rgfdg fdgfg 5464645Active553437Без лимита∞test do not change0,00\xa0$', '••6860 POu  hgyf54534545Active553437Месяц100,00\xa0$test do not change0,00\xa0$', '••4097 ufhg 57868 vbvtftfiyuActive489683Неделя90,00\xa0$test do not change0,00\xa0$', '••8112 NJHY jhgjhjhbActive559666Без лимита∞test do not change0,00\xa0$', '••1412 freezeFrozen441112Без лимита∞test do not change0,00\xa0$', '••2505 tuporeActive519075День45,00\xa0$test do not change0,00\xa0$', '••9246 5678Active559666Неделя200,00\xa0$test do not change0,00\xa0$', '••0166 closedClosed559292Лайфтайм675,00\xa0$test do not change0,00\xa0$', '••4694 xeawsdretActive489683Неделя678,00\xa0$test do not change0,00\xa0$', '••3920 ghjkllActive531993День100,00\xa0$test do not change0,00\xa0$'])
    def check_all_cards_filter_by_calendar_rows_next_page(self, page):
        expect(page.locator("//tr[contains(@class, 'hover-visible-container')]")).to_have_text(['••6980 testActive553437Без лимита∞12,50\xa0$', '••1839 ASQWEDCActive556150Месяц567,00\xa0$76,20\xa0$', '••4518 HRTYUActive531993Неделя99,00\xa0$5,00\xa0$', '••9053 ASDCXActive556150Месяц44,00\xa0$61,00\xa0$', '••3663 WEDSCXSActive559292Лайфтайм60,51\xa0$ / 100,00\xa0$60,51\xa0$', '••8662 ASXCvfg bfdfgActive556150День89,00\xa0$0,00\xa0$', '••9880 56 yuhjiko9Active553437Месяц44,00\xa0$0,00\xa0$', '••6978 fdgfgfd erweActive404038Неделя33,00\xa0$15,15\xa0$', '••9542 23Frozen489683Без лимита∞0,00\xa0$', '••7669 fdfer gfhgfhgfh 34343432Closed556150Без лимита∞0,00\xa0$', '••4039 dfd vcvcvcbcvActive559292Без лимита∞19,19\xa0$', '••6044 34 rgfdg fdgfg 5464645Active553437Без лимита∞0,00\xa0$', '••6860 POu  hgyf54534545Active553437Месяц100,00\xa0$0,00\xa0$', '••4097 ufhg 57868 vbvtftfiyuActive489683Неделя90,00\xa0$0,00\xa0$', '••8112 NJHY jhgjhjhbActive559666Без лимита∞0,00\xa0$', '••1412 freezeFrozen441112Без лимита∞0,00\xa0$', '••2505 tuporeActive519075День45,00\xa0$0,00\xa0$', '••9246 5678Active559666Неделя200,00\xa0$0,00\xa0$', '••0166 closedClosed559292Лайфтайм675,00\xa0$0,00\xa0$', '••4694 xeawsdretActive489683Неделя678,00\xa0$0,00\xa0$', '••3920 ghjkllActive531993День100,00\xa0$0,00\xa0$', '••8741 tyuiopActive556150Без лимита∞0,00\xa0$', '••0414 qwertyActive519075Месяц78,00\xa0$0,00\xa0$', '••9759 VisaActive441112Лайфтайм600,00\xa0$0,00\xa0$', '••1089 ADCActive559666Месяц800,00\xa0$0,00\xa0$'])

    def check_cards_filter_by_bin_user(self, page):
        expect(page.locator("//tr[contains(@class, 'hover-visible-container')]")).to_have_text(
            ['••6980 testActive553437Без лимита∞test do not change12,50\xa0$', '••9880 56 yuhjiko9Active553437Месяц44,00\xa0$test do not change0,00\xa0$', '••6044 34 rgfdg fdgfg 5464645Active553437Без лимита∞test do not change0,00\xa0$', '••6860 POu  hgyf54534545Active553437Месяц100,00\xa0$test do not change0,00\xa0$', '••8112 NJHY jhgjhjhbActive559666Без лимита∞test do not change0,00\xa0$', '••9246 5678Active559666Неделя200,00\xa0$test do not change0,00\xa0$', '••1089 ADCActive559666Месяц800,00\xa0$test do not change0,00\xa0$', '••6513 taboolaActive553437Неделя80,00\xa0$test do not change0,00\xa0$'])

    def check_cards_filter_by_bin_user_next_page(self, page):
        expect(page.locator("//tr[contains(@class, 'hover-visible-container')]")).to_have_text(['••6980 testActive553437Без лимита∞12,50\xa0$', '••9880 56 yuhjiko9Active553437Месяц44,00\xa0$0,00\xa0$', '••6044 34 rgfdg fdgfg 5464645Active553437Без лимита∞0,00\xa0$', '••6860 POu  hgyf54534545Active553437Месяц100,00\xa0$0,00\xa0$', '••8112 NJHY jhgjhjhbActive559666Без лимита∞0,00\xa0$', '••9246 5678Active559666Неделя200,00\xa0$0,00\xa0$', '••1089 ADCActive559666Месяц800,00\xa0$0,00\xa0$', '••6513 taboolaActive553437Неделя80,00\xa0$0,00\xa0$'])

    def check_all_cards_check_spend_all_cards(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableSpend')]")).to_have_text(
            ['0,00\xa0$', '10,00\xa0$', '3,00\xa0$', '0,00\xa0$', '12,50\xa0$', '76,20\xa0$', '5,00\xa0$', '61,00\xa0$',
             '60,51\xa0$', '0,00\xa0$', '0,00\xa0$', '15,15\xa0$', '0,00\xa0$', '0,00\xa0$', '19,19\xa0$', '0,00\xa0$',
             '0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$',
             '0,00\xa0$'])

    def check_all_cards_check_spend_all_cards_next_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableSpend')]")).to_have_text(
            ['0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$'])

    def check_all_cards_check_user_name_all_cards(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableUser')]")).to_have_text(
            ['invated emploee', 'invated emploee', 'invated emploee', 'invated emploee', 'test do not change',
             'test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change',
             'test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change',
             'test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change',
             'test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change'])

    def check_all_cards_check_user_name_all_cards_next_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableUser')]")).to_have_text(
            ['test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change',
             'test do not change', 'test do not change'])

    def all_cards_check_limit_all_cards(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableLimit')]")).to_have_text(['Без лимита∞', 'Лайфтайм10,00\xa0$ / 100,00\xa0$', 'Неделя67,00\xa0$', 'Без лимита∞', 'Без лимита∞', 'Месяц567,00\xa0$', 'Неделя99,00\xa0$', 'Месяц44,00\xa0$', 'Лайфтайм60,51\xa0$ / 100,00\xa0$', 'День89,00\xa0$', 'Месяц44,00\xa0$', 'Неделя33,00\xa0$', 'Без лимита∞', 'Без лимита∞', 'Без лимита∞', 'Без лимита∞', 'Месяц100,00\xa0$', 'Неделя90,00\xa0$', 'Без лимита∞', 'Без лимита∞', 'День45,00\xa0$', 'Неделя200,00\xa0$', 'Лайфтайм675,00\xa0$', 'Неделя678,00\xa0$', 'День100,00\xa0$'])

    def all_cards_check_limit_all_cards_next_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableLimit')]")).to_have_text(['Без лимита∞', 'Месяц78,00\xa0$', 'Лайфтайм600,00\xa0$', 'Месяц800,00\xa0$', 'Неделя80,00\xa0$', 'День40,00\xa0$', 'Без лимита∞'])

    def check_all_cards_check_bin_all_cards(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableBIN')]")).to_have_text(
            ['553437', '433451', '489683', '559666', '553437', '556150', '531993', '556150', '559292', '556150',
             '553437',
             '404038', '489683', '556150', '559292', '553437', '553437', '489683', '559666', '441112', '519075',
             '559666',
             '559292', '489683', '531993'])

    def check_all_cards_check_bin_all_cards_next_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableBIN')]")).to_have_text(['556150', '519075', '441112', '559666', '553437', '556371', '404038'])

    def check_all_cards_check_all_status_cards(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableStatus')]")).to_have_text(
            ['Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Frozen', 'Closed', 'Active', 'Active', 'Active', 'Active', 'Active', 'Frozen', 'Active', 'Active', 'Closed', 'Active', 'Active'])

    def check_all_cards_check_all_status_cards_next_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableStatus')]")).to_have_text(
            ['Active', 'Active', 'Active',
             'Active',
             'Active', 'Active', 'Active'])

    def all_cards_check_all_name_cards(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCard')]")).to_have_text(
            ['••7485 string', '••8002 6 apple', '••6070 65767', '••7752 123456', '••6980 test', '••1839 ASQWEDC',
             '••4518 HRTYU', '••9053 ASDCX', '••3663 WEDSCXS', '••8662 ASXCvfg bfdfg', '••9880 56 yuhjiko9',
             '••6978 fdgfgfd erwe', '••9542 23', '••7669 fdfer gfhgfhgfh 34343432', '••4039 dfd vcvcvcbcv',
             '••6044 34 rgfdg fdgfg 5464645', '••6860 POu  hgyf54534545', '••4097 ufhg 57868 vbvtftfiyu',
             '••8112 NJHY jhgjhjhb', '••1412 freeze', '••2505 tupore', '••9246 5678', '••0166 closed',
             '••4694 xeawsdret',
             '••3920 ghjkll'])

    def all_cards_check_all_name_cards_next_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCard')]")).to_have_text(
            ['••8741 tyuiop', '••0414 qwerty', '••9759 Visa', '••1089 ADC', '••6513 taboola', '••3860 tik tok',
             '••3495 Facebook'])

    def check_check_spend_all_cards(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableSpend')]")).to_have_text(
            ['12,50\xa0$', '76,20\xa0$', '5,00\xa0$', '61,00\xa0$', '60,51\xa0$', '0,00\xa0$', '0,00\xa0$',
             '15,15\xa0$',
             '0,00\xa0$', '0,00\xa0$', '19,19\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$',
             '0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$', '0,00\xa0$',
             '0,00\xa0$'])

    def check_check_spend_all_cards_next_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableSpend')]")).to_have_text(['0,00\xa0$', '0,00\xa0$', '0,00\xa0$'])

    def check_check_user_name_all_cards(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableUser')]")).to_have_text(
            ['invated emploee', 'invated emploee', 'invated emploee', 'invated emploee', 'test do not change',
             'test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change',
             'test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change',
             'test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change',
             'test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change'])

    def check_check_user_name_all_cards_next_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableUser')]")).to_have_text(
            ['test do not change', 'test do not change', 'test do not change', 'test do not change',
             'test do not change',
             'test do not change', 'test do not change'])
    def check_limit_all_cards(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableLimit')]")).to_have_text(
            ['Без лимита∞', 'Месяц567,00\xa0$', 'Неделя99,00\xa0$', 'Месяц44,00\xa0$', 'Лайфтайм60,51\xa0$ / 100,00\xa0$', 'День89,00\xa0$', 'Месяц44,00\xa0$', 'Неделя33,00\xa0$', 'Без лимита∞', 'Без лимита∞', 'Без лимита∞', 'Без лимита∞', 'Месяц100,00\xa0$', 'Неделя90,00\xa0$', 'Без лимита∞', 'Без лимита∞', 'День45,00\xa0$', 'Неделя200,00\xa0$', 'Лайфтайм675,00\xa0$', 'Неделя678,00\xa0$', 'День100,00\xa0$', 'Без лимита∞', 'Месяц78,00\xa0$', 'Лайфтайм600,00\xa0$', 'Месяц800,00\xa0$'])

    def check_limit_all_cards_next_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableLimit')]")).to_have_text(['Неделя80,00\xa0$', 'День40,00\xa0$', 'Без лимита∞'])

    def check_bin_all_cards(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableBIN')]")).to_have_text(
            ['553437', '556150', '531993', '556150', '559292', '556150', '553437', '404038', '489683', '556150',
             '559292',
             '553437', '553437', '489683', '559666', '441112', '519075', '559666', '559292', '489683', '531993',
             '556150',
             '519075', '441112', '559666'])

    def check_bin_all_cards_next_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableBIN')]")).to_have_text(['553437', '556371', '404038'])

    def check_all_status_cards(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableStatus')]")).to_have_text(
            ['Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Frozen', 'Closed', 'Active', 'Active', 'Active', 'Active', 'Active', 'Frozen', 'Active', 'Active', 'Closed', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active'])


    def check_all_status_cards_next_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableStatus')]")).to_have_text(['Active', 'Active', 'Active'])

    def check_all_name_cards(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCard')]")).to_have_text(
            ['••6980 test', '••1839 ASQWEDC', '••4518 HRTYU', '••9053 ASDCX', '••3663 WEDSCXS', '••8662 ASXCvfg bfdfg',
             '••9880 56 yuhjiko9', '••6978 fdgfgfd erwe', '••9542 23', '••7669 fdfer gfhgfhgfh 34343432',
             '••4039 dfd vcvcvcbcv', '••6044 34 rgfdg fdgfg 5464645', '••6860 POu  hgyf54534545',
             '••4097 ufhg 57868 vbvtftfiyu', '••8112 NJHY jhgjhjhb', '••1412 freeze', '••2505 tupore', '••9246 5678',
             '••0166 closed', '••4694 xeawsdret', '••3920 ghjkll', '••8741 tyuiop', '••0414 qwerty', '••9759 Visa',
             '••1089 ADC'])

    def check_all_name_cards_next_page(self, page):
        expect(page.locator("//td[contains(@class, 'styles_tableCard')]")).to_have_text(['••6513 taboola', '••3860 tik tok', '••3495 Facebook'])

    def check_popper_activator_info(self, page):
        page.locator(
            "//th[contains(@class, 'text-align_end')]//div[@data-test-id = 'floating-activator']").hover()
        expect(page.locator("//div[@data-test-id = 'info-popover-content']")).to_have_text(['Settled203,00\xa0$Pending90,00\xa0$Reversed18,00\xa0$Refund47,00\xa0$Междунар. комиссия1,46\xa0$Комиссия за деклайн1,00\xa0$Конвертация1,09\xa0$'])

    def check_from_all_cards_total_spend(self, page):
        page.locator(
            "//th[contains(@class, 'text-align_end')]//div[@data-test-id = 'floating-activator']").hover()
        expect(page.locator("//div[@data-test-id = 'info-popover-content']")).to_have_text(['Settled205,00\xa0$Pending101,00\xa0$Reversed18,00\xa0$Refund47,00\xa0$Междунар. комиссия1,46\xa0$Комиссия за деклайн1,00\xa0$Конвертация1,09\xa0$'])

    def check_rows_employee_cards(self, page):
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[1]")).to_have_text ('••7485 stringActive553437Без лимита∞0,00\xa0$')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[2]")).to_have_text ('••8002 6 appleActive433451Лайфтайм10,00 $ / 100,00 $0,00 $')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[3]")).to_have_text ('••6070 65767Active489683Неделя67,00 $0,00 $')
        expect(page.locator("(//tr[contains(@class, 'hover-visible-container')])[4]")).to_have_text ('••7752 123456Active559666Без лимита∞0,00\xa0$')

    def check_total_sum_spend(self, page):
        expect(page.locator("(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[1]")).to_have_text('Settled205,00 $')
        expect(page.locator("(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[2]")).to_have_text('Pending101,00 $')
        expect(page.locator("(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[3]")).to_have_text('Reversed18,00 $')
        expect(page.locator("(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[4]")).to_have_text('Refund47,00 $')
        expect(page.locator("(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[5]")).to_have_text('Междунар. комиссия1,46 $')
        expect(page.locator("(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[6]")).to_have_text('Комиссия за деклайн1,00 $')
        expect(page.locator("(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[7]")).to_have_text('Конвертация1,09 $')

    def check_total_sum_of_one_card(self, page):
        page.locator('(//*[@data-test-id="info-popover-activator"])[5]').hover()
        page.locator('(//*[@data-test-id="floating-activator"])[9]').click()
        expect(page.locator(
            "(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[1]")).to_have_text('Settled74,00 $')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[2]")).to_have_text('Refund1,00 $')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[3]")).to_have_text('Междунар. комиссия2,10 $')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[4]")).to_have_text('Комиссия за деклайн0,50 $')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[5]")).to_have_text('Конвертация0,60 $')
        page.locator('//h1').click()
        page.locator('(//*[@data-test-id="info-popover-activator"])[8]').hover()
        page.locator('(//*[@data-test-id="floating-activator"])[12]').click()
        expect(page.locator(
            "(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[1]")).to_have_text(
            'Settled60,00 $')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[2]")).to_have_text(
            'Pending44,00 $')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[3]")).to_have_text(
            'Refund43,00 $')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[4]")).to_have_text(
            'Междунар. комиссия0,64 $')
        expect(page.locator(
            "(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[4]")).to_have_css("color", "rgb(20, 21, 26)")
        expect(page.locator(
            "(//*[contains(@class, 'display_flex align-items_center justify-content_space-between gap_3')])[5]")).to_have_text(
            'Конвертация0,15 $')

    def check_color_status_at_table(self, page):
        expect(page.locator('(//*[@data-test-id="badge"]//span[text()="Active"])[1]')).to_have_css("color", "rgb(20, 21, 26)")
        expect(page.locator('(//*[@data-test-id="badge"]//span[text()="Frozen"])[1]')).to_have_css("color", "rgb(20, 21, 26)")
        expect(page.locator('(//*[@data-test-id="badge"])[14]')).to_have_css("color", "rgba(20, 21, 26, 0.4)")
