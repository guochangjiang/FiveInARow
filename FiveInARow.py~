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

if __name__ == "__main__":
    main(sys.argv[1:])
