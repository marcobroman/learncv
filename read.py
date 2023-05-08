import cv2 as cv

#read img
img = cv.imread("img/duck.JPG")
cv.imshow("duck",img)
cv.waitKey(0)