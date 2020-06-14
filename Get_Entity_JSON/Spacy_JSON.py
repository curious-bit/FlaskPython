#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import re 
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm

imdb_data = pd.read_csv(r"IMDB Dataset.csv")
print(imdb_data.head())
print(imdb_data.shape)

imdb_data_col1 = imdb_data.iloc[:5000,0]
print(imdb_data_col1)

imdb_filter = []
for line in imdb_data_col1:
    imdb_filter.append(preprocess(line))
    
print(len(imdb_filter))
    
def preprocess(sentence):
    sentence=str(sentence)
    sentence = sentence.lower()
    return_list = ''.join(e for e in sentence if e.isalnum() or e == " ")
    return return_list

data_list = []
count = 0
def entity_indentify(sentence):
    nlp = en_core_web_sm.load()
    doc = nlp(sentence)
    for X in doc.ents:
        if X.label_ == 'PERSON' or X.label_ == 'GPE':
            data_list.append([X.text,X.label_])
                        
for sentence in imdb_filter:
    entity_indentify(sentence)
    count += 1
    if count % 100 == 0:
        print(count)
print(len(data_list))

print(len(data_list))
import numpy as np
print(np.unique(data_list))

data_frame_reduced = pd.DataFrame(np.unique(data_list), columns = ['Item', 'Entity'])
data_frame_reduced.to_json(r'C:\Users\AM20111609\Downloads\imdb-dataset-of-50k-movie-reviews\data_map_unique.json',orient='split')


data_list_frame = pd.DataFrame(data_list, columns = ['Item', 'Entity']) 
print(data_list_frame)
data_list_frame.to_json(r'C:\Users\AM20111609\Downloads\imdb-dataset-of-50k-movie-reviews\data_map.json',orient='split')


import json
with open(r'C:\Users\AM20111609\Downloads\imdb-dataset-of-50k-movie-reviews\data_map.json', "r") as read_file:
    load_json = json.load(read_file)
    
print(load_json['data'])

for each in range(len(load_json['data'])):
    if load_json['data'][each][0].find("new york") >= 0:
        print(load_json['data'][each])

