import cv2

image = cv2.imread("image.jpeg")

if image is not None:
    cv2.imshow("Q1 - Original Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image could not be loaded.")