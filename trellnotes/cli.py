#!/usr/bin/env python
"""Contains the main CLI and arg parsing code"""

from argparse import ArgumentParser
from . import __version__
# from trellnotes.parser import BoardData


class CLI:
    """
    Contains the class for the main CLI object. It matches the cli imputs
    and kick off the appropriate functionality.
    """

    def __init__(self):
        self.parser = ArgumentParser(description='Read in trello board json\
                                     exports and convert to a readable note\
                                     format')
        self.parser.add_argument('--version', action='version',
                                 version=__version__)

    def main(self):
        """Main CLI Method"""
        print('in main')
        args = self.parser.parse_args()
        print('args: ' + args)
