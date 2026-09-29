import cv2
import numpy as np
import matplotlib.pyplot as plt

gray = cv2.imread("image.jpeg", cv2.IMREAD_GRAYSCALE)

if gray is not None:
    quantized_4bit = (gray // 16) * 17
    quantized_4bit = quantized_4bit.astype(np.uint8)

    cv2.imwrite("Q21_4bit_quantized.jpg", quantized_4bit)

    plt.imshow(quantized_4bit, cmap="gray", vmin=0, vmax=255)
    plt.title("Q21 - 4-bit Quantized Image")
    plt.axis("off")
    plt.show()

    print("Q21 - 4-bit quantization completed.")
else:
    print("Error: Image could not be loaded.")