import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from preentrega.tests.utils import iniciarSesion

@pytest.mark.parametrize("username, password, isRemovingRequired", [
    # 1. OK: check products are added to cart list
    ("standard_user", "secret_sauce", False),
    
    # 2. OK: check added products were removed from cart list
    ("standard_user", "secret_sauce", True)
])
def test_carrito(username, password, isRemovingRequired):
    # Configurar el controlador del navegador (por ejemplo, Chrome)
    driver = webdriver.Chrome()

    try:
        # 0) Abrir la página de inicio de sesión
        driver.get("https://www.saucedemo.com/") 
        # 1) Iniciar sesión
        iniciarSesion(driver, username, password)
        # 2) Verificar el resultado del inicio de sesión
        assert "/inventory.html" in driver.current_url
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"
        titulo = driver.find_element(By.CSS_SELECTOR,"[data-test='title']")
        assert titulo.text == "Products"
        # 3) Verificar que la lista de productos se muestre
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0, "No se encontraron productos en la lista."
        
        print(f"Adding products to cart ...")
        wait = WebDriverWait(driver, 10)
        btnAddCartBackpack = wait.until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]'))
        )
        btnAddCartBackpack.click()
          
        btnAddCartTshirt = wait.until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        btnAddCartTshirt.click()
        
        print(f"Checking quantity of products in cart ...")
        shoppingCartBadge = wait.until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]'))
        )
        quantityOfProductsInCart = int(shoppingCartBadge.text) if shoppingCartBadge.text.isdigit() else 0
        NO_PRODUCTS_ADDED_TO_CART = 2
        assert quantityOfProductsInCart == NO_PRODUCTS_ADDED_TO_CART
        print(f"OK: There are {NO_PRODUCTS_ADDED_TO_CART} products in cart red badge as expected")
      
        print(f"Opening the cart list...")
        btnShoppingCartLink = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="shopping-cart-link"]'))
        )
        btnShoppingCartLink.click()
        assert "/cart.html" in driver.current_url
        
        cartItems = driver.find_elements(By.CLASS_NAME, "cart_item") # document.getElementsByClassName("cart_item")
        assert len(cartItems) == NO_PRODUCTS_ADDED_TO_CART
        print(f"OK: The cart list contains the expected number of items: {NO_PRODUCTS_ADDED_TO_CART}")
        
        listOfExpectedProductNames = ["Backpack", "T-Shirt"]
        hasBackpack = any(listOfExpectedProductNames[0] in item.get_attribute("innerHTML") for item in cartItems)
        hasTshirt = any(listOfExpectedProductNames[1] in item.get_attribute("innerHTML") for item in cartItems)
        assert hasBackpack, f"{listOfExpectedProductNames[0]} not found in cart items."
        assert hasTshirt, f"{listOfExpectedProductNames[1]} not found in cart items."
        #assert "Backpack" in cartItems[0].get_attribute("innerHTML")
        #assert "Sauce Labs Bolt T-Shirt" in cartItems[1].get_attribute("innerHTML")
        print(f"OK: The cart list contains the expected product items: {listOfExpectedProductNames}")

        if isRemovingRequired:
            print(f"Checking if products can be removed from cart list...")
            btnRemoveBackpack = wait.until(
              EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="remove-sauce-labs-backpack"]'))
            )
            btnRemoveBackpack.click()
            btnRemoveTshirt = wait.until(
              EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="remove-sauce-labs-bolt-t-shirt"]'))
            )
            btnRemoveTshirt.click()
            
            cartItemsAfterRemoval = driver.find_elements(By.CLASS_NAME, "cart_item") # document.getElementsByClassName("cart_item")
            assert len(cartItemsAfterRemoval) == 0, f"Expected 0 items in cart after removal, but found {len(cartItemsAfterRemoval)}"
            print(f"OK: The cart list contains the expected number of items after removal: {len(cartItemsAfterRemoval)}")
    except Exception as e:
        # Manejar cualquier excepción que ocurra durante la prueba
        print(f"Error durante la prueba: {e}")
        raise e
    finally:
        # Cerrar el navegador
        driver.quit()