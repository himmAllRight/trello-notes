import trellnotes.parser
import pytest

# Global variable of test input file
test_imput_src = 'test-data/test-board-export.json'


# Just until I get a better sample input file I can use to test what I already
# have.pytest.fixture
def test_board():
    loaded_board = trellnotes.parser.BoardData(test_imput_src)
    return loaded_board


def test_data(test_board):
    assert test_board.src == test_imput_src


def test_members(test_board):
    """Tests the member list and objects are loaded correctly"""
    assert len(test_board.members) == 1

    member = test_board.members[0]
    assert member.username == 'ryanhimmelwright'
    assert member.full_name == 'Ryan Himmelwright'
