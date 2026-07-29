print "Would you like your class to be a specific ID? (Press Enter to skip) ";
$id = <STDIN>;
chomp($id);

print "Would you like to search by course name? (Press Enter to skip) ";
$courseName = <STDIN>;
chomp($courseName);

print "Would you like the course to above a certain GPA? (Press Enter to skip) ";
$gpaFloor = <STDIN>;
chomp($gpaFloor);

print "Would you like the course to be below a certain GPA? (Press Enter to skip) ";
$gpaCeiling = <STDIN>;
chomp($gpaCeiling);

print "Would you like the course to be a specific term(Fall, Spring, Summer)? (Press Enter to skip) ";
$term = <STDIN>;
chomp($term);

print "Would you like the course to be above a certain unit amount? (Press Enter to skip) ";
$unitsFloor = <STDIN>;
chomp($unitsFloor);

print "Would you like the course to be below a certain unit amount? (Press Enter to skip) ";
$unitsCeiling = <STDIN>;
chomp($unitsCeiling);

# Returns 0 on success
my $status = system("python3", "search.py", $id, $courseName, $gpaFloor, $gpaCeiling, $term, $unitsFloor, $unitsCeiling);
