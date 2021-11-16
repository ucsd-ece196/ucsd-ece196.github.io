import cv2
import imutils
import numpy as np

frame = cv2.imread("tennis_balls.png")
frame_color = cv2.imread("tennis_balls.png")

frame = cv2.GaussianBlur(frame, (11, 11), 0)
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


ret, mask = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)

mask = cv2.erode(mask, None, iterations=3)
mask = cv2.dilate(mask, None, iterations=3)



contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

for contour in contours: 
    cv2.drawContours(frame_color, contour, -1, (0,255,0), 4)
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    box = np.int0(box)

cv2.imshow('image', frame_color)






if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()




