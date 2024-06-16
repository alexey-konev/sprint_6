import pytest
import allure

from pages.header_page import HeaderPage
from pages.yandex_page import YandexPage


class TestLogoNavigation:

    @allure.title("Проверка перехода на страницу Дзена через логотип")
    def test_click_on_yandex(self, driver):
        header_page = HeaderPage(driver)
        yandex_page = YandexPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/order")

        header_page.click_yandex_logo()
        s = driver.window_handles  # список открытых окон
        driver.switch_to.window(s[1])  # переключаемся на последнее окно
        yandex_page.find_logo()  # ждем, что страница загрузится
        assert "dzen.ru" in driver.current_url

    @allure.title("Проверка перехода на галвную старницу Самоката через логотип")
    def test_click_on_scooter(self, driver):
        header_page = HeaderPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/order")

        header_page.click_scooter_logo()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"


