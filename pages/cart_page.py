from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def view_cart(self):
        cart = self.driver.find_element(By.ID, "cart-total")
        cart.click()
        self.driver.implicitly_wait(5)
        view_cart_button = self.driver.find_element(By.XPATH, "//strong[normalize-space()='View Cart']")
        view_cart_button.click()

    def get_product_names(self):
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, ".table-responsive tbody tr .text-left a")
        return [product.text for product in product_elements]

    def remove_product(self):
        remove_button = self.driver.find_element(By.CSS_SELECTOR, ".table-responsive tbody tr .btn-danger")
        remove_button.click()

    def is_cart_empty(self):
        try:
            empty_cart_message = self.driver.find_element(By.XPATH, "//div[@id='content']//p[contains(text(),'Your shopping cart is empty!')]")
            return "Your shopping cart is empty!" in empty_cart_message.text
        except NoSuchElementException:
            return False
