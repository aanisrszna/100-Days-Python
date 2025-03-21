import time
import pyautogui
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import detect_obstacle, jump
from config import CHECK_INTERVAL

GAME_URL = "https://elgoog.im/t-rex/"  # T-Rex game URL
BOT_STATUS_XPATH = '//*[@id="botStatus"]'  # XPath for the bot button


def open_game():
    """Open the T-Rex game in a browser, click bot status, focus the window, and start the game."""
    print("Opening Chrome T-Rex game...")

    # Launch Chrome with Selenium
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # Keep browser open
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(GAME_URL)

    time.sleep(5)  # Allow the page to load

    # Click on the "botStatus" button
    try:
        print("Clicking the bot status button...")
        bot_button = driver.find_element(By.XPATH, BOT_STATUS_XPATH)
        bot_button.click()
        print("Bot status activated!")
    except Exception as e:
        print(f"Error clicking bot button: {e}")

    time.sleep(2)

    # Get screen center coordinates
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2

    # Click the game window to bring focus
    print("Focusing on the game window...")
    pyautogui.click(x=center_x, y=center_y)
    time.sleep(1)

    # Press space to start the game
    print("Starting the game...")
    pyautogui.press("space")
    time.sleep(1)


def main():
    """Open the game, then run the T-Rex bot."""
    open_game()  # Automatically open and start the game

    print("Bot is now running... Press CTRL+C to stop.")
    while True:
        if detect_obstacle():
            jump()
            time.sleep(0.1)  # Prevent multiple jumps for the same obstacle
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
