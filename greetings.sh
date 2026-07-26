#!/bin/bash
greetings()
{
	echo "Welcome to TerminalGPAMetrics: GPA Calculator"
	if [ -e "$database" ]
	then
		echo "You have existing date in the program."
	else
		echo "You do not have data in the program."
		echo "You will need to create one."
	fi
		sqlite3 "$database" << EOF
CREATE TABLE IF NOT EXISTS classes (
	id INTEGER PRIMARY KEY,
	course_name VARCHAR(100) NOT NULL,
	grade_point_average DOUBLE NOT NULL,
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
		echo "Enter the number of units in the class: "
		read units
		echo "Enter the ID of the class: "
		read ID
		sqlite3 "$database" "INSERT INTO classes
		(course_name, grade_point_average, units, id)
		VALUES ('$cName', $GPA,  $units, $ID);"
	fi
}
	
