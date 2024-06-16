import pytest
import allure

from pages.header_page import HeaderPage
from pages.main_page import MainPage


class TestFromMainToOrder:

    @allure.title("Проверка перехода на страницу заказа через кнопку Заказать в хэдере")
    def test_header_order_button_to_order(self, driver):
        header_page = HeaderPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")

        header_page.click_order_button()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/order"

    @allure.title("Проверка перехода на страницу заказа через кнопку Заказать на главной странице")
    def test_main_order_button_to_order(self, driver):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")

        main_page.accept_cookies()
        main_page.click_order_button()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/order"

