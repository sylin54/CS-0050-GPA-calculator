#!/bin/bash
database="classes.db"
reportHTML()
{
	file="gpaReport.html"
	data=$(sqlite3 "$database" "SELECT COUNT(*) FROM classes;")
	if [ "$data" -eq 0 ]
	then
		echo "You have no information saved."
		echo "Please use the add some information in the Edit Data Table function first."
		return
	fi
	#seperator used in awk file
	sqlite3 "$database" "SELECT id, course_name, grade_point_average, term, units FROM classes;" |
	awk -f ./reportHtml.awk > "$file"
	echo "HTML file created. It is saved as $file."
}
