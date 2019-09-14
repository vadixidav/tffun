import cv2
import numpy as np


def show(image):
    cv2.imshow("", np.array(image))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
