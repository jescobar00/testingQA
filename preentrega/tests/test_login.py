from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    # Configurar el controlador del navegador (por ejemplo, Chrome)
    driver = webdriver.Chrome()

    try:
        # Abrir la página de inicio de sesión
        driver.get("https://www.saucedemo.com/") 

        # Esperar a que los elementos estén presentes
        wait = WebDriverWait(driver, 10)
        txtUsername = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        txtPassword = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        btnLogin = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

        # Ingresar las credenciales de inicio de sesión
        txtUsername.send_keys("testuser")  # Cambia esto según tu usuario de prueba
        txtPassword.send_keys("testpassword")  # Cambia esto según tu contraseña de prueba

        # Hacer clic en el botón de inicio de sesión
        btnLogin.click()

        # Verificar que se haya iniciado sesión correctamente
        success_message = wait.until(EC.presence_of_element_located((By.ID, "success-message")))  # Cambia el selector según tu aplicación
        assert success_message.is_displayed(), "El mensaje de éxito no se muestra."
        assert "/inventory.html" in driver.current_url
    finally:
        # Cerrar el navegador
        driver.quit()