from selenium.webdriver.remote.webelement import WebElement

from scraper.common import do_and_sleep, wait_for_change


class Button:
    def __init__(self, element: WebElement) -> None:
        self.html = element

    @do_and_sleep(level=1)
    def click(self) -> None:
        self.html.click()

    def click_and_wait(self) -> None:
        with wait_for_change(self.html):
            self.html.click()