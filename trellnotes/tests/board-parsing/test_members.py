"""Tests that the member objects are being set as expected"""


def test_member_id(test_member):
    """Tests the member's id was set correcly"""
    assert test_member.trelloid == '599d995a97a48d942e3cf4f2'


def test_member_username(test_member):
    """Tests the member's username was set correcly"""
    assert test_member.username == 'ryanhimmelwright'


def test_member_full_name(test_member):
    """Tests the member's full name was set correcly"""
    assert test_member.full_name == 'Ryan Himmelwright'


def test_member_url(test_member):
    """Tests the member's url name was set correcly"""
    assert test_member.url == 'https://trello.com/ryanhimmelwright'


def test_member_bio(test_member):
    """Tests the member's bio name was set correcly"""
    assert test_member.bio == ''
