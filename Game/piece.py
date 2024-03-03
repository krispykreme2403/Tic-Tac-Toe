from Game.player import Player


class Piece(object):
    def __init__(self, owner=None, coords=None):
        self.owner = owner
        self.code = owner.code
        coords = coords

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, player):
        if not isinstance(player, Player):
            raise TypeError('Every piece must have a player owner')
        else:
            self._owner = player

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, coordinates):
        if coordinates is None:
            self._coords = coordinates
        elif not isinstance(coordinates, tuple):
            raise TypeError('Coordinates must be tuple')
        elif len(coordinates) > 2:
            raise TypeError('Coordinates must be 2 digit tuple')
        elif not isinstance(coordinates[0], int) or not isinstance(coordinates[1], int):
            raise ValueError('Coordinate values must be integers')
        else:
            self._coords = coordinates

    @staticmethod
    def check_piece(piece, piece_code):
        if piece is None:
            return False
        else:
            return piece.code == piece_code
