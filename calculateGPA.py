#!/usr/bin/env python3
# Creator: Lilyana
#------------------------------------- Imported Modules ---------------------------------------
# os: allows python to interact directly with the OS file structure(changing file permissions)
# sqlite3: provides database API to connect to ("classes.db")
# subprocess: allows python to directly execute native Bash commands from within the code.
#----------------------------------------------------------------------------------------------
import os
import sqlite3
import subprocess
import sys

def calc_gpa(cursor):
    #pulling existing records to calculate gpa
    cursor.execute("SELECT grade_point_average, units FROM classes;")
    records = cursor.fetchall()

    #if no records found
    if not records:
        print("Unable to calculate GPA, no course records found.")
        return

    total_points = 0.0
    total_units = 0

    #sum of total grade points and units
    for row in records:
        grade_val =  row[0]
        units = row[1]
        total_points += (grade_val * units)
        total_units += units

    #checking if total units is equal to 0 to avoid error
    if total_units == 0:
        print("\nTotal units cannot be zero.")
        return

    #calcuclated final gpa
    final_gpa = (total_points / total_units)
    print(f"Final Calculated GPA: {final_gpa:.2f}")

# ========================================================================================
database = sys.argv[1]
connection = sqlite3.connect(database)
cursor = connection.cursor()
calc_gpa(cursor)
connection.close()





