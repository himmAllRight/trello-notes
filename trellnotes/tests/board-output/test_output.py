"""Tests that the output functions work as expected"""

def test_output_src(test_output):
    assert test_output.output_src == 'test_output.md'
