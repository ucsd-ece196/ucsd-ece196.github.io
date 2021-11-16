import cv2


img_grayscale = cv2.imread('image.jpg',0)
# The function cv2.imshow() is used to display an image in a window.
cv2.imshow('graycsale image',img_grayscale)
# waitKey() waits for a key press to close the window and 0 specifies indefinite loop
cv2.waitKey(0)
# cv2.destroyAllWindows() simply destroys all the windows we created.
cv2.destroyAllWindows()
# The function cv2.imwrite() is used to write an image.
cv2.imwrite('grayscale.jpg',img_grayscale)
 