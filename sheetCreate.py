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
 # Prototype on how to get your stats, only rolls 3 dice and adds them together
def rollStats():
    anotherList = []
    
    first = random.randint(3,19)
    anotherList.append(first)
    
    second =random.randint(3,19)
    anotherList.append(second)
    
    third = random.randint(3,19)
    anotherList.append(third)
    
    fourth = random.randint(3,19)
    anotherList.append(fourth)
    
    fifth = random.randint(3,19)
    anotherList.append(fifth)
    
    sixth = random.randint(3,19)
    anotherList.append(sixth)
    
    return anotherList



# Main function, puts everything together
def main():
    file = open('names.txt', 'r')
    series=[]
    
    for lines in file:
        series.append(lines.split())
    
    print ("Name: " + str(getFirstName(series))[2:-2] + " " + str(getSecondName(series))[2:-2])
    
    statRoll = rollStats()
    for x in range(0, 6):
        print (statRoll[x])


# runs the main function
if __name__ == "__main__":
    main()
