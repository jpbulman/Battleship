import random


class Board:
    # Initializes a 2D array of length and width 10
    mainBoard = [['-' for x in range(10)] for y in range(10)]

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


theBoard = Board()
theBoard.randomly_populate_board()
theBoard.print_board()
