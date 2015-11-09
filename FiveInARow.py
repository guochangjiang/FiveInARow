import http.client as httpc
import http.server as https
import sys
import argparse

def main(argv):
    """ The main entry point for the program """
    args = parse_args(argv)
    ## set up server
    ## handshake
    ## run game
    return

def parse_args(argv):
    """ argparse setup """
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", default=None,
                        help="port for the server to run on")
    return parser.parse_args(argv)

def run_game(server):
    """ them main loop for the game """
    ## Pick first player
    ## Loop
    ##  Wait for opponent to move
    ##  Check if game is won
    ##  Prompt for move
    ##  Send move to opponent
    ## Cleanup
    return

if __name__ == "__main__":
    main(sys.argv[1:])
