import pytest
import allure

from pages.header_page import HeaderPage
from pages.main_page import MainPage
from data import MAIN_PAGE_URL, ORDER_PAGE_URL


class TestFromMainToOrder:

    @allure.title("Проверка перехода на страницу заказа через кнопку Заказать в хэдере")
    def test_header_order_button_to_order(self, driver):
        header_page = HeaderPage(driver)
        header_page.open_url(MAIN_PAGE_URL)

        header_page.click_order_button()
        assert header_page.opened_page_url() == ORDER_PAGE_URL

    @allure.title("Проверка перехода на страницу заказа через кнопку Заказать на главной странице")
    def test_main_order_button_to_order(self, driver):
        main_page = MainPage(driver)
        main_page.open_page_and_accept_cookies(MAIN_PAGE_URL)

        main_page.click_order_button()
        assert main_page.opened_page_url() == ORDER_PAGE_URL

