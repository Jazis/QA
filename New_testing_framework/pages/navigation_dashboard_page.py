from pages.base_page import BasePage
from widgets.button import Button


class NavigationDashboardPage(BasePage):
    def __init__(self) -> None:
        super().__init__()

        self.companies = Button(selector=self._locators.navigation_dashboard.companies)
        self.accounts = Button(selector=self._locators.navigation_dashboard.accounts)
        self.wallets = Button(selector=self._locators.navigation_dashboard.wallets)
        self.transactions = Button(selector=self._locators.navigation_dashboard.transactions)
        self.cards = Button(selector=self._locators.navigation_dashboard.cards)
        self.users = Button(selector=self._locators.navigation_dashboard.users)
        self.top_ups = Button(selector=self._locators.navigation_dashboard.top_ups)
        self.batches = Button(selector=self._locators.navigation_dashboard.batches)
        self.referrals = Button(selector=self._locators.navigation_dashboard.referrals)
        self.dash_subscriptions = Button(selector=self._locators.navigation_dashboard.dash_subscriptions)
