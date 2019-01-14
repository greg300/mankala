from utils.read_input import *


class Player:
    name = ''
    player_number = 0
    games_won = 0
    board = []

    def __init__(self, name, player_number):
        self.board = [3] * 6 + [0]
        self.name = name
        self.player_number = player_number

    def print_pits(self):
        print "  ",
        for pit in range(0, 6):
            print self.board[pit],

    def print_pits_backwards(self):
        print "  ",
        for pit in range(5, -1, -1):
            print self.board[pit],

    def out_of_moves(self):
        pits = self.board[0:6:1]
        for pit in pits:
            if pit != 0:
                return False
        return True

    def wins(self, opponent):
        if self.board[6] > opponent.board[6]:
            return True
        elif self.board[6] == opponent.board[6]:
            print "A tie!"
            return False
        else:
            return False

    def reset_board(self, stones_per_pit):
        self.board = [stones_per_pit] * 6 + [0]

    def take_turn(self, opponent):
        go_again = False
        print self.name + ": "
        pit_choice = pick_pit_letter()
        pit_number = assign_pit_number(pit_choice, self)

        while self.board[pit_number] == 0:
            print "That pit is empty. Please pick another."
            pit_choice = pick_pit_letter()
            pit_number = assign_pit_number(pit_choice, self)

        stones = self.board[pit_number]
        go_again = move_stones(stones, pit_number, self, opponent)
        if self.out_of_moves():
            go_again = False
            print_board()
            print self.name + " is out of moves."
        return go_again


def pick_pit_letter():
    pit_choice = read_char("Which pit? (A - F) ", [])
    while not is_valid_pit(pit_choice):
        print "Not a valid pit."
        pit_choice = read_char("Which pit? (A - F) ", [])
    return pit_choice


def is_valid_pit(pit_choice):
    if pit_choice != 'A' and pit_choice != 'B' and pit_choice != 'C' \
            and pit_choice != 'D' and pit_choice != 'E' and pit_choice != 'F':
        return False
    else:
        return True


def assign_pit_number(pit_choice, player):
    letters = ['A'] + ['B'] + ['C'] + ['D'] + ['E'] + ['F']
    if player.player_number == 1:
        for letter in letters:
            if letter == pit_choice:
                pit_number = letters.index(letter)
    elif player.player_number == 2:
        letters = letters[::-1]
        for letter in letters:
            if letter == pit_choice:
                pit_number = letters.index(letter)
    return pit_number


def print_board():
    print "\n",
    player2.print_pits_backwards()
    print "\n" + str(player2.board[6]) + "               " + str(player1.board[6])
    player1.print_pits()
    print "\n   A B C D E F\n"


def move_stones(stones, pit_number, player, opponent):
    go_again = False
    rounds = stones/13 + 1

    player.board[pit_number] = 0
    for round in range(1, rounds + 1):
        if stones >= 13:
            round_stones = 12
            stones -= 12
        else:
            round_stones = stones

        for num in range(1, round_stones + 1):
            if round > 1: # Skip picked pit on first round
                stone_number = pit_number + num - 1
            else:
                stone_number = pit_number + num

            if stone_number < 7:  # Stone is on player's side
                player.board[stone_number] += 1
                if player.board[stone_number] == 1:  # Pit was empty
                    if is_last_stone(num, round_stones) and round == rounds:  # This was the last stone of the last round
                        if stone_number != 6:  # This is NOT the homebin
                            # transfer stones
                            player.board[6] += opponent.board[5 - stone_number]
                            opponent.board[5 - stone_number] = 0
                if is_last_stone(num, round_stones) and round == rounds:  # This was the last stone of the last round
                    if stone_number == 6:  # This is the homebin
                        go_again = True
                        print "\nGo again!"
                        # if player.board.index(player.board[stone_number]) == 6: # This is the homebin

            elif stone_number >= 7:  # Stone could be on opponent's side
                if stone_number == 13:  # Skip opponent's home bin
                    continue
                elif stone_number > 13:  # Stone is actually on player's side
                    player.board[stone_number - 13] += 1
                else:  # Go to opponent's side
                    opponent.board[stone_number - 7] += 1


        """for num in range(1, stones + 1):
            stone_number = pit_number + num

            if stone_number < 7:  # Stone is on player's side
                player.board[stone_number] += 1
                if player.board[stone_number] == 1:  # Pit was empty
                    if is_last_stone(num, stones) and extra_stones == 0:  # This was the last stone
                        if stone_number != 6:  # This is NOT the homebin
                            # transfer stones
                            player.board[6] += opponent.board[5 - stone_number]
                            opponent.board[5 - stone_number] = 0
                if is_last_stone(num, stones) and extra_stones == 0:  # This was the last stone
                    if stone_number == 6:  # This is the homebin
                        go_again = True
                        print "\nGo again!"
                        # if player.board.index(player.board[stone_number]) == 6: # This is the homebin


            elif stone_number >= 7:  # Stone is on opponent's side
                if stone_number >= 13:  # Skip opponent's home bin
                    if stone_number - 13 == pit_number:
                        extra_stones += 1
                        continue
                    elif stone_number - 13 >= 6:
                        opponent.board[stone_number - 13] += 1
                    else:
                        player.board[stone_number - 13 - 7] += 1
                else:  # Go to opponent's side
                    opponent.board[stone_number - 7] += 1

    if extra_stones > 0: # Add in extra stones (for skipped piles)
        stone_number = pit_number + stones # Take the pit after the one that had the last stone
        move_stones(extra_stones, stone_number, player, opponent)"""

    return go_again


def is_last_stone(num, last_number):
    if num == last_number:
        return True
    else:
        return False


def end_game(finished, not_finished):
    for pit in not_finished.board[0:6:1]:
        not_finished.board[6] += pit

play_again = 'y'
finished = None
not_finished = None
stones_per_pit = 3

print "ooooooo ~~~ WELCOME TO MANKALA ~~~ ooooooo\n"

player_name = raw_input("Enter name of Player 1: ")
player1 = Player(player_name, 1)
player_name = raw_input("Enter name of Player 2: ")
player2 = Player(player_name, 2)
print "\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"

while play_again == 'y': # Loop through the game to replay
    stones_per_pit = read_int_min_max("How many stones per pit? (Between 1 and 20): ", 1, 20)
    player1.reset_board(stones_per_pit)
    player2.reset_board(stones_per_pit)

    while not player1.out_of_moves() and not player2.out_of_moves():
        print_board()
        while player1.take_turn(player2): # If Player 1 goes again, loop
            print_board()
        if player1.out_of_moves():
            finished = player1
            not_finished = player2
            break
        print "\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"
        print_board()
        while player2.take_turn(player1): # If Player 2 goes again, loop
            print_board()
        if player2.out_of_moves():
            finished = player2
            not_finished = player1
        print "\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"

    print "\n",

    end_game(finished, not_finished)
    if player1.wins(player2):
        print player1.name + " wins!"
        print "Final score: " + str(player1.board[6]) + " to " + str(player2.board[6])
        player1.games_won += 1
    elif player2.wins(player1):
        print player2.name + " wins!"
        print "Final score: " + str(player2.board[6]) + " to " + str(player1.board[6])
        player2.games_won += 1

    play_again = read_char("Would you like to play again? (y or n) ", ['y', 'n'])
    if play_again == 'n':
        print "Final stats: \n"
        print "%s: %d" % (player1.name, player1.games_won)
        print "%s: %d" % (player2.name, player2.games_won)
        print "\nThanks for playing!"
        break
