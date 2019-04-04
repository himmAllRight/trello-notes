"""Contains functions for importing and parsing the json export files"""
import json


class BoardData:
    """Contains the parsed data of the trello board"""
    def __init__(self, src):
        self.src = src
        self.data = self.load_json()
        self.members = self.instantiate_object('members', Member)
        self.lists = self.instantiate_object('lists', CardList)

    def load_json(self):
        """loads the json file into a data structre"""
        with open(self.src, 'r') as data_file:
            file_data = data_file.read()
        board_data = json.loads(file_data)
        return board_data

    def instantiate_object(self, data_id, class_name):
        """Parses through and instantiates all objects for a class."""
        object_list = {}
        for item_data in self.data[data_id]:
            obj = class_name(item_data)
            object_list[obj.trelloid] = obj
        return object_list


class Member:
    """A Trello Board Member"""
    def __init__(self, data):
        self.trelloid = data['id']
        self.username = data['username']
        self.full_name = data['fullName']
        self.url = data['url']
        self.bio = data['bio']


class CardList:
    """A List of Trello Cards"""
    def __init__(self, data):
        self.trelloid = data['id']
        self.name = data['name']
        self.closed = data['closed']
        self.position = data['pos']

class Label:
    """A Trello Label"""
    def __init__(self, data):
        pass


class Card:
    """A Trello Card"""
    def __init__(self, data):
        pass


class checklist:
    """A Trello Checklist"""
    def __init__(self, data):
        pass


class Action:
    """A Trello Action"""
    def __init__(self, data):
        pass
