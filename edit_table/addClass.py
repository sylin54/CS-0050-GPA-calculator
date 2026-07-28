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
        elif(modifier == "+"):
            if baseGrade != "A":
                returnValue = returnValue + 0.3
        else:
            return -1
    return returnValue
            


def addClass(name, gpa, units, ID, term):
    cursor.execute("""
    INSERT INTO classes (course_name, grade_point_average, units, id, term)
    VALUES(?, ?, ?, ?, ?);""", (name, gpa, units, ID, term))
        

isValid = True

name = input("Enter the name of the class: ")
grade = input("Enter the grade of the class: ")
gpa = getGPA(grade)

units = input("Enter the units in the class: ")
ID = input("Enter the ID of the class: ")
term = input("Enter the term of the class, either Fall, Spring, or Summer: ")

if(term != "Fall" and term != "Spring" and term != "Summer"):
    print("Invalid term")
    isValid = False

if(gpa == -1):
    print("Invalid grade")
    isValid = False

if(not isInteger(units)):
    print("Invalid units")
    isValid = False

if(not isInteger(ID)):
    print("Invalid ID")
    isValid = False

cursor.execute("""SELECT course_name FROM classes WHERE id = ?""", (ID,))

potentialDuplicates = cursor.fetchall()
if len(potentialDuplicates) > 0:
    print("Duplicate ID")
    isValid = False


if(isValid):
    print("Added class")

    addClass(name, gpa, units, ID, term)
    connection.commit()
    connection.close()
