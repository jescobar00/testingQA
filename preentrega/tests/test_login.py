import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from preentrega.tests.utils import iniciarSesion

@pytest.mark.parametrize("username, password, esValido, expectedIndicator", [
    # 1. OK / Successful Login (Checking if URL changes to inventory)
    ("standard_user", "secret_sauce", True, "inventory.html"),
    
    # 2. Error: Unregistered User 
    ("wrong_user", "secret_sauce", False, "Epic sadface: Username and password do not match"),
    
    # 3. Error: Locked User
    ("locked_out_user", "secret_sauce", False, "Epic sadface: Sorry, this user has been locked out.")
])
def test_login(username, password, esValido, expectedIndicator):
    # Configurar el controlador del navegador (por ejemplo, Chrome)
    driver = webdriver.Chrome()

    try:
        # 0) Abrir la página de inicio de sesión
        driver.get("https://www.saucedemo.com/") 
        # 1) Iniciar sesión
        iniciarSesion(driver, username, password)
        # 2) Verificar el resultado del inicio de sesión
        if esValido:
            # success_message = wait.until(EC.presence_of_element_located((By.ID, "success-message")))  # Cambia el selector según tu aplicación
            # assert success_message.is_displayed(), "El mensaje de éxito no se muestra."
            logo = driver.find_element(By.CLASS_NAME, "app_logo")
            assert logo.text == "Swag Labs"

            titulo = driver.find_element(By.CSS_SELECTOR,"[data-test='title']")
            assert titulo.text == "Products"
            
            assert "/inventory.html" in driver.current_url
        else:
            wait = WebDriverWait(driver, 10) #  $x("//h3[@data-test='error']")[0].textContent
            error_element = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']")))
            assert expectedIndicator in error_element.text
    except Exception as e:
        # Manejar cualquier excepción que ocurra durante la prueba
        print(f"Error durante la prueba: {e}")
        raise e
    finally:
        # Cerrar el navegador
        driver.quit()