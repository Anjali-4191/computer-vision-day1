import cv2
import numpy as np
import matplotlib.pyplot as plt

ramp = np.tile(np.arange(256, dtype=np.uint8), (256, 1))

cv2.imwrite("Q20_intensity_ramp.jpg", ramp)

plt.imshow(ramp, cmap="gray", vmin=0, vmax=255)
plt.title("Q20 - Grayscale Intensity Ramp")
plt.axis("off")
plt.show()

print("Q20 - Intensity ramp created successfully.")