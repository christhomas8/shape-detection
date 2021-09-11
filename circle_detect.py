import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

image = cv2.imread('bw.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.5, 100)

for i in circles[0,:]:
	#draw outer circle
	cv2.circle(image,(i[0], i[1]), i[2], (255, 0 ,0), 2)

	#draw the center of the circle
	cv2.circle(image, (i[0], i[1]), 2, (0,255,0), 5)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Circle Detection')
plt.show()
cv2.imwrite('photograph.jpg',image)

