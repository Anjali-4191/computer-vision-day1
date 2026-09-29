import cv2

image = cv2.imread("image.jpeg")

if image is None:
    print("Q2 - Error: Image failed to load. Check the file path.")
else:
    print("Q2 - Image loaded successfully.")