import cv2
import numpy as np

img = cv2.imread('HQ1.png')
img = cv2.resize(img,None,fx=.3,fy=.3,interpolation = cv2.INTER_CUBIC)

retval , threashold = cv2.threshold(img,12,255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 165, 1)

#retval2,threshold2 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow('original',img)
#cv2.imshow('threshold',threshold)
cv2.imshow('Gaus',gaus)
#cv2.imshow('Otsu threshold',threshold2)





cv2.waitKey(0)
cv2.destroyAllWindows()
