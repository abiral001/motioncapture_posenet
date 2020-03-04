# Motion Capture using Posenet

The Project is divided into two phases:
- Video to Rig Conversion Phase (VTRC)
	
- Rig to 3D Model Conversion Phase (RT3MC)

Additionally, VTRC Phase is divided into three phases:
- Human Detection 
	
- Boundary and Heat Map Creation
	
- 2D Pose Estimation

## VTRC Phase

![VTRC Phase](https://github.com/abiral001/motioncapture_posenet/blob/master/resources/vtrc_model.png)

### Human Detection

Currently, Human Detection has been completed. To run and train the model in your computer you have to perform the following:

#### Requirements

#### Steps:

1.	Download the Coco Dataset from [COCO Datasest](http://cocodataset.org/#download).
2.	Keep the following root directory:
		
	|
	|_ dataset
	|	|
	|	|_ annotation2017
	|	|
	|	|_ train2017
	|	|
	|	|_ val2017
	|	|
	|	|_ test2017
	|
	|_ dp_json_csv.py
	|
	|_ dp_human_detection.py
	|
	|_ training_human_detection.py


3.	Run the dp_json_csv.py file directly or copy the contents to a Jupyter notebook to run gradually. This will create six files:
		- annotations_train.csv
		- annotations_val.csv
		- category_train.csv
		- category_val.csv
		- images_train.csv
		- images_val.csv

4.	Run the dp_human_detection.py. NOTE: THE SIZE OF IMAGE USED FOR PROCESSING DEPENDS ON YOUR PC'S COMPUTING POWER AND RAM. IF YOUR 	PC HAS LOTS OF RAM (>16GB), INCREASE THE IMAGE SIZE TO SOMETHING MORE THAN 128 X 128 OR ELSE REDUCE IT TO LESS THAN 80 X 80. This 	will create the following files:
		- X_test.npy
		- X_train.npy
		- X_val.npy
		- y_train.npy
		- y_val.npy

5.	Finally run the training_human_detection.py file to train a model. Th output will be Human_detection.keras 
