#2 Player Tic Tac Toe
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def draw_boards(game_pieces):
    """Print two game baords -> a number board for moves and the current game state"""
    print("\n\t Tic Tac Toe")
    print("\t~~~~~~~~~~~~~~~~~")
    print("\t|| 1 || 2 || 3 ||")
    print("\t|| 4 || 5 || 6 ||")
    print("\t|| 7 || 8 || 9 ||")
    print("\t~~~~~~~~~~~~~~~~~")

    print("\n\t Tic Tac Toe")
    print("\t~~~~~~~~~~~~~~~~~")
    print(f"\t|| {game_pieces[0]} || {game_pieces[1]} || {game_pieces[2]} ||")
    print(f"\t|| {game_pieces[3]} || {game_pieces[4]} || {game_pieces[5]} ||")
    print(f"\t|| {game_pieces[6]} || {game_pieces[7]} || {game_pieces[8]} ||")
    print("\t~~~~~~~~~~~~~~~~~")


def get_player_move(player_piece, game_pieces):
    """Get a payers move until is valid"""
    is_getting_move = True
    while is_getting_move:
        try:
            player_move = int(input(f"{player_piece}: Where would you like to place your piece (1-9)? "))
            if player_move > 0 and player_move < 10:
                if game_pieces[player_move -1] == "_":
                    game_pieces[player_move -1] = player_piece
                    is_getting_move = False
                else:
                    print("That spot has already been taken. Please choose another spot.")
            else:
                print("Invalid move. Please choose a spot between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def determine_winner(player_piece, game_pieces):
    """Return a bool to determine if the given player has won the game"""
    return ((game_pieces[0] == player_piece and game_pieces[1] == player_piece and game_pieces[2] == player_piece) or
            (game_pieces[3] == player_piece and game_pieces[4] == player_piece and game_pieces[5] == player_piece) or
            (game_pieces[6] == player_piece and game_pieces[7] == player_piece and game_pieces[8] == player_piece) or
            (game_pieces[0] == player_piece and game_pieces[3] == player_piece and game_pieces[6] == player_piece) or
            (game_pieces[1] == player_piece and game_pieces[4] == player_piece and game_pieces[7] == player_piece) or
            (game_pieces[2] == player_piece and game_pieces[5] == player_piece and game_pieces[8] == player_piece) or
            (game_pieces[0] == player_piece and game_pieces[4] == player_piece and game_pieces[8] == player_piece) or
            (game_pieces[2] == player_piece and game_pieces[4] == player_piece and game_pieces[6] == player_piece))


def show_game_intro():
    """Display welcome message and game instructions"""
    print("\n" + "="*50)
    print("        Welcome to Keko's Tic Tac Toe Game!")
    print("="*50)
    print("\nGame Setup:")
    print("  • Player 1: X")
    print("  • Player 2: O")
    print("  • X goes first!")
    print("\nHow to play:")
    print("  • Choose positions 1-9 as shown on the number board below")
    print("  • Enter the number where you want to place your piece")
    print("\nNumber positions:")
    print("\t~~~~~~~~~~~~~~~~~")
    print("\t|| 1 || 2 || 3 ||")
    print("\t|| 4 || 5 || 6 ||")
    print("\t|| 7 || 8 || 9 ||")
    print("\t~~~~~~~~~~~~~~~~~")
    print("\nLet's start!")
    input("Press Enter to begin the game...")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main code
show_game_intro()
player_1 = "X"
player_2 = "O"
current_game_pieces = ["_"] * 9 
draw_boards(current_game_pieces)


is_running = True
while is_running:
    #Player 1 turn
    get_player_move(player_1, current_game_pieces)
    draw_boards(current_game_pieces)
    if determine_winner(player_1, current_game_pieces):
        print(f"Congratulations! Player 1 has won the game!")
        is_running = False
    elif "_" not in current_game_pieces:
        print("The game is a tie!")
        is_running = False
    else:
        get_player_move(player_2, current_game_pieces)
        draw_boards(current_game_pieces)
        if determine_winner(player_2, current_game_pieces):
            print(f"Congratulations! Player 2 has won the game!")
            is_running = False

print("Thanks for playing Keko's Tic Tac Toe Game! Goodbye!")