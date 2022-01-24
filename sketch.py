import cv2

img=cv2.imread("ajs.jpeg")

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

invert=cv2.bitwise_not(gray)

blur=cv2.GaussianBlur(invert,(111,111),0)

invert=cv2.bitwise_not(blur)

sketch=cv2.divide(gray,invert,scale=256)

cv2.imshow("Sketch",sketch)
