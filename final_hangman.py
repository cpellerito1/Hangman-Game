#  Chris Pellerito
#  Final project
#  This program will run the game hangman


def hangman():  # Main function that runs everything
    print('''Welcome, this game is a two player variation of hangman. Player 1 is choosing the word to be guessed
    and Player 2 is guessing.''')
    # list of every variation of the hangman board
    hangman_boards = ['''   
______
|     |
|     
|    
|       
|    
|
|
|________
''', '''
 
 ______
|      |
|      O 
|      
|       
|     
|
|
|________
''', '''
______
|     |
|     O
|     |
|     |
|     
|
|
|________
''', '''
______
|     |
|     O
|    \|
|     |
|    
|
|
|________
''', '''
______
|     |
|     O
|    \|/
|     |
|    
|
|
|________
''', '''
______
|     |
|     O
|    \|/  
|     |
|    / 
|
|
|________
''', '''
______
|     |
|     O  
|    \|/ 
|     |   
|    / \ 
|
|________
''']

    replay = 'yes'  # initialize counter loop
    while replay == 'yes':  # Replay loop
        print(hangman_boards[0])  # prints the first hangman board with nothing on it
        word = input("Player 1, type which word would you like to use: ").lower()
        board = ["_ "] * len(word)  # Creates the dashed lines that will be replaced by correct letters
        letters_guessed = [ ]  # empty list to store the guessed letters
        incorrect_guesses = 0  # initialize variable to track number of incorrect incorrect_guesses
        while "_ " in board and incorrect_guesses < 6:  # sets u loop that will run all the mechanics of the game
            print("Your incorrect guesses are:", "".join(letters_guessed))  # Prints the letters you already guessed
            guess = input("What letter would you like to guess: ").lower()
            for i in range(len(word)):  # go through every letter in word
                if guess == word[i]:  # checks if the letter guessed is in the word
                    board[i] = guess  # places letter where it should be in board
                    print("".join(board))  # prints the board with the letters just replaced
                elif guess in letters_guessed:  # checks if you already guessed that letter
                    print("You already guessed that letter, guess again ")
                    break  # breaks back out so player 2 can guess again
                if guess not in word:  # checks if letter is not in the word. used as a check to make sure its a letter
                    print("Sorry, that letter is wrong, guess again")
                    letters_guessed.append(guess)  # adds letter guessed to the list
                    incorrect_guesses += 1  # tracks how many incorrect_guesses you made
                    if incorrect_guesses == 1:
                        print(hangman_boards[1])
                    elif incorrect_guesses == 2:
                        print(hangman_boards[2])
                    elif incorrect_guesses == 3:
                        print(hangman_boards[3])
                    elif incorrect_guesses == 4:  # Checks to see how many incorrect guesses have been made to determine which board to print
                        print(hangman_boards[4])
                    elif incorrect_guesses == 5:
                        print(hangman_boards[5])
                    elif incorrect_guesses == 6:
                        print(hangman_boards[6])
                    break
        if "_ " not in board:  # checks if board variable has no blank spaces to check for a win
            print("Congratulations! You won!")
        else:  # if board has blank spaces they lose
            print("Sorry, you lost. Better luck next time.")
        replay = str(input("Would you like to play again? type 'yes' or 'no' ")).lower()  # asks user if they want to reply
        print("Thanks for playing! Have a nice day!")


hangman()
