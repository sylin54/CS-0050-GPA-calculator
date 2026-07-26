import sqlite3

connection = sqlite3.connect("../classes.db")
cursor = connection.cursor()

def isInteger(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def removeClass(classID):
    if(not isInteger(classID)):
        print("invalid ID")
        return

    cursor.execute("SELECT course_name FROM classes WHERE ID = ?", (classID,))

    courseRemoved = cursor.fetchall()

    if len(courseRemoved) < 1:
        print("invalid ID")
        return

    print("Deleting course", courseRemoved[0][0])

    cursor.execute("DELETE FROM classes WHERE ID = ?", (classID,))
    connection.commit()

cursor.execute("""
                   SELECT course_name, ID FROM classes""")

rows = cursor.fetchall()

for row in rows:
    print("Name:", row[0], "ID:",row[1])

user_input = input("Enter the ID of the class you want to remove: ")

removeClass(user_input)
