import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpeg")

if image is not None:
    blue, green, red = cv2.split(image)

    merged_image = cv2.merge([blue, green, red])

    cv2.imwrite("Q15_merged_image.jpg", merged_image)

    merged_rgb = cv2.cvtColor(merged_image, cv2.COLOR_BGR2RGB)

    plt.imshow(merged_rgb)
    plt.title("Q15 - Merged Color Image")
    plt.axis("off")
    plt.show()

    print("Q15 - Channels merged successfully.")
else:
    print("Error: Image could not be loaded.")