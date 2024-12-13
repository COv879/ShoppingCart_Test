import unittest
from pages.store_page import StorePage
from pages.cart_page import CartPage
from pages.search_results import SearchResultsPage
from pages.product import ProductPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestCart(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://opencart.abstracta.us/")

        self.store_page = StorePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_add_and_remove_product(self):
        # Usa la lógica de tu POM aquí
        self.store_page.search_product("iPhone")
        self.search_results_page.select_first_product()
        self.product_page.add_to_cart()
        self.cart_page.view_cart()

        # Validación de que el producto esté en el carrito
        self.assertIn("iPhone", self.cart_page.get_product_names())
        print("✅ Validación: El iPhone está en el carrito.")

        # Remueve el producto y valida que el carrito esté vacío
        self.cart_page.remove_product()
        self.assertTrue(self.cart_page.is_cart_empty())
        print("✅ Validación: El carrito está vacío.")


