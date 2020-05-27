#!/usr/bin/env python
# coding: utf-8

# In[1]:
import json
from flask import Flask, render_template, request

with open(r'DataSet_JSON\imdb_json.json', "r") as read_json:
    load_json = json.load(read_json)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('entity_identification.html')

@app.route('/', methods=['POST'])
def get_entity():
    name  = request.form['name']
    if request.form['submit_btn'] == 'Get Entity':
        for each_ind in range(len(load_json['data'])):
            if load_json['data'][each_ind][0].find(name) >= 0:
                if load_json['data'][each_ind][0] == name:
                    display_name = "{0} is".format(name)
                else:
                    display_name = "{0} dosen\'t exist but nearest Name to {1} is {2} which " \
                                   "is".format(name,name,load_json['data'][each_ind][0])
                if load_json['data'][each_ind][1] == 'GPE':
                    return "{0} a City".format(display_name)
                else:
                    return "{0} a {1}".format(display_name,load_json['data'][each_ind][1])
        else:
            return 'No Such Name exists, no nearest name found.'


if __name__ == '__main__':
    app.run()

