import random
import pytest
import string
from selenium import webdriver


@pytest.fixture()
def driver():  # инициализация драйвера
    options = webdriver.FirefoxOptions()
    options.add_argument('--window-size=1366,768')
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

