#!/bin/bash
# Creator: Avissa Perera
# This code has the menu. Users will be able to select 5 different options. I used select and case in order for this code to function. In most cases, with valid input, the program will
# take the user straight to the file (or directory and then file) that the functions are located in. For Edit, there are multiple functions, so the code will use another case expression
# to send the user into their preferred function. As for Exit, it will ask if the user wants to delete their data. The user is able to skip it, but if they choose to do so, their data 
# will be erased.

database="classes.db"
test="false"
if [ "$test" = "true" ]
then
	rm -f "$database"
	echo "Previous data erased."
fi
#Load the files for the functions here
source ./greetings.sh
source ./gradetoGPA.sh
source ./reportHtml.sh
greetings

#defines the prompt text that appears before the select statement
PS3=$'\nChoose your selection by using the numbers assigned to each function.\nReminder:(1) Display, (2) Calculate GPA, (3) Edit, (4) Search, (5) Exit \n'
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
			python3 displayData.py "$database"
			#displayData
			;;
		"Calculate GPA")
			echo "Going to function: Calculate GPA "
			python3 calculateGPA.py "$database"
			#calculateGPA
			;;
		"Edit Data Table")
			echo "Going to function: Edit Data Table "
			#sets the selecrtion prompt message to nothing so it won't prompt when we select
			PS3=$''
			select edit in "Add a Class" "Edit a Class" "Remove a Class"
			do 
				case "$edit" in 
				"Add a Class")
				(
					cd edit_table && python3 addClass.py
				)
				break
				;;
				"Edit a Class")
				(
					cd edit_table && python3 editClass.py
				)
				break
				;;
				"Remove a Class")
				(
					cd edit_table && python3 removeClass.py
				)
				break
				;;
				"Return to Menu")
				break
				;;
				*)
					echo "Invalid Input"
					break
				;;
				esac
			done	
			#editData
			#Reset to ps3 to the other select statement
			PS3=$'\nChoose your selection by using the numbers assigned to each function.\nReminder:(1) Display, (2) Calculate GPA, (3) Edit, (4) Search, (5) Exit \n'
			;;
		"Search Data Table")
			echo "Going to function: Search Data Table "
			(
			cd search_function && perl searchInterface.pl
			)
			#search
			;;
		"Exit")
			echo "You are exiting the GPA Calculator"
			echo "Would you like to delete your data?"
			echo "Press Y to delete your data, and ENTER to skip."
			read deleteAnswer
			if [[ "$deleteAnswer" == "Y" || "$deleteAnswer" == "y" ]];
			then
				rm -f "$database"
				echo "Previous data erased."
			fi
			break
			;;
		*)
			echo "Please enter a number from 1 through 5."
			;;
	esac
done

	
