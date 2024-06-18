import pytest
import allure

from pages.order_page import OrderPage
from data import SET_ORDER_INFO, RANDOM_ORDER_INFO, ORDER_PAGE_URL


class TestOrderPage:

    @allure.title("Проверка заказа с набором данных №1")
    @allure.description("Проверка позитивного сценария заказа самоката. Заполняются только обязательные поля."
                        "Используются заранее подготовленные данные")
    def test_order_success_with_set_data(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page_and_accept_cookies(ORDER_PAGE_URL)

        order_page.fill_in_first_form(SET_ORDER_INFO)
        order_page.fill_in_second_form(SET_ORDER_INFO)
        order_page.click_confirm_button()
        assert "Заказ оформлен" in order_page.find_confirm_order_text()

    @allure.title("Проверка заказа с набором данных №2")
    @allure.description("Проверка позитивного сценария заказа самоката. Заполняются только обязательные поля."
                        "Используются рандомно сгенерированные данные")
    def test_order_success_with_random_data(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page_and_accept_cookies(ORDER_PAGE_URL)

        order_page.fill_in_first_form(RANDOM_ORDER_INFO)
        order_page.fill_in_second_form(RANDOM_ORDER_INFO)
        order_page.click_confirm_button()
        assert "Заказ оформлен" in order_page.find_confirm_order_text()

