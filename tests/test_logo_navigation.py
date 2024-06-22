import pytest
import allure

from pages.header_page import HeaderPage
from pages.yandex_page import YandexPage
from data import MAIN_PAGE_URL, ORDER_PAGE_URL


class TestLogoNavigation:

    @allure.title("Проверка перехода на страницу Дзена через логотип")
    def test_click_on_yandex(self, driver):
        header_page = HeaderPage(driver)
        yandex_page = YandexPage(driver)

        header_page.open_url(ORDER_PAGE_URL)
        header_page.click_yandex_logo()

        header_page.switch_to_last_window()  # переключаемся на последнее окно
        yandex_page.find_logo()  # ждем, что страница загрузится
        assert "dzen.ru" in yandex_page.opened_page_url()

    @allure.title("Проверка перехода на главную старницу Самоката через логотип")
    def test_click_on_scooter(self, driver):
        header_page = HeaderPage(driver)
        header_page.open_url(ORDER_PAGE_URL)

        header_page.click_scooter_logo()
        assert header_page.opened_page_url() == MAIN_PAGE_URL


