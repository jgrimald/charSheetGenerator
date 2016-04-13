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
        
 #Prints the name of the class for your character
def getClass():
    selection = random.randint(1, 11)

    if selection == 1:
        return "Barbarian"

    elif selection == 2:
        return "Bard"

    elif selection == 3:
        return "Cleric"

    elif selection == 4:
        return "Druid"

    elif selection == 5:
        return "Fighter"

    elif selection == 6:
        return "Monk"

    elif selection == 7:
        return "Paladin"

    elif selection == 8:
        return "Ranger"

    elif selection == 9:
        return "Rogue"

    elif selection == 10:
        return "Sorcerer"

    elif selection == 11:
        return "Wizard"

    else:
        return "There was an error in the program"
        
 #Prioritizes scores for relevant abilities
def adjustScores(scores, order):
    priority = order

    first = 0
    second = 0
    third = 0
    fourth = 0
    fifth = 0
    sixth= 0


    for num in scores:
        if num > first:
            sixth = fifth
            fifth = fourth
            fourth = third
            third = second
            second = first
            first = num
            
        elif num > second and num <= first:
            sixth = fifth
            fifth = fourth
            fourth = third
            third = second
            second = num
            
        elif num > third and num <= second:
           sixth = fifth
           fifth = fourth
           fourth = third
           third = num
           
        elif num > fourth and num <= third:
            sixth = fifth
            fifth = fourth
            fourth = num
            
        elif num > fifth and num <= fourth:
            sixth = fifth
            fifth = num
            
        else:
            sixth = num
            

    finalStats = [first, second, third, fourth, fifth, sixth]
    return finalStats, priority
    
 #Finds your classes priority of abilities in a list, passes to the above method
def priorityList(classType):
    if classType == "Barbarian":
        return ["STR","CON", "DEX", "WIS", "CHA", "INT"]
    if classType == "Bard":
        return ["CHA", "DEX", "INT", "WIS", "CON", "STR"]
    if classType == "Cleric":
        return ["WIS", "CON", "CHA", "INT", "STR", "DEX"]
    if classType == "Druid":
        return ["WIS", "DEX", "INT", "CHA", "CON", "STR"]
    if classType == "Fighter":
        return["STR", "CON", "DEX", "INT", "CHA", "WIS"]
    if classType == "Monk":
        return["WIS", "DEX", "STR", "CON", "INT", "CHA"]
    if classType == "Paladin":
        return ["CHA", "STR", "WIS", "CON", "INT", "DEX"]
    if classType == "Ranger":
        return ["DEX", "WIS", "CON", "STR", "INT", "CHA"]
    if classType == "Rogue":
        return ["DEX", "INT", "WIS", "CHA", "CON", "STR"]
    if classType == "Sorcerer":
        return["CHA", "DEX", "CON", "WIS", "INT", "STR"]
    if classType == "Wizard":
        return ["INT", "DEX", "CON", "CHA", "WIS", "STR"]
    else:
        return ("There was an error in the code")
        
 #Prints your characters race
def getRace():
    selection = random.randint(1,7)

    if selection == 1:
        return "Human"
    elif selection == 2:
        return "Dwarf"
    elif selection == 3:
        return "Elf"
    elif selection == 4:
        return "Gnome"
    elif selection == 5:
        return "Half-elf"
    elif selection == 6:
        return "Half-orc"
    elif selection == 7:
        return "Halfling"
    else:
        return "This is not a race in Dungeons and Dragons"
        
 #Adjusts ability scores due to racial modifications
