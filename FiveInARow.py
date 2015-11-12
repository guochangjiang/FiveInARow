import http.client as httpc
import http.server as https
import random
import sys

def main(argv):
    """ The main entry point for the program """
    game = Game()
    game.run()
    return

class MyHandler(https.BaseHTTPHandler):

    last_path = ''

    opponent = ''

    def do_GET(self):
        port = self.path[1:]
        MyHandler.opponent = self.client_address[0] + ':' + port
        return
    
    def do_POST(self):
        MyHandler.last_path = self.path
        return


class Game():

    def __init__(self):
        self.boardsize = 19
        self.board = [['.' for x in range(self.boardsize)] for y in range(self.boardsize)]
        self.own_moves = []
        self.opp_moves = []
    
    def run(self):
        """ them main loop for the game """
        port = int(input("enter a port number to run on"))
        # set up server
        self.server = https.BaseHTTPServer(('',port),MyHander)
        print("one player must listen first, the other player will must reach out")
        is_listener = int(input("enter 1 if to be the listener, 0 to if the other player will be: "))
        if (is_listener == 1):
            self.server.handler_request()
            if random.randint(0,1) == 1:
                self.print_board()
                self.send_move()
            else:
                self.send_you_go()
        else:
            self.handshake(port)
        while True:
            self.server.handle_request()
            if MyHandler.last_path == "/youwin":
                print("you win!")
                break
            self.print_board()
            if MyHandler.last_path[:5] == "/move":
                self.process_move(MyHandler.last_path[-4:])
            move = input("input move: ")
            self.send_move()
        return

    def process_move(self, move):
        x, y = move[:2], move[2:]
        opp_moves.append((int(x),int(y)))
        return

    def send_move(self):
        move = input("enter move: ")
        x,y = move.split(',')
        move_string = x.strip().zfill(2) + y.strip().zfill(2)
        httpc.HTTPConnection(MyHandler.opponent)
        httpc.requset("POST", "/move/" + move_string)
        return

    def self_handshake(self, my_port):
        host = input("enter the other players address ")
        port = input("enter the other players port: ")
        MyHandler.opponent = host + ':' + port
        httpc.HTTPConnection(MyHandler.opponent[0], MyHandler.opponent[1])
        httpc.request("GET", '/'+str(my_port))
        return

    def print_board(self):
        for i in range(100):
            print("")
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
        return (self._check_horizontal_win ||
                self._check_vertical_win ||
                self._check_diagonal_win ||
                self._check_reverse_diagonal_win)

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
