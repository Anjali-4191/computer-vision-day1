import cv2
import numpy as np

gray = cv2.imread("image.jpeg", cv2.IMREAD_GRAYSCALE)

if gray is not None:
    mean_intensity = np.mean(gray)

    print("Q17 - Mean Intensity:", mean_intensity)
else:
    print("Error: Image could not be loaded.")