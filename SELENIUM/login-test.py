from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.keys import Keys
import time

# Define la ruta
chromedriver_path = r"C:\dchrome\chromedriver.exe"

# Objeto Service para manejar el driver
service = Service(chromedriver_path)

# Inicializando el webdriver
driver = webdriver.Chrome(service=service)

# Navegar a la página web
driver.get("https://www.pinterest.es/login/")

# Datos
user = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='id']")))
user.clear()
user.send_keys("pascualsebastian@gmail.com")

password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
password.clear()
password.send_keys("12345")

content = driver.find_element(By.CSS_SELECTOR, ".SignupButton")

content.click()

assert driver.current_url.startswith("https://www.pinterest.es/")

profile_image = driver.find_element(By.CSS_SELECTOR, ".zI7")

assert profile_image.is_displayed()

# Espera implícita de 10 segundos
driver.implicitly_wait(10)

# Cerrar el navegador
driver.close()