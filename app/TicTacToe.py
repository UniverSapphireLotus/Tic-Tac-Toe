

class TicTacToe:
    def __init__(self, player_a = 'X', player_b = 'O', size = 3):
        self.size = size
        self.board = [['' for _ in range(size)] for _ in range(size)]

        self.player_a = player_a
        self.player_b = player_b

        self.turn = True # true for player_a, false for player_b

        self.diag_1 = [[i,i] for i in range(size)]
        self.diag_2 = [[size - i - 1,i] for i in range(size)]

        self.moves = 0
        
    def print_board(self):
        print('===============')
        for i in self.board:
            print(i)
        print('===============')
    
    def make_move(self, x, y):
        print('moves....', self.turn)
        if self.is_valid_move(x,y):
            if self.turn:
                self.board[x][y] = self.player_a
                self.turn = False
            else:
                self.board[x][y] = self.player_b
                self.turn = True

            self.moves += 1
            return True
        else:
            print('Invalid move....')
            return False
    
    def is_valid_move(self, x, y):
        return True if self.board[x][y] == '' else False

    def check(self, set_player):
        return True if len(set_player) == 1 and set_player != {''} else False
    
    def is_board_full(self):
        return True if self.moves == 9 else False
    
    def reset_board(self):
        self.board = [['' for _ in range(self.size)] for _ in range(self.size)]

    def empty_boxes(self):
        return [[i,j] for i in range(self.size) for j in range(self.size) if self.board[i][j] == '']

    def is_winner(self, x, y, player):

        if self.check(set(self.board[x])):
            print('winner row', player)
            return True
        elif self.check(set([i[y] for i in self.board])):
            print('winner col', player)
            return True
        else:
            #print(self.diag_1)
            #print(self.diag_2)
            if [x, y] in self.diag_1:
                if self.check(set([self.board[d[0]][d[1]] for d in self.diag_1])):
                    print('winner diag_1', player)
                    return True
            elif [x, y] in self.diag_2:
                if self.check(set([self.board[d[0]][d[1]] for d in self.diag_2])):
                    print('winner cdiag_2', player)
                    return True
        return False

        
print('Start....')
print('================================================================')
import random
pos_ = [0,1,2]

game = TicTacToe()
player_list = ['X', 'O']

while not game.is_board_full() :
    xx, xy = random.choice(pos_), random.choice(pos_)
    game.make_move(xx, xy)
    game.print_board()
    if game.is_winner(xx, xy, 'O' if game.turn else 'X'):
        print(f'winner: player_list[{not game.turn}]')
        break
    
print(game.empty_boxes())
print('================================================================')
print('....end')