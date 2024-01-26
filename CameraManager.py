import cv2

CAM_0_INDEX = 0
CAM_1_INDEX = 2
#CAM_INDEXES = [CAM_0_INDEX, CAM_1_INDEX]
'''
def capture_image(cam_index, cam_num):
	cam = cv2.VideoCapture(cam_index)
	
	if not cam.isOpened():
		print("Cannot open camera", i)
		return
	
	while True:
		ret, image = cam.read()
		img_name = "test_image" + str(cam_num)
		cv2.imshow(img_name, image)
		k = cv2.waitKey(1)
		if k != -1:
			break
	cv2.imwrite(IMAGE_OUTPUT_PATH + img_name + ".jpg", image)
	cam.release()

def capture_images(cam_indexes):
	for cam_num, cam_index in enumerate(cam_indexes):
		print("Camera", cam_num)
		capture_image(cam_index, cam_num)
	cv2.destroyAllWindows()
'''
class CameraManager():
	def __init__(self):
		self.IMAGE_OUTPUT_PATH = '/home/unscrambler/source/repos/Unscrambler/CubeDataset/'
		self.CAM_INDEXES = [CAM_0_INDEX, CAM_1_INDEX]
	
	def capture_image(self, cam_num, label, flag=''):
		cam = cv2.VideoCapture(self.CAM_INDEXES[cam_num])
		
		if not cam.isOpened():
			print("Cannot open camera", i)
			return
		
		while True:
			ret, image = cam.read()
			img_name = label + "-" + str(cam_num) + flag
			cv2.imshow(img_name, image)
			k = cv2.waitKey(1)
			if k != -1:
				break
		cv2.imwrite(self.IMAGE_OUTPUT_PATH + img_name + ".jpg", image)
		cam.release()
		cv2.destroyAllWindows()
		

