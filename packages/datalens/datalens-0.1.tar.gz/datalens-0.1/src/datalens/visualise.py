import random
from datalens.app import *
from colorhash import ColorHash
# from datalens.helpers import *
# Links : 
# https://packaging.python.org/tutorials/packaging-projects/

# Support for image_list and annotation_list -- data_loader
# Support for annotation type, single file or multiple files -- data_loader (check format of different datasets)
# Dynamic UI and label sizes, adjusting on changing window size by the user 
# Prevent system exit, close the window properly
# Put QT window infront of notebook tab 
# Add annotations 
# Add functionalities to support different file extensions 
	# Images - png, jpg, jpeg
	# Annotations - COCO, Kitti etc
				# - .txt, .json, graphxml
# Support for segmentation and classification  
# Support for instance vs semantic segmentation 
  # Its better to choose just semantic segmentation, so convert instance to semantic segmentation
# Data selection techniques - random, mean based, number of annotation based
# Add necessary assert statements and respective error explanantions for the user
# Easy integration format to avoid hassels, in the format used just before training


# Current Accepted format: 
# Images and Object Detection  
# - Images Directory 
# - Annotation Dictionary
		# - Key: Image Name
		# - Value: BBox List i.e. [{'bbox': [x, y, width, height], 'category_id': <int>}, ...]
# - Category id to Class Name JSON (Optional)

FONT_FACE = cv2.FONT_HERSHEY_DUPLEX
FONT_SIZE = 0.5
FONT_WEIGHT = 1
TEXT_PADDING = 3

class Visualise():
	def __init__(self, 
		datatype='images', 
		task='detection', 
		image_dir_path=None,
		annotations_dict=None,
		label_map=None,
		count = 1
		):

		self.datatype = datatype
		self.task = task 
		self.image_dir_path = image_dir_path
		self.annotations_dict = annotations_dict
		self.label_map = label_map
		self.count = count

	# def show(self):#show_image_dir_path(self, imageList, annotationList):
		image_list, filenames = self.getImageList()
		if task == "detection":
			image_list = self.mergeBBoxAnnotations(image_list, filenames)

		app = QApplication(sys.argv)
		win = AppWindow(image_list)
		win.show()
		app.exec_() # sys.exit(app.exec_())

	def mergeBBoxAnnotations(self, image_list, filenames):
		images_with_bbox = []
		annotations_list = []
		for filename in filenames:
			try:
				annotations_list.append(self.annotations_dict[filename])
			except:
				annotations_list.append(None)

		for image_index, a_image in enumerate(annotations_list):
			image = image_list[image_index]
			if a_image == None:
				images_with_bbox.append(image)
				continue

			for a_box in a_image:
				bbox = a_box['bbox']
				category_id = a_box['category_id']
				assert type(category_id) == type(1)

				left, top = int(bbox[0]), int(bbox[1])
				right, bottom = int(bbox[0]) + int(bbox[2]), int(bbox[1]) + int(bbox[3])
				
				label = self.label_map[category_id] if self.label_map != None else str(category_id)
				color = ColorHash(str(category_id)).rgb

				imgHeight, imgWidth, _ = image.shape
				thick = int((imgHeight + imgWidth) // 900)

				cv2.rectangle(image,(left, top), (right, bottom), color, thick)

				text_dim = cv2.getTextSize(label, FONT_FACE, FONT_SIZE, FONT_WEIGHT)
				total_label_height = text_dim[0][1] + text_dim[1]  + (TEXT_PADDING * 2) 
				border_offset = (thick // 2) if thick % 2 == 0 else (thick // 2) + 1

				label_left = left - border_offset
				label_top = top - total_label_height - border_offset
				if label_top < 0:
					label_top = bottom + border_offset

				text_width = text_dim[0][0]
				text_height = text_dim[0][1]
				text_baseline = text_dim[1]
				label_height = text_dim[0][1] + text_dim[1] + TEXT_PADDING * 2

				label_right = label_left + text_width + TEXT_PADDING * 2
				label_bottom = label_top + label_height

				cv2.rectangle(image, (label_left, label_top), (label_right, label_bottom), color, -1)
				cv2.putText(image, label,(label_left + TEXT_PADDING, label_top + text_height + TEXT_PADDING), FONT_FACE, FONT_SIZE,(255,255,255), FONT_WEIGHT, cv2.LINE_AA)

			images_with_bbox.append(image)
		return images_with_bbox

	def imageSelectionStrategy(self, paths):
		assert self.count <= len(paths)
		selected_paths = random.sample(paths, self.count)

		filenames = [os.path.basename(path) for path in selected_paths]
		image_list = [cv2.imread(path) for path in selected_paths]
		return image_list, filenames

	def getImageList(self):
		assert self.image_dir_path != None 
		file_type = "*.jpg"
		# Load images and annotations
		paths = glob.glob(os.path.join(self.image_dir_path, file_type))
		image_list, filenames = self.imageSelectionStrategy(paths)
		return image_list, filenames




	# def show_from_list(self, imagePathList, annotationPathList):
