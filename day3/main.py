# Advent of code Puzzle input reader.
# The following code assumes that your puzzle input exists in a
# file called data.txt, one entry per line
 
# with open('data_test.txt', 'r') as f:
with open('data.txt', 'r') as f:
    lines = f.readlines()
puzzle_input = [e.strip() for e in lines]

def list_to_string(my_list):
    my_string = ""
    for i in my_list:
        my_string += str(i)
    return my_string


# FOR PART 1
my_gamma_list = list()
my_epsilon_list = list()

data_lengt = len(puzzle_input[0])
data_list_lengt = len(puzzle_input)

for i in range(0, data_lengt):
    count_ones = 0
    for input in puzzle_input:
        if int(input[i]):
            count_ones += 1
    my_gamma_list.append(1 if count_ones > (data_list_lengt / 2) else 0)
    my_epsilon_list.append(1 if count_ones < (data_list_lengt / 2) else 0)

my_gamma = int(list_to_string(my_gamma_list), 2)
my_epsilon = int(list_to_string(my_epsilon_list), 2)

print(f"my_gamma_list: {my_gamma}")
print(f"my_epsilon_list: {my_epsilon}")

print(f"Answer of part 1: {my_gamma * my_epsilon}")

# FOR PART 2
# oxygen_generator
oxygen_generator_puzzle_input = puzzle_input.copy()

for i in range(0, data_lengt):
    if len(oxygen_generator_puzzle_input) == 1: # check if only one entry left then break
        break

    count_ones = 0
    for input in oxygen_generator_puzzle_input:
        if int(input[i]):
            count_ones += 1
    match_this_loop = 1 if count_ones >= (len(oxygen_generator_puzzle_input) / 2) else 0
    
    oxygen_generator_puzzle_input_copy = oxygen_generator_puzzle_input.copy()
    for input in oxygen_generator_puzzle_input:
        if int(input[i]) != match_this_loop:
            oxygen_generator_puzzle_input_copy.remove(input)
    oxygen_generator_puzzle_input = oxygen_generator_puzzle_input_copy


# CO2_scrubber
CO2_scrubber_puzzle_input = puzzle_input.copy()

for i in range(0, data_lengt):
    if len(CO2_scrubber_puzzle_input) == 1: # check if only one entry left then break
        break

    count_ones = 0
    for input in CO2_scrubber_puzzle_input:
        if int(input[i]):
            count_ones += 1
    match_this_loop = 1 if count_ones < (len(CO2_scrubber_puzzle_input) / 2) else 0
    
    CO2_scrubber_puzzle_input_copy = CO2_scrubber_puzzle_input.copy()
    for input in CO2_scrubber_puzzle_input:
        if int(input[i]) != match_this_loop:
            CO2_scrubber_puzzle_input_copy.remove(input)
    CO2_scrubber_puzzle_input = CO2_scrubber_puzzle_input_copy


my_oxygen_generator = int(oxygen_generator_puzzle_input[0], 2)
my_CO2_scrubber = int((CO2_scrubber_puzzle_input[0]), 2)

print(f"my_oxygen_generator: {my_oxygen_generator}")
print(f"my_CO2_scrubber: {my_CO2_scrubber}")

print(f"Answer of part 2: {my_oxygen_generator * my_CO2_scrubber}")