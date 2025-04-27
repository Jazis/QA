from playwright.sync_api import expect
from steps._base import BaseSteps


class CashSteps(BaseSteps):
    def check_row_at_popover(self, page, n, text):
        expect(page.locator('(//*[@data-test-id="info-popover-content"]//span)' + f"[{n}]")).to_have_text(text)
