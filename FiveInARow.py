from __future__ import print_function, division
try:
    import http.client as httpc
    import http.server as https
except:
    import httplib as httpc
    import BaseHTTPServer as https
import random
import sys
if sys.version_info[0] == 2: input = raw_input

def main(argv):
    """ The main entry point for the program """
    game = Game()
    game.run()
    return

class MyHandler(https.BaseHTTPRequestHandler):

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
        self.own_char = 'b'
        self.opp_char = 'w'
    
    def run(self):
        """ them main loop for the game """
        port = int(input("enter a port number to run on: "))
        # set up server
        self.server = https.HTTPServer(('',port),MyHandler)
        print("one player must listen first, the other player will must reach out")
        is_listener = int(input("enter 1 if to be the listener, 0 to if the other player will be: "))
        if (is_listener == 1):
            self.server.handle_request()
            if random.randint(0,1) == 1:
                self.print_board()
                self.send_move()
            else:
                self.print_board()
                self.send_you_go()
                print("waiting for opponent")
        else:
            self.handshake(port)
        while True:
            self.server.handle_request()
            if MyHandler.last_path == "/youwin":
                print("you win!")
                break
            if MyHandler.last_path[:5] == "/move":
                self.process_move(MyHandler.last_path[-4:])
            self.print_board()
            if self.check_win():
                print("Opponent won!")
                self.send_you_win()
                break
            self.send_move()
            self.print_board()
            print("waiting on opponent")
        return

    def process_move(self, move):
        x, y = move[:2], move[2:]
        self.opp_moves.append((int(x),int(y)))
        self.board[int(x)][int(y)] = self.opp_char
        return

    def send_move(self):
        while True:
            move = input("enter move: ")
            x,y = move.split(',')
            if (int(x) < 19 and int(x) >= 0 and
                int(y) < 19 and int(y) >= 0):
                if (int(x),int(y)) not in (self.own_moves + self.opp_moves):
                    break
                else:
                    print("that move has already been made")
            else:
                print("invalid move")
        move_string = x.strip().zfill(2) + y.strip().zfill(2)
        self.own_moves.append((int(x),int(y)))
        self.board[int(x)][int(y)] = self.own_char
        conn = httpc.HTTPConnection(MyHandler.opponent)
        conn.request("POST", "/move/" + move_string)
        return

    def send_you_go(self):
        conn = httpc.HTTPConnection(MyHandler.opponent)
        conn.request("POST","/yougo")
        return

    def send_you_win(self):
        conn = httpc.HTTPConnection(MyHandler.opponent)
        conn.request("POST","/youwin")
        return

    def handshake(self, my_port):
        host = input("enter the other players address ")
        port = input("enter the other players port: ")
        MyHandler.opponent = host + ':' + port
        conn = httpc.HTTPConnection(MyHandler.opponent)
        conn.request("GET", '/'+str(my_port))
        return

    def print_board(self):
        for i in range(100):
            print("")
        row_string = '   '
        for i in range(self.boardsize):
            row_string += str(i).rjust(3)
        print(row_string)
        for i, row in enumerate(self.board):
            row_string = str(i).rjust(3)
            for c in row:
                row_string += c.rjust(3)
            print(row_string)
        return

    def check_win(self):
        print(self.opp_moves)
        if len(self.opp_moves) == 0:
            return False
        return (self._check_horizontal_win() or
                self._check_vertical_win() or
                self._check_diagonal_win() or
                self._check_reverse_diagonal_win())

    def _check_horizontal_win(self):
        for (x, y) in self.opp_moves:
            if (((x+1),y) in self.opp_moves and
                ((x+2),y) in self.opp_moves and
                ((x+3),y) in self.opp_moves and
                ((x+4),y) in self.opp_moves):
                return True
        return False

    def _check_vertical_win(self):
        for (x, y) in self.opp_moves:
            if ((x,(y+1)) in self.opp_moves and
                (x,(y+2)) in self.opp_moves and
                (x,(y+3)) in self.opp_moves and
                (x,(y+4)) in self.opp_moves):
                return True
        return False

    def _check_diagonal_win(self):
        for (x, y) in self.opp_moves:
            if (((x+1),(y+1)) in self.opp_moves and
                ((x+2),(y+2)) in self.opp_moves and
                ((x+3),(y+3)) in self.opp_moves and
                ((x+4),(y+4)) in self.opp_moves):
                return True
        return False

    def _check_reverse_diagonal_win(self):
        for (x, y) in self.opp_moves:
            if (((x+1),(y-1)) in self.opp_moves and
                ((x+2),(y-2)) in self.opp_moves and
                ((x+3),(y-3)) in self.opp_moves and
                ((x+4),(y-4)) in self.opp_moves):
                return True
        return False

if __name__ == "__main__":
    main(sys.argv[1:])
