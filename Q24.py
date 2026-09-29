import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpeg")

if image is not None:
    x1 = int(input("Q24 - Enter starting x: "))
    y1 = int(input("Q24 - Enter starting y: "))
    x2 = int(input("Q24 - Enter ending x: "))
    y2 = int(input("Q24 - Enter ending y: "))

    height, width = image.shape[:2]

    if 0 <= x1 < x2 <= width and 0 <= y1 < y2 <= height:

        roi = image[y1:y2, x1:x2]

        cv2.imwrite("Q24_cropped_ROI.jpg", roi)

        roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

        plt.imshow(roi_rgb)
        plt.title("Q24 - Cropped ROI")
        plt.axis("off")
        plt.show()

        print("Q24 - ROI cropped successfully.")
        print("Saved as Q24_cropped_ROI.jpg")

    else:
        print("Error: Invalid coordinates.")
else:
    print("Error: Image could not be loaded.")