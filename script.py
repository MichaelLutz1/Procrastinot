from PIL import ImageGrab
import pytesseract

# Take a screenshot of the entire screen
screenshot = ImageGrab.grab()
print(pytesseract.image_to_string(screenshot))
# Save the screenshot to a file

# Display the screenshot
screenshot.show()
