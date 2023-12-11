from os import walk
import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET

# dataloader is a functional file with functionalities concerning loading data from different files in str format
# main function which crawles through files and returns data list is load_data(directory_path), only one accesible
# for tests and running of code OS_PATH variable refers to my implementation, if path is different it need to be changed further in use

class DataLoader:

    def __init__(self, directory_path="../data"):
        self.directory_path=directory_path

    def load_data(self):
        data_folader_path=self.directory_path
        data_packs=[]
        file_paths=get_file_paths(data_folader_path)
        for file_path in file_paths:
            data_packs.append(get_file_contents(file_path))
        data=[item for file_sublist in data_packs for item in file_sublist]
        return data

#used functions

def format_read_xml(file_path):
    tree=ET.parse(file_path)
    all_users=tree.getroot()#users
    users=[]
    for user in all_users:
        firstName=user[0].text
        telephone_number=user[1].text
        email=user[2].text
        password=user[3].text
        role=user[4].text
        created_at=user[5].text
        children=[]
        for child in user[6]:
            new_child=[child[0].text, child[1].text]
            children.append(new_child)
        users.append([firstName, telephone_number, email, password, role, created_at, children])
    return users


def get_string_between(string, start_char, stop_char):#function that can be usefull
    index_1=string.index(start_char)
    index_2=string.index(stop_char)
    return string[(index_1 + len(start_char)) : index_2]
def format_read_csv(data):#change format to same as stated in xml for ease of transformation and verification
    for index, item in enumerate(data):
        children=[]
        if len(str(item[6]))>3:
            children_str=item[6]
            children_str=children_str.split(',')
            for child_str in children_str:
                name=child_str[:child_str.index('(')]
                age=get_string_between(child_str, '(', ')')
                children.append([name, age])

        data[index][6]=children
    return data


def format_read_json(data):
    # print(data)
    for index, item in enumerate(data):
        data[index][5]=str(item[5])#timestamp to string
        children=[]
        if item[6]!=[]:
            children_list=item[6]
            for child_dict in children_list:
                name=child_dict['name']
                age=child_dict['age']
                children.append([name, age])
        data[index][6]=children
    return data


def get_file_paths(data_folader_path):
    final_paths=[]
    supported_formats=[".csv", ".xml", ".json"]
    w=walk(data_folader_path)
    for (dirpath, dirnames, filenames) in w:
        for filename in filenames:
            for supported_format in supported_formats:
                if supported_format in filename[-5:]:#checcks last substring
                    final_paths.append(dirpath+"/"+filename)
                    break
    return(final_paths)

def get_file_contents(file_path):
    supported_formats=[".csv", ".xml", ".json"]

    if supported_formats[0] in file_path[-5:]:#csv
        return format_read_csv(pd.read_csv(file_path, delimiter=";").to_numpy().tolist())

    if supported_formats[1] in file_path[-5:]:#xml
        return format_read_xml(file_path)

    if supported_formats[2] in file_path[-5:]:#json
        return format_read_json(pd.read_json(file_path).to_numpy().tolist())