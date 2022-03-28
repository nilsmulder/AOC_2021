# Advent of Code, Day 3 part 1

from pylab import loadtxt, zeros

# Save binary code in list
binary_code = loadtxt("BinaryCode.txt", dtype = "str")

# Setting up counters for 1's and 0's for calculating gamma & epsilon rates
counter_1 = 0
counter_0 = 0

# Setting gamma and epsilon rates to "empty" strings
gamma_rate = " "
epsilon_rate = " "

# From 0 to length of entry of element in first row (this length is the same for all elements)
for j in range(0, len(binary_code[0])):
    # Checking the j'th number of the i'th element of each row in list
    for i in range(len(binary_code)):  
        # binary_code[row][letter in element]
        if (binary_code[i][j]) == "1":
            counter_1 = counter_1 + 1
        else:
            counter_0 = counter_0 + 1


    if counter_1 > counter_0:
        gamma_rate = gamma_rate +"1"
      
    else:
        gamma_rate = gamma_rate +"0"
    
    #Reset counter so it starts again when checking next letter inn the entries
    counter_1 = 0
    counter_0 = 0 

# Calculating epsilon_rate
    
for k in range(0, len(gamma_rate)):
    if gamma_rate[k] == "1":
        epsilon_rate = epsilon_rate + "0"
    elif gamma_rate[k] == " ":
        continue
    else:
        epsilon_rate= epsilon_rate + "1"

#Checking if binary numbers are "correct"
print(gamma_rate, epsilon_rate)

# Convert from binary string to decimal and printing
gamma_rate_decimal = int(gamma_rate, 2)
epsilon_rate_decimal = int(epsilon_rate, 2)
print(gamma_rate_decimal, epsilon_rate_decimal)

# Multiplying rates to get answer
print(gamma_rate_decimal * epsilon_rate_decimal)
