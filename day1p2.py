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
        count = right.count(left[i])
        preoutput = left[i] * count
        output += preoutput
print("The total similarity is: " + str(output))

#similarity = 0

#for z in range(len(left)):
#    if left[z] == right[z]:
#        occurences = right[z] / right[z]
#        tempsimilarity = left[z] * occurences
#        similarity += tempsimilarity

#print("The total similarity is: " + str(similarity))

