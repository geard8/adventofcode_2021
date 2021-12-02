# Advent of code Puzzle input reader.
# The following code assumes that your puzzle input exists in a
# file called data.txt, one entry per line
 
with open('data.txt', 'r') as f:
    lines = f.readlines()
puzzle_input = [e.strip() for e in lines]

# PART 1
print("------------part 1---------------")
horizontal_position_1 = 0
depth_1 = 0
for input in puzzle_input:
    # print(f"{input}") # TEST CODE
    string_list = input.split()
    # print(string_list) # TEST CODE
    if string_list[0] == "forward":
        horizontal_position_1 += int(string_list[1])
    elif string_list[0] == "up":
        depth_1 -= int(string_list[1])
    elif string_list[0] == "down":
        depth_1 += int(string_list[1])

print(horizontal_position_1)
print(depth_1)

print(f"multplay is: {horizontal_position_1 * depth_1}")

# -----------------------------
# PART 2
print("------------part 2---------------")
horizontal_position_2 = 0
depth_2 = 0
aim_2 = 0

for input in puzzle_input:
    # print(f"{input}") # TEST CODE
    string_list = input.split()
    # print(string_list) # TEST CODE
    if string_list[0] == "forward":
        horizontal_position_2 += int(string_list[1])
        depth_2 += (aim_2*int(string_list[1]))
    elif string_list[0] == "up":
        aim_2 -= int(string_list[1])
    elif string_list[0] == "down":
        aim_2 += int(string_list[1])

print(horizontal_position_2)
print(depth_2)
print(aim_2)

print(f"multplay is: {horizontal_position_2 * depth_2}")
