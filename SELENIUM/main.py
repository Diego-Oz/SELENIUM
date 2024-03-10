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

search_bar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='searchBoxInput']")))
search_bar.clear()
search_bar.send_keys("paisajes")    
search_bar.send_keys(Keys.ENTER)

time.sleep(1000)

# Cerrar el navegador
driver.close()