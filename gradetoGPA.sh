#!/bin/bash
#Creator: Avissa Perera
# Used in the greetings.sh file to calculate the GPA of the first piece of data. Uses case to go through all of the possible inputs.
gradetoGPA()
{
	grade="$1"
	case "$grade" in
		"A+"|"A")
			GPA=4
			;;
		"A-")
			GPA=3.7
			;;
		"B+")
			GPA=3.3
			;;
		"B")
			GPA=3
			;;
		"B-")
			GPA=2.7
			;;
		"C+")
			GPA=2.3
			;;
		"C") 
			GPA=2
			;;
		"C-")
			GPA=1.7
			;;
		"D+") 
			GPA=1.3
			;;
		"D")
			GPA=1
			;;
		"D-")
			GPA=0.7
			;;
		"F"|"F+"|"F-")
			GPA=0
			;;
		*)
			echo "This letter grade is not valid."
			return 1
			;;
	esac
	return 0
}
