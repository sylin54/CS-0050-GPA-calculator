import sys
import sqlite3
import re

connection = sqlite3.connect("../classes.db")
cursor = connection.cursor()

def isInteger(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def isFloat(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

#Get input of all of the search parameters
ID = sys.argv[1]
courseName = sys.argv[2]
gpaFloor = sys.argv[3]
gpaCeiling = sys.argv[4]
term = sys.argv[5]
unitsFloor = sys.argv[6]
unitsCeiling = sys.argv[7]

print(ID)

cursor.execute("SELECT * FROM classes")

classes = cursor.fetchall()

#loop through every class and see if it matches all of the inputs
for course in classes:
    #go through every one and skip if it doesn't match
    if len(ID) > 0:
        if not isInteger(ID) or int(ID) != course[0]:
            continue

    
    if not re.search(rf"{re.escape(courseName)}", course[1]):
        continue

    if len(gpaFloor) > 0 and (not isFloat(gpaFloor) or  float(gpaFloor) > course[2]):
        continue

    if len(gpaCeiling) > 0 and (not isFloat(gpaCeiling) or  float(gpaCeiling) < course[2]):
        continue


    if not re.search(rf"{re.escape(term)}", course[3]):
        continue

    if len(unitsFloor) > 0 and (not isFloat(unitsFloor) or float(unitsFloor) > course[4]):
        continue

    if len(unitsCeiling) > 0 and (not isFloat(unitsCeiling) or float(unitsCeiling) < course[4]):
        continue

    print("Course ID:", course[0], "Course Name:", course[1], "Course GPA:", course[2], "Course Term:", course[3], "Course Units:", course[4])
