from selenium.webdriver.common.by import By

class StorePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.NAME, "search")
        self.search_button = (By.CLASS_NAME, "btn-lg")

    def search_product(self, product_name):
        self.driver.find_element(*self.search_bar).send_keys(product_name)
        self.driver.find_element(*self.search_button).click()
