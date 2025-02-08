from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Driver, options
chrome_option = Options()
chrome_option.add_argument("--start-maximized")  # Open browser in maximized mode
service = Service('chromedriver-win64/chromedriver.exe')  # Path to your WebDriver executable
driver = webdriver.Chrome(options=chrome_option, service=service)

try:
    # Load the web page
    driver.get('https://demoqa.com/login')

    # Locate the fields, buttons
    username_field = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, 'userName'))
    )
    password_field = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, 'password'))
    )
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'login'))
    )

    # Fill in the fields
    username_field.send_keys("jobi_07")
    password_field.send_keys("7Qh3hsnCnznr*ZW")
    login_button.click()

    # Additional wait to observe the result (optional)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'main-header'))  # Adjust based on the post-login behavior
    )
finally:
    # Quit the browser
    driver.quit()
