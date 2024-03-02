from PIL import ImageGrab

# Take a screenshot of the entire screen
screenshot = ImageGrab.grab()

# Save the screenshot to a file
screenshot.save("screenshot.png")

# Display the screenshot
screenshot.show()
