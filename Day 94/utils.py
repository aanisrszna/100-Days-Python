import pyautogui
from PIL import ImageGrab

# Define coordinates for obstacle detection (adjust based on screen)
DETECTION_X = 600
DETECTION_Y = 400


def detect_obstacle():
    """Check if there is an obstacle in front of the dinosaur."""
    screen = ImageGrab.grab()  # Capture screen
    pixel = screen.getpixel((DETECTION_X, DETECTION_Y))  # Get pixel color

    # If pixel is dark (obstacle detected), return True
    return pixel[0] < 100 and pixel[1] < 100 and pixel[2] < 100


def jump():
    """Make the dinosaur jump."""
    pyautogui.press("space")
