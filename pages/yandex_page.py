import pytest

from pages.base_page import BasePage
from locators import YandexPageLocators


class YandexPage(BasePage):

    def find_logo(self):
        self.wait_and_find_element(YandexPageLocators.DZEN_LOGO)
