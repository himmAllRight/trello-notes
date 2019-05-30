#!/usr/bin/env python
"""Contains the main CLI and arg parsing code"""


import os
from argparse import ArgumentParser
from trellnotes.parser import BoardData
from trellnotes.writer import Output
from . import __version__


class CLI:
    """
    Contains the class for the main CLI object. It matches the cli imputs
    and kick off the appropriate functionality.
    """

    def __init__(self):
        self.parser = ArgumentParser(description='Read in trello board json\
                                     exports and convert to a readable note\
                                     format')
        self.parser.add_argument('input_src', type=str,
                                 help='The file path of the input trello json\
                                 file to parse')
        self.parser.add_argument('--output-src', '-o', type=str,
                                 help='The file path of the output notes file',
                                 default='trellnotes-output.md')
        self.parser.add_argument('--include-archived', '-a',
                                 action='store_true', default=False,
                                 dest='include_archived',
                                 help='Also include archived cards in output')
        self.parser.add_argument('--version', action='version',
                                 version=__version__)
        self.args = vars(self.parser.parse_args())

    def main(self):
        '''Main CLI Method'''
        print('in main')
        print('args: ' + str(self.args))
        loaded_board = self.load_board()
        print(loaded_board)
        # Testing output
        output = Output(self.args['output_src'])
        output.generate_output_string(self.args, loaded_board)
        output.write_output()

    def src_path(self, src_arg='input_src'):
        '''Creates the file path to load the json input file from.'''
        src = self.args[src_arg]
        path = os.path.abspath(src)
        return path

    def load_board(self):
        '''Loads the board file and instantiates an object'''
        loaded_board = BoardData(self.src_path())
        return loaded_board
