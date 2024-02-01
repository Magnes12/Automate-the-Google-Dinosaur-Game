import time
from PIL import Image, ImageGrab
import pyautogui


def obstacle():
    screenshot = ImageGrab.grab(bbox=(300, 150, 1000, 400))
    region = (150, 100, 250, 150)
    image = screenshot.crop(region)
    image = image.convert("L")
    template = Image.open("template.png").convert("L")
    match = pyautogui.locate(template, image, grayscale=True)

    return match is not True


game_region = (300, 150, 1000, 400)

pyautogui.click(x=game_region[0] + 50, y=game_region[1] + 50)

while True:

    if obstacle():

        pyautogui.keyDown("space")
        time.sleep(0.05)
        pyautogui.keyUp("space")

    time.sleep(0.1)
