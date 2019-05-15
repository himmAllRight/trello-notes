'''Contains functions which control printout output'''
from trellnotes.parser import BoardData


class Output:
    '''Organizes and writes the data to an output'''
    def __init__(self, src):
        self.output_src = src

    def write_output(self):
        '''Writes output to output file'''
        with open(self.output_src, 'w') as output:
            output.write('Hello World!\n')

    def generate_output_string(self):
        '''Generates the default string to output from the data.'''
