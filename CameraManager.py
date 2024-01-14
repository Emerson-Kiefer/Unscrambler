import cv2

CAM_0_INDEX = 0
CAM_1_INDEX = 2

cam0 = cv2.VideoCapture(CAM_0_INDEX)

if not cam0.isOpened():
	print("Cannot open camera")
	exit()
while True:
	ret0, image0 = cam0.read()
	cv2.imshow('Image0',image0)
	k= cv2.waitKey(1)
	if k != -1:
		break

cv2.imwrite('/home/unscrambler/images/test0.jpg', image0)
cam0.release()



cam1 = cv2.VideoCapture(CAM_1_INDEX)

if not cam1.isOpened():
	print("Cannot open camera")
	exit()
while True:
	ret1, image1 = cam1.read()
	cv2.imshow('Image1',image1)
	k= cv2.waitKey(1)
	if k != -1:
		break

cv2.imwrite('/home/unscrambler/images/test1.jpg', image1)
cam1.release()
cv2.destroyAllWindows()
