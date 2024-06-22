import pytest
import allure

from pages.base_page import BasePage
from locators import YandexPageLocators


class YandexPage(BasePage):

    @allure.step("С ожиданием ищем логотип Дзена")
    def find_logo(self):
        self.wait_and_find_element(YandexPageLocators.DZEN_LOGO)
