import allure
import pytest

from pages.base_page import BasePage
from locators import HeaderPageLocators


class HeaderPage(BasePage):

    @allure.step("Нажимаем Заказать в хэдере")
    def click_order_button(self):
        self.wait_and_click_element(HeaderPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Нажимаем Яндекс в хэдере")
    def click_yandex_logo(self):
        self.wait_and_click_element(HeaderPageLocators.YANDEX_IN_LOGO)

    @allure.step("Нажимаем Самокат в хэдере")
    def click_scooter_logo(self):
        self.wait_and_click_element(HeaderPageLocators.SCOOTER_IN_LOGO)

