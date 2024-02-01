import cv2
from PIL import ImageGrab
import numpy as np


class Object:

    def __init__(self, path):
        img = cv2.imread(path, 0)
        self.img = img
        self.width = img.shape[1]
        self.height = img.shape[0]
        self.location = None

    def match(self, scr):
        res = cv2.matchTemplate(scr, self.img, cv2.TM_CCOEFF_NORMED)
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
        startLoc = maxLoc
        endLoc = (startLoc[0]+self.width, startLoc[1]+self.height)

        if maxVal > 0.8:
            self.location = (startLoc, endLoc)
            return True
        else:
            self.location = None
            return False
