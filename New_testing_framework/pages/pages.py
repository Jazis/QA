from .auth import AuthPage
from .cards import CardPage
from .dashboard_page import DashboardPage
from .navigation_dashboard_page import NavigationDashboardPage
from .navigation_page import NavigationPage
from .onboarding import OnboardingPage
from .team_page import TeamPage
from .transaction import TransPage
from .user_setting_page import SettingsUserPage
from .сashBalance_page import CashBalancePage


class Pages:
    def __init__(self) -> None:
        self.auth = AuthPage()
        self.onboard = OnboardingPage()
        self.navigation = NavigationPage()
        self.cards = CardPage()
        self.trans = TransPage()
        self.cash_balance = CashBalancePage()
        self.team = TeamPage()
        self.settings_user = SettingsUserPage()
        self.dashboard = DashboardPage()
        self.navigation_dashboard = NavigationDashboardPage()
