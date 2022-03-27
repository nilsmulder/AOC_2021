#Day 2 part 1

from pylab import loadtxt

#load text files and make lists

position_numbers = loadtxt("Position.txt", delimiter = " ", usecols = [1], dtype = int)
position_directions = loadtxt("Position.txt", delimiter = " ", usecols = [0], dtype="str")


sum_horizontal = 0
depth = 0


# check which way direction changes and update sum of movement
for i in range(0, len(position_numbers)):
    if position_directions[i] == "forward":
        sum_horizontal = sum_horizontal + position_numbers[i]
    elif position_directions[i] == "up":
        depth = depth - position_numbers[i]
    elif position_directions[i] == "down":
        depth = depth + position_numbers[i]

print(sum_horizontal*depth)