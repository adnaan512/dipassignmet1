import cv2

# Load the input image
input_image = cv2.imread('input.webp')

# Resize the image to 256x256 pixels
resized_image = cv2.resize(input_image, (256, 256))

# Save the resized image
cv2.imwrite('resized_image.webp', resized_image)
