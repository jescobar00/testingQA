import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from preentrega.tests.utils import iniciarSesion

@pytest.mark.parametrize("username, password, isOrderingRequired", [
    # 1. OK: check products list is displayed
    ("standard_user", "secret_sauce", False),
    
    # 2. OK: order products by price (low to high)
    ("standard_user", "secret_sauce", True)
])
def test_products(username, password, isOrderingRequired):
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
        
        if isOrderingRequired:
            print(f"Ordering products by their price HighToLow ...")
            ddlOrder = driver.find_element(By.CLASS_NAME, "product_sort_container")
            ddlOrder.click()
            orderOptionHighLow = driver.find_element(By.CSS_SELECTOR, "option[value='hilo']")
            orderOptionHighLow.click()
            
            listOfPrices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
            firstProductPrice = (listOfPrices[0].text).split("$")[1]  # (listOfPrices[0].textContent).split("$")[1]
            secondProductPrice = (listOfPrices[1].text).split("$")[1] 
            
            print(f"the first product price is '{firstProductPrice}' and the second is '{secondProductPrice}'")
            isOrderedHighToLowPrice = float(firstProductPrice) >= float(secondProductPrice)
            assert isOrderedHighToLowPrice == True
    except Exception as e:
        # Manejar cualquier excepción que ocurra durante la prueba
        print(f"Error durante la prueba: {e}")
        raise e
    finally:
        # Cerrar el navegador
        driver.quit()