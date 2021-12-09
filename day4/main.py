# Advent of code Puzzle input reader.
# The following code assumes that your puzzle input exists in a
# file called data.txt, one entry per line
 
# with open('data_test.txt', 'r') as f:
with open('data.txt', 'r') as f:
    lines = f.readlines()
puzzle_input = [e.strip() for e in lines]

class Bingo_board:
    rows, cols = (5, 5) # Size of board
    
    def __init__(self, board_number_list) -> None:
        self.position_hit = list() # position_hit is a list with list of position [row, cols] that been hit. # Don't know that to call what been match so use hit to describe it.
        self.is_bingo = False # Check if it has already got bingo

        # board_number_list need to be longer then rows * cols
        if len(board_number_list) < (Bingo_board.rows * Bingo_board.cols):
            print("board_number_list is to short")
            return None

        self.board = [[0 for i in range(Bingo_board.cols)] for j in range(Bingo_board.rows)]

        i = 0
        for number_row, row in enumerate(self.board):
            for number_col, cell in enumerate(row):
                self.board[number_row][number_col] = board_number_list[i]
                i += 1

    def hit(self, hit_number):
        """
        Will check if hit_number is in this board and save what position in position_hit
        return True if a position is hit otherwise return False
        """
        for number_row, row in enumerate(self.board):
            for number_col, cell in enumerate(row):
                if cell == hit_number:
                    self.position_hit.append([number_row, number_col])
                    return True
        return False

    def bingo(self):
        """
        Check if there is bingo on any row or column
        """

        # if not even 5 hit it can't have bingo
        if len(self.position_hit) < 5:
            return False # not bingo

        # check all rows for bingo
        for number_row,  row in enumerate(self.board):
            count_hit = 0
            for number_col, cell in enumerate(row):
                if [number_row, number_col] in self.position_hit:
                    count_hit += 1
                    if count_hit  == self.rows:
                        self.is_bingo = True # set bingo to True
                        return True # BINGO
                else:
                    break # next row

        # check all columns for bingo
        i_col = 0
        while i_col < self.cols:
            count_hit = 0
            i_row = 0
            while i_row < self.rows:
                if [i_row, i_col] in self.position_hit:
                    count_hit += 1
                    if count_hit  == self.cols:
                        self.is_bingo = True # set bingo to True
                        return True # BINGO
                else:
                    break # next row
                i_row += 1
            i_col += 1

        return False # not bingo

    def sum_not_hit(self):
        """
        add all number that are not hit toghter as sum
        return sum
        """

        sum = 0
        for number_row,  row in enumerate(self.board):
            for number_col, cell in enumerate(row):
                if [number_row, number_col] not in self.position_hit:
                    sum += int(cell)

        return sum


# bingo_number_list is list of all the number in order it will be drawn for bingo game
bingo_number_list = puzzle_input[0].split(",")

# fix bingo_boards that is a list with all bingo boards based on class Bingo_board
bingo_boards = list()
i = 2
puzzle_input_length = len(puzzle_input)
while i < puzzle_input_length:
    number_string = ""
    number_string += (puzzle_input[i] + " ")
    number_string += (puzzle_input[i+1] + " ")
    number_string += (puzzle_input[i+2] + " ")
    number_string += (puzzle_input[i+3] + " ")
    number_string += (puzzle_input[i+4] + " ")
    bingo_boards.append(Bingo_board(number_string.split()))
    i += 6


def play_bingo(bingo_number_list, bingo_boards):
    for draw_number in bingo_number_list:
        for i_board, board in enumerate(bingo_boards):
            if not board.is_bingo:
                is_hit = board.hit(draw_number)
                if board.bingo():
                    sum = board.sum_not_hit()
                    print(f"SUM is: {int(draw_number) * sum} for board: {i_board}")

play_bingo(bingo_number_list, bingo_boards)






# # TEST CODE START
# x = bingo_boards[0]
# x.hit("22")
# x.hit("23")
# x.hit("13")
# x.hit("17")
# x.hit("11")
# x.hit("0")
# x.hit("8")
# print(x.bingo())
# print(x.sum_not_hit())
# # TEST CODE END


# # TEST CODE START
# x = bingo_boards[0]
# print(x.hit("22"))
# print(x.hit("23"))
# print(x.hit("28"))
# print(x.position_hit)
# # TEST CODE END


# # TEST CODE START
# data_board = "22 13 17 11  0 8  2 23  4 24 21  9 14 16  7 6 10  3 18  5 1 12 20 15 19".split()
# print(data_board)
# board = Bingo_board(data_board)
# print(board.board)
# # TEST CODE END



# # method 2b

# arr = [[0 for i in range(cols)] for j in range(rows)]
 
# # again in this new array lets change
# # the first element of the first row
# # to 1 and print the array
# arr[0][0] = 1
# arr[1][4] = 5
# for row in arr:
#     print(row)
 
# # outputs the following as expected
# #[1, 0, 0, 0, 0]
# #[0, 0, 0, 0, 0]
# #[0, 0, 0, 0, 0]
# #[0, 0, 0, 0, 0]
# #[0, 0, 0, 0, 0]

