from copy import copy
import time
from typing import Callable, Dict, List, Union
from typing_extensions import Literal

import allure
from playwright.sync_api import Locator, Page, expect, TimeoutError
from playwright.async_api import Locator as AsyncLocator, Page as AsyncPage
from utils.consts import WAIT_TIME_MSEC


def parse_attribute(attr: str, selector: str) -> str:
    attr_idx = selector.find(attr)
    end_idx = selector[attr_idx:].find("]")
    result = selector[attr_idx: end_idx + attr_idx].split("=")[-1].strip("\"'")
    return result


class Element:
    page: Page = None

    def __init__(self, selector: str):
        self.selector = selector
        self.debug_id = parse_attribute("@data-debug-id", selector)
        self.label_id = f"//*[@data-debug-id='widgets-label'][@data-debug-for='{self.debug_id}' or ancestor::*[@data-debug-id='{self.debug_id}']]"

    @allure.step("Get {0} visibility status")
    def is_visible(self, page: Page = None) -> bool:
        return self._find(page).is_visible()

    def __str__(self):
        return f"«{self.selector}»"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(selector={self.selector!r})"

    # https://playwright.dev/python/docs/locators
    # https://playwright.dev/python/docs/api/class-framelocator
    def _find(self, page: Union[Page, AsyncPage] = None) -> Union[Locator, AsyncLocator]:
        page = page or self.page
        return page.locator(self.selector)

    def find(self, page: Union[Page, AsyncPage]):
        element = copy(self)
        element.page = page
        return element

    def _wait(self, condition: Callable, timeout: int, period: int = 250) -> bool:
        while timeout:
            try:
                if condition():
                    return True
            except Exception:
                pass
            finally:
                timeout -= period
                time.sleep(period / 1000)
        else:
            return False

    def _get_inner_locators(self, selector: str, page: Page = None) -> List[Locator]:
        locator = self._find(page).locator(selector)
        return [locator.nth(i) for i in range(locator.count())]

    def _evaluate_js(self, expr: str, arg=None, page: Page = None):
        return self._find(page).evaluate(expression=expr, arg=arg)

    def _get_css_property(self, prop: str, page: Page = None):
        return self._evaluate_js(f"node => window.getComputedStyle(node).getPropertyValue({prop!r})", page=page)

    def _get_attribute(self, attr: str, page: Page = None) -> str:
        return self._find(page).get_attribute(attr)

    @allure.step("Click offset from element {0}")
    def click_offset(self, x: float = -10.0, y: float = -10.0, page: Page = None, **kwargs) -> None:
        box = self._find(page).bounding_box()
        self._find(page).page.mouse.click(box["x"] + x, box["y"] + y, **kwargs)

    @allure.step
    def get_coords(self, page: Page = None):
        box = self.bounding_box(page=page)
        return box["x"], box["y"]

    @allure.step
    def drag_to(self, x: float = None, y: float = None, target=None, page: Page = None):
        self._find(page).hover()
        if target is not None:
            self._find(page).drag_to(target._find(page), target_position={"x": 10, "y": 10})
        else:
            self.page.mouse.down()
            self.page.mouse.move(x, y)
            self._find(page).wait_for()
            self.page.mouse.up()

    @allure.step("Click element {0}")
    def click(self, page: Page = None, **kwargs) -> None:
        try:
            self._find(page).click(**kwargs)
        except Exception as e:
            raise TimeoutError(f"Error while clicking element {self}: {e}")

    @allure.step("Click element {0}")
    async def async_click(self, page: Page = None, **kwargs):
        try:
            await self._find(page).click(**kwargs)
        except Exception as e:
            raise TimeoutError(f"Error while clicking element {self}: {e}")

    def press(self, key="Shift+Enter", page: Page = None, **kwargs):
        self._find(page).press(key=key, **kwargs)

    @allure.step("Click offset from element {0}")
    async def async_click_offset(self, x: float = -10.0, y: float = -10.0, page: Page = None, **kwargs) -> None:
        box = await self._find(page).bounding_box()
        if page is None:
            await self.page.mouse.click(box["x"] + x, box["y"] + y, **kwargs)
        else:
            await page.mouse.click(box["x"] + x, box["y"] + y, **kwargs)

    # https://playwright.dev/python/docs/api/class-locator#locator-wait-for
    @allure.step("Wait for element {0} is {state}")
    def wait_for(self, state: Literal["attached", "detached", "visible", "hidden"] = "visible",
                 timeout: int = WAIT_TIME_MSEC, page: Page = None) -> bool:
        try:
            self._find(page).wait_for(state=state, timeout=timeout)
        except Exception:
            return False
        return True

    @allure.step("Wait for {0} is on page")
    def is_on_page(self, timeout: int = WAIT_TIME_MSEC, page: Page = None) -> bool:
        return self.wait_for(state="visible", timeout=timeout, page=page)

    @allure.step("Get {0} visibility status")
    def is_visible(self, page: Page = None) -> bool:
        return self._find(page).is_visible()

    @allure.step("Wait for {0} is attached")
    def is_attached(self, timeout: int = WAIT_TIME_MSEC, page: Page = None) -> bool:
        return self.wait_for(state="attached", timeout=timeout, page=page)

    @allure.step("Wait for {0} is not on page")
    def is_not_on_page(self, timeout: int = WAIT_TIME_MSEC, page: Page = None) -> bool:
        return self.wait_for(state="hidden", timeout=timeout, page=page)

    @allure.step("Wait for {0} is detached")
    def is_detached(self, timeout: int = WAIT_TIME_MSEC, page: Page = None) -> bool:
        return self.wait_for(state="detached", timeout=timeout, page=page)

    @allure.step("Expect {0} to be hidden")
    def expect_to_be_hidden(self, timeout: int = WAIT_TIME_MSEC, page=None):
        expect(self._find(page)).to_be_hidden(timeout=timeout)

    @allure.step("Expect {0} not to be hidden")
    def expect_not_to_be_hidden(self, timeout: int = WAIT_TIME_MSEC, page=None):
        expect(self._find(page)).not_to_be_hidden(timeout=timeout)

    @allure.step("Check text of element")
    def check_text(self, text: str, page=None):
        expect(self._find(page)).to_have_text(str(text))

    @allure.step("Get {0} disability status")
    def is_disabled(self, page: Page = None, timeout: int = WAIT_TIME_MSEC) -> bool:
        assert self.is_on_page(page=page, timeout=timeout), f"{self}.is_disabled(): элемент не отображается"
        el = self._find(page=page)
        pl_disabled = el.is_disabled(timeout=timeout)
        class_disabled = "disabled" in el.get_attribute("class")
        atribute_disabled = "disabled" in el.evaluate("node => node.getAttributeNames()")
        return any([pl_disabled, class_disabled, atribute_disabled])

    @allure.step("Get {0} requirement status")
    def is_required(self, page: Page = None) -> bool:
        return self.are_classes_in({"is-invalid"}, page=page)

    @allure.step("Are classes in {0}")
    def are_classes_in(self, expected: set, page: Page = None) -> bool:
        classes = self._find(page).get_attribute("class")
        if classes:
            actual_classes = set(classes.split())
            return bool(expected.intersection(actual_classes))
        return False

    @allure.step("Wait until {0} enabled")
    def wait_until_enabled(self, timeout: int = WAIT_TIME_MSEC, period: int = 250, page: Page = None) -> bool:
        return self._wait(lambda: not self.is_disabled(page=page), timeout, period)

    @allure.step("Wait until {0} disabled")
    def wait_until_disabled(self, timeout: int = WAIT_TIME_MSEC, period: int = 250, page: Page = None) -> bool:
        return self._wait(lambda: self.is_disabled(page=page), timeout, period)

    @allure.step("Wait until {0} not required")
    def wait_until_not_required(self, timeout: int = WAIT_TIME_MSEC, period: int = 250, page: Page = None) -> bool:
        return self._wait(lambda: not self.is_required(page=page), timeout, period)

    @allure.step("Wait until {0} required")
    def wait_until_required(self, timeout: int = WAIT_TIME_MSEC, period: int = 250, page: Page = None) -> bool:
        return self._wait(lambda: self.is_required(page=page), timeout, period)

    @allure.step("Get text from {0}")
    def get_text(self, page: Page = None) -> str:
        text = self._find(page).text_content()
        if text is None:
            return ""
        return text

    @allure.step("Get title from {0}")
    def get_title(self, page: Page = None):
        return self._get_attribute("title", page=page)

    @allure.step
    def wait_for_text(self, text: str, timeout: int = WAIT_TIME_MSEC, period: int = 250, page: Page = None) -> bool:
        return self._wait(lambda: self.get_text(page=page) == text, timeout, period)

    @allure.step
    def wait_for_any_text(self, timeout: int = WAIT_TIME_MSEC, period: int = 250, page: Page = None) -> bool:
        return self._wait(lambda: self.get_text(page=page), timeout, period)

    @allure.step("Hover on element {0}")
    def hover(self, page: Page = None, **kwargs) -> None:
        self._find(page).hover(**kwargs)

    def bounding_box(self, timeout: int = WAIT_TIME_MSEC, page: Page = None) -> Dict:
        return self._find(page).bounding_box(timeout=timeout)

    @allure.step
    def check_in_viewport(self, ratio: float = 1, timeout: int = WAIT_TIME_MSEC, page: Page = None):
        expect(self._find(page)).to_be_in_viewport(ratio=ratio, timeout=timeout)

    def get_style(self, locator: str = "//*[contains(@style, 'rgb')]", page: Page = None) -> str:
        if not locator:
            return self._find(page).get_attribute("style") or ""
        if self._find(page).locator(locator).count():
            return self._find(page).locator(locator).nth(0).get_attribute("style")
        return ""

    def get_label_text(self, page: Page = None):
        if page is None:
            return self.page.locator(self.label_id).text_content()
        return page.locator(self.label_id).text_content()

