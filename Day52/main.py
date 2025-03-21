from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "rszna2"
PASSWORD = "Winter12345@"


class InstaFollower:

    def __init__(self):
        # Optional - Keep browser open (helps diagnose issues during a crash)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)  # Wait for the page to load

        # Enter username
        username_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(USERNAME)

        # Enter password
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(PASSWORD)

        # Click login button
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

        time.sleep(5)  # Wait for login to complete

    def find_followers(self):
        # Go to the target account
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(5)  # Wait for the page to load

        # Click on followers link
        followers_link = self.driver.find_element(By.XPATH, '//a[contains(@href, "/followers/")]')
        followers_link.click()
        time.sleep(5)  # Wait for the followers modal to load

        # Scroll through the followers modal to load more followers
        modal = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]')
        for _ in range(10):  # Adjust the range for more scrolling
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        # Find all follow buttons in the followers modal
        follow_buttons = self.driver.find_elements(By.XPATH, '//button[@type="button" and .//div[text()="Follow"]]')
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(5)  # Wait between follows to avoid detection as a bot
            except Exception as e:
                print(f"Error following: {e}")


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()