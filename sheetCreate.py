#Character Sheet Generator
#
#Will create a 3.5 DnD Player Character
import random


 # Returns a random element from the list of fantasy names in the text file on the list aList, or series[]
 # This is how you get your first name
def getFirstName(aList):
    return (aList[random.randint(0,len(aList))])
 # Returns a random element from the list of fantasy names in the text file on the list aList, or series[]
 # This is how you get your last name
def getSecondName(aList):
    return (aList[random.randint(0, len(aList))])

#Rolls 4 6-sided die, keeps the highest 3 numbers
def statDiceRoll():
    total= []

    for x in range (0,4):
        roll = random.randint(1,6)
        total.append(roll)
        
    largest = 0
    second = 0
    third = 0

    for i in range(0,4):
        if total[i] > largest:
            third = second
            second = largest
            largest = total[i]
            continue
        elif total[i] > second and total[i] <= largest:
            third = second
            second = total[i]
            continue
        elif total[i] > third and total[i] <= second:
            third = total[i]
            continue
        else:
            continue
    statTotal = largest + second + third
    return statTotal


# Main function, puts everything together
def main():
    file = open('names.txt', 'r')
    series=[]
    
    for lines in file:
        series.append(lines.split())
    
    print ("Name: " + str(getFirstName(series))[2:-2] + " " + str(getSecondName(series))[2:-2])
    
    statsList = []
    for x in range(0,6):
        statsList.append(statDiceRoll())
    print("STR: " + str(statsList[0]))
    print("DEX: " + str(statsList[1]))
    print("CON: " + str(statsList[2]))
    print("INT: " + str(statsList[3]))
    print("CHA: " + str(statsList[4]))
    print("WIS: " + str(statsList[5]))


# runs the main function
if __name__ == "__main__":
    main()
