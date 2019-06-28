"""Tests that the card objects are being set as expected"""


def get_cards(test_cards):
    '''Gets test cards by their id's and returns to 4 vars.'''
    card1 = test_cards['5ca69576a8eb8a041854896a']
    card2 = test_cards['5ca6961225bbb14b254dd829']
    card3 = test_cards['5ca69616babd363d99f53e9d']
    card4 = test_cards['5ca696b7ccdaee7e3731479a']
    return card1, card2, card3, card4


def test_card_count(test_cards):
    """Tests the number of cards parsed"""
    assert len(test_cards) == 4


def test_trello_id(test_cards):
    '''Test the card ids are set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    assert card1.trelloid == '5ca69576a8eb8a041854896a'
    assert card2.trelloid == '5ca6961225bbb14b254dd829'
    assert card3.trelloid == '5ca69616babd363d99f53e9d'
    assert card4.trelloid == '5ca696b7ccdaee7e3731479a'


def test_card_idshort(test_cards):
    '''Test that the card short ids are set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    assert card1.idshort == 1
    assert card2.idshort == 2
    assert card3.idshort == 3
    assert card4.idshort == 4


def test_card_name(test_cards):
    '''Test that the card names are set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    assert card1.name == 'Foo Card'
    assert card2.name == 'Bar Card'
    assert card3.name == 'Foobar Card'
    assert card4.name == 'empty card'


def test_card_position(test_cards):
    '''Test that the card positions are set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    assert card1.position == 65535
    assert card2.position == 131071
    assert card3.position == 65535
    assert card4.position == 131071


def test_card_closed(test_cards):
    '''Test that the card closed is set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    assert not card1.closed
    assert not card2.closed
    assert not card3.closed
    assert not card4.closed


def test_card_date_last_activity(test_cards):
    '''Test that the card last activity date is set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    assert card1.date_last_activity == '2019-04-04T23:43:02.498Z'
    assert card2.date_last_activity == '2019-04-04T23:43:41.669Z'
    assert card3.date_last_activity == '2019-04-04T23:44:47.021Z'
    assert card4.date_last_activity == '2019-04-04T23:43:51.410Z'


def test_card_description(test_cards):
    '''Test that the card description is set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    card2_expected = "bar card description\n\n`code`\n\n```\ncode block\n```"

    assert card1.description == "This is the foo card's description."
    assert card2.description == card2_expected
    assert card3.description == "I'm a card with a checklist and due date"
    assert card4.description == ''


def test_card_cardlist(test_cards):
    '''Test that the card labels id lists are set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    assert card1.card_list == '5ca69567b826c4317ec4971f'
    assert card2.card_list == '5ca69567b826c4317ec4971f'
    assert card3.card_list == '5ca6956870d34940b0644a2e'
    assert card4.card_list == '5ca6956870d34940b0644a2e'


def test_card_labels(test_cards):
    '''Test that the card labels id lists are set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    assert card1.label_ids == ['5ca6956191d0c2ddc59562dc']
    assert card2.label_ids == ['5ca6956191d0c2ddc59562df',
                               '5ca6956191d0c2ddc59562dd']
    assert card3.label_ids == ['5ca6956191d0c2ddc59562dd']
    assert card4.label_ids == []


def test_card_short_link(test_cards):
    '''Test that the card's short link is set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    assert card1.short_link == 'UQbQ9G1a'
    assert card2.short_link == 'evt8hxWA'
    assert card3.short_link == 'Aweh7xYH'
    assert card4.short_link == 'EpjRTyGv'


def test_card_due_complete(test_cards):
    '''Test that the card due complete field is set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    assert not card1.due_complete
    assert not card2.due_complete
    assert not card3.due_complete
    assert not card4.due_complete


def test_card_due(test_cards):
    '''Test that the card due field is set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    assert card1.due is None
    assert card2.due is None
    assert card3.due == '2025-04-05T16:00:00.000Z'
    assert card4.due is None


def trellemail(middle_hash, user_part='ryanhimmelwri+'):
    """Constructs the full trello email from the middle hash"""
    return user_part + middle_hash + '@boards.trello.com'


def test_card_email(test_cards):
    '''Test that the card email is set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    expect1 = trellemail('2osudntp278mqruarqq+2s2v9eul9qidzo3uoa2+2jbnvtxcyz')
    expect2 = trellemail('2osudntp278mqruarqq+2s2v9vnwt0tqq4rbhgp+08jkom1b7i')
    expect3 = trellemail('2osudntp278mqruarqq+2s2v9w5qz9tyee26isd+0srxwfhpe1')
    expect4 = trellemail('2osudntp278mqruarqq+2s2vadkt01y3sv9eeu2+1f78u2pj1p')
    assert card1.email == expect1
    assert card2.email == expect2
    assert card3.email == expect3
    assert card4.email == expect4


def test_short_url(test_cards):
    '''Test that the card short url is set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    assert card1.short_url == 'https://trello.com/c/UQbQ9G1a'
    assert card2.short_url == 'https://trello.com/c/evt8hxWA'
    assert card3.short_url == 'https://trello.com/c/Aweh7xYH'
    assert card4.short_url == 'https://trello.com/c/EpjRTyGv'


def test_url(test_cards):
    '''Test that the card url is set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    assert card1.url == 'https://trello.com/c/UQbQ9G1a/1-foo-card'
    assert card2.url == 'https://trello.com/c/evt8hxWA/2-bar-card'
    assert card3.url == 'https://trello.com/c/Aweh7xYH/3-foobar-card'
    assert card4.url == 'https://trello.com/c/EpjRTyGv/4-empty-card'


def test_subscribed(test_cards):
    '''Test that the card subscribed item is set'''
    card1, card2, card3, card4 = get_cards(test_cards)
    assert card1.subscribed is True
    assert card2.subscribed is True
    assert card3.subscribed is not True
    assert card4.subscribed is not True
