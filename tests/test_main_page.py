import pytest
import allure

from pages.main_page import MainPage
from data import Q_AND_A_SECTION


class TestMainPage:

    @allure.title("Проверка секции Q&A внизу главной страницы")
    @pytest.mark.parametrize("num, answer",
                             [
                                 (0, Q_AND_A_SECTION.get(0)),
                                 (1, Q_AND_A_SECTION.get(1)),
                                 (2, Q_AND_A_SECTION.get(2)),
                                 (3, Q_AND_A_SECTION.get(3)),
                                 (4, Q_AND_A_SECTION.get(4)),
                                 (5, Q_AND_A_SECTION.get(5)),
                                 (6, Q_AND_A_SECTION.get(6)),
                                 (7, Q_AND_A_SECTION.get(7))
                             ])
    def test_q_and_a_section(self, driver, num, answer):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")

        assert main_page.check_answer_text(num) == answer
