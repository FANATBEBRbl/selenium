import pytest
from .pages.action_page import ActionPage
from .pages.locators import ActionPageLocators

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

@pytest.mark.negative_checks
class TestNegativeChecks:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = ActionPage(browser, link)
        self.page.open()

    @pytest.mark.xfail(reason="Сообщение об успехе появилось")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        self.page.click_on_bucket()
        self.page.solve_quiz_and_get_code()
        assert self.page.is_not_element_present(*ActionPageLocators.SUCCESS_MESSAGE), \
           "Сообщение об успехе появилось, но не должно было"

    def test_guest_cant_see_success_message(self, browser):
        assert self.page.is_not_element_present(*ActionPageLocators.SUCCESS_MESSAGE), \
           "Сообщение об успехе появилось, но не должно было"

    @pytest.mark.xfail(reason="Сообщение не исчезло")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        self.page.click_on_bucket()
        self.page.solve_quiz_and_get_code()
        assert self.page.is_disappeared(*ActionPageLocators.SUCCESS_MESSAGE), \
           "Сообщение не исчезло, но должно было"