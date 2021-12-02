# Advent of code Puzzle input reader.
# The following code assumes that your puzzle input exists in a
# file called data.txt, one entry per line
 
with open('data.txt', 'r') as f:
    lines = f.readlines()
puzzle_input = [int(e.strip()) for e in lines]


# FOR PART 1
count_1 = 0
for num, input in enumerate(puzzle_input[1:], start=1):
    # print(f"{num}: {input}")
    if input > puzzle_input[num-1]:
        count_1 += 1

# FOR PART 2
count_2 = 0
previous_sum = 0
for num, input in enumerate(puzzle_input):
    if num == (len(puzzle_input) - 2):
        break

    current_sum = input + puzzle_input[num+1] + puzzle_input[num+2]
    if current_sum > previous_sum and previous_sum != 0:
        count_2 += 1
    previous_sum = current_sum

print(f"count is: {count_1}")
print(f"count is: {count_2}")
