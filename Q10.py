import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpeg")

if image is not None:
    height, width = image.shape[:2]

    new_width = int(width * 0.5)
    new_height = int(height * 0.5)

    resized = cv2.resize(image, (new_width, new_height))

    print("Q10 - Original Resolution:", width, "x", height)
    print("Q10 - New Resolution:", new_width, "x", new_height)

    cv2.imwrite("Q10_resized.jpg", resized)

    resized_rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

    plt.imshow(resized_rgb)
    plt.title("Q10 - Resized Image")
    plt.axis("off")
    plt.show()
else:
    print("Error: Image could not be loaded.")