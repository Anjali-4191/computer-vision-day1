import cv2

image = cv2.imread("image.jpeg")

if image is not None:
    height, width = image.shape[:2]
    total_pixels = height * width

    print("Q4 - Total Number of Pixels:", total_pixels)
else:
    print("Error: Image could not be loaded.")