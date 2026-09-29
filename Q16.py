import cv2
import numpy as np

gray = cv2.imread("image.jpeg", cv2.IMREAD_GRAYSCALE)

if gray is not None:
    minimum = np.min(gray)
    maximum = np.max(gray)

    print("Q16 - Minimum Intensity:", minimum)
    print("Q16 - Maximum Intensity:", maximum)
else:
    print("Error: Image could not be loaded.")