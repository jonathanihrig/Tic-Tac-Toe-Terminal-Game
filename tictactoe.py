class TicTacToeGame:
    def __init__(self):
        self.board = [["", "", ""],["", "", ""],["", "", ""]]
        self.current_player = "X" # Here, X or O is available. X will start the game.
        self.gamecomplete = False

    def game_loop(self):
        while not self.gamecomplete:
            self.print_board()
            self.get_input()
            self.check_board()
            self.switch_player()
        
        print("Do you want to play another round?")
        if input("Answer (y/n): ") == "y":
            self.board = [["", "", ""],["", "", ""],["", "", ""]]
            self.current_player = "X" # Here, X or O is available. X will start the game.
            self.gamecomplete = False
            self.game_loop()

    def clear_console(self):
        empty_space = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        print(empty_space)

    def print_board(self):
        self.clear_console()

        print("Current Board: ")
        print("")

        for row in self.board:
            rowstring = "|".join([item if item != "" else " " for item in row])
            print(f" {rowstring} ")
            print("---|---|---")

        print("Next Player: {p}".format(p = self.current_player))

        
    def get_input(self):

        selection_valid = False
        
        while selection_valid == False:
        
            print("Use Numpad (1 - 9) to select the next box. \n")
            sel = input("Your selection: ")
        
            selection_valid = True

            row = 0
            col = 0

            match sel:
                case "1":
                    row = 2
                    col = 0
                case "2":
                    row = 2
                    col = 1
                case "3":
                    row = 2
                    col = 2
                case "4":
                    row = 1
                    col = 0
                case "5":
                    row = 1
                    col = 1
                case "6":
                    row = 1
                    col = 2
                case "7":
                    row = 0
                    col = 0
                case "8":
                    row = 0
                    col = 1
                case "9":
                    row = 0
                    col = 2
                case _:
                    selection_valid = False
                    continue

            if self.board[row][col] != "":
                selection_valid = False
                print("This field is already occupied! Choose another one!")
                continue
            else:
                self.board[row][col] = self.current_player
                selection_valid = True
                break
                

    def check_board(self):
        
        game_won = False
        winner = ""

        # Check Horizontal
        for row in self.board:
            check_character = row[0]

            rowcheck = True # Turns false if a row is not winning

            for item in row:
                if item != check_character:
                    rowcheck = False
                    break
            
            if rowcheck and check_character != "":
                game_won = True
                winner = check_character
                break
        
        # Check Vertical
        for col in range(3):
            check_character = self.board[0][col]
            colcheck = True # Turns false if a column is not winning

            for row in range(3):
                if self.board[row][col] != check_character:
                    colcheck = False
                    break
            
            if colcheck and check_character != "":
                game_won = True
                winner = check_character
                break

        # Check Diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != "":
            game_won = True
            winner = self.board[0][0]
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != "":
            game_won = True
            winner = self.board[0][2]
        
        if game_won:

            self.clear_console()
            self.print_board()
            print("")

            print(f"Player {winner} has won the game!")
            self.gamecomplete = True
        
        if not game_won:

            # Check for draw

            draw = True
            for row in self.board:
                for item in row:
                    if item == "":
                        draw = False
                        break
            
            if draw:
                self.clear_console()
                self.print_board()
                print("")
                print("The game is a draw!")
                self.gamecomplete = True



    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
    

            


if input("Do you want to start a new game? (y/n): ") == "y":
    game = TicTacToeGame()
    game.game_loop()
else:
    print("You may close this program.")