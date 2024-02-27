import cv2
import numpy as np

# Create a NumPy array
data = np.zeros((300, 400, 3), dtype=np.uint8)  # Example: A black image

# Convert the NumPy array to an image
image = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)

# Display the image (optional)
cv2.imshow("NumPy Array to Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
