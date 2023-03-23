import sys


def create_state(line_1, line_2):
    """"
    Takes as input two strings, the first two lines of the game file.
    Returns either an array containing the starting state of the game, or None if the state is invalid.

    Examples:
    Valid State:
    Input:
        line_1='12;3'
        line_2='3;3;6'
    Output:
        return [3,3,6]

    Invalid State:
    Input:
        line_1='12;3'
        line_2='4;4;6'
    Output:
        return None
    TODO: Implement this
    """
    line_1 = line_1.strip('\n')  # Ensure that any trailing new line is removed. Do not erase.
    line_2 = line_2.strip('\n')  # Ensure that any trailing new line is removed. Do not erase.


def is_game_over(state):
    """
    Given an array containing the state of the game, checks if the game is over.
    The game is over if exactly one token remains in any pile.
    Returns True if the game is over, or False if it is not.
    This function assumes that the state it is given is valid.

    Examples:
    Input:
        state=[0,1,0,0]
    Output:
        return True

    Input:
        state=[0,1,0,1]
    Output:
        return False

    TODO: Implement this
    """


def simulate_move(state, move_string, player_num):
    """
    Given an array containing the current state, a line from the game file describing a move,
    and the player_num (either 1 or 2),
    either return an updated state and a properly formatted string describing that move,
    or return None if the move is invalid.

    The output string should end with a newline character.
    Use 1-indexed strings to describe pile numbers i.e. pile 1 instead of pile 0.

    Examples:
    Valid Move:
    Input:
        state=[3,3,6]
        move_string="0,3"
    Output:
        return ([0,3,6],"Player 1 takes 3 tokens from the pile 1.\n")

    Invalid Move:
    Input:
        state=[3,3,6]
        move_string="0,5"
    Output:
        return None

    TODO: Implement this
    """
    move_string = move_string.strip('\n')  # Ensure that any trailing new line is removed. Do not erase.


def print_state(state):
    """
    Prints the given state as a string.
    The result should be two lines long and end with a newline character.
    This function assumes a valid state.
    There are exactly two space between each number in the state.

    Examples:
    Input:
        state=[3,3,6]
    Output:
        return "State:\n3  3  6\n"

    TODO: Implement this
    """


def simulate_game(input_file):
    """
    Simulates a game of Nim based on the input file.
    Use the other required functions as needed to complete this function.

    TODO: Implement this
    """


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage: python nim.py [input_file]")
        exit()

    input_filename = sys.argv[1]
    with open(input_filename) as f:
        simulate_game(f.read())
