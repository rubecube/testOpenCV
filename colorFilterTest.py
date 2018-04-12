import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	hav = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	

	## hsv color to filter
	lower_color = np.array([0,130,30])
	upper_color = np.array([10,255,255])
	
	
	mask = cv2.inRange(hav , lower_color, upper_color)
	
	res = cv2.bitwise_and(frame,frame,mask = mask)


	#kernel = np.ones((15,15),np.float32)/225
	#smoothed = cv2.filter2D(res,-1, kernel)

# filter for reducing noise
#	blur = cv2.GaussianBlur(res,(15,15),0)
#	median = cv2.medianBlur(res,15)
#	bilateral = cv2. bilateralFilter(res,15,75,75)

	kernel = np.ones((5,5),np.uint8)
#	erosion = cv2.erode(mask, kernel, iteration = 1)
#	dialiation = cv2.dilate(mask, kernel, iteration = 1)


# opening false positive

	opening =  cv2.morphologyEx(mask, cv2.MORPH_OPEN,kernel)
	closing =  cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernel)




	cv2.imshow('frame',frame)
	#cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	#cv2.imshow('median',median)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break	

cv2.destroyAllWindows()
cap.release()
