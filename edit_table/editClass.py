#Benjamin Jobart - Wrote Code

import sqlite3

connection = sqlite3.connect("../classes.db")
cursor = connection.cursor()

def isInteger(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

#make sure the id actually exists
def checkIDValidity(classID):
    if(not isInteger(classID)):
        return False

    cursor.execute("SELECT course_name FROM classes WHERE ID = ?", (classID,))

    courseRemoved = cursor.fetchall()

    if len(courseRemoved) < 1:
        return False

    return True

#convert a string grade into a gpa
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

def checkClassValidity(term, gpa, units):
    if(term != "Fall" and term != "Spring" and term != "Summer"):
        print("Invalid term")
        return False

    if(gpa == -1):
        print("Invalid grade")
        return False

    if(not isInteger(units)):
        print("Invalid units")
        return False

    return True

def editClass():
    ID = input("Enter the ID of the class you want to edit: ")

    IDValid = checkIDValidity(ID)

    if(not IDValid):
        print("Invalid ID")
        return

    name = input("Enter the new name of the class: ")
    grade = input("Enter the new grade of the class: ")
    gpa = getGPA(grade)

    units = input("Enter the new units in the class: ")
    term = input("Enter the new term of the class, either Fall, Spring, or Summer: ")

    classValid = checkClassValidity(term, gpa, units)

    if(not classValid):
        print("Invalid new Value")
        return
    
    cursor.execute("""
    UPDATE classes SET
    course_name = ?,
    grade_point_average = ?,
    units = ?,
    term = ?
    WHERE id = ?""", (name, gpa, units, term, ID))

    connection.commit()

    print("Sucessfully replaced the class")

cursor.execute("""
                   SELECT course_name, ID, grade_point_average, units, term FROM classes""")

#print out all of the classes before hand so the sure knows which one to edit
rows = cursor.fetchall()

for row in rows:
    print("Name:", row[0], "ID:",row[1], "GPA:", row[2], "Units:", row[3], "Term:", row[4])

editClass()
