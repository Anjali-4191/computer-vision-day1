import cv2
import numpy as np
import matplotlib.pyplot as plt

image_128 = np.full((256, 256), 128, dtype=np.uint8)

cv2.imwrite("Q19_intensity_128.jpg", image_128)

plt.imshow(image_128, cmap="gray", vmin=0, vmax=255)
plt.title("Q19 - Intensity 128")
plt.axis("off")
plt.show()

print("Q19 - Image created successfully.")
print("Image size:", image_128.shape)
print("Pixel value:", image_128[0, 0])