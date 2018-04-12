import numpy as np 
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)


# draw a line (file, start, stop, color[b,g,r], [width])
cv2.line(img,(0,0),(150,150),(255,255,0), 15)

# draw rectagle (file, top left, bottom right,color, width)
cv2.rectangle(img,(15,25),(200,150),(0,0,0),5)

# draw a circle ( file, center, radious, color, width)
cv2.circle(img,(100,63),55,(0,0,255),-1)

# draw POLYGON 

pts = np.array([[10,4],[20,6],[50,50],[70,20],[50,10]],np.int32)
#pts = pts.reshape(-1,1,2)

# (file, points, connect last point, color, width)
cv2.polylines(img,[pts],True,(0,0,0),5)

## put text  
font = cv2.FONT_HERSHEY_SIMPLEX
## (file, text, location, font, size, color ,width)
cv2.putText(img, 'OPENCV',(0,130),font,1,(200,200,200),2)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
