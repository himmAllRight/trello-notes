"""Sets up needed and shared functions for testing"""


# import sys
import os

from trellnotes.parser import BoardData
from trellnotes.writer import Output
import pytest

TEST_DIR = os.path.abspath(os.path.join(os.getcwd(), 'trellnotes/tests'))
TEST_DATA = os.path.abspath(os.path.join(TEST_DIR, 'test-data'))

test_board_export = os.path.abspath(os.path.join(TEST_DATA,
                                                 'test-board-export.json'))
test_output_src = 'test_output.md'


def load_board():
    loaded_board = BoardData(test_board_export)
    return loaded_board


@pytest.fixture
def test_board():
    return load_board()


@pytest.fixture(scope='session')
def test_member():
    loaded_board = load_board()
    member = loaded_board.members['599d995a97a48d942e3cf4f2']
    return member


@pytest.fixture(scope='session')
def test_cardlist():
    loaded_board = load_board()
    cardlist = loaded_board.lists
    return cardlist


@pytest.fixture(scope='session')
def test_labels():
    loaded_board = load_board()
    labels = loaded_board.labels
    return labels


@pytest.fixture(scope='session')
def test_cards():
    loaded_board = load_board()
    cards = loaded_board.cards
    return cards


@pytest.fixture(scope='session')
def test_checklist():
    loaded_board = load_board()
    checklists = loaded_board.checklists
    return checklists


@pytest.fixture(scope='session')
def test_output():
    output_obj = Output(test_output_src)
    return output_obj
