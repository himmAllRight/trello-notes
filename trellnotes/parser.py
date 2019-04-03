"""Contains functions for importing and parsing the json export files"""
import json


def load_json(src):
    """loads the json file into a data structre"""
    with open(src, 'r') as data_file:
        file_data = data_file.read()
    board_data = json.loads(file_data)
    return board_data
