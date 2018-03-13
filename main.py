import random

# Need to add:
# Better computer player
# Statistics


class Board:

    mainBoard = []

    def __init__(self):
        # Initializes a 2D array of length and width 10
        self.mainBoard = [['-' for x in range(10)] for y in range(10)]

    # Places a ship of length n randomly onto the board
    def place_random_ship(self, length):

        # Default character for the ship
        ship_character = 'x'

        # Change the ship's representation based on its length
        if length == 2:
            ship_character = '2'

        if length == 3:
            ship_character = '3'

        if length == 4:
            ship_character = '4'

        if length == 5:
            ship_character = '5'

        # Generates a random x value between 1 and 10
        rand_x = random.randint(1, 10)

        # Generates a random y value between 1 and 10
        rand_y = random.randint(1, 10)

        # Generates a random direction for the boat to expand (1 up, 2 right, 3 down, 4 left)
        rand_dir = random.randint(1, 4)

        # If the starting space is already taken, make new x and y's
        while self.mainBoard[rand_x-1][rand_y-1] != '-':
            rand_x = random.randint(1, 10)
            rand_y = random.randint(1, 10)

        # Ship can't go off the board, so if it is at the right edge and the direction is right, make a new direction
        while rand_x+length > 10 and rand_dir == 2:
            rand_dir = random.randint(1, 4)

        # If it is at the left edge and the direction is left, make a new direction
        while rand_x-length < 1 and rand_dir == 4:
            rand_dir = random.randint(1, 4)

        # If it is at the bottom edge and the direction is down, make a new direction
        while rand_y+length > 10 and rand_dir == 3:
            rand_dir = random.randint(1, 4)

        # If it is at the top edge and the direction is up, make a new direction
        while rand_y-length < 1 and rand_dir == 1:
            rand_dir = random.randint(1, 4)

        # Corner cases where two of the possible cases above are true
        # Have to be added because if both are true, then one will run, finish running, and then go to the next
        # rather than both conditions being examined at the same time

        # Top left corner
        while rand_x-length < 1 and rand_y-length < 1 and (rand_dir == 1 or rand_dir == 4):
            rand_dir = random.randint(1, 4)

        # Top right corner
        while rand_x+length > 10 and rand_y-length < 1 and (rand_dir == 1 or rand_dir == 2):
            rand_dir = random.randint(1, 4)

        # Bottom left corner
        while rand_x-length < 1 and rand_y+length > 10 and (rand_dir == 3 or rand_dir == 4):
            rand_dir = random.randint(1, 4)

        # Bottom right corner
        while rand_x+length > 10 and rand_y+length > 10 and (rand_dir == 2 or rand_dir == 3):
            rand_dir = random.randint(1, 4)

        # The list of adjacent spots to the starting x and y for the ship to expand into
        adj_coords = [None]*(length-1)

        # Finds the adjacent coordinates by iterating through the board in the needed direction

        if rand_dir == 2:
            # Go through the adjacent coordinates and add them to the list
            for x in range(1, length):
                adj_coords[x-1] = self.mainBoard[rand_x-1+x][rand_y-1]

        if rand_dir == 1:
            for x in range(1, length):
                adj_coords[x-1] = self.mainBoard[rand_x-1][rand_y-1-x]

        if rand_dir == 3:
            for x in range(1, length):
                adj_coords[x-1] = self.mainBoard[rand_x-1][rand_y-1+x]

        if rand_dir == 4:
            for x in range(1, length):
                adj_coords[x-1] = self.mainBoard[rand_x-1-x][rand_y-1]

        # If any of the adjacent coordinates have part of a ship, start over again
        for x in adj_coords:
            if x != '-':
                self.place_random_ship(length)
                return

        # Place the ship now that it is known there is no overlap with other ships

        if rand_dir == 2:
            for x in range(0, length):
                self.mainBoard[rand_x-1+x][rand_y-1] = ship_character

        if rand_dir == 1:
            for x in range(0, length):
                self.mainBoard[rand_x-1][rand_y-1-x] = ship_character

        if rand_dir == 3:
            for x in range(0, length):
                self.mainBoard[rand_x-1][rand_y-1+x] = ship_character

        if rand_dir == 4:
            for x in range(0, length):
                self.mainBoard[rand_x-1-x][rand_y-1] = ship_character

    # Prints the board to the console
    def print_board(self):
        for x in range(len(self.mainBoard)):
            for y in range(len(self.mainBoard)):
                print(self.mainBoard[y][x], end='')
            print()

    # Prints two boards side by side
    def print_boards(self, board2):
        for x in range(len(self.mainBoard)):
            for y in range(len(self.mainBoard)):
                print(self.mainBoard[y][x], end='')
            print(" ", end='')
            for z in range(len(board2.mainBoard)):
                print(board2.mainBoard[z][x], end='')

            print()

    # Populates a board
    def randomly_populate_board(self):

        # Ships that are placed in order are
        # 1- Destroyer length 2
        # 2- Cruiser length 3
        # 3- Submarine length 3
        # 4- U length 4
        # 5- Aircraft carrier length 5

        self.place_random_ship(2)
        self.place_random_ship(3)
        self.place_random_ship(3)
        self.place_random_ship(4)
        self.place_random_ship(5)

    # Returns hit or miss for a given coordinate
    def hit_or_miss(self, x, y):
        space = self.mainBoard[x-1][y-1]
        if space != '-' and space != 'o':
            return 'h'
        else:
            return 'm'

    # Adds a miss to a tracker board
    def add_miss(self, x, y):
        self.mainBoard[x-1][y-1] = 'o'

    # Adds a hit to a board
    def add_hit(self, x, y):
        self.mainBoard[x-1][y-1] = 'x'

    # Determines if all the ships have been destroyed
    def are_all_ships_gone(self):
        for x in range(len(self.mainBoard)):
            for y in range(len(self.mainBoard)):
                if self.mainBoard[x][y] != 'x' and self.mainBoard[x][y] != 'o' and self.mainBoard[x][y] != '-':
                    return False

        return True

    # Destroys all ships in a board
    def destroy_ships(self):
        for x in range(len(self.mainBoard)):
            for y in range(len(self.mainBoard)):
                if self.mainBoard[x][y] != 'x' and self.mainBoard[x][y] != 'o' and self.mainBoard[x][y] != '-':
                    self.mainBoard[x][y] = 'x'

    # Determines if n ship has sunk
    def n_has_sunk(self, n):
        for x in range(len(self.mainBoard)):
            for y in range(len(self.mainBoard)):
                if self.mainBoard[x][y] == n:
                    return False
        return True

    # If the 2 ship has sunk
    def two_has_sunk(self):
        return self.n_has_sunk('2')

    # If either of the 3 ships has sunk
    def three_has_sunk(self):
        num_of_threes = 0

        for x in range(len(self.mainBoard)):
            for y in range(len(self.mainBoard)):
                if self.mainBoard[x][y] == '3':
                    num_of_threes += 1

        if num_of_threes == 3 or num_of_threes == 0:
            return True
        else:
            return False

    # If the 4 ship has sunk
    def four_has_sunk(self):
        return self.n_has_sunk('4')

    # If the 5 ship has sunk
    def five_has_sunk(self):
        return self.n_has_sunk('5')

    # If one of the three ships has been sunk


