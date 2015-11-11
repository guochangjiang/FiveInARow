import http.client as httpc
import http.server as https
import sys

def main(argv):
    """ The main entry point for the program """
    game = Game()
    game.run()
    return

class MyHandler(https.BaseHTTPHandler):
    
    def do_POST(self):
        return


class Game():

    def __init__(self):
        port = int(input("enter a port number to run on"))
        # set up server
        # handshake
        self.boardsize = 19
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
