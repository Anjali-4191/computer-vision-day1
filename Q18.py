import cv2
import numpy as np

gray = cv2.imread("image.jpeg", cv2.IMREAD_GRAYSCALE)

if gray is not None:
    mean = np.mean(gray)
    standard_deviation = np.std(gray)

    print("Q18 - Mean:", mean)
    print("Q18 - Standard Deviation:", standard_deviation)
else:
    print("Error: Image could not be loaded.")