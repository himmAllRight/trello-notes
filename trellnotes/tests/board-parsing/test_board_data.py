"""Tests the methods of the BoardData Class"""

# TODO: Expand this
def test_get_objects(test_board):
    list_objs = test_board.get_objects('lists')
    for obj in list_objs:
        assert obj.name == test_board.lists[obj.trelloid].name
