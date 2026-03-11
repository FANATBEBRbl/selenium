from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.action_page import ActionPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()                      
    page.go_to_login_page()
    page = LoginPage(browser, link) 
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()