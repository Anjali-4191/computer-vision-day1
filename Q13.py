import cv2

image = cv2.imread("image.jpeg")

if image is not None:
    x = int(input("Q13 - Enter x coordinate: "))
    y = int(input("Q13 - Enter y coordinate: "))

    height, width = image.shape[:2]

    if 0 <= x < width and 0 <= y < height:
        blue, green, red = image[y, x]

        print("Blue value:", blue)
        print("Green value:", green)
        print("Red value:", red)
    else:
        print("Error: Coordinate is outside the image.")
else:
    print("Error: Image could not be loaded.")