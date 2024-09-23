from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from helpers.network import get_online_offline_devices
from helpers.general import get_operation_type

# Params
URL = 'http://185.185.127.219:8080/login.jsp'             # Url of the orange website
USERNAME_INPUT_ID = 'login-form-username'       # Id of username input element
PASSWORD_INPUT_ID = 'login-form-password'       # Id of password input element
SUBMIT_BTN_ID = 'login-form-submit'             # Id of submit btn
username='username'
password='password'
driver_path = "./driver/chromedriver.exe"

def initiateTask():
    online_ips, offline_ips = get_online_offline_devices(['192.168.1.68'])
    operation_type = get_operation_type()

    if operation_type == 'PI':
        print('Punch in process started...')
        print('Punching in for ips', online_ips)
    elif operation_type == 'PO':
        print('Punch out process started...')
        print('Punching out for ips', offline_ips)

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(URL)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, USERNAME_INPUT_ID))
    )

    username_input_el = driver.find_element(by=By.ID, value=USERNAME_INPUT_ID)
    password_input_el = driver.find_element(by=By.ID, value=PASSWORD_INPUT_ID)
    
    # clear
    username_input_el.clear()
    password_input_el.clear()
    
    # type
    username_input_el.send_keys(username)
    password_input_el.send_keys(password)

    # submit
    btn = driver.find_element(by=By.ID, value=SUBMIT_BTN_ID)
    # heading = driver.find_element(By.TAG_NAME, 'h1')

    driver.quit()
    print("<><><><><><> MISSION COMPLETED <><><><><><>")
    