import cv2

image = cv2.imread("image.jpeg")

if image is not None:
    height, width = image.shape[:2]

    new_width = width // 2
    new_height = height // 2

    downsampled = cv2.resize(
        image,
        (new_width, new_height),
        interpolation=cv2.INTER_AREA
    )

    print("Q23 - Original Resolution:")
    print(width, "x", height)

    print("Q23 - New Resolution:")
    print(new_width, "x", new_height)

    cv2.imwrite("Q23_downsampled.jpg", downsampled)
else:
    print("Error: Image could not be loaded.")