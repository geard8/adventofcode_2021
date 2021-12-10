# Advent of code Puzzle input reader.
# The following code assumes that your puzzle input exists in a
# file called data.txt, one entry per line
 
# with open('data_test.txt', 'r') as f:
with open('data.txt', 'r') as f:
    lines = f.readlines()
puzzle_input = [e.strip() for e in lines]

class Coordinate_line:
    def __init__(self, data_input) -> None:

        coordinate1, coordinate2 = data_input.split(" -> ")
        coordinate1_x, coordinate1_y = coordinate1.split(",")
        coordinate2_x, coordinate2_y = coordinate2.split(",")

        self.x1 = int(coordinate1_x)
        self.y1 = int(coordinate1_y)
        self.x2 = int(coordinate2_x)
        self.y2 = int(coordinate2_y)
        self.is_x_straight_line = False
        self.is_y_straight_line = False
        self.is_straight_line = False

        if (self.x1 == self.x2) ^ (self.y1 == self.y2): # check it is a straight line
            self.is_straight_line = True
            
            if self.x1 == self.x2: # check if x is straight line
                self.is_x_straight_line = True
            else: # if not x is straight line then y will be straight line
                self.is_y_straight_line = True
            

    def __str__(self) -> str:
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"

    def add_to_board_if_straight_line(self, board):
        if self.is_straight_line:
            if self.is_y_straight_line:
                low_num = 0
                high_num = 0
                if self.x1 < self.x2:
                    low_num = self.x1
                    high_num = self.x2
                else:
                    low_num = self.x2
                    high_num = self.x1

                for i in range(low_num, high_num+1): # +1 as range is up to but not included the secound parameter
                    board[i][self.y1] += 1 # y1 can be y2 as it is a is_y_straight_line and they will be the same

            if self.is_x_straight_line:
                low_num = 0
                high_num = 0
                if self.y1 < self.y2:
                    low_num = self.y1
                    high_num = self.y2
                else:
                    low_num = self.y2
                    high_num = self.y1

                for i in range(low_num, high_num+1): # +1 as range is up to but not included the secound parameter
                    board[self.x1][i] += 1 # x1 can be x2 as it is a is_x_straight_line and they will be the same
        else: # as it is not straight line it will be diagonal line
            
            # prep for drawing diagonal line
            low_num_x = 0
            high_num_x= 0
            is_x1_low = False
            if self.x1 < self.x2:
                low_num_x = self.x1
                high_num_x = self.x2
                is_x1_low = True
            else:
                low_num_x = self.x2
                high_num_x = self.x1

            if is_x1_low:
                y_start = self.y1
                is_y_getting_higher = (self.y1 < self.y2)
            else:
                y_start = self.y2
                is_y_getting_higher = (self.y2 < self.y1)

            # draw diagonal line
            for loop_count, x_index in enumerate(range(low_num_x, high_num_x+1)): # +1 as range is up to but not included the secound parameter
                if is_y_getting_higher:
                    board[x_index][y_start+loop_count] += 1
                else:
                    board[x_index][y_start-loop_count] += 1

        return None


# create 2d board to work with
board = [[0 for i in range(1000)] for j in range(1000)]

# take data and use it with class Coordinate_line and use it is function add_to_board_if_straight_line to add it straight line to board
list_of_lines = list()
for input in puzzle_input:
    coordinate_line = Coordinate_line(input)
    list_of_lines.append(coordinate_line)
    coordinate_line.add_to_board_if_straight_line(board)

# print out board and count coordinate overlap.
count_overlap = 0
for row in board:
    for cell in row:
        if cell > 1:
            count_overlap += 1

# print result for count_overlap
print(count_overlap)