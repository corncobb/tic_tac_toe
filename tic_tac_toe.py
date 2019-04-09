import random

'''Tic Tac Toe board class'''

class Board():

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
        count = 0
        for i in self.Board:
            for j in i:
                if j == '_':
                    count = 1
        if count == 1:
            return False
        else:
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
                
def player1():
    if not TIC_TAC_TOE.check_full():
        TIC_TAC_TOE.print_board()
        print("Player 1's turn!")
        row = int(input("Row: "))
        col = int(input("Col: "))
        while row not in range(1, 4) or col not in range(1, 4) or not TIC_TAC_TOE.insert(row, col, 'X'):
            print("Invalid move!")
            print("Player 1's turn!")
            row = int(input("Row: "))
            col = int(input("Col: "))
        
def player2():
    if not TIC_TAC_TOE.check_full():
        TIC_TAC_TOE.print_board()
        print("Player 2's turn!")
        row = int(random.randint(1, 3))
        col = int(random.randint(1, 3))
        while not TIC_TAC_TOE.insert(row, col, 'O'):
            row = int(random.randint(1, 3))
            col = int(random.randint(1, 3))
                
        print("Player 2's move: {},{}".format(str(row), str(col)))

def main():
    print("Tic-Tac-Toe Game!")
    play = 'Y'
    while play == 'Y':
        TIC_TAC_TOE.clear_board()
        while not TIC_TAC_TOE.check_winner('X') and not TIC_TAC_TOE.check_winner('O') and not TIC_TAC_TOE.check_full():
            player1()
            player2()
            if TIC_TAC_TOE.check_winner('X'):
                TIC_TAC_TOE.print_board()
                print("Player 1 WON!!!")

            elif TIC_TAC_TOE.check_winner('O'):
                TIC_TAC_TOE.print_board()
                print("Player 2 WON!!!")

        if TIC_TAC_TOE.check_full() and not TIC_TAC_TOE.check_winner('O') and not TIC_TAC_TOE.check_winner('X'):
            TIC_TAC_TOE.print_board()
            print("Tie Game!!")

        play = input("Do you want to play again (Y/n)?: ")
        while play not in ('Y', 'n'):
            print("Invalid input!")
            play = input("Do you want to play again (Y/n)?: ")
    
if __name__ == '__main__':
    TIC_TAC_TOE = Board()
    main()
