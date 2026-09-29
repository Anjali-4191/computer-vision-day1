import cv2

image = cv2.imread("image.jpeg")

if image is not None:
    x = int(input("Q12 - Enter x coordinate: "))
    y = int(input("Q12 - Enter y coordinate: "))

    height, width = image.shape[:2]

    if 0 <= x < width and 0 <= y < height:
        image[y, x] = [0, 0, 255]

        cv2.imwrite("Q12_modified_pixel.jpg", image)

        print("Q12 - Pixel modified successfully.")
        print("Modified image saved as Q12_modified_pixel.jpg")
    else:
        print("Error: Coordinate is outside the image.")
else:
    print("Error: Image could not be loaded.")