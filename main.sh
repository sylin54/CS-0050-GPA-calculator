#!/bin/bash
database="classes.db"
test="true"
if [ "$test" = "true" ]
then
	rm -f "$database"
	echo "Previous data erased."
fi
#Load the files for the functions here
source ./greetings.sh
source ./gradetoGPA.sh
greetings
PS3="Choose your selection by using the numbers assigned to each function: "
#echo "(1) to Display the Data Table"
#echo "(2) to Calculate the GPA"
#echo "(3) to Edit the Data Table"
#echo "(4) To Open the Search Function"
#echo "(5) to Exit: "
select option in "Display Data Table" "Calculate GPA" "Edit Data Table" "Search Data Table" "Exit"
do
	case "$option" in 
		"Display Data Table")
			echo "Going to function: Display Data Table "
			#displayData
			;;
		"Calculate GPA")
			echo "Going to function: Calculate GPA "
			#calculateGPA
			;;
		"Edit Data Table")
			echo "Going to function: Edit Data Table "
			#editData
			;;
		"Search Data Table")
			echo "Going to function: Search Data Table "
			#search
			;;
		"Exit")
			echo "You are exiting the GPA Calculator"
			break
			;;
		*)
			echo "Please enter a number from 1 through 5."
			;;
	esac
done

	
