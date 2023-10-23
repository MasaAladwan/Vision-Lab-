import numpy as np
import cv2 as cv

# Load the input image
input_image = cv.imread("test_image.jpeg")


 # Invert the image using NumPy vectorized operations
inverted_image = 255 - input_image

# Display the inverted image
cv.imshow("Inverted Image", inverted_image)

# Save the inverted image
cv.imwrite("InvertedImage.png", inverted_image)
cv.imshow('Image', input_image)
# Wait for a key press and close the window
cv.waitKey(0)
cv.destroyAllWindows()
