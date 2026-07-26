import sqlite3

connection = sqlite3.connect("../classes.db")
cursor = connection.cursor()

def isInteger(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def getGPA(classGrade):

    returnValue = 0

    if(len(classGrade) > 2):
        return -1

    baseGrade = classGrade[0]

    match baseGrade:
        case "A":
            returnValue = 4 
        
        case "B":
            returnValue = 3

        case "C":
            returnValue = 2

        case "D":
            returnValue = 1

        case "F":
            returnValue = 0
            #If it is an f no need to do + or - stuff
            return returnValue

        case _:
            return -1

    if(len(classGrade) == 2):
        modifier = classGrade[1]

        if(modifier == "-"):
            returnValue = returnValue - 0.3
        elif(modifier == "+" and baseGrade != "A"):
            returnValue = returnValue + 0.3
        else:
            return -1
    return returnValue
            


def addClass(name, gpa, units, ID):
    cursor.execute("""
    INSERT INTO classes (course_name, grade_point_average, units, id)
    VALUES(?, ?, ?, ?);""", (name, gpa, units, ID))
        

isValid = True

name = input("Enter the name of the class: ")
grade = input("Enter the grade of the class: ")
gpa = getGPA(grade)

units = input("Enter the units in the class: ")
ID = input("Enter the ID of the class: ")

if(gpa == -1):
    print("Invalid grade")
    isValid = False

if(not isInteger(units)):
    print("Invalid units")
    isValid = False

if(not isInteger(ID)):
    print("Invalid ID")
    isValid = False

if(isValid):
    print("Adding class", name, "with an id of", ID, "and with a gpa of", gpa, "and", units, "units")
    addClass(name, gpa, units, ID)
    connection.commit()
    connection.close()
