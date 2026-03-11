from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasketPage(BasePage):
    def empty_basket(self):
        assert "empty" in self.browser.find_element(By.CSS_SELECTOR, "#content_inner > p").text