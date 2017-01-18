# RandomWalk.py

# This program simulates a drunkard walking along a sidewalk. Each step is
# unpredictable, so the program determines, on average, how far from his
# starting point he will be after a specified number of steps and how many
# times, on average, he will return to his starting point after a specified
# number of steps.

# The results of the simulations are sent to a CSV file to be graphed in
# Microsoft Excel.

# import random library
import random

# returns file object in write mode named randomWalk.csv
# csv = comma separated values text file
dataFile = open("randomWalk.csv", "w")

# function to simulate a drunkard walking a specified amount of steps
# returns final position and the number of returns to the starting point
def randomWalk(steps):
    position = 0
    returns = 0
    for i in range(steps):
        directions = ["East", "West"]
        step = random.choice(directions)
        # uncomment for troubleshooting
        # print(step)
        if step == "East":
            position += 1
        else:
            position -= 1
        if position == 0:
            returns += 1
    # takes the absolute value of the position for average distance calculation
    position = abs(position)
    # uncomment for troubleshooting
    # print("position =", position, "returns =", returns)
    return [position, returns]

# variables to hold necessary information for trials and simulations
steps = 200
numTrials = 5000

# runs trials for all steps from 1 to provided number of steps
for i in range(1, steps + 1):
    sumOfLocations = 0
    sumOfReturns = 0
    finalLocation = [0,0]
    for j in range(numTrials):
        finalLocation = randomWalk(i)
        sumOfLocations += finalLocation[0]
        sumOfReturns += finalLocation[1]

    # calculates average final location and returns to starting location
    avgFinalLocation = sumOfLocations / numTrials
    avgReturns = sumOfReturns / numTrials

    # uncomment to print averages
    # print(i, "Step Average Distance from Starting Location:", avgFinalLocation)
    # print(i, "Step Average Returns to Starting Location:", avgReturns)
    # print()

    # writes the averages to randomWalk.csv
    dataFile.write(str(i) + "," + str(avgFinalLocation) + "," + str(avgReturns) + "\n")

# closes file object
dataFile.close()

# prints confirmation that the program has completed
print("Open randomWalk.csv in Microsoft Excel.")
