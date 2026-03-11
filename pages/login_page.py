from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login page is no opened yet"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.browser.find_element(*LoginPageLocators.REG_INPUT_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_INPUT_PASS1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_INPUT_PASS2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((LoginPageLocators.THX_TEXT)))
        except TimeoutException:
            assert False, "Element not found"