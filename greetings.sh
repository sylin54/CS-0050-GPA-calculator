#!/bin/bash
greetings()
{
	#clears terminal screen
    	clear
    	echo "Welcome to TerminalGPAMetrics: GPA Calculator"

    	#prints exact username of current user ID
    	username=$(whoami)
    	echo "Current user: $username"

    	#displays current date and time
    	currentDate=$(date)
    	echo "Session started: $currentDate"

    	#gets host performance stats
    	sysStats=$(uptime)
    	echo "System Status: $sysStats"
    	echo " "

	if [ -e "$database" ]
	then
		echo "You have existing data in the program."
	else
		echo "You do not have data in the program."
		echo "You will need to create one."
	fi
		sqlite3 "$database" << EOF
CREATE TABLE IF NOT EXISTS classes (
	id INTEGER PRIMARY KEY,
	course_name VARCHAR(100) NOT NULL,
	grade_point_average DOUBLE NOT NULL,
	term VARCHAR(20) NOT NULL,
	units INTEGER NOT NULL);
EOF
countData=$(sqlite3 "$database" "SELECT COUNT(*) FROM classes;")
	if [ "$countData" -gt 0 ]
	then
		echo "You will be directed to the menu."
	else
		echo "Enter the name of the class: "
		read cName
		while true
		do
			echo "Enter the grade of the class: "
			read grade
			gradetoGPA "$grade"
			if [ $? -eq 0 ]
			then
				break
			else
				echo "Please enter a valid letter grade: "
			fi
		done
		echo "Enter the class term (Fall/Spring/Summer)"
		read term
		echo "Enter the number of units in the class: "
		read units
		echo "Enter the ID of the class: "
		read ID
		sqlite3 "$database" "INSERT INTO classes
		(course_name, grade_point_average, units, term, id)
		VALUES ('$cName', $GPA,  $units, '$term', $ID);"
	fi
}
	
