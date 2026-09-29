import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpeg")

if image is not None:
    blue, green, red = cv2.split(image)

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(blue, cmap="gray")
    plt.title("Q14 - Blue Channel")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(green, cmap="gray")
    plt.title("Q14 - Green Channel")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(red, cmap="gray")
    plt.title("Q14 - Red Channel")
    plt.axis("off")

    plt.show()
else:
    print("Error: Image could not be loaded.")