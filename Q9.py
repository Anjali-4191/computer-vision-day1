import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpeg")

if image is not None:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(image_rgb)
    plt.title("Q9 - Image using Matplotlib")
    plt.axis("off")
    plt.show()
else:
    print("Error: Image could not be loaded.")