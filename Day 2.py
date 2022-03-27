from pylab import loadtxt

position_numbers = loadtxt("Position.txt", delimiter = " ", usecols = [1])
position_directions = loadtxt("Position.txt", delimiter = " ", usecols = [0], dtype="str")

directions = position_directions
numbers = position_numbers[0:]
sum_horizontal = 0
sum_vertical = 0



for i in range(0, len(numbers)):
    if directions[i] == "forward":
        sum_horizontal = sum_horizontal + numbers[i]
    elif directions[i] == "up":
        sum_vertical = sum_vertical - numbers[i]
    elif directions[i] == "down":
        sum_vertical = sum_vertical + numbers[i]

print(sum_horizontal*sum_vertical)