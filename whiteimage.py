import numpy as np
import cv2

# Define the dimensions of the image
width = 640
height = 480

# Create a white image with all pixels set to 255 (maximum intensity)
white_image = np.full((height, width), 255, dtype=np.uint8)

# Display the white image using OpenCV (you need to have OpenCV installed)
cv2.imshow("White Image", white_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

