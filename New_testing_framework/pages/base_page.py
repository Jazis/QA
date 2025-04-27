from locators.locators import Locators


class BasePage:
    def __init__(self) -> None:
        self._locators: Locators = Locators()

    # def fields_are_on_page(self):
    #     for k, v in vars(self).items():
    #         print(k, v)
