import cv2

image = cv2.imread("image.jpeg")

if image is not None:
    print("Q5 - Data Type:", image.dtype)
else:
    print("Error: Image could not be loaded.")