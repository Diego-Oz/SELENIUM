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

user = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='id']")))
user.clear()
user.send_keys("pascualsebastian@gmail.com")

password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
password.clear()
password.send_keys("12345")

content = driver.find_element(By.CSS_SELECTOR, ".SignupButton")

content.click()

assert driver.current_url.startswith("https://www.pinterest.es/")

# Hacer clic en el icono de mensaje
message_icon = driver.find_element_by_css_selector(".message-icon")
message_icon.click()

# Seleccionar un usuario
user_to_message = driver.find_element_by_css_selector(".user-to-message")
user_to_message.click()

# Introducir el texto del mensaje
message_text = driver.find_element_by_id("message-text")
message_text.send_keys("Hola, ¿cómo estás?")

# Hacer clic en "Enviar"
send_button = driver.find_element_by_css_selector(".send-button")
send_button.click()

# Verificar que se muestra la notificación
notification = driver.find_element_by_css_selector(".notification")

time.sleep(1000)

# Cerrar el navegador
driver.close()
