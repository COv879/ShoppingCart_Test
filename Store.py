from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://opencart.abstracta.us/")

    # Buscar iPhone
    search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search"))
    )
    search_bar.send_keys("iPhone")

    search_button = driver.find_element(By.CLASS_NAME, "btn-lg")
    search_button.click()

    iphone = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "iPhone"))
    )
    iphone.click()

    add_to_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "button-cart"))
    )
    add_to_cart.click()

    cart = driver.find_element(By.ID, "cart-total")
    cart.click()

    view_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//strong[normalize-space()='View Cart']"))
    )
    view_cart.click()

    # Validar que el iPhone está en el carrito
    product_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table-responsive tbody tr .text-left a"))
    )
    assert "iPhone" in product_name.text, "El producto iPhone no está en el carrito de compras."
    print("✅ Validación: El iPhone está en el carrito de compras.")

    # Remover el producto
    remove_button = driver.find_element(By.CSS_SELECTOR, ".table-responsive tbody tr .btn-danger")
    remove_button.click()

    # Validar carrito vacío
    empty_cart_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='content']//p[contains(text(),'Your shopping cart is empty!')]"))
    )
    assert "Your shopping cart is empty!" in empty_cart_message.text, "El carrito no está vacío."
    print("✅ Validación: El carrito está vacío.")
    
except NoSuchElementException as e:
    print(f"❌ Error: {e}")
finally:
    driver.quit()
