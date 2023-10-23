import cv2
import numpy as np

# Load the image
image = cv2.imread('images.jpeg')

# Apply Unsharp Masking for sharpening
sharpened_image = cv2.addWeighted(image, 2.5, cv2.GaussianBlur(image, (0, 0), 10), -1.5, 0)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imwrite("outputimage.jpg.png", sharpened_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
