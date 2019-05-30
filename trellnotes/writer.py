'''Contains functions which control printout output'''
from trellnotes.parser import BoardData


class Output:
    '''Organizes and writes the data to an output'''
    def __init__(self, src):
        self.output_src = src
        self.output_str = ""

    def write_output(self):
        '''Writes output to output file'''
        with open(self.output_src, 'w') as output:
            output.write(self.output_str)

    def generate_output_string(self, args, board_data):
        '''Generates the default string to output from the data.'''
        out_list = []
        for card_list in board_data.get_objects('lists'):
            out_list.append(card_list.output())
            for card in card_list.cards.values():
                if not (not args['include_archived'] and card.closed):
                    out_list.append(card.output())
            out_list.append("\n")
        self.output_str = "\n".join(out_list)
