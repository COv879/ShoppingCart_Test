from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = (By.ID, "button-cart")

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()