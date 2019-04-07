"""Tests that the card objects are being set as expected"""


def get_cards(test_cards):
    card1 = test_cards['5ca69576a8eb8a041854896a']
    card2 = test_cards['5ca6961225bbb14b254dd829']
    card3 = test_cards['5ca69616babd363d99f53e9d']
    card4 = test_cards['5ca696b7ccdaee7e3731479a']
    return card1, card2, card3, card4


def test_card_count(test_cards):
    """Tests the number of labels"""
    assert len(test_cards) == 4


def test_labels_id(test_cards):
    '''Test the label ids are set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    card1.trelloid = '5ca69576a8eb8a041854896a'
    card2.trelloid = '5ca6961225bbb14b254dd829'
    card3.trelloid = '5ca69616babd363d99f53e9d'
    card4.trelloid = '5ca696b7ccdaee7e3731479a'
