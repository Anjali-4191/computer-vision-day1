import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpeg")

if image is not None:

    rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    cv2.imwrite("Q25_rotated_image.jpg", rotated)

    rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

    plt.imshow(rotated_rgb)
    plt.title("Q25 - Rotated Image")
    plt.axis("off")
    plt.show()

    print("Q25 - Image rotated by 90 degrees.")
    print("Saved as Q25_rotated_image.jpg")

else:
    print("Error: Image could not be loaded.")