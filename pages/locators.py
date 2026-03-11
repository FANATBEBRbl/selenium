from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    INVALID_LOGIN_LINK = (By.CSS_SELECTOR, "#invalid_login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REG_INPUT_EMAIL = (By.ID, "id_registration-email")
    REG_INPUT_PASS1 = (By.ID, "id_registration-password1")
    REG_INPUT_PASS2 = (By.ID, "id_registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")
    THX_TEXT = (By.CSS_SELECTOR, "#messages > div.alert.alert-success.fade.in > div")

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By. CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")