#!/usr/bin/awk -f
# Creator: Avissa Perera
# This file is related to reportHtml.sh. It uses a mix of HTML and AWK in order to produce the contents of gpaReport.html.
BEGIN {
	#This is the field seperator. It will be the what seperates each piece of data
	FS = "|"
	print "<html>"
	print "<body>"
	print "<h1>GPA Report</h1>"
	print "<table>"
	print "<tr>"
	print "<th>ID</th>"
	print "<th>Class Name</th>"
	print "<th>GPA</th>"
	print "<th>Term</th>"
	print "<th>Units</th>"
	print "</tr>"
}
{
	#this allows awk to work with the data it receives
	print "<tr>"
	print "<td>" $1 "</td>"
	print "<td>" $2 "</td>"
	print "<td>" $3 "</td>"
	print "<td>" $4 "</td>"
	print "<td>" $5 "</td>"
	print "</tr>"
}
END {
	print "</table>"
	print "</body>"
	print "</html>"
}

