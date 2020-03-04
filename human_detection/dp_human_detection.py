import pandas as pd
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt

images_train_csv = pd.read_csv('images_train.csv')
annotation_train_csv = pd.read_csv('annotation_train.csv')
category_train_csv = pd.read_csv('category_train.csv')
images_val_csv = pd.read_csv('images_val.csv')
annotation_val_csv = pd.read_csv('annotation_val.csv')
category_val_csv = pd.read_csv('category_val.csv')

images_train_path = 'dataset/train2017/'
images_val_path = 'dataset/val2017/'
images_test_path = 'dataset/test2017/'

def create_data(images_path, annotation_dataframe, image_res = (64, 64), is_test = False):
    read_path = images_path
    directory = sorted(os.listdir(read_path))
    size_of_directory = len(directory)
    data_human_classifier = list()
    for image in directory:
        read_image = cv2.imread(read_path+image, cv2.IMREAD_GRAYSCALE)
        read_image = cv2.resize(read_image, image_res, interpolation = cv2.INTER_AREA)
        read_image = np.asarray(read_image)
        ## for label to extract from the respective csv file
        if is_test == False:
            if int(image.split('.')[0]) in annotation_dataframe.image_id.unique():
                label = 1
            else:
                label = 0
            data_human_classifier.append([read_image, label])
        else:
            data_human_classifier.append(read_image)
        print('Processed {} file {} out of {}'.format(int(image.split('.')[0]), 
                                                      directory.index(image)+1, 
                                                      size_of_directory))
        
    return data_human_classifier

data_val = create_data(images_val_path, annotation_val_csv, (80, 80))
X_val = list()
y_val = list()
for x, y in data_val:
    X_val.append(x)
    y_val.append(y)
    
X_val = np.asarray(X_val)
X_val = np.reshape(X_val, (-1, 80, 80, 1))
y_val = np.asarray(y_val)

np.save('X_test.npy', X_test)

data_train = create_data(images_train_path, annotation_train_csv, (80, 80))
X_train = list()
y_train = list()

for x, y in data_train:
    X_train.append(x)
    y_train.append(y)
    
X_train = np.asarray(X_train)
X_train = np.reshape(X_train, (-1, 80, 80, 1))
y_train = np.asarray(y_train)

np.save('X_train.npy', X_train)
np.save('y_train.npy', y_train)