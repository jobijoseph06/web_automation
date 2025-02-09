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
    username_field.send_keys("test")
    password_field.send_keys("Test@123")

    driver.execute_script("arguments[0].click();", login_button)


    #select the element tag
    element = (WebDriverWait(driver, 20).
               until(EC.visibility_of_element_located((By.XPATH,
               '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
    element.click()

    #text box
    text_box = (WebDriverWait(driver, 20).
               until(EC.visibility_of_element_located((By.ID,
              'item-0'))))
    text_box.click()

    #text box content
    fullname = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'userName')))
    email = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
    current_address = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
    permanent_address = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
    #submit button
    submit_button =  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'submit')))



    #information
    fullname.send_keys("Jobi joseph")
    email.send_keys("bear062005@gmail.com")
    current_address.send_keys("Airtel tower street, melapalangur")
    permanent_address.send_keys("Airtel tower street, melapalangur")
    submit_button.click()

    upload_download = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'item-7'))))
    upload_download.click()
    download_button =  WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'downloadButton')))
    download_button.click()


    # Additional wait to observe the result
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'main-header'))  # Adjust based on the post-login behavior
    )


finally:
    # Quit the browser
    driver.quit()
