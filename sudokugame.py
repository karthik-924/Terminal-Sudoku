
from random import shuffle
import copy
# declaring question sudoku and solution sudoku as global variables
question = [[0]*9]*9
sol = []

# Function to solve the 9x9 list of zeroes to generate random sudoku


def solve(G):
    currentRow = 0
    currentCol = 0
    emptyCellFound = False
    for i in range(9):
        for j in range(9):
            if G[i][j] == 0:
                currentRow = i
                currentCol = j
                emptyCellFound = True
                break
        if(emptyCellFound):
            break
    if(emptyCellFound == False):
        # copying the solution of the sudoku to sol
        global sol
        sol = copy.deepcopy(G)
        getQuestion(G)
        return True
    possibilities = [x for x in range(1, 10)]
    shuffle(possibilities)
    for row in range(9):
        if G[row][currentCol] in possibilities:
            possibilities.remove(G[row][currentCol])
    for col in range(9):
        if G[currentRow][col] in possibilities:
            possibilities.remove(G[currentRow][col])
    firstCellX = (currentRow // 3) * 3
    firstCellY = (currentCol // 3) * 3

    for i in range(firstCellX, firstCellX + 3):
        for j in range(firstCellY, firstCellY + 3):
            if G[i][j] in possibilities:
                possibilities.remove(G[i][j])

    if len(possibilities) == 0:
        return False
    else:
        for p in possibilities:
            G[currentRow][currentCol] = p
            ok = solve(G)
            if ok == True:
                return True
            else:
                G[currentRow][currentCol] = 0
        return False


def get_non_empty_squares(grid):
    # function returns a shuffled list of non-empty squares in the puzzle
    non_empty_squares = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != 0:
                non_empty_squares.append((i, j))
    shuffle(non_empty_squares)
    return non_empty_squares


def remove_numbers_from_grid(grid):
    # Function to remove 50-52 numbers from solution matrix to generate the question
    non_empty_squares = get_non_empty_squares(grid)
    non_empty_squares_count = len(non_empty_squares)
    rounds = 3
    while rounds > 0 and non_empty_squares_count >= 30:
        row, col = non_empty_squares.pop()
        non_empty_squares_count -= 1
        grid[row][col] = 0
    return grid


def printGrid(G):
    # Function to print the sudoku
    print("")
    print("")
    print('― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ')
    count2 = 0
    for row in G:
        count1 = 0
        print("| ", end="")
        for cell in row:
            count1 += 1
            if count1 % 3 == 0:
                print(cell, end=' | ')
            else:
                print(cell, end="  ")
        count2 += 1
        if count2 % 3 == 0:
            print('')
            print('― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ')
        else:
            print('')
            print("")
    print("")


def getQuestion(grid):
    # function to generate the question and display question to user
    global question
    # print(check_sudoku(grid))
    question = remove_numbers_from_grid(grid)
    return


def check_sudoku(game):
    # function to check whether the user entered inputs for sudoku are correct or not,Returns true if correct,If wrong returns False
    n = len(game)
    if n < 1:
        return False
    for i in range(0, n):
        horizontal = []
        vertical = []
        for k in range(0, n):
            # vertical check
            if game[k][i] in vertical and game[k][i] != 0:
                return False
            if game[k][i] != 0:
                vertical.append(game[k][i])
            if game[i][k] in horizontal and game[i][k] != 0:
                return False
            if game[i][k] != 0:
                horizontal.append(game[i][k])
    return True


def startGame():
    # Starting sudoku game
    correct = 0
    game_continue = 'Y'
    fill = 0
    error_count = 0
    re_change = 0
    while correct == 0 and game_continue == 'Y':
        # copy the question to another variable to use question for next try
        error_correction = 'n'
        printGrid(question)
        copy_question = copy.deepcopy(question)
        zero_count = 0
        try_count = 0
        fixed_box = []
        # counting no of zeroes in sudoku
        for i in range(9):
            for j in range(9):
                if copy_question[i][j] == 0:
                    zero_count += 1
                else:
                    fixed_box.append([i, j])
        print("")
        while(try_count < zero_count):
            try:
                re_change = 0
                re_fill = 0
                print("Enter row position(1-9):", end="")
                row = int(input())
                row -= 1
                print("")
                print("Enter column position(1-9):", end="")
                column = int(input())
                column -= 1
                if (row >= 9 or column >= 9):
                    print("Invalid!!Enter correct row and column")
                    print("")
                elif (row < 0 or column < 0):
                    print("Invalid!!Enter correct row and column")
                    print("")
                else:
                    change_choice = 'y'
                    if copy_question[row][column] != 0 and fill != 1 and [row, column] not in fixed_box:
                        print(
                            "\nPosition is already filled. Select different position or\n")
                        print(
                            "Do you want to change the  selected box!Enter (Y or y) if you want to change:", end="")
                        change_choice = input()
                        print("")
                        if change_choice == 'y' or change_choice == 'Y' and check_sudoku(copy_question):
                            re_change = 1
                            re_fill = 1
                    if [row, column] in fixed_box:
                        print(
                            "\nPosition is already filled. You cannot change. Select different position\n")
                    elif change_choice != 'Y' and change_choice != 'y':
                        pass
                    else:
                        copyof_copy_question = copy.deepcopy(copy_question)
                        fill = 0
                        print("\nEnter the number(1-9):", end="")
                        choice = int(input())
                        if choice > 9 or choice <= 0:
                            print("\nInvalid number! Please enter correct number.\n")
                        else:
                            copyof_copy_question[row][column] = choice
                            if check_sudoku(copyof_copy_question):
                                error_count = 0
                                if re_change == 1:
                                    try_count -= 1
                                copy_question[row][column] = choice
                                printGrid(copy_question)
                                try_count += 1
                            else:
                                fill = 1
                                print(
                                    "\n\nThe row or column already has the number! Please enter another number\n")
                                error_count += 1
                                if re_fill == 1:
                                    fill = 0
                                if error_count == 3:
                                    error_count = 0
                                    error_correction = 'Y'

            except:
                print(
                    "\nInvalid row or column or number! Please check and enter again\n")
            if error_correction == 'Y':
                break
        # checking if the inputs entered by user are correct or not if incorrect then the user is allowed to restart the game
        if check_sudoku(copy_question) and error_correction != "Y":
            print("Congratulations! Your solution is correct")
            print("")
            correct = 1
            game_continue = 'N'
        else:
            print("Your solution is incorrect!Please try again")
            print("")
            print(
                "Do you want to retry your game!!\n Enter Y if you want to retry(capital only):", end="")
            game_continue = input()
            if game_continue != "Y":
                print("")
                print("Enter Y if you want to see solution:", end="")
                see_solution = input()
                if see_solution == 'Y' or see_solution == 'y':
                    print("\n\t\tSolution!")
                    printGrid(sol)


# filling the 9 rows and 9 columns of sudoku with
# grid=[[0]*9]*9
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0,
                                                                                                                             0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# To get the question for sudoku
print("")
print("\tWelcome! to Sudoku Game. Your Question is below")
print("\n\nGuidelines to follow:")
print("\n->First you need to enter the row number(1-9).")
print("\n->Then you need to enter the column number(1-9).")
print("\n->If the box in the row and column you entered is already filled then you will be asked if you want to change the value in the box. You are allowed to change the box values.")
print("\n->You cant change the question, If you try to change an error message is shown.")
print("\n->If the row and column is valid then you need to enter the number.")
print("\n->An error message is shown if the row or column you entered already has the number.")
print("\n->The solution you entered is checked at the last")
print("\n->You have a chance to retry your game when you enter number at invalid row and column for 3 times")
print("\n->Incase you donot want to retry your game you have an option to see the solution and exit")
canISolve = solve(grid)
startGame()
