"""Tests that the card list objects are being set as expected"""


def get_cardlists(test_cardlist):
    list1 = test_cardlist['5ca69567b826c4317ec4971f']
    list2 = test_cardlist['5ca6956870d34940b0644a2e']
    return list1, list2


def test_cardlist_length(test_cardlist):
    """Tests the cardlist is the correct length"""
    assert len(test_cardlist) == 2


def test_cardlist_id(test_cardlist):
    """Tests the cardlist id"""
    list1, list2 = get_cardlists(test_cardlist)
    assert list1.trelloid == '5ca69567b826c4317ec4971f'
    assert list2.trelloid == '5ca6956870d34940b0644a2e'


def test_cardlist_name(test_cardlist):
    """Tests the cardlist name"""
    list1, list2 = get_cardlists(test_cardlist)
    assert list1.name == 'List A'
    assert list2.name == 'List B'


def test_cardlist_position(test_cardlist):
    """Tests the cardlist position"""
    list1, list2 = get_cardlists(test_cardlist)
    assert list1.position == 65535
    assert list2.position == 131071


def test_cardlist_closed(test_cardlist):
    """Tests the cardlist closed parameter"""
    list1, list2 = get_cardlists(test_cardlist)
    assert list1.closed == False
    assert list2.closed == False
