from trellnotes.parser import BoardData
import pytest

# Global variable of test input file
test_imput_src = '/home/ryan/Documents/Programming/python/trello-notes/trellnotes/tests/test-data/test-board-export.json'


def test_members(test_board):
    """Tests the member list and objects are loaded correctly"""
    assert len(test_board.members) == 1

    member = test_board.members['599d995a97a48d942e3cf4f2']
    assert member.username == 'ryanhimmelwright'
    assert member.full_name == 'Ryan Himmelwright'
