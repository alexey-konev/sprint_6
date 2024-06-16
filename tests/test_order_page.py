import pytest
import allure

from pages.order_page import OrderPage
from data import SET_ORDER_INFO, RANDOM_ORDER_INFO


class TestOrderPage:

    @allure.title("Проверка заказа с набором данных №1")
    @allure.description("Проверка позитивного сценария заказа самоката. Заполняются только обязательные поля."
                        "Используются заранее подготовленные данные")
    def test_order_success_with_set_data(self, driver):
        order_page = OrderPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/order")
        order_page.accept_cookies()

        order_page.fill_in_first_form(SET_ORDER_INFO["name"], SET_ORDER_INFO["surname"],
                                      SET_ORDER_INFO["address"], SET_ORDER_INFO["metro"],
                                      SET_ORDER_INFO["phone"])
        order_page.fill_in_second_form(SET_ORDER_INFO["date"], SET_ORDER_INFO["duration"])
        order_page.click_confirm_button()
        assert "Заказ оформлен" in order_page.find_confirm_order_text()

    @allure.title("Проверка заказа с набором данных №2")
    @allure.description("Проверка позитивного сценария заказа самоката. Заполняются только обязательные поля."
                        "Используются рандомно сгенерированные данные")
    def test_order_success_with_random_data(self, driver):
        order_page = OrderPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/order")
        order_page.accept_cookies()

        order_page.fill_in_first_form(RANDOM_ORDER_INFO["name"], RANDOM_ORDER_INFO["surname"],
                                      RANDOM_ORDER_INFO["address"], RANDOM_ORDER_INFO["metro"],
                                      RANDOM_ORDER_INFO["phone"])
        order_page.fill_in_second_form(RANDOM_ORDER_INFO["date"], RANDOM_ORDER_INFO["duration"])
        order_page.click_confirm_button()
        assert "Заказ оформлен" in order_page.find_confirm_order_text()

