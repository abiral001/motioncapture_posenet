import json
import pandas
import numpy

def create_csv_from_json(cat):
    json_path = 'dataset/annotations/'
    keypoints = json_path+'person_keypoints_'+cat+'2017.json'
    
    with open(keypoints) as json_file: 
        data = json.load(json_file)
    tab = 'images'
    image_frame = pandas.DataFrame()
    columns = list(data[tab][0].keys())
    height = list()
    width = list()
    ids = list()
    for dictionary in data[tab]:
        height.append(dictionary[columns[3]])
        width.append(dictionary[columns[4]])
        ids.append(dictionary[columns[7]])

    image_frame[columns[3]] = height
    image_frame[columns[4]] = width
    image_frame[columns[7]] = ids
    
    tab = 'annotations'
    annotation_frame = pandas.DataFrame()
    columns = list(data[tab][0].keys())
    segmentation = list()
    num_keypoints = list()
    area = list()
    keypoints = list()
    image_id = list()
    bbox = list()
    category_id = list()
    ids = list()

    for dictionary in data[tab]:
        segmentation.append(dictionary[columns[0]])
        num_keypoints.append(dictionary[columns[1]])
        area.append(dictionary[columns[2]])
        keypoints.append(dictionary[columns[4]])
        image_id.append(dictionary[columns[5]])
        bbox.append(dictionary[columns[6]])
        category_id.append(dictionary[columns[7]])
        ids.append(dictionary[columns[8]])

    annotation_frame[columns[0]] = segmentation
    annotation_frame[columns[1]] = num_keypoints
    annotation_frame[columns[2]] = area
    annotation_frame[columns[4]] = keypoints
    annotation_frame[columns[5]] = image_id
    annotation_frame[columns[6]] = bbox
    annotation_frame[columns[7]] = category_id
    annotation_frame[columns[8]] = ids
    
    tab = 'categories'
    categories_frame = pandas.DataFrame()
    columns = list(data[tab][0].keys())
    ids = list()
    name = list()
    keypoints = list()
    skeleton = list()
    for dictionary in data[tab]:
        ids.append(dictionary[columns[1]])
        name.append(dictionary[columns[2]])
        keypoints.append(dictionary[columns[3]])
        skeleton.append(dictionary[columns[4]])

    categories_frame[columns[1]] = ids
    categories_frame[columns[2]] = name
    categories_frame[columns[3]] = keypoints
    categories_frame[columns[4]] = skeleton
    
    image_frame.set_index('id').to_csv('images_'+cat+'.csv')
    annotation_frame.set_index('image_id').to_csv('annotation_'+cat+'.csv')
    categories_frame.set_index('id').to_csv('category_'+cat+'.csv')
    
create_csv_from_json('val')
create_csv_from_json('train')