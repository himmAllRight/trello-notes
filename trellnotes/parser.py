"""Contains functions for importing and parsing the json export files"""
import json


class BoardData:
    """Contains the parsed data of the trello board"""
    def __init__(self, src):
        self.src = src
        self.data = self.load_json()
        pass

    def load_json(self):
        """loads the json file into a data structre"""
        with open(self.src, 'r') as data_file:
            file_data = data_file.read()
        board_data = json.loads(file_data)
        return board_data
