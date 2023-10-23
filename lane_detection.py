import cv2
import numpy as np

# Open the test image
image = cv2.imread('test_image.jpeg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create Sobel kernels for horizontal and vertical gradients
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Initialize an output image
output_image = np.zeros_like(gray_image)

# Loop through all pixels in the image
for y in range(1, gray_image.shape[0] - 1):
    for x in range(1, gray_image.shape[1] - 1):
        # Read the pixel values around the current position
        pixel_values = gray_image[y-1:y+2, x-1:x+2]

        # Calculate the gradients using the Sobel kernels
        gradient_x = np.sum(sobel_x * pixel_values)
        gradient_y = np.sum(sobel_y * pixel_values)

        # Combine the gradients to get the magnitude
        gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

        # Normalize and invert the colors
        normalized_gradient = (255 - gradient_magnitude).astype(np.uint8)

        # Write the resulting value to the output image
        output_image[y, x] = normalized_gradient

# Save the output image
cv2.imwrite('outputimage.jpg', output_image)
cv2.imshow('test_image', image)
##Load an image from file
image = cv2.imread('outputimage.jpg')
cv2.imshow('Image', image)

# Wait for a key press and close the window when a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
