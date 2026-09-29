import cv2
import numpy as np
import matplotlib.pyplot as plt

gray = cv2.imread("image.jpeg", cv2.IMREAD_GRAYSCALE)

if gray is not None:
    quantized_2bit = (gray // 64) * 85
    quantized_2bit = quantized_2bit.astype(np.uint8)

    cv2.imwrite("Q22_2bit_quantized.jpg", quantized_2bit)

    plt.imshow(quantized_2bit, cmap="gray", vmin=0, vmax=255)
    plt.title("Q22 - 2-bit Quantized Image")
    plt.axis("off")
    plt.show()

    print("Q22 - 2-bit quantization completed.")
else:
    print("Error: Image could not be loaded.")