import pyautogui

# Get screen size
screen_width, screen_height = pyautogui.size()

# Define game region (update these values based on your screen)
GAME_REGION = (screen_width // 3, screen_height // 2, 300, 100)  # (x, y, width, height)

# Pixel threshold to detect obstacles (dark pixels)
PIXEL_THRESHOLD = 100

# Delay settings
CHECK_INTERVAL = 0.02  # Adjust reaction time
