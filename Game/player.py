import re


class Player(object):
    def __init__(self, username, code, is_turn=False):
        self.username = username
        self.code = code
        self.is_turn = is_turn

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, name):
        if not isinstance(name, str):
            raise TypeError('A string must be passed')
        if not re.match(r'^\w+$', name, re.IGNORECASE):
            raise ValueError(
                'Username must only contain alpha-numeric characters')
        else:
            self._username = name

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, letter):
        if not isinstance(letter, str):
            raise TypeError('A string must be passed')
        if len(letter) > 1 or not re.match(r'^[A-Z]$', letter, flags=re.IGNORECASE):
            raise ValueError('A single alpha character string must be passed')
        else:
            self._code = letter.upper()
