from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from helper import get_mac_addr_list



url = 'http://185.185.127.219:8080/login.jsp'
username='phurba.sherpa'
password='Phurb@12'

username_input_id = 'login-form-username'
password_input_id = 'login-form-password'
submit_btn_id = 'login-form-submit'

def main():
    service = Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, username_input_id))
    )

    username_input_el = driver.find_element(by=By.ID, value=username_input_id)
    password_input_el = driver.find_element(by=By.ID, value=password_input_id)
    
    # clear
    username_input_el.clear()
    password_input_el.clear()
    
    # type
    username_input_el.send_keys(username)
    password_input_el.send_keys(password)

    # submit
    driver.find_element(by=By.ID, value=submit_btn_id).click()
    heading = driver.find_element(By.TAG_NAME, 'h1')
    title = heading.text

    time.sleep(10)
    driver.quit()
    print(title)
    
if __name__=="__main__": 
    main() 