#Character Sheet Generator
#
#Will create a 3.5 Dungeons and Dragons Player Character
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
    
#Finds the ability modifier for your given ability score
def modCheck(score):
    if score == 1:
        return "-5"
    elif score <=3:
        return "-4"
    elif score <=5:
        return "-3"
    elif score <= 7:
        return "-2"
    elif score <= 9:
        return "-1"
    elif score <= 11:
        return "0"
    elif score <= 13:
        return "+1"
    elif score <= 15:
        return "+2"
    elif score <= 17:
        return "+3"
    elif score<= 19:
        return "+4"
    elif score <= 21:
        return "+5"
    elif score <= 23:
        return "+6"
    else:
        return "You are too strong for a starting character"


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
    print("STR: " + str(statsList[0]) + " MOD: " + modCheck(statsList[0]))
    print("DEX: " + str(statsList[1]) + " MOD: " + modCheck(statsList[1]))
    print("CON: " + str(statsList[2]) + " MOD: " + modCheck(statsList[2]))
    print("INT: " + str(statsList[3]) + " MOD: " + modCheck(statsList[3]))
    print("CHA: " + str(statsList[4]) + " MOD: " + modCheck(statsList[4]))
    print("WIS: " + str(statsList[5]) + " MOD: " + modCheck(statsList[5]))


# runs the main function
if __name__ == "__main__":
    main()
