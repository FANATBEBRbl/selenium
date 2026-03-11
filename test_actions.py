from .pages.action_page import ActionPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_add_to_bucket(browser):
    page = ActionPage(browser, link)
    page.open()
    page.click_on_bucket()
    page.solve_quiz_and_get_code()
    
