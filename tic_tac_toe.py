import random



'''Tic Tac Toe board class'''

class Board:

    def __init__(self):
        self.Board = [['_', '_', '_'],
                      ['_', '_', '_'],
                      ['_', '_', '_']]

    def print_board(self):
        print('\n' + '*'*30 + '\n')
        print("Current state:")
        k = 0
        for i in self.Board:
            for j in i:
                print(j, end=' ')
                k += 1
                if k >= 3:
                    print('\n')
                    k = 0
        print('\n' + '*'*30 + '\n')

    def insert(self, row, col, player):

        if self.Board[row-1][col-1] == '_':
            self.Board[row-1][col-1] = player
            return True
        else:
            return False

    def check_full(self):
        for i in self.Board:
            for j in i:
                if j == '_':
                    return False

        return True

    def check_winner(self, player):
        #across
        if self.Board[0][0] == player and self.Board[0][1] == player and self.Board[0][2] == player:
            return True
        elif self.Board[1][0] == player and self.Board[1][1] == player and self.Board[1][2] == player:
            return True
        elif self.Board[2][0] == player and self.Board[2][1] == player and self.Board[2][2] == player:
            return True
        #down
        elif self.Board[0][0] == player and self.Board[1][0] == player and self.Board[2][0] == player:
            return True
        elif self.Board[0][1] == player and self.Board[1][1] == player and self.Board[2][1] == player:
            return True
        elif self.Board[0][2] == player and self.Board[1][2] == player and self.Board[2][2] == player:
            return True
        #diagnal
        elif self.Board[0][0] == player and self.Board[1][1] == player and self.Board[2][2] == player:
            return True
        elif self.Board[0][2] == player and self.Board[1][1] == player and self.Board[2][0] == player:
            return True
        else:
            return False

    def clear_board(self):
        self.Board = [['_', '_', '_'],
                      ['_', '_', '_'],
                      ['_', '_', '_']]

class Game:

    def __init__(self):
        self.TIC_TAC_TOE = Board()

    def player1(self):
        if not self.TIC_TAC_TOE.check_full():
            self.TIC_TAC_TOE.print_board()
            print("Player 1's turn!")
            row = int(input("Row: "))
            col = int(input("Col: "))
            while row not in range(1, 4) or col not in range(1, 4) or not self.TIC_TAC_TOE.insert(row, col, 'X'):
                print("Invalid move!")
                print("Player 1's turn!")
                row = int(input("Row: "))
                col = int(input("Col: "))
        
    def player2(self):
        if not self.TIC_TAC_TOE.check_full():
            self.TIC_TAC_TOE.print_board()
            print("Player 2's turn!")
            row = int(random.randint(1, 3))
            col = int(random.randint(1, 3))
            while not self.TIC_TAC_TOE.insert(row, col, 'O'):
                row = int(random.randint(1, 3))
                col = int(random.randint(1, 3))
                    
            print("Player 2's move: {},{}".format(str(row), str(col)))         

def main():
    print("Tic-Tac-Toe Game!")
    game = Game()

    player_list = [game.player1, game.player2]

    play = 'Y'
    while play == 'Y':
        game.TIC_TAC_TOE.clear_board()
        while not game.TIC_TAC_TOE.check_winner('X') and not game.TIC_TAC_TOE.check_winner('O') and not game.TIC_TAC_TOE.check_full():
            random.choice(player_list)()
            if game.TIC_TAC_TOE.check_winner('X'):
                game.TIC_TAC_TOE.print_board()
                print("Player 1 WON!!!")

            elif game.TIC_TAC_TOE.check_winner('O'):
                game.TIC_TAC_TOE.print_board()
                print("Player 2 WON!!!")

        if game.TIC_TAC_TOE.check_full() and not game.TIC_TAC_TOE.check_winner('O') and not game.TIC_TAC_TOE.check_winner('X'):
            game.TIC_TAC_TOE.print_board()
            print("Tie Game!!")

        play = input("Do you want to play again (Y/n)?: ")
        while play not in ('Y', 'n'):
            print("Invalid input!")
            play = input("Do you want to play again (Y/n)?: ")
    
if __name__ == '__main__':
    main()
