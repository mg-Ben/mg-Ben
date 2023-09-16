import cv2
import numpy as np

# Load the image
image = cv2.imread('hello-world.png', cv2.IMREAD_GRAYSCALE)

# Set a threshold value (you can adjust this value based on your image)
threshold_value = 128

# Binarize the image
_, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
binary_image = cv2.bitwise_not(binary_image)

# Save the binary image
cv2.imwrite('binary_image.jpg', binary_image)

# Display the binary image (optional)
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()