# Player's fleet
playersShipBoard = Board()
# Populates the board
playersShipBoard.randomly_populate_board()

# Makes a board to keep track of guesses
playersTrackingBoard = Board()

# Enemy's ships
enemyFleet = Board()
enemyFleet.randomly_populate_board()

# Enemy tracker
enemyTracker = Board()

# If there are still ships on either board, keep going
while playersShipBoard.are_all_ships_gone() is False and enemyFleet.are_all_ships_gone() is False:

    print("Here is your current fleet and your tracking board: ")
    playersShipBoard.print_boards(playersTrackingBoard)

    print("What is your guess?")

    coordinate_guess = input("Coordinate guess: ")

    letter_coordinates = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10
    }

    # Variable determining if the given input is a valid coordinate or not, 0 is false
    is_coord = 0

    # While the input from the user is a valid coordinate
    while is_coord == 0:

        # Secret!
        while coordinate_guess == '/E':
            enemyFleet.print_boards(enemyTracker)
            coordinate_guess = input("Coordinate guess: ")

        # Secret!
        while coordinate_guess == '/D':
            enemyFleet.destroy_ships()
            coordinate_guess = input("Coordinate guess: ")

        # Try making coordinates out of the input
        try:
            y_guess = str(coordinate_guess[:1])
            y_guess = letter_coordinates[y_guess]

            x_guess = int(str(coordinate_guess[1:]))

            if x_guess > 10 or x_guess < 1:
                raise KeyError

            # If there are no errors, then it is a coordinate
            is_coord = 1
        # If the user enters invalid coordinates, have them try again
        except (KeyError, ValueError):
            print("Not a valid coordinate, try again")
            coordinate_guess = input("Coordinate guess: ")

    # Gets the result of the user's guess
    result = enemyFleet.hit_or_miss(x_guess, y_guess)

    # If the user hits
    if result == 'h':
        print("Hit!\n")
        playersTrackingBoard.add_hit(x_guess, y_guess)
        enemyFleet.add_hit(x_guess, y_guess)
    # If the user misses
    else:
        print("You missed\n")
        playersTrackingBoard.add_miss(x_guess, y_guess)
        enemyFleet.add_miss(x_guess, y_guess)

    # If the enemy ships have been defeated, skip to the end
    if enemyFleet.are_all_ships_gone():
        break

    # If any of the ships have been sunk from the last turn
    if enemyFleet.two_has_sunk()or enemyFleet.three_has_sunk()or enemyFleet.four_has_sunk()or enemyFleet.five_has_sunk():
        print("Great job commander, you sunk one of their battleships!\n")

    # Makes a guess for the computer
    # At the moment, it is random, but hopefully I can modify it later to play strategically
    rand_x_guess = random.randint(1, 10)
    rand_y_guess = random.randint(1, 10)

    enemy_plays = playersShipBoard.hit_or_miss(rand_x_guess, rand_y_guess)

    print("The enemy has guessed ", rand_x_guess, ",", rand_y_guess)

    if enemy_plays == 'h':
        print("The enemy has hit!\n")
        playersShipBoard.add_hit(rand_x_guess, rand_y_guess)
        enemyTracker.add_hit(rand_x_guess, rand_y_guess)
    else:
        print("The enemy missed\n")
        enemyTracker.add_miss(rand_x_guess, rand_y_guess)
        playersShipBoard.add_miss(rand_x_guess, rand_y_guess)

    if playersShipBoard.two_has_sunk()or playersShipBoard.three_has_sunk()or playersShipBoard.four_has_sunk()or playersShipBoard.five_has_sunk():
        print("The enemy has sunk one of your ships!")

# If the player has lost
if playersShipBoard.are_all_ships_gone() is True:
    print("All of your ships have been compromised, you lose")

# If the player has won the game
if enemyFleet.are_all_ships_gone() is True:
    print("The enemy fleet has been defeated! Well done commander, you win!")
