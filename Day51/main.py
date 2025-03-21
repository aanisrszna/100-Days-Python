from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "anisruszanna08@gmail.com"
TWITTER_PASSWORD = "Winter12345@"
TWITTER_PHONE = "ARuszanna"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        """
        Uses Speedtest.net to measure internet speed and stores the upload and download speeds.
        """
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        # Accept cookies if prompted
        try:
            cont_button = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
            cont_button.click()
        except Exception:
            pass

        # Click on the "Go" button to start the test
        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        # Wait for the test to complete
        time.sleep(60)

        # Fetch download and upload speeds
        self.down = self.driver.find_element(
            By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
        ).text
        self.up = self.driver.find_element(
            By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        ).text

        print(f"Download Speed: {self.down} Mbps")
        print(f"Upload Speed: {self.up} Mbps")

    def tweet_at_provider(self):
        """
        Logs into Twitter and tweets about the internet speed.
        """
        self.driver.get("https://x.com/i/flow/login?lang=en")
        try:
            # Enter email
            email_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'))
            )
            email_field.send_keys(TWITTER_EMAIL)
            time.sleep(2)

            # Click "Next"
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]'))
            )
            next_button.click()
            time.sleep(2)

            # Enter phone if prompted
            phone_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'))
            )
            phone_field.send_keys(TWITTER_PHONE)
            time.sleep(2)

            # Click "Next"
            next2_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button'))
            )
            next2_button.click()
            time.sleep(2)

            # Enter password
            password_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))
            )
            password_field.send_keys(TWITTER_PASSWORD)
            time.sleep(2)

            # Click "Login"
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button'))
            )
            login_button.click()
            time.sleep(5)

            # Compose tweet
            tweet_box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div'))
            )
            tweet_content = (
                f"Hey Internet Provider, why is my internet speed {self.down} Mbps download and {self.up} Mbps upload "
                f"when I pay for {PROMISED_DOWN} Mbps down and {PROMISED_UP} Mbps up? #speedtest"
            )
            tweet_box.send_keys(tweet_content)
            time.sleep(3)

            # Click "Tweet"
            tweet_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button'))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", tweet_button)
            self.driver.execute_script("arguments[0].click();", tweet_button)
            time.sleep(2)

            print("Tweet successfully posted!")

        except Exception as e:
            print(f"Error during tweeting: {e}")

    def close_browser(self):
        """
        Closes the browser after all actions.
        """
        self.driver.quit()


# Instantiate the bot and perform actions
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
bot.close_browser()