#Calls using a dictionary, returns a dict with modified scores
#Much more efficient than before
def racialModifier(d, racial):
    if racial == "Human":
        return d

    elif racial == "Dwarf":
        d['CON'] = int(d['CON'] + 2)
        d['CHA'] = int(d['CHA'] - 2)
        return d
    elif racial == "Elf":
        d['DEX'] = int(d['DEX'] + 2)
        d['CON'] = int(d['CON'] - 2)
        return d

    elif racial == "Gnome":
        d['CON'] = int(d['CON'] + 2)
        d['STR'] = int(d['STR'] - 2)
        return d
            
    elif racial == "Half-elf":
        return d

    elif racial ==  "Half-orc":
        d['STR'] = int(d['STR'] + 2)
        d['INT'] = int(d['INT'] - 2)
        d['CHA'] = int(d['CHA'] - 2)
        return d
       
    elif racial == "Halfling":
        d['DEX'] = int(d['DEX'] + 2)
        d['STR'] = int(d['STR'] - 2)
        return d
        
 #Gets saving throw and base attack bonuses in accordance to your class
def Saves(yourClass):
    fort = 0
    ref = 0
    will = 0
    base = 0
    
    if yourClass == "Barbarian":
        fort = 2
        base = 1
    elif yourClass == "Bard":
        ref = 2
        will = 2
    elif yourClass == "Cleric":
        fort = 2
        will = 2
    elif yourClass== "Druid":
        fort = 2
        will = 2
    elif yourClass == "Fighter":
        fort = 2
        base = 1
    elif yourClass == "Monk":
        fort = 2
        ref = 2
        will = 2
    elif yourClass == "Paladin":
        fort = 2
        base = 1
    elif yourClass == "Ranger":
        fort = 2
        ref = 2
        base = 1
    elif yourClass == "Rogue":
        ref = 2
    elif yourClass == "Sorcerer":
        will = 2
    elif yourClass == "Wizard":
        will = 2
    else:
        return "Your class is not a class in DnD, or there was an error in the program"

    return (fort, ref, will, base)
    
 #Dict of Scores
#
#Creates a dictionary of your ability scores, making it easier to find the modifier for a specific score
#this will take two parameters, $statsList and $priorityList(userClass)
#With this, you will be able to find the relevant score on statsList tied to the skill on the priorityList.

def dictionaryOfSkill(scoreList, skillList):
    dictionary = dict(zip(skillList, scoreList))
    return dictionary




# Main function, puts everything together
def main():
    file = open('names.txt', 'r')
    series=[]
    
    for lines in file:
        series.append(lines.split())
    
    print ("Name: " + str(getFirstName(series))[2:-2] + " " + str(getSecondName(series))[2:-2])
    
    userClass = getClass()
    print("Class: " + userClass)

    userRace = getRace()

    print("Race: " + userRace)
    
    statsList = []
    for x in range(0,6):
        statsList.append(statDiceRoll())
        
    
    sco, scoPrio = adjustScores(statsList, priorityList(userClass))
    dicOfSkill = dictionaryOfSkill(sco, scoPrio)
    
    finalD = racialModifier(dicOfSkill, userRace)
    
    
    print(finalD)

    

    conMod = int(modCheck(finalD['CON']))
    dexMod = int(modCheck(finalD['DEX']))
    wisMod = int(modCheck(finalD['WIS']))
    intMod = int(modCheck(finalD['INT']))
    chaMod = int(modCheck(finalD['CHA']))
    strMod = int(modCheck(finalD['STR']))
    
    modList = [conMod, dexMod, wisMod, intMod, chaMod, strMod]
    modNameList = ['ConMod: ', 'DexMod : ', 'WisMod : ', 'IntMod :', 'ChaMod: ', 'StrMod: ',]
    modDict = dict(zip(modNameList, modList))

    print(modDict)
    
    
    fortitude, reflex, willSave, baseAttack = Saves(userClass)
    print("FORTITUDE: " + str(fortitude + conMod))
    print("REFLEX: " + str(reflex + dexMod))
    print("WILL: " + str(willSave + wisMod))
    print("BASE ATTACK BONUS: " + str(baseAttack))
    print("")

# runs the main function
if __name__ == "__main__":
    main()
