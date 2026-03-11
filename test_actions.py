from .pages.action_page import ActionPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ActionPage(browser, link)
    page.open()
    page.click_on_bucket()
    page.solve_quiz_and_get_code()
    page.check_names_and_price()