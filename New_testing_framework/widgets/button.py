import allure

from playwright.sync_api import Page

from utils.consts import WAIT_TIME_MSEC
from widgets.element import Element


class Button(Element):
    def __init__(self, selector: str):
        super().__init__(selector)
        self.button = None
        # self.button = Element(f"{self.selector}//*[@data-debug-id='widgets-button']")

    def is_active(self) -> bool:
        return self.button.are_classes_in({"active"})

    def get_popup_label(self) -> str:
        return self.button._get_attribute("title")

    def is_disabled(self, page=None, timeout: int = WAIT_TIME_MSEC) -> bool:
        return self.button.is_disabled(page=page, timeout=timeout)


class MapButton(Element):
    def __init__(self, selector: str):
        super().__init__(selector)

    def is_active(self, page=None) -> bool:
        return self.are_classes_in({"active"}, page=page)


class ModalButton(Button):
    def __init__(self, selector: str):
        super().__init__(selector)
        self.button = Element(self.selector)


class AddToTableButton(Button):
    def __init__(self, selector: str):
        super().__init__(selector)

    def click(self, **kwargs):
        self.button.click()


class OnHoverButton(Button):
    def __init__(self, selector: str):
        super().__init__(selector)
        self.button = Element(self.selector)


class ButtonWithOuterTooltip(MapButton):
    def __init__(self, selector: str):
        super().__init__(selector)
        self.outer_div = Element(f"{selector}/parent::div")

    @allure.step("Hover on element {0}")
    def hover(self, page: Page = None, **kwargs) -> None:
        self.outer_div.hover()
