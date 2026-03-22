import random
import time
import os

def clear_screen():        
    """
    Clears the terminal screen. If the operating system is Windows, it uses the 'cls' command, otherwise it uses the 'clear' command.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(squares):
    """
    Displays the Tic Tac Toe board with the given squares.

    The function takes a list of 9 strings as an argument, where each string
    represents a square on the board. It prints the board in a 3x3 grid
    format, with each square separated by a line and a vertical line.

    :param squares: A list of 9 strings representing the squares on the board.
    :return: None
    """
    print("+------+------+------+\n"
          "|      |      |      |\n"
          "|", end="")
    for i in range(9):
        print(f"  {squares[i]}   |", end="")
        if i != 8 and i % 3 == 2:
            print("\n"
                  "|      |      |      |\n"
                  "+------+------+------+\n"
                  "|      |      |      |\n"
                  "|", end="")
    print("\n"
          "|      |      |      |\n"
          "+------+------+------+")

def get_valid_board_move(prompt, valid_options):
    """
    Gets a valid board move from the user.

    The function takes two arguments, a prompt string and a list of valid options.
    It prompts the user for input until the user enters a valid option.
    If the user enters an invalid option, it prints an error message and waits
    1.5 seconds before clearing the screen and displaying the board again.
    Once the user enters a valid option, it removes the option from the list
    of valid options and returns the option as an integer.

    :param prompt: A string to prompt the user for input.
    :param valid_options: A list of strings representing the valid options.
    :return: An integer representing the user's board move.
    """
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            valid_options.remove(user_input)
            return int(user_input)
        else:
            print(f"the option {user_input} is not valid. Please enter one of the following: {', '.join(valid_options)}")
            
def get_valid_board_move_computer(valid_options):
    """
    Gets a valid board move from the computer.

    The function takes one argument, a list of valid options.
    If the option "5" is in the list of valid options, it chooses this option.
    Otherwise, it randomly selects an option from the list of valid options.
    It removes the option from the list of valid options and returns the option as an integer.

    :param valid_options: A list of strings representing the valid options.
    :return: An integer representing the computer's board move.
    """
    if "5" in valid_options:
        computer_input = "5"
    else:
        computer_input = random.choice(valid_options)
    valid_options.remove(computer_input)
    return int(computer_input)

def get_valid_input(prompt, valid_options):
    """
    Gets a valid input from the user.

    The function takes two arguments, a string to prompt the user for input and a
    list of strings representing the valid options. It repeatedly asks the user
    for input until a valid option is entered. If the user enters an invalid
    option, it prints an error message and waits 1.5 seconds before clearing
    the screen and prompting the user again. Once the user enters a valid option, it
    returns the option as a string.

    :param prompt: A string to prompt the user for input.
    :param valid_options: A list of strings representing the valid options.
    :return: A string representing the user's input.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")
            time.sleep(1.5)
            clear_screen()

def get_player_names():
    """
    Gets the names of the two players from the user.

    The function prints a welcome message and waits 1.5 seconds before
    clearing the screen and prompting the user for their name.
    It then asks the user if they are playing with a friend and waits for a
    response. If the user is playing with a friend, it prompts the user for
    their friend's name. Otherwise, it sets the friend's name to an empty
    string. Finally, it returns the two player names as a tuple of strings.

    :return: A tuple of two strings representing the names of the two players.
    """
    print("Welcome to Tic Tac Toe!")
    time.sleep(1.5)
    clear_screen()
    player_1_name = input("What's your name?\n")
    clear_screen()
    if get_valid_input("Are you playing with a friend?(y/n)\n", ['y', 'yes', 'n', 'no']).startswith('y'):
        clear_screen()
        player_2_name = input("What's his name?\n")
    else:
        player_2_name = "computer"
    return player_1_name, player_2_name

def game_logic(placeholder, empty):
    """
    Checks if there is a winner of the game based on the given placeholder.

    The function takes two arguments, a list of strings representing the squares on the board and a string representing an empty square.
    It returns 1 if there is a winner, and 0 otherwise.

    :param placeholder: A list of 9 strings representing the squares on the board.
    :param empty: A string representing an empty square.
    :return: An integer indicating whether there is a winner of the game.
    """
    if placeholder[0] == placeholder[1] == placeholder[2] and placeholder[0] not in empty or\
        placeholder[3] == placeholder[4] == placeholder[5] and placeholder[3] not in empty or\
        placeholder[6] == placeholder[7] == placeholder[8] and placeholder[6] not in empty or\
        placeholder[0] == placeholder[3] == placeholder[6] and placeholder[0] not in empty or\
        placeholder[1] == placeholder[4] == placeholder[7] and placeholder[1] not in empty or\
        placeholder[2] == placeholder[5] == placeholder[8] and placeholder[2] not in empty or\
        placeholder[0] == placeholder[4] == placeholder[8] and placeholder[0] not in empty or\
        placeholder[2] == placeholder[4] == placeholder[6] and placeholder[2] not in empty:
        return 1
    return 0


def main():
    """
    This is the main function of the Tic Tac Toe game. It keeps asking the user to play
    until the user decides to quit. It first gets the names of the two players, then
    displays the board and asks the user to make a move. If the user is playing with
    the computer, the computer makes a move after the user's move. The game continues
    until the user decides to quit or until there is a winner (if all squares are
    filled and no one has won) or until there is a winner (if one of the players has
    three of their squares in a row). After the game ends, it asks the user if they want
    to play again. If the user decides not to play again, it prints a message and ends
    the game.

    :return: None
    """
    keep_going = True
    while keep_going:
        empty_square = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
        placeholder = [empty_square[i] for i in range(9)]
        SQUARES_TO_POP = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        clear_screen()
        player_1_name, player_2_name = get_player_names()
        clear_screen()
        display_board(placeholder)
        player = "🅾️" 
        turn = 0
        while True:
            if turn >= 5:
                winner = game_logic(placeholder, empty_square)
                if winner != 0:
                    name = player_1_name if player == "🅾️" else player_2_name
                    print(f"{name} Won!!!")
                    break

                if not SQUARES_TO_POP:
                    print("Draw!, No one wins!")
                    time.sleep(1.5)
                    break
            turn += 1
            player = "🅾️" if player == "🗙" else "🗙"
            current_player_name = player_2_name if player == "🗙" else player_1_name
            if player_2_name == "computer" and player == "🗙":
                clear_screen()
                placeholder[get_valid_board_move_computer(SQUARES_TO_POP) - 1] = player
                clear_screen()
                display_board(placeholder)
                continue

            placeholder[get_valid_board_move(f"Enter your move {current_player_name}: ", SQUARES_TO_POP) - 1] = player
            clear_screen()
            display_board(placeholder)

        if get_valid_input("Play again?(y/n)\n", ['y', 'yes', 'n', 'no']).startswith('n'):
            keep_going = False
            print("Thanks for playing!")

if __name__ == "__main__":
    main()