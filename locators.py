from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.ID, "accordion__heading-{}"
    ANSWER_LOCATOR = By.ID, "accordion__panel-{}"
    ACCEPT_COOKIES_LOCATOR = By.ID, "rcc-confirm-button"
    ORDER_BUTTON_MAIN_PAGE = By.XPATH, ".//*[contains(@class, 'Home_FinishButton')]/*[contains(@class, 'Button_Button')]"


class OrderPageLocators:
    ACCEPT_COOKIES_LOCATOR = By.ID, "rcc-confirm-button"
    NAME_FIELD = By.XPATH, ".//*[@placeholder = '* Имя']"
    SURNAME_FIELD = By.XPATH, ".//*[@placeholder = '* Фамилия']"
    ADDRESS_FIELD = By.XPATH, ".//*[@placeholder = '* Адрес: куда привезти заказ']"
    METRO_FIELD = By.XPATH, ".//*[@placeholder = '* Станция метро']"
    METRO_STATION = By.XPATH, ".//li[@data-value = '{}']/*[contains(@class, 'Order_SelectOption')]"
    PHONE_FIELD = By.XPATH, ".//*[@placeholder = '* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, ".//*[contains(@class, 'Button_Button') and text()='Далее']"
    DATE_FIELD = By.XPATH, ".//*[@placeholder = '* Когда привезти самокат']"
    RENT_DURATION_FIELD = By.XPATH, ".//*[@class = 'Dropdown-arrow']"
    RENT_DURATION_OPTION = By.XPATH, ".//*[@class = 'Dropdown-option' and text() = '{}']"
    ORDER_BUTTON = By.XPATH, (".//*[contains(@class, 'Order_Buttons')]/*[contains(@class, 'Button_Button')"
                              " and text() = 'Заказать']")
    CONFIRM_ORDER_BUTTON = By.XPATH, (".//*[contains(@class, 'Order_Buttons')]/*[contains(@class, 'Button_Button')"
                                      " and text() = 'Да']")
    ORDER_CONFIRMED_MESSAGE = By.XPATH, ".//*[contains(@class, 'Order_ModalHeader')]"


class HeaderPageLocators:
    ORDER_BUTTON_HEADER = By.XPATH, ".//*[contains(@class, 'Header_Nav')]/*[contains(@class, 'Button_Button')]"
    YANDEX_IN_LOGO = By.XPATH, ".//*[contains(@class, 'Header_LogoYandex')]"
    SCOOTER_IN_LOGO = By.XPATH, ".//*[contains(@class, 'Header_LogoScooter')]"


class YandexPageLocators:
    DZEN_LOGO = By.XPATH, ".//*[contains(@class, 'desktop-base-header__logoContainer')]"


