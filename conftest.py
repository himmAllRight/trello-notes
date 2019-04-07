from trellnotes.parser import BoardData
import pytest

# import sys
import os

TEST_DIR = os.path.abspath(os.path.join(os.getcwd(), 'trellnotes/tests'))
TEST_DATA = os.path.abspath(os.path.join(TEST_DIR, 'test-data'))

test_board_export = os.path.abspath(os.path.join(TEST_DATA,
                                                 'test-board-export.json'))


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
