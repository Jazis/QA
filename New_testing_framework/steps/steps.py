from pages.pages import Pages
from steps.cardsSteps import CardsSteps

from steps.auth import AuthSteps
from steps.cashSteps import CashSteps
from steps.dashboardSteps import DashboardSteps
from steps.onboardingSteps import OnboardingSteps
from steps.teamSteps import TeamSteps
from steps.transactionSteps import TransactionSteps
from steps.universalSteps import UniversalSteps


class Steps:
    def __init__(self, pages=None) -> None:
        if pages is None:
            pages = Pages()

        self.auth = AuthSteps(pages)
        self.onboarding = OnboardingSteps(pages)
        self.cardsSteps = CardsSteps(pages)
        self.universalSteps = UniversalSteps(pages)
        self.teamSteps = TeamSteps(pages)
        self.dashboardSteps = DashboardSteps(pages)
        self.transactionSteps = TransactionSteps(pages)
        self.cashSteps = CashSteps(pages)

