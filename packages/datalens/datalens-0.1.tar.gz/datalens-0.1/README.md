# Data Lens

_Visualise your dataset before training the model in one line!_

Made changes to the bounding boxes or images? 
Save time by visualising the data and avoid mistakes before starting the training process

Use Case: 
- Sanity check for the right dataset and annotations
- Dont forget to resize the bounding boxes
- Visualise what augmentation functions do to your data

Using simple GUI, visualise random images for your tasks

Installation (Python 3.6+):
~~~
pip install datalens
~~~

Usage: 
```
import datalens
datalens.Visualise(image_dir_path = image_dir_path, annotations_dict = annotations_dict, count = count)
```

Current version supports Object Detection in 2D images.

Data Formatting:
```
image_dir_path = #PATH TO IMAGE DIRECTORY
annotations_dict = #OBJECT DETECTION - {image_filename: [{"bbox": [x, y, width, height], "category_id": <int>}, ...], ...}
count = 10 #NUMBER OF IMAGES TO VISUALISE
```

Contributions are welcome for different machine learning tasks for text, images and 3D Point cloud data.
