#!/usr/bin/env python3

#------------------------------------- Imported Modules ---------------------------------------
# os: allows python to interact directly with the OS file structure(changing file permissions)
# sqlite3: provides database API to connect to ("classes.db")
# subprocess: allows python to directly execute native Bash commands from within the code.
#----------------------------------------------------------------------------------------------
import os
import sqlite3
import subprocess
import sys

# =====================
# FUNCTIONS
# =====================

# ====================================================================================
# ====================================================================================
def display_data_table(cursor):
    output_method = input("choose ouput method(In Program or HTML): ")

    if output_method.lower() == "in program":
        #pulls records from database to format for terminal output
        cursor.execute("SELECT id, course_name, units, grade_point_average, term FROM classes;")
        records = cursor.fetchall()

        if not records:
            print("No records found.")
            return

        #creating file and setting reference variable
        temp_file = "temp_gpa_data.txt"
        with open(temp_file, "w") as f:
            #printing rows from records into file
            for row in records:
                f.write(f"{row[0]}|{row[1]}|{row[2]}|{row[3]}|{row[4]}\n")

	# command 5 (Bash): wc -l -> counts number of entries exported to file
        lines_proc = subprocess.run(["wc", "-l", temp_file], capture_output=True, text=True)
        total = lines_proc.stdout.strip().split()[0]
        print(f"\nTotal active records processed: {total}")

        print("\n----- Data Table (formatted in AWK) -----")

	# command 6 (Bash) awk -> formats lines into structured columns
        #awk = (
        #    'BEGIN {FS="|"; printf "%-20s | %-6s | %-12s | %-12s\n", "Course Name", "Units", "Grade Point", "Term";'
        #    ' print "-----------------------------------------------------------------"}'
        #    '{printf "%-20s | %-6s | %-12s | %-12s\n", $1, $2, $3, $4}'
	#    )
        awk = r'''
BEGIN {
	FS="[|]"

	print "------------------------------------------------------------------"
	printf "%-10s | %-20s | %-6s | %-12s | %-12s\n", "Course ID", "Course Name", "Units", "Grade Point", "Term"
	print "------------------------------------------------------------------"
}
{
		printf "%-10s | %-20s | %-6s | %-12s | %-12s\n", $1, $2, $3, $4, $5
	}
	'''
	#runs the data file into formated version with awk
        subprocess.run(["awk", awk, temp_file])

	#deletes temp file
        if os.path.exists(temp_file):
            os.remove(temp_file)

    elif output_method.lower() == "html":
        #calling group members external HTML report
	#CHANGE generate_report_placeholder.sh to actual file name
        subprocess.run(["bash", "-c","source ./reportHtml.sh && reportHTML"])

        print("\nHTML report generation complete. Verifying file safety properties:")

	# command 7 (Bash): ls -l -> verifies permmissions of the file
        subprocess.run(["chmod", "644", "gpaReport.html"])
        subprocess.run(["ls", "-l", "gpaReport.html"])

    else:
	    print("\nInvalid output method selection.")

database = sys.argv[1]
connection = sqlite3.connect(database)
cursor = connection.cursor()
display_data_table(cursor)
connection.close()



