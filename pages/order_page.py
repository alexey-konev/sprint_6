import allure
import pytest

from pages.base_page import BasePage
from locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Принимаем куки")
    def accept_cookies(self):
        self.wait_and_click_element(OrderPageLocators.ACCEPT_COOKIES_LOCATOR)

    @allure.step("Заполняем Имя")
    def fill_in_name(self, name):
        self.add_text_to_element(OrderPageLocators.NAME_FIELD, name)

    @allure.step("Заполняем Фамилию")
    def fill_in_surname(self, surname):
        self.add_text_to_element(OrderPageLocators.SURNAME_FIELD, surname)

    @allure.step("Заполняем Адрес")
    def fill_in_address(self, address):
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step("Выбираем Станцию метро")
    def choose_station(self, num1):
        self.wait_and_click_element(OrderPageLocators.METRO_FIELD)
        formatted_locator_s = self.format_locators(OrderPageLocators.METRO_STATION, num1)
        self.scroll_to_element(formatted_locator_s)  # скроллим до станции
        self.wait_and_click_element(formatted_locator_s)

    @allure.step("Заполняем Телефон")
    def fill_in_phone(self, phone):
        self.add_text_to_element(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step("Нажимаем кнопку Далее")
    def click_next_button(self):
        self.wait_and_click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполняем Когда привезти самокат")
    def fill_in_date(self, date):
        self.add_text_to_element(OrderPageLocators.DATE_FIELD, date)

    @allure.step("Выбираем Срок аренды")
    def choose_rental_duration(self, num2):
        self.wait_and_click_element(OrderPageLocators.RENT_DURATION_FIELD)
        formatted_locator_r = self.format_locators(OrderPageLocators.RENT_DURATION_OPTION, num2)
        self.wait_and_click_element(formatted_locator_r)

    @allure.step("Нажимаем кнопку Заказать под формой заказа")
    def click_order_button(self):
        self.wait_and_click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтверждаем заказ")
    def click_confirm_button(self):
        self.wait_and_click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Получаем текст окна о завершении заказа")
    def find_confirm_order_text(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_CONFIRMED_MESSAGE)

    @allure.step("Заполняем первую форму заказа и нажимаем Далее")
    def fill_in_first_form(self, name, surname, address, num1, phone):
        self.fill_in_name(name)
        self.fill_in_surname(surname)
        self.fill_in_address(address)
        self.choose_station(num1)
        self.fill_in_phone(phone)
        self.click_next_button()

    @allure.step("Заполняем вторую форму заказа и нажимаем Заказать")
    def fill_in_second_form(self, date, num2):
        self.fill_in_date(date)
        self.choose_rental_duration(num2)
        self.click_order_button()






