from pages.pages import Pages


class BaseSteps:
    def __init__(self, pages: Pages) -> None:
        self.pages = pages
