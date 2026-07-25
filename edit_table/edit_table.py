while(True):
    print("""How would you like to edit the courses list?
    Press A to add a course
    Press D to delete a course
    Press C to change a course
    Press E to exit out of the editing GUI""")

    selection = input("Please enter your selection here: ")

    if(selection == "A"):
        print("adding")
    elif(selection == "D"):
        print("deleting")
    elif(selection == "C"):
        print("changing")
    elif(selection == "E"):
        break
    else:
        print("Invalid input, please enter it again")

print("exiting")
