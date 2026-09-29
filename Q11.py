import cv2

image = cv2.imread("image.jpeg")

if image is not None:
    x = int(input("Q11 - Enter x coordinate: "))
    y = int(input("Q11 - Enter y coordinate: "))

    height, width = image.shape[:2]

    if 0 <= x < width and 0 <= y < height:
        print("Pixel value at (x, y):", image[y, x])
    else:
        print("Error: Coordinate is outside the image.")
else:
    print("Error: Image could not be loaded.")