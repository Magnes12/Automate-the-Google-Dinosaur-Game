from PIL import ImageGrab
import time
import pyautogui as pag
import cv2
import numpy as np
from classes import Object

player_index = 0
enemies_index = 0

player = [Object('objects/dino.png'), Object('objects/dino_b.png')]
enemies = [
    [Object('objects/cact1.png'), Object('objects/cact2.png'), Object('objects/bird.png')],
    [Object('objects/cact1_b.png'), Object('objects/cact2_b.png'), Object('objects/bird_b.png')],
]


def grabSs(bbox=None):
    img = ImageGrab.grab(bbox=bbox)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img


while True:
    img = grabSs()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if player[0].match(img):
        top_left_x = int(player[0].location[0][0] - player[0].width)
        top_left_y = int(player[0].location[0][1] - 3*player[0].height)
        bottom_right_x = int(player[0].location[1][0] + 14*player[0].width)
        bottom_right_y = int(player[0].location[1][1] + 0.5*player[0].height)
        screenStart = (top_left_x, top_eft_y)
        screenEnd = (bottom_right_x, bottom_right_y)
        break
l
pag.press('space')

while True:

    img_1 = grabSs(bbox=(*screenStart, *screenEnd))
    img = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)

    if player[0].match(img):
        player_index = 0
        enemies_index = 0
    elif player[1].match(img):
        player_index = 1
        enemies_index = 1

    cv2.imshow("Screen", img)

    if cv2.waitKey(0) == ord('q'):
        break
