"""
#Advent of code, Day 1

from pylab import loadtxt

depth = loadtxt("SonarSweep.txt", skiprows = 0)
counter = 0


for i in range(len(depth) - 1):
    if depth[i+1] > depth[i]:
        counter = counter + 1
print(counter)

"""

from pylab import loadtxt
depth = loadtxt("SonarSweep.txt")
counter = 0


for i in range(len(depth)-3):
    if (depth[i+2] + depth [i+1] + depth[i]) < (depth[i+3] + depth [i+2] + depth[i+1]):
        counter = counter + 1

print(counter)
