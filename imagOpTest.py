import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

#img[55,55] = [255,255,255]
#px = img[55,55]

## ROI (Region of Image)
## region to be white

# cover the image white 
#img[250:450,250:450] = [255,255,255]


# replace the location of the image
face = img[250:450,250:450]
img[0:200,0:200] = face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
