from locators.auth import AuthLocators
from locators.cards import Cards
from locators.cash_balance import CashBalance
from locators.dashboard import Dashboard
from locators.navigation import Navigation
from locators.navigation_dashboard import NavigationDashboard
from locators.onboarding import OnboardingLocator
from locators.team import Team
from locators.trans import Transactions
from locators.user_settings import UserSettings


class Locators:
    def __init__(self) -> None:
        self.auth = AuthLocators()

        self.obdord = OnboardingLocator()

        self.navigation = Navigation()

        self.cards = Cards()
        self.trans = Transactions()
        self.cash_balance = CashBalance()
        self.team = Team()
        self.settings_user = UserSettings()
        self.dashboard = Dashboard()
        self.navigation_dashboard = NavigationDashboard()
