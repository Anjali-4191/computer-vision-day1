import cv2

image = cv2.imread("image.jpeg")

if image is not None:
    cv2.imwrite("Q6_saved_image.jpg", image)
    print("Q6 - Image saved successfully.")
else:
    print("Error: Image could not be loaded.")