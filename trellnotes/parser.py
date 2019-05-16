"""Contains functions for importing and parsing the json export files"""
import json


class BoardData:
    """Contains the parsed data of the trello board"""
    def __init__(self, src):
        self.src = src
        self.data = self.load_json()
        self.members = self.instantiate_object('members', Member)
        self.labels = self.instantiate_object('labels', Label)
        self.cards = self.instantiate_object('cards', Card)
        self.checklists = self.instantiate_object('checklists', Checklist)
        self.lists = self.instantiate_object('lists', CardList)
        for card_list in list(self.lists.values()):
            card_list.set_cards(self.cards)

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

    def get_objects(self, data_id):
        """Returns a list of all the Objects for each data class"""
        data_dict = getattr(self, data_id)
        return list(data_dict.values())


class Member(object):
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
        self.cards = {}

    def set_cards(self, card_list):
        """Link the cards in this card list."""
        for card in list(card_list.values()):
            if self.trelloid == card.card_list:
                self.cards[card.trelloid] = card
        return self

    def output(self):
        '''Returns a string of the object's data to write to the output.'''
        return f"{self.name}\n------\n"


class Label:
    """A Trello Label"""
    def __init__(self, data):
        self.trelloid = data['id']
        self.name = data['name']
        self.color = data['color']


class Card:
    """A Trello Card"""
    def __init__(self, data):
        self.trelloid = data['id']
        self.idshort = data['idShort']
        self.name = data['name']
        self.position = data['pos']
        self.closed = data['closed']
        self.date_last_activity = data['dateLastActivity']
        self.description = data['desc']
        self.card_list = data['idList']
        self.label_ids = data['idLabels']
#        self.id_members_voted = data['idMembersVoted']
        self.short_link = data['shortLink']
        self.due_complete = data['dueComplete']
        self.due = data['due']
        self.email = data['email']
        self.short_url = data['shortUrl']
        self.url = data['url']
        self.subscribed = data['subscribed']

    def output(self):
        '''Returns a string of the card's data to write to the output.'''
        return f"{self.name}\n"


class Checklist:
    """A Trello Checklist"""
    def __init__(self, data):
        self.trelloid = data['id']
        self.name = data['name']
        self.cardID = data['idCard']
        self.position = data['pos']
        self.checkItems = [CheckListItem(item) for item in data['checkItems']]


class CheckListItem:
    """An item in a CheckList"""
    def __init__(self, data):
        self.trelloid = data['id']
        self.checklistID = data['idChecklist']
        self.name = data['name']
        self.state = data['state']
        self.position = data['pos']


class Action:
    """A Trello Action"""
    def __init__(self, data):
        pass
