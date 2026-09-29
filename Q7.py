import cv2

gray = cv2.imread("image.jpeg", cv2.IMREAD_GRAYSCALE)

if gray is not None:
    cv2.imshow("Q7 - Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image could not be loaded.")