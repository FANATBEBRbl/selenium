import pytest
from .pages.action_page import ActionPage
from .pages.locators import ActionPageLocators

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ActionPage(browser, link)
    page.open()
    page.click_on_bucket()
    page.solve_quiz_and_get_code()
    assert page.is_not_element_present(*ActionPageLocators.SUCCESS_MESSAGE), \
       "Показано сообщение об успехе"

def test_guest_cant_see_success_message(browser):
    page = ActionPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ActionPageLocators.SUCCESS_MESSAGE), \
       "Показано сообщение об успехе"

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ActionPage(browser, link)
    page.open()
    page.click_on_bucket()
    page.solve_quiz_and_get_code()
    assert page.is_disappeared(*ActionPageLocators.SUCCESS_MESSAGE), \
       "Сообщение не исчезло"