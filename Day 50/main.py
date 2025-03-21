from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

EMAIL = "anisruszanna08@gmail.com"
PASSWORD = "Winter12345@"

# Set up the WebDriver
driver = webdriver.Chrome()

# Open Tinder
driver.get("http://www.tinder.com")

# Maximize the window for better visibility
driver.maximize_window()

# Wait for the cookie button to appear and click it
try:
    sleep(3)  # Extra time for the page to load
    cookie_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="t636489831"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div'))
    )
    sleep(1)  # Delay before clicking
    cookie_button.click()
    print("Accepted cookies.")
except Exception as e:
    print("Cookie button not found:", e)

# Click the login button
try:
    sleep(3)  # Extra delay to ensure the page loads completely
    login_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="t636489831"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]'))
    )
    sleep(1)
    login_button.click()
    print("Clicked login button.")
except Exception as e:
    print("Login button not found:", e)

# Click the Facebook login button
try:
    sleep(3)
    fb_login = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="t-1091891245"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button'))
    )
    sleep(1)
    fb_login.click()
    print("Clicked Facebook login button.")
except Exception as e:
    print("Facebook login button not found:", e)

# Switch to the Facebook login popup
try:
    sleep(3)  # Allow time for the popup to open
    main_window = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != main_window:
            driver.switch_to.window(handle)
            break

    print("Switched to Facebook login popup.")

    # Wait for the email field and enter the email
    email_field = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    sleep(1)
    email_field.send_keys(EMAIL)
    print("Entered email.")

    # Enter the password
    sleep(1)  # Short delay before entering password
    password_field = driver.find_element(By.ID, "pass")
    password_field.send_keys(PASSWORD)
    print("Entered password.")

    # Click the Facebook login button
    sleep(2)  # Delay before clicking login
    fb_login_button = driver.find_element(By.ID, "loginbutton")
    fb_login_button.click()
    print("Clicked Facebook login button.")

    # Wait for the "Continue as Siswa" button
    siswa_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Continue as Siswa']"))
    )
    siswa_button.click()
    print("Clicked 'Continue as Siswa' button.")

    allow_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="t-1091891245"]/div/div/div/div/div[3]/button[1]'))
    )
    allow_button.click()

    # Switch back to the main window
    sleep(5)  # Allow time for login to process
    driver.switch_to.window(main_window)
    print("Switched back to the main window.")

except Exception as e:
    print("Error during Facebook login:", e)

# Add delay to observe the result (optional)
sleep(10)

# Close the browser
driver.quit()
