import http.client as httpc
import http.server as https
import sys
import argparse
import logging

def main(argv):
    """ The main entry point for the program """
    args = parse_args(argv)
    logger = get_logger()
    game = Game(logger,args.port)
    game.run()
    return

def parse_args(argv):
    """ argparse setup """
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", default=None,
                        help="port for the server to run on")
    return parser.parse_args(argv)

def get_logger():
    # create logger
    logger = logging.getLogger('five_in_a_row_game')
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    return logger

class Game():

    def __init__(self,logger,port):
        if not port:
            port = int(input("enter a port number to run on"))
        # set up server
        # handshake
        self.boardsize = 5
        self.board = [['.' for x in range(self.boardsize)] for y in range(self.boardsize)]
        self.own_moves = []
        self.opp_moves = []
    
    def run(self):
        """ them main loop for the game """
        # Pick first player
        # Loop
        #  Wait for opponent to move
        #  Check if game is won
        #  Prompt for move
        #  Send move to opponent
        # Cleanup
        return

    def print_board(self):
        row_string = '   '
        for i in range(boardsize):
            rowstring += str(i).rjust(3)
        print(row_string)
        for i, row in enumerate(self.board):
            row_string = str(i).rjust(3)
            for c in row:
                row_string += c.rjust(3)
        return

    def check_win(self):
        if (self._check_horizontal_win ||
            self._check_vertical_win ||
            self._check_diagonal_win ||
            self._check_reverse_diagonal_win):
            return True
        return False

    def _check_horizontal_win(self):
        return False

    def _check_vertical_win(self):
        return False

    def _check_diagonal_win(self):
        return False

    def _check_reverse_diagonal_win(self):
        return False

if __name__ == "__main__":
    main(sys.argv[1:])
