from typing import Union
import allure

from playwright.sync_api import expect, Page

from utils.consts import WAIT_TIME_MSEC
from widgets.element import Element


class Input(Element):
    def __init__(self, selector: str):
        super().__init__(selector)
        self.input = Element(f"{self.selector}//*[@data-debug-id='widgets-input']")
        if not self.debug_id:
            self.input = Element(self.selector)
        # self.label = Label(self.label_id)

    @allure.step("Fill input {0}")
    def fill(self, text, page=None) -> str:
        self.input._find(page=page).fill(str(text))
        return text

    @allure.step("Fill input {0}")
    async def async_fill(self, text: str) -> None:
        if not text or await self.input.async_is_disabled():
            return
        await self.input._find().fill(text)
        await self.async_click_offset()

    @allure.step("Type in input {0}")
    def type(self, text, **kwargs) -> str:
        if text is None or self.is_disabled():
            return ""
        self.input._find().type(str(text), **kwargs)
        return text

    @allure.step("Type number in input {0}")
    def type_number(self, text, **kwargs) -> str:
        if text is None or self.is_disabled():
            return
        self.input._find().type(str(text), **kwargs)
        if str(text)[0] == "-":
            self.input._find().page.keyboard.press("Home")
            self.input._find().type("-", **kwargs)

    @allure.step("Type in input {0}")
    async def async_type(self, text: str, **kwargs):
        if text is None or await self.async_is_disabled():
            return ""
        await self.input._find().type(text, **kwargs)

    @allure.step("Get title from {0}")
    def get_title(self):
        return self._find().get_attribute("title")

    @allure.step("Get value from {0}")
    def get_value(self) -> str:
        return self.input._find().input_value()

    @allure.step("Get text from {0}")
    def get_text(self, page=None) -> str:
        value = self._find(page=page).get_attribute("value")
        if value is not None:  # для совместимости со старыми инпутами
            return value
        return self.input._find(page=page).get_attribute("value")

    @allure.step("Get text from {0}")
    async def async_get_text(self, page=None) -> str:
        value = await self._find(page=page).get_attribute("value")
        if value is not None:  # для совместимости со старыми инпутами
            return value
        return await self.input._find(page=page).get_attribute("value")

    @allure.step
    def is_readonly(self) -> bool:
        readonly = self._find().get_attribute("readonly")
        if readonly is not None:
            return readonly != "false"
        else:
            return False

    @allure.step
    def is_required(self) -> bool:
        return self.input.are_classes_in({"has-error", "is-invalid"})

    @allure.step
    async def async_is_required(self) -> bool:
        return await self.input.async_are_classes_in({"has-error", "is-invalid"})

    @allure.step
    def paste(self):
        self.input._find().focus()
        self.input._find().press("Control+A")
        self.input._find().press("Control+V")
        self.page.wait_for_timeout(100)

    @allure.step
    def clear(self, page=None):
        self.input._find(page=page).focus()
        self.input._find(page=page).press("Control+A")
        self.input._find(page=page).press("Delete")
        self.page.wait_for_timeout(100)

    @allure.step
    def copy(self):
        self.input._find().focus()
        self.input._find().press("Control+A")
        self.input._find().press("Control+C")

    @property
    def keyboard(self):
        return self.page.keyboard

    @allure.step
    async def async_clear(self):
        await self.input._find().press("Control+A")
        await self.input._find().press("Delete")

    @allure.step
    def get_maxlength(self) -> str:
        return self.input._get_attribute("maxlength")

    def is_disabled(self, page=None, timeout: int = WAIT_TIME_MSEC) -> bool:
        return self.input.is_disabled(page=page, timeout=timeout)

    @allure.step("Get placeholder from {0}")
    def get_placeholder(self):
        return self.input._find().get_attribute("placeholder")

    def check_equal(self, value: Union[str, None], page=None):
        if value is None:
            return
        self._check_equal(self.get_text(page=page), str(value))

    async def async_check_equal(self, value: Union[str, None]):
        if value is None:
            return
        self._check_equal(await self.async_get_text(), str(value))

    @allure.step
    def wait_for_value_to_change(self, prev_value: str = None, timeout: int = WAIT_TIME_MSEC, period: int = 50,
                                 page: Page = None):
        if prev_value is None:
            prev_value = self.get_text(page=page)
        return self._wait(lambda: self.get_text(page=page) != prev_value, timeout, period)


class ModalInput(Input):
    def __init__(self, selector: str):
        super().__init__(selector)
        self.input = Element(self.selector)


class AddDeptModalInput(Input):
    def __init__(self, selector: str):
        super().__init__(selector)
        self.input = Element(self.selector)
