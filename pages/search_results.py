from selenium.webdriver.common.by import By

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_product = (By.PARTIAL_LINK_TEXT, "iPhone")

    def select_first_product(self):
        self.driver.find_element(*self.first_product).click()
