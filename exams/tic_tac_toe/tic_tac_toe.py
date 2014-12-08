import random


class Tic_tac_toe():
    def __init__(self):
        pass

    def draw_board(self, board):
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def setting_player_letter(self):
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Choose letter: X or O?')
            letter = input().upper()

        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def setting_first_player(self):
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'

    def play_again(self):
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def make_move(self, board, letter, move):
        board[move] = letter

    def is_winner(self, bo, le):
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or
                (bo[4] == le and bo[5] == le and bo[6] == le) or
                (bo[1] == le and bo[2] == le and bo[3] == le) or
                (bo[7] == le and bo[4] == le and bo[1] == le) or
                (bo[8] == le and bo[5] == le and bo[2] == le) or
                (bo[9] == le and bo[6] == le and bo[3] == le) or
                (bo[7] == le and bo[5] == le and bo[3] == le) or
                (bo[9] == le and bo[5] == le and bo[1] == le))

    def board_copy(self, board):
        board_copy = []

        for i in board:
            board_copy.append(i)

        return board_copy

    def is_free(self, board, move):
        return board[move] == ' '

    def plaer_move(self, board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.is_free(board, int(move)):
            print('Choose your next move? (1-9)')
            move = input()
        return int(move)

    def random_move_from_list(self, board, moves_list):
        possible_moves = []
        for i in moves_list:
            if self.is_free(board, i):
                possible_moves.append(i)

        if len(possible_moves) != 0:
            return random.choice(possible_moves)
        else:
            return None

    def computer_move(self, board, computer_letter):
        if computer_letter == 'X':
            player_letter = 'O'
        else:
            player_letter = 'X'

        for i in range(1, 10):
            copy = self.board_copy(board)
            if self.is_free(copy, i):
                self.make_move(copy, computer_letter, i)
                if self.is_winner(copy, computer_letter):
                    return i

        for i in range(1, 10):
            copy = self.board_copy(board)
            if self.is_free(copy, i):
                self.make_move(copy, player_letter, i)
                if self.is_winner(copy, player_letter):
                    return i

        move = self.random_move_from_list(board, [1, 3, 7, 9])
        if move != None:
            return move

        if self.is_free(board, 5):
            return 5

        return self.random_move_from_list(board, [2, 4, 6, 8])

    def is_full(self, board):
        for i in range(1, 10):
            if self.is_free(board, i):
                return False
        return True

    def execute(self):
        while True:
            theBoard = [' '] * 10
            player_letter, computer_letter = self.setting_player_letter()
            turn = self.setting_first_player()
            print('The ' + turn + ' will go first.')
            is_playing = True

            while is_playing:
                if turn == 'player':
                    self.draw_board(theBoard)
                    move = self.plaer_move(theBoard)
                    self.make_move(theBoard, player_letter, move)

                    if self.is_winner(theBoard, player_letter):
                        self.draw_board(theBoard)
                        print('You have won the game!')
                        is_playing = False
                    else:
                        if self.is_full(theBoard):
                            self.draw_board(theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'computer'

                else:
                    move = self.computer_move(theBoard, computer_letter)
                    self.make_move(theBoard, computer_letter, move)

                    if self.is_winner(theBoard, computer_letter):
                        self.draw_board(theBoard)
                        print('You lose.')
                        is_playing = False
                    else:
                        if self.is_full(theBoard):
                            self.draw_board(theBoard)
                            print('Tie!')
                            break
                        else:
                            turn = 'player'

            if not self.play_again():
                break


def main():
    test = Tic_tac_toe()
    test.execute()

if __name__ == '__main__':
    main()
