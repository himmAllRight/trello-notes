import trellnotes
import pytest


test_imput_src = 'trellnotes/tests/test-data/test-board-export.json'
print("hello")

@pytest.fixture
def test_board():
    loaded_board = trellnotes.parser.BoardData(test_imput_src)
    return loaded_board
