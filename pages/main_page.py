import allure
import pytest

from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):  # наследуем общие методы

    @allure.step("Принимаем куки")
    def accept_cookies(self):
        self.wait_and_click_element(MainPageLocators.ACCEPT_COOKIES_LOCATOR)

    @allure.step("Открываем страницу и принимаем куки")
    def open_page_and_accept_cookies(self, url):
        self.open_url(url)
        self.accept_cookies()

    @allure.step("Нажимаем на вопрос")
    def click_on_question(self, num):
        formatted_locator_q = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(formatted_locator_q)  # скроллим до вопроса
        self.wait_and_click_element(formatted_locator_q)  # нажимаем на вопрос

    @allure.step("Получаем текст ответа")
    def get_text_from_answer(self, num):
        formatted_locator_a = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(formatted_locator_a)

    @allure.step("Проверяем текст ответа")
    def check_answer_text(self, num):
        self.accept_cookies()  # принимаем куки
        self.click_on_question(num)
        return self.get_text_from_answer(num)

    @allure.step("Нажимаем кнопку Заказать на главной странице")
    def click_order_button(self):
        self.wait_and_click_element(MainPageLocators.ORDER_BUTTON_MAIN_PAGE)
