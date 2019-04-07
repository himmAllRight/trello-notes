"""Tests that the label objects are being set as expected"""


def get_labels(test_labels):
    label1 = test_labels['5ca6956191d0c2ddc59562dd']
    label2 = test_labels['5ca6956191d0c2ddc59562dc']
    label3 = test_labels['5ca6956191d0c2ddc59562df']
    return label1, label2, label3


def test_labels_length(test_labels):
    """Tests the number of labels"""
    assert len(test_labels) == 3


def test_labels_id(test_labels):
    '''Test the label ids are set'''
    label1, label2, label3 = get_labels(test_labels)
    assert label1.trelloid == '5ca6956191d0c2ddc59562dd'
    assert label2.trelloid == '5ca6956191d0c2ddc59562dc'
    assert label3.trelloid == '5ca6956191d0c2ddc59562df'


def test_labels_names(test_labels):
    '''Test the label names are set'''
    label1, label2, label3 = get_labels(test_labels)
    assert label1.name == 'Red Label'
    assert label2.name == 'Green Label'
    assert label3.name == 'Orange Label'


def test_labels_colors(test_labels):
    '''Test the label colors are set'''
    label1, label2, label3 = get_labels(test_labels)
    assert label1.color == 'red'
    assert label2.color == 'green'
    assert label3.color == 'orange'
