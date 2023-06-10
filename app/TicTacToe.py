

class TicTacToe:
    def __init__(self, player_a = 'X', player_b = 'O', size = 3):
        self.board = [['' for _ in range(size)] for _ in range(size)]
        self.player_a = player_a
        self.player_b = player_b

        self.diag_1 = [[i,i] for i in range(size)]
        self.diag_2 = [[size - i - 1,i] for i in range(size)]
        
    def print_board(self):
        print('===============')
        for i in self.board:
            print(i)
        print('===============')
    
    def make_move(self, x, y, player):
        self.board[x][y] = player

    def check(self, set_player):
        return True if len(set_player) == 1 and set_player != {''} else False

    def is_winner(self, x, y, player):
        #-----
        print(f'[{x},{y}]')
        print('row>', self.board[x])
        print('col>', [i[y] for i in self.board])
        #print('diag 1>', [i[y] for i in self.board])

        if self.check(set(self.board[x])):
            print('winner row', player)
        elif self.check(set([i[y] for i in self.board])):
            print('winner col', player)
        else:
            print(self.diag_1)
            print(self.diag_2)
            if [x, y] in self.diag_1:
                if self.check(set([self.board[d[0]][d[1]] for d in self.diag_1])):
                    print('winner diag_1', player)
            elif [x, y] in self.diag_2:
                if self.check(set([self.board[d[0]][d[1]] for d in self.diag_2])):
                    print('winner cdiag_2', player)
            #[0,0], [1,1], [2,2]
            #[0,2], [1,1], [2,0]

    
        

        
        

game = TicTacToe()
game.print_board()
game.make_move(0, 0, 'X')
game.make_move(1, 2, 'O')
game.make_move(1, 1, 'X')
game.make_move(2, 2, 'O')
game.make_move(2, 2, 'X')
game.print_board()
game.is_winner(2, 2, 'O')