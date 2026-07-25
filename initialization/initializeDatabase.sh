sqlite3 ../classes.db << EOF
CREATE TABLE IF NOT EXISTS classes (
id INTEGER PRIMARY KEY,
course_name VARCHAR(100) NOT NULL,
grade_point_average DOUBLE NOT NULL,
units INTEGER NOT NULL);
EOF
