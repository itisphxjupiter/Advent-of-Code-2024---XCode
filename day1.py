import math

list = open("/Users/itsphxjupiter/Documents/xcode-beta/macDev/macapp/Advent of Code 2024 - XCode/day1-input.md")

left = []
right = []

for n in list:
    strSep = n.split('   ')
    left.append(int(strSep[0]))
    right.append(int(strSep[1]))
    # this works lol ^

left.sort()
right.sort()

output = 0

for i in range(len(left)):
    tempoutput = abs(left[i] - right[i])
    output += tempoutput
print("The total difference is: " + str(output))
