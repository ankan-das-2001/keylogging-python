##for screenshot functionality
from PIL import ImageGrab

def screenshot () :
    im = ImageGrab.grab()
    im.save("screenshot.png")