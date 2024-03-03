from Game.piece import Piece
from Game.player import Player
from pyfiglet import Figlet, print_figlet, FigletFont
from colorama import Fore
from random import randint


class Board(object):
    pass


class Game(object):
    ROW_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    COLUMN_LABELS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    def __init__(self, grid_size, player1, player2):
        self.width = grid_size
        self.height = grid_size
        self.board = [[None for x in range(self.width)]
                      for y in range(self.height)]
        self.player1 = player1
        self.player2 = player2
        self.players = [self._player1, self._player2]
        self.layout = {self.ROW_LABELS[i] + self.COLUMN_LABELS[j]: (
            i, j) for i in range(0, self.width) for j in range(0, self.height)}

    def __str__(self):
        out_string = ''
        f = Figlet('blocks', width=220)
        out_string += f"                    {''.join(self.COLUMN_LABELS[:self.width])}\n"
        for idx, row in enumerate(self.board):
            out_string += self.ROW_LABELS[idx]
            for piece in row:
                if piece is None:
                    out_string += '_'
                else:
                    out_string += piece.code
            out_string += '\n'

        out_string = f.renderText(out_string)
        return out_string

    @property
    def player1(self):
        return self._player1

    @player1.setter
    def player1(self, player):
        if not isinstance(player, Player):
            raise TypeError('Board must have valid player')
        else:
            self._player1 = player

    @property
    def player2(self):
        return self._player2

    @player2.setter
    def player2(self, player):
        if not isinstance(player, Player):
            raise TypeError('Board must have valid player')
        else:
            self._player2 = player

    def check_board(self, code):
        return any([
            # Rows
            any(
                [all(
                    list(
                        map(
                            Piece.check_piece,
                            [cell for cell in row],
                            [code for _ in range(0, self.width)]
                        )
                    )
                ) for row in self.board]
            ),
            # Columns
            any(
                [all(
                    list(
                        map(
                            Piece.check_piece,
                            [row[x] for row in self.board],
                            [code for _ in range(0, self.height)]
                        )
                    )
                ) for x in range(0, self.height)]
            ),
            # Diagonally top left to bottom right
            all(
                list(
                    map(
                        Piece.check_piece,
                        [row[idx] for idx, row in enumerate(self.board)],
                        [code for _ in range(0, self.width)]
                    )
                )
            ),
            # Diagonally bottom left to top right
            all(
                list(
                    map(
                        Piece.check_piece,
                        [row[idx]
                            for idx, row in enumerate(reversed(self.board))],
                        [code for _ in range(0, self.height)]
                    )
                )
            )
        ])

    def pick_starting_player(self):
        self.players[randint(0, 1)].is_turn = True

    def get_available_moves(self):
        open_spots = []
        current_spot = 0
        for row in self.board:
            for cell in row:
                current_spot += 1
                if cell is None:
                    open_spots.append(current_spot)
        # ['\t\t'.join([row[x] for row in lists]) for x in range(0, 3)]
        return open_spots

    def add_piece(self, location, player):
        # unpack coordinate tuple
        x, y = location
        # if value is None we can set to new Piece object
        if self.board[x][y] is None:
            self.board[x][y] = Piece(player, location)
        else:
            raise ValueError('Location already taken')

    def toggle_turn(self):
        self._player1.is_turn = not self._player1.is_turn
        self._player2.is_turn = not self._player2.is_turn

    @staticmethod
    def declare_winner(player=None):
        f = Figlet('doom', width=220)
        if player is None:
            return str(f.renderText("It's a Tie!"))
        return str(f.renderText(f'{player.username} Wins The Game!!'))
