from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def iniciarSesion(driver, username, password):
    """
    A partir de un "selenium.webdriver", inicia sesión en SauceDemo.
    """
    # 1) Abrir la página de inicio de sesión
    #driver.get("https://www.saucedemo.com/") 
    
    # 2) Esperar a que los elementos estén presentes
    wait = WebDriverWait(driver, 10)
    txtUsername = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    txtPassword = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    ## btnLogin = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    btnLogin = wait.until(EC.element_to_be_clickable((By.ID,"login-button")))

    # 3) Ingreso de credenciales
    txtUsername.clear()
    txtUsername.send_keys(username)
    txtPassword.clear()
    txtPassword.send_keys(password)
    btnLogin.click()