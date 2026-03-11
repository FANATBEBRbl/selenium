from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import math

class ProductPage(BasePage):
    def click_on_bucket(self):
        self.browser.find_element(By.CLASS_NAME, "btn-add-to-basket").click()
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_names_and_price(self):
        try:
            book_name = self.browser.find_element(By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong").text
            book_price = self.browser.find_element(By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong").text
            
            assert book_name == "Coders at Work", f"Expected 'Coders at Work', got '{book_name}'"
            assert book_price == "£19.99", f"Expected '£19.99', got '{book_price}'"
            
        except NoSuchElementException:
            assert False, "Битая страница - элементы не найдены"
        except AssertionError as e:
            assert False, f"Битая страница - {str(e)}"
