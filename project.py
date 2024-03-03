from Game.player import Player
from Game.board import Game
import os
from time import sleep
import re
import sys


def main():
    players = create_players()
    while True:
        os.system('clear')
        board_size = input('How big of a game would you like? (3-10) ').strip()
        if re.match(r'^\d+$', board_size) and 3 <= int(board_size) <= 10:
            break
        else:
            print('Invalid size. Try again.')
            sleep(1)
    board = Game(int(board_size), *players)
    turn_num = 1
    board.pick_starting_player()
    while turn_num <= board.width ** 2:
        current_player = list(
            filter(lambda player: player.is_turn, board.players))[0]
        while True:
            os.system('clear')
            print(board)
            message = f'{current_player.username} > Place a piece in one of the following spots:'
            for open_spot in board.get_available_moves():
                message += f'\n {open_spot}: {list(board.layout.keys())[open_spot - 1]}'
            message += '\nRequest: '
            try:
                request = input(message).strip()
            except (EOFError, KeyboardInterrupt):
                sys.exit()
            if re.match(r'^[1-9][0-9]*$', request):
                try:
                    board.add_piece(
                        board.layout[list(board.layout.keys())[int(request) - 1]], current_player)
                except ValueError:
                    print('Space already taken. Try again.')
                    sleep(1)
                else:
                    os.system('clear')
                    print(board)
                    if board.check_board(current_player.code):
                        print(board.declare_winner(current_player))
                        return
                    turn_num += 1
                    board.toggle_turn()
                    break
            else:
                print('Invalid request. Try again.')
                sleep(1)
    print(board.declare_winner())


def create_players():
    player_list = []
    player_num = 1
    codes = ('X', 'O')
    while player_num <= 2:
        os.system('clear')
        try:
            player_uname = input(
                f'Player {player_num}: What would you like your username to be? ').strip().replace(' ', "_")
            player = Player(player_uname, codes[player_num - 1])
        except ValueError:
            print('Invalid player code or username. Try again')
            sleep(1)
        except (EOFError, KeyboardInterrupt):
            sys.exit()
        else:
            if len(list(filter(lambda code: code == player.code, player_list))) > 0:
                print('Code cannot be the same as Player 1. Try again.')
                sleep(1)
            else:
                player_list.append(player)
                player_num += 1
    return player_list


if __name__ == '__main__':
    main()
