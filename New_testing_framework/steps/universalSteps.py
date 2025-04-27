from playwright.sync_api import expect

from steps._base import BaseSteps
from io import BytesIO

from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch


class UniversalSteps(BaseSteps):
    @staticmethod
    def assert_snapshot(img: bytes, name: str, threshold=0.1) -> None:
        image = Image.open(BytesIO(img))
        golden = Image.open(name)
        diff_pixels = pixelmatch(image, golden, threshold=threshold)
        assert diff_pixels == 0,  "Скриншоты разные"

    def check_titles_at_table(self, page, m, text):
        expect(page.locator("(//th)" + f"[{m}]")).to_have_text(text)

    def check_any_text_at_row_table(self, page, m, text):
        expect(page.locator("(//td)" + f"[{m}]")).to_have_text(text)

    def check_one_row_in_table(self, page, m, text):
        expect(page.locator("(//tr)" + f"[{m}]")).to_have_text(text)

    def check_second_title(self, page, text):
        expect(page.locator("//h2")).to_have_text(text)